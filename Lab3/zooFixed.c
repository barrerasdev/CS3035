#include <stdio.h>

int main() {
    const int size = 5;
    const char *zoo[size];

    zoo[0] = "Zebra";
    zoo[1] = "Lion";
    zoo[2] = "Elephant";
    zoo[3] = "Otter";
    zoo[4] = "Monkey";

    printf("All animals in zoo:\n");
    for (int i = 0; i < size; i++) {
        printf("%s\n", zoo[i]);
    }

    return 0;
}
