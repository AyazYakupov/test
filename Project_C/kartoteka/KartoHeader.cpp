
#include <iostream>
#include <cstring>
#include <stdio.h>
#include <cstdlib>
#include "KartoHeader.h"


int i;
int workersMount;

worker* w;
worker person;

char *fn = ("kartoteka.txt");

void menuCircle(){

  for (i = 0; i < 1000; i++) {

    int menu(0);
    system("clear");
    cout << '\n' << "1. Создать картотеку" << '\n'
      << "2. Показать картотеку" << '\n'
      << "3. Добавить человека" << '\n'
      << "4. Удалить работника" << '\n'
      << "5. Сохранить в файл" << '\n'
      << "6. Открыть файл" << '\n'
      << "7. Выйти" << '\n'
    << "Выберите пункт меню: ";
    cin >> menu;

    switch(menu){
      case 1:
        creatCard();
        break;
      case 2:
        show(w, workersMount);
        if (question() == true){
        srt(w,workersMount);
        }
        break;
      case 3:
        addWorker(w, workersMount);
        break;
      case 4:
        delWorker(w, N, workersMount);
        break;
      case 5:
        if (create(w, fn, workersMount) == true)
          cout << "Файл успешно записан";
        else cout << "Ошибка записи файла";
        break;
      case 6:
        openfile(w,fn,workersMount);
        break;
      case 7:
        delete[] w;
        system("clear");
        goto exit_loop;
        break;

        
    }
  }
  exit_loop: ;

}

void creatCard(){
        cout << "Введите количество работников: ";
        cin >> workersMount;
        w = new worker[workersMount];
        /* worker w[workersMount]={}; */
        cout << '\n' << "Картотека создана";
}

void addWorker(worker *Obj, int b){

  for (i = 0; i < b; i++) {
    if (Obj[i].year == 0){
      cout << '\n' << "Введите имя: " << '\n';
      cin >> Obj[i].fio;
      cout << '\n' << "Введите год рождения: " << '\n';
      cin >> Obj[i].year;
      cout << '\n' << "Введите зарплату: " << '\n';
      cin >> Obj[i].salary;

      break;
    }
  }
}

void show(worker *Obj, int b){
  system("clear");
  for (i = 0; i < b; i++) {
    if(Obj[i].year != 0){
      cout << '\n' << "Имя: " << Obj[i].fio << '\t'
          << "Год рождение: " << Obj[i].year << '\t'
          << "Зарплата: " << Obj[i].salary << '\t';
    }
  }
}
void delWorker(worker *Obj,const int N, int b){
  system("clear");

  char delPerson[N];
  cout << "Кого удалить? ";
  cin >> delPerson;

  for (i = 0; i < b; i++) {
    char * istr;
    istr = strstr(Obj[i].fio, delPerson);
    if (istr != NULL){
      strncpy(Obj[i].fio, "", N);
      Obj[i].year = 0;
      Obj[i].salary = 0;
      break;
    }
  }
}

int comp(const int *i, const int *j){
   struct worker *x = (struct worker *)i;
   struct worker *y = (struct worker *)j;
   return (x->year - y->year);
}
int comp_salary(const int *i, const int *j){
  struct worker *x = (struct worker *)i;
  struct worker *y = (struct worker *)j;
   return (x->salary - y->salary);

}

bool question(){
   int answ(0);
   cout << '\n' << "Отсортировать картотеку? " << '\n';
   cout << "1. Да" << '\t' << "2. Нет" << '\n';
   cin >> answ;
   for (i = 0; i < 100; i++) {
    if (answ == 1){ return true; break;}
    else if (answ == 2) {return false;break;}
    else cout << "Неправильный ввод!" << '\n';
   }



}
int srt(worker *Obj, int workersMount){
   system("clear");
   int howsort(0);
   cout << '\n' << "Отсортировать массив по: " << '\n'
     << '\t' << "1. Году рождения" << '\t' << "2. Зарплате" << '\n';
   cin >> howsort;
   if (howsort == 1){
     qsort(Obj, workersMount, sizeof (person), (int(*) (const void *, const void *)) comp);
   }
   else if(howsort == 2){
     qsort(Obj, workersMount, sizeof (person), (int(*) (const void *, const void *)) comp_salary);
   }
}

int openfile(worker *Obj, const char *fn, int workersMount){
   FILE *pf(NULL);
   if ((pf = fopen (fn, "rb")) == NULL){
    cout << '\n' << "Не удалось открыть файл";
    int ch = cin.get();
    return 1;
   }   
   else {
     FILE *pf = fopen (fn, "rb");
     w = new worker[10];
     fread(Obj, sizeof(struct worker), workersMount, pf);
     cout << '\n' << "Файл загружен в картотеку";
   }
}

bool create(worker *Obj, const char *fn, int workersMount){
  FILE *wf(NULL);
  if (!(wf=fopen(fn, "wb")))
    return false;
  for (i = 0; i < workersMount; i++) {
   fwrite(Obj, sizeof(struct worker), workersMount, wf);
  }
  fclose(wf);
  return true;
}

  
