#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;
int main(int argc, char** argv){

const int a(3),b(20);
char* myString;//Array initialization
myString = (char*)malloc(sizeof(char)*256);

cout << "Введите текст: ";
fgets(myString,256, stdin); 

size_t rows(0), colums(0), count(0), flag(0),k(0);

//Start words count
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
cout << '\n' << k << '\n';
//end WC
//
//char newArray[k][b];
//Two-dimensional array initialization
char **newArray;
newArray = (char**)calloc(k,sizeof(char*));
for(int i = 0; i < k; i++){
  newArray[i] = (char*)calloc(b,sizeof(char));
}

for(rows = 0; rows < k; rows++){
  for(colums = 0; colums < b; colums++){
    if(isalpha(myString[count])){
      if(flag == 0){
         colums = 0;
         newArray[rows][colums] = myString[count];
         flag = 1;
      }
      else if(flag == 1){
         newArray[rows][colums] = myString[count];
      }
    }
    else{
      if(flag == 0){
         flag = 0;
         colums--; 
         }
      else if(flag == 1){
         flag = 0;
         cout <<myString[count];
         count++;
         break;
        
      /* } */
    }
      cout << myString[count];
      count++;
  }
}

cout << '\n' << "Введите номер слова: ";
int Word;
cin >> Word;
FOR(INT I = 0; i <b; i++){
   cout << newArray[Word-1][i];}
free(myString);
for(int i = 0; i < k; i++){
  free(newArray[i]); 
} 
free(newArray);
  
   return 0;
}
