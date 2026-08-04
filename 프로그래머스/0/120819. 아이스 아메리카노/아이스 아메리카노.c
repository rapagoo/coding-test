#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int answer[2]={0};
int* solution(int money) {
    int count = -1;
    int result = -1;
    while (money>=5500) {
        money -= 5500;
        answer[0]++;
    }
    answer[1] = money;
    return answer;
}