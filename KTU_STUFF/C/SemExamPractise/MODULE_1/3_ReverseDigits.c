#include <stdio.h>
int main()
{
  int n,temp,rev=0;
  printf("Enter n: ");
  scanf("%d",&n);
  temp=n;
  while(temp>0)
  {
    rev*=10;
    rev+=temp%10;
    temp/=10;
  }
  printf("Reverse of %d: %d\n",n,rev);
  return 0;
}
