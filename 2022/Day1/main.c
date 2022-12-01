#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int maximum_calories = 0, maximum_elf = 0, current_sum = 0, current_elf = 1;
    FILE* ptr;
    char s[7];
    ptr = fopen("input.txt", "a+");
    if (NULL == ptr) {
        printf("file can't be opened \n");
    }
 
    printf("content of this file are \n");
 
    while (fgets(s, 50, ptr) != NULL) {
        if (strcmp(s, "\0") == 0){
            current_sum += atoi(s);
        }
        else{
            if (current_sum > maximum_calories){
                maximum_calories = current_sum;
                maximum_elf = current_elf;
            }
            current_elf++;
            current_sum = 0;
        }
        // printf("%s", s);
        printf("%d: %d", current_elf, current_sum);
    }
    printf("\nResult: \nMax Calories = %d\nElf No: %d", maximum_calories, maximum_elf);
    fclose(ptr);
    
    return 0;
}
