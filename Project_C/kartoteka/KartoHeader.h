#pragma once

using namespace std;

extern int i;
extern int workersMount;

const int N(50);
struct worker{
    char fio[N];
    int year;
    int salary;
};

extern worker* w;
extern worker person;

void menuCircle();
void creatCard();
void addWorker(worker *Obj, int);
void show(worker* Obj, int);
void delWorker(worker* Obj, const int, int);
int comp (const int *, const int *);
int comp_salary(const int *, const int *);
int srt(worker *Obj, int);
bool question();
bool create(worker *Obj, const char *, int);
int openfile(worker *Obj, const char *, int);
