#include <iostream>
#include <stdlib.h>

using namespace std;
int main(){
  int N = 10, i(0),j(0), tmp;
  int myArr[N];
   
  srand(time(NULL));
  for (i = 0; i < N; i++) {
    myArr[i] = rand()%99;
  }
  for (i = 0; i < N-1; i++) {
    for (j = 0; j < N-1; j++) {
      if(myArr[j] > myArr[j+1]){
        tmp = myArr[j];
        myArr[j] = myArr[j+1];
        myArr[j+1] = tmp;  }
    }
  }
  for (i = 0; i < N; i++) {
    printf("\t %d", myArr[i]); 
  }
  
  int average = 0;
  int left = 0;
  int right = N;
  int sint;

  printf("\n \t Какое число найти? \t");
  cin >> sint;
  while(left<right){
    average = (left + right) / 2;

    if (sint < myArr[average])
      right = average;
    else if (sint > myArr[average])
      left = average;
    else {
      cout << '\n' << "Ваше число элемент в массиве №" << average;
      /* printf("\n\t ваше число элемент в массиве № %d", mid); */
      break;
    }
  }
  return 0;
}
