#define _XOPEN_SOURCE
#include <sys/ipc.h>
#include <sys/sem.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <signal.h>
#include <unistd.h>
#define E_CREATE_SH_MEM -1
#define E_AT_SH_MEM -2
#define E_CREATE_MAS_SEM -3
#define E_CREATE_CHILD -4
#define E_DT_SH_MEM -5
#define E_DEL_SH_MEM -5
#define SUCCESS 0
#define FULL_SEM 0
#define EMPTY_SEM 1
#define BIN_SEM 2
#define SIZE 10
int next = 1;
void next_in_false(int sig) {
  next = 0;
}
struct sembuf producer_request[2] = {
  {EMPTY_SEM, -1, 0},
  {BIN_SEM, -1, 0}
};
struct sembuf producer_release[2] = {
  {FULL_SEM, 1, 0},
  {BIN_SEM, 1, 0}
};
struct sembuf consumer_request[2] = {
  {FULL_SEM, -1, 0},
  {BIN_SEM, -1, 0}
};
struct sembuf consumer_release[2] = {
  {EMPTY_SEM, 1, 0},
  {BIN_SEM, 1, 0}
};
void producer(int sem_id, char *shm_buf) {
  int point_buf = 0;
  while (next) {
    semop(sem_id, producer_request, 2);
    shm_buf[point_buf] = 65 + rand() % 26;
    printf("\tProducer: %c\n", shm_buf[point_buf]);
    point_buf = (point_buf + 1) % SIZE;
    semop(sem_id, producer_release, 2);
    sleep(rand() % 5);
  }
  printf("%s\n", "LOG: producer is ended");
}
void consumer(int sem_id, char *shm_buf) {
  int point_buf = 0;
  while (next) {
    semop(sem_id, consumer_request, 2);
    printf("Consumer: %c\n", shm_buf[point_buf]);
    point_buf = (point_buf + 1) % SIZE;
    semop(sem_id, consumer_release, 2);
    sleep(rand() % 5);
  }
  printf("%s\n", "LOG: consumer is ended");
}
int main() {
  srand(time(NULL));
  signal(SIGINT, next_in_false);
   //id разделяемого сегмента
   // создаем разделяемый сегмент
   int shm_id = shmget(IPC_PRIVATE, SIZE * sizeof(char),
   IPC_CREAT | S_IRWXU | S_IRWXG | S_IRWXO);
   if (shm_id == -1) {
   printf("%s\n", "ERROR: Ошибка создания разделяемой области");
   return E_CREATE_SH_MEM;
   }
   // присоединяем разделяемый сегмент памяти
   char *shm_buf = shmat(shm_id, 0, 0);
   if (shm_buf == (void*) -1) {
   printf("%s\n", "ERROR: Ошибка подсоединения к разделяемой области");
   return E_AT_SH_MEM;
   }
   // id массива семафоров
   // создаем массив из 3х семафоров
   int sem_id = semget(IPC_PRIVATE, 3,
   IPC_CREAT | S_IRWXU | S_IRWXG | S_IRWXO);
   if (sem_id == -1) {
   printf("%s\n", "ERROR: Ошибка создания массива семафоров");
   return E_CREATE_MAS_SEM;
   }
   semctl(sem_id, EMPTY_SEM, SETVAL, SIZE);
   semctl(sem_id, BIN_SEM, SETVAL, 1);
   pid_t pid = fork();
   if (pid == -1) {
   printf("%s\n", "ERROR: Ошибка создания потомка");
   return E_CREATE_CHILD;
   }
   if (pid == 0) {
   producer(sem_id, shm_buf);
   } else {
   consumer(sem_id, shm_buf);
   }
   // отсоединяем разделяемый сегмент памяти
   if (shmdt(shm_buf) == -1) {
   printf("%s\n", "ERROR: Ошибка отсоединения разделяемой области");
   return E_DT_SH_MEM;
   }
   //родитель ждет завершения потомка и удаляет разд.сегмент
   if (pid != 0) {
   int *status;
   wait(status);
   if (shmctl(shm_id, IPC_RMID, NULL) == -1) {
   printf("%s\n", "ERROR: Ошибка удаления разделяемой области");
   return E_DEL_SH_MEM;
   }
   }
   return SUCCESS;
   }

