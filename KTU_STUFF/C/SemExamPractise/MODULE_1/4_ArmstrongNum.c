#include <stdio.h>
int main()
{
  int num,sum=0,temp,rem,pow,n=0,i;
  printf("Enter num: ");
  scanf("%d",&num);
  temp=num;
  while(temp>0)
  {
    n++;
    temp/=10;
  }
  temp=num;
  while(temp>0)
  {
    rem=temp%10;
    pow=1;
    for(i=0;i<n;i++)
    {
      pow*=rem;
    }
    sum+=pow;
    temp/=10;
  }
  if(sum==num)
    printf("%d is an Armstrong number\n",num);
  else 
    printf("%d is not an Armstrong number\n",num);
  return 0;
}
