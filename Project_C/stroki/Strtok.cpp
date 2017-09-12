#include <iostream>
#include <cstring>
using namespace std;
int main(int argv, char** argc){
   

  size_t i(0), j(0),k(0),flag(0),b(20),count(0);

  char S[128] = "Osobennosti national'noi ribalki - est' to samoe, chego ne znayut inostranci";
  cout << "Razdelenie stroki - " << S << " - na leksemi" << '\n';
   
  char *str = strtok(S," ,.-");
  while(str != NULL){ 

    cout  << str << '\n';
    str = strtok(NULL, " ,.-"); 
  }
  for(i = 0;i < ; i++){
     if(isalpha(str[i])){
       if(flag == 0){
        flag = 1;
        k++; } 
     } 
     else flag = 0;
  }
  cout << '\n' << k << '\n';
  char **myArray;
  myArray = (char**)calloc(k,sizeof(char*));
  for(i = 0; i < k; i++){
     myArray[i] = (char*)calloc(b,sizeof(char));     
  }
  for(i=0;i < k; i++){
    for(j = 0;j < b; j++){
       if(isalpha(str[count])){
           myArray[i][j] = str[count];            
         }

       else{count++;break;
         }
       }
       count++;
    }     
  for(i = 0; i<k; i++){
    for(j = 0; j < b; j++){
      cout << myArray[i][j];
    }
    cout << '\n';
  }
  for(i = 0; i<k; i++){
      free(myArray[i]);
  }
  free(myArray);



  return 0;
}
