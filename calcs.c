#include <stdio.h>

int main() {

    int no1, no2;
    int operation;
    int result;
    float div_result;
    int is_valid = 1; 

    printf("====================================\n");
    printf("          STUDENT CALCULATOR\n");
    printf("====================================\n");

    printf("Enter first number: ");
    fflush(stdout); 
    scanf("%d", no1);

    printf("Enter second number: ");
    fflush(stdout); 
    scanf("%d", no2);

    printf("\n----------- OPERATIONS -------------\n");
    printf("[1] Addition (+)\n");
    printf("[2] Subtraction (-)\n");
    printf("[3] Multiplication (*)\n");
    printf("[4] Division (/)\n");
    printf("[5] Modulus (%%)\n");
    printf("------------------------------------\n");

    printf("Enter your choice: ");
    fflush(stdout); 
    scanf("%d", &operation);

    printf("\n====================================\n");
    printf("               RESULT\n");
    printf("====================================\n");

    switch (operation) {

        case 1:
            result = no1 + no2;
            printf("%d + %d = %d\n", no1, no2, result);
            break;

        case 2:
            result = no1 - no2;
            printf("%d - %d = %d\n", no1, no2, result);
            break;

        case 3:
            result = no1 * no2;
            printf("%d * %d = %d\n", no1, no2, result);
            break;

        case 4:
            if (no2 == 0) {
                printf("Error: You Cannot Divide By Zero.\n");
                is_valid = 0; 
            } else {
                div_result = (float)no1 / no2;
                printf("%d / %d = %.2f\n", no1, no2, div_result);
                is_valid = 0; 
            }
            break;

        case 5:
            if (no2 == 0) {
                printf("Error: You Cannot Divide By Zero.\n");
                is_valid = 0;
            } else {
                result = no1 % no2;
                printf("%d %% %d = %d\n", no1, no2, result);
            }
            break;

        default:
            printf("Invalid Choice.\n");
            is_valid = 0;
            break;
    }

    if (is_valid) {
        if (result % 2 == 0) {
            printf("The Result (%d) is Even.\n", result);
        } else {
            printf("The Result (%d) is Odd.\n", result);
        }
    }

    printf("====================================\n");
    printf("          END OF PROGRAM\n");
    printf("====================================\n");

    return 0;
}
