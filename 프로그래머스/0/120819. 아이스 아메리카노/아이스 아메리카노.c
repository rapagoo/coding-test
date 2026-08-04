#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int answer[2]={0};
int* solution(int money) {
    answer[0] = money / 5500;
    answer[1] = money % 5500;
    return answer;
}