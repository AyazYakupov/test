#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, char** argv){

   int i, j, n = 0;
   cout << "Матрица размером (2n-1)*(2n-1). Введите n: ";
   cin >> n;
   /* int number = 1; */
   int side = 2*n - 1;
   int matrix[side][side];//матрица
   int iter = side/2;
   int currentSide = 1;//счетчик стороны
   int count = 1;

   for (i = 0; i < side; i++){ // составляем матрицу и заполняем числами
     for(j = 0; j < side; j++){
       matrix[i][j] = count;
       count++;
     }   
   } 
   /* while (iter<n-1){ */
   /*   for(i = 0; i<currentSide; i++){ */
   /*     matrix[iter][i+iter] = number; */
   /*     number++; */
   /*   } */

   /*   for(i = 0; i<currentSide-2; i++){ */
   /*     matrix[i+1+iter][side-1-iter] = number; */
   /*     number++; */
   /*   } */

   /*   for(i = 0; i<currentSide; i++){ */
   /*     matrix[side-1-iter][side-1-i-iter] = number; */
   /*     number++; */
   /*   } */

   /*   for(i = 0; i<currentSide-2; i++){ */
   /*     matrix[side-2-i-iter][0+iter] = number; */
   /*     number++; */
   /*   } */

   /*   currentSide -= 2; */
   /*   iter++; */
   /* } */

   /* matrix[side/2][side/2] = number; */

   for (i = 0; i < side; i++){
     for(j = 0; j < side; j++){
       cout << "\t" << matrix[i][j];
     }   
     cout << "\n";
   } 

   //код на раскручивание матрицы
   cout << "\n" << matrix[side/2][side/2] << " "; //вытаскиваем значение из середины

   while (iter>0){ //итерация пока не закончится массив
   for (i = currentSide; i>0; i--){ //сверху вниз
     cout << matrix[side - iter - i][iter - 1] << " "; 
   }
   for (i = currentSide + 2; i>0; i--){ //слева направо
     cout << matrix[side - iter][side-i-iter+1] << " ";
   }
   for (i = currentSide; i>0; i--){ //снизу вверх
     cout << matrix[iter + i-1][side-iter] << " ";
   }
   for (i = currentSide + 2; i>0; i--){ //справа налево
     cout << matrix[iter-1][i+iter-2] << " ";
   }
   iter--;
   currentSide+=2; 
   /* for (i = currentSide; i>0; i--){ */
   /*   cout << matrix[side - iter - i][iter - 1] << " "; */ 
   /* } */
   /* for (i = currentSide + 2; i>0; i--){ */
   /*   cout << matrix[side - iter][side-i-iter+1] << " "; */
   /* } */
   /* for (i = currentSide; i>0; i--){ */
   /*   cout << matrix[iter+i-1][side-iter] << " "; */
   /* } */
   /* for (i = currentSide + 2; i>0; i--){ */
   /*   cout << matrix[iter-1][i+iter-2] << " "; */
   /* } */
   }
   return 0;

}
