#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int number, guess, attempts, max_attempts, choice;
    char play_again;

    srand(time(0));

    do {
        
        printf("Select difficulty level:\n");
        printf("1. Easy (10 attempts)\n");
        printf("2. Medium (7 attempts)\n");
        printf("3. Hard (5 attempts)\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: max_attempts = 10; break;
            case 2: max_attempts = 7; break;
            case 3: max_attempts = 5; break;
            default: max_attempts = 7; printf("Invalid choice. Defaulting to Medium.\n");
        }

        number = rand() % 100 + 1;
        attempts = 0;

        printf("Guess the number between 1 and 100. You have %d attempts.\n", max_attempts);

        while (attempts < max_attempts) {
            printf("Enter your guess: ");
            scanf("%d", &guess);
            attempts++;

            if (guess > number) {
                printf("Too high!\n");
            } else if (guess < number) {
                printf("Too low!\n");
            } else {
                printf("🎉 Correct! You guessed it in %d attempts.\n", attempts);
                break;
            }

            if (attempts == max_attempts) {
                printf(" Out of attempts! The correct number was %d.\n", number);
            }
        }

        printf("Do you want to play again? (y/n): ");
        scanf(" %c", &play_again);

    } while (play_again == 'y' || play_again == 'Y');

    printf("Thanks for playing!\n");

    return 0;
}
