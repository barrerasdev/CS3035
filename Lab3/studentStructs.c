#include <stdio.h>

struct Student {
    char name[50];
    int age;
    float gpa;
    char major[50];
};

void printStudents(struct Student *students, int count) {
    for (int i = 0; i < count; i++) {
        printf("Record %d:\n", i + 1);
        printf("Student Name: %s\n", students[i].name);
        printf("Student Age: %d\n", students[i].age);
        printf("Student GPA: %.1f\n", students[i].gpa);
        printf("Student Major: %s\n", students[i].major);
        printf("\n");
    }
}

int main() {
    const int NUM_STUDENTS = 5;
    struct Student students[NUM_STUDENTS];

    for (int i = 0; i < NUM_STUDENTS; i++) {
        printf("Enter info for Student %d:\n", i + 1);
        printf("Name: ");
        scanf(" %[^\n]", students[i].name);
        printf("Age: ");
        scanf("%d", &students[i].age);
        printf("GPA: ");
        scanf("%f", &students[i].gpa);
        printf("Major: ");
        scanf(" %[^\n]", students[i].major);
        printf("\n");
    }

    printStudents(students, NUM_STUDENTS);

    return 0;
}
