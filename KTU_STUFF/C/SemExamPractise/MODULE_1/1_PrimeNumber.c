#include <stdio.h>
int main()
{
  int n,i,flag=0;
  printf("Enter num: ");
  scanf("%d",&n);
  for(i=2;i<n;i++)
  {
    if(n%i==0)
    {
      flag=1;
      break;
    }
  }
  if(flag=1)
    printf("%d is prime\n",n);
  else
    printf("%d is not prime\n",n);
  return 0;
}
