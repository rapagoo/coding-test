#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int factorial(int n)
{
    if(n==1) return 1;
    return n * factorial(n-1);
}

int solution(int n) {
    for(int i=1;i<=n;++i){
        if(factorial(i)>n)
        {
            return i - 1;
        }
    }
}