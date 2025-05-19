#include <stdio.h>
typedef struct{
  char name[32];
  int day;
  char month[10];
  int year;
  float salary;
} Employee;

void main(){
  Employee e1;
  puts("Enter name of employee: ");
  fgets(e1.name, sizeof(e1.name), stdin);
  puts("Enter date of joining: ");
  scanf("%d %s %d",&e1.day,e1.month,&e1.year);
  puts("Enter salary: ");
  scanf("%f",&e1.salary);
  printf("Name: %sDate of joining: %d %s %d\nSalary: %f\n",e1.name,e1.day,e1.month,e1.year,e1.salary);
}
