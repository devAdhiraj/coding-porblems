#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int is_prime(int a){
    int step;
    if(a % 2 == 0){
        return 2;
    }
    else{
        step = 2;
    }
    for(int i = 3; i <= sqrt(a); i += step){
        if(a % i == 0){
            return i;
        }
    }
    return -1;
}

int main()
{
    int iter, a, temp;
    scanf("%d", &iter);
    for(int i = 0; i < iter; i++){
        scanf(" %d", &a);
        temp = 1;
        while(temp != -1){
            temp = is_prime(a);
            if(temp == -1 || (a == 2 && temp == 2)){
                printf("%d\n", a);
            }
            else{
                printf("%d ", temp);
                a /= temp;
            }
        }

    }
}