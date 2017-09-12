#include <stdio.h>
#include <iostream>
#include <string.h>
#include <ctype.h>
using namespace std;
int main(void){

char *myString;
myString = (char*)malloc(sizeof(*myString)*64);
int flag(0), k(0);

cout << "Введите текст: ";
fgets(myString, 64, stdin);
//считаем сколько слов в строке
for(int i = 0; i<63; i++){
      if(isalpha(myString[i])){
           if(flag == 0){
           flag = 1;
           k++;
           }
      }
      else {
           flag = 0;
      }
}
//объявляем двумерный массив
char myMass[k][20]; 
      int o = 0;
      flag = 0;
for(int i = 0; i<k; i++){
   for(int j = 0; j < 20; j++){

      if(isalpha(myString[o])){
         myMass[i][j] = myString[o];
        flag = 1; 
        printf("%c", myString[o]);
      } 
      else if(myString[o]==' ' || myString[o]=='.' || myString[o]=='.')
      {
             if(flag==0){} 
            flag = 0;
            o++;
              break;}
      o++;
   }
}
printf("%1.20s", myMass[1]);
free(myString);

return(0);
}
