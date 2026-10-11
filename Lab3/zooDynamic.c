#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;

    do {
        printf("Enter zoo capacity (must be > 4): ");
        scanf("%d", &n);
    } while (n <= 4);

    char **zoo = (char **)malloc(n * sizeof(char *));
    if (zoo == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    zoo[0] = "Monkey";
    zoo[1] = "Tiger";
    zoo[2] = "Gorilla";
    zoo[n - 1] = "Otter";

    printf("\nAnimals in zoo:\n");
    printf("1: %s\n", zoo[0]);
    printf("2: %s\n", zoo[1]);
    printf("3: %s\n", zoo[2]);
    printf("%d: %s\n", n, zoo[n - 1]);

    free(zoo);

    return 0;
}

