#include <iostream>
#include <cstdlib>
#include <string.h>
#include <new>

using namespace std;

int main(int argv, char** argc){

  int i,j, count = 1000, words = 0,letters=20,arExist = 0,flag=0,ret;
  int k = 0;
        char* word = new char[20]();
        char* tmp;
  char choice;
  for(i=0;i<count; i++) {

    cout << "Выберите пункт меню: " << '\n' << "1) Создать словарь \t 2) Показать словарь \t 3) Добавить слово \t 4) Удалить слово \t 5) Удалить словарь \t 6) Exit" << '\n';
    cin >> choice;

    switch(choice){
      case '1':
        cout << "Сколько слов будет в словаре?" << '\n';
        cin >> words;
        char** myDictionary;
        myDictionary = (char**)calloc(words, sizeof(char*));
        for (i = 0; i < words; i++) {
          myDictionary[i] = (char*)calloc(letters, sizeof(char));
        }
        arExist = 1;
        break;

      case '2':
        if(arExist == 1){
          for (i = 0; i < words - 1; i++) {
            for (j = 0; j < words - 1; j++) {
              if(myDictionary[j][0] != '\0' && myDictionary[j+1][0] != '\0'){
              ret = strncmp(myDictionary[j],myDictionary[j+1],1);
              if(ret>0){
                tmp = myDictionary[j];
                myDictionary[j] = myDictionary[j+1];
                myDictionary[j+1] = tmp;} 
            } 
          }}
          int number = 1;
          for (i = 0; i < words; i++) {
            if(isalpha(myDictionary[i][0])) cout << number << ") ";
            for (j = 0; j < letters; j++) {
              if(isalpha(myDictionary[i][j])){
                    cout << myDictionary[i][j];
                    }
              else break;
            }   
            cout << '\t';
            number++;
         }
         cout << '\n';
         break;
          }
       else { cout << "Словарь не существует" << '\n';
          break;
        }
       break;
      case '3':
        if(arExist == 1){
          strcpy(word,"");
          cout << "Введите слово" << '\n';
          k = 0;
          cin >> word;
          for (i = 0; i < words && isalpha(word[k]); i++) {
            for (j = 0; j < letters; j++) {
              if(isalpha(myDictionary[i][j])){
                break;
              }
              else{
                myDictionary[i][j] = word[k];
                k++;
              }
            }
          }
        }
        else{
          cout << "Словарь не существует!" << '\n';
          break;} 
        break;
      case '4':
        if(arExist == 1){
          cout << "Какое слово удалить?" << '\n';
          int delWord = 0;
          cin >> delWord;
          strncpy(myDictionary[delWord-1], "", letters); 
          for (i = delWord-1; i < words - 1; i++) {
             tmp = myDictionary[i];
             myDictionary[i] = myDictionary[i+1];
             myDictionary[i+1] = tmp;
          }
        }
        else{cout << "Словарь не существует" << '\n';
          break;
        }
      break;

      case '5':
        if(arExist == 1){
          for (i = 0; i < words; i++) {
            free(myDictionary[i]);
          }
            free(myDictionary);
            arExist = 0;
            cout << "Словарь удален" << '\n';
            break;
        }
        else{
          cout << "Словарь не существует" << '\n';
          break;
        }
      case '6':
        free(word);
        free(tmp);
        goto exit_loop; 
    } 
  }

exit_loop: ;
}
