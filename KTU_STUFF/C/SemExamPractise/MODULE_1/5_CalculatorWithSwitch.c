#include <stdio.h>
int main()
{
  int ch,a,b;
  printf("[1] Addition\n[2] Substraction\n[3] Multiplication\n[4] Division\n[5] Remainder\n[0] Exit\n");
  while(1)
  {
    printf("Enter choice[1,2,3,4,5,0]: ");
    scanf("%d",&ch);
    if(ch==0){
      printf("Exiting...\n");
      break;
    }
    printf("Enter a and b:\n");
    scanf("%d%d",&a,&b);
    switch(ch)
    {
      case 1:
        printf("Output: %d\n",a+b);
        continue;
      case 2:
        printf("Output: %d\n",a-b);
        continue;
      case 3:
        printf("Output: %d\n",a*b);
        continue;
      case 4:
        if(b!=0)
          printf("Output: %d\n",a/b);
        else
          printf("Error: Division by Zero\n");
        continue;
      case 5:
        if(b!=0)
          printf("Output: %d\n",a%b);
        else
          printf("Error: Division by Zero\n");
        continue;
      default:
        printf("Error: Invalid choice");
        continue;
    }
  }
}
