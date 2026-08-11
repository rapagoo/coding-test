#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
int answer[2] = {0, 0};
int* solution(int num_list[], size_t num_list_len) {
    for(int i=0;i<num_list_len;++i){
        if(num_list[i]%2==0)
        {
            answer[0]++;
        }
        else answer[1]++;
    }
    return answer;
}