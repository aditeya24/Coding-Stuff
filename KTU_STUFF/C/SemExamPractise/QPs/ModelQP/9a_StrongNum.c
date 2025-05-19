#include <stdio.h>
void main()
{
  int num,temp,sum=0,rem,fact=1,i;
  printf("Enter num: ");
  scanf("%d",&num);
  temp=num;
  while(temp>0)
  {
    rem=temp%10;
    for(i=2;i<=rem;i++)
      fact*=i;
    sum+=fact;
    temp/=10;
  }
  if(sum==num)
    printf("%d is a Strong num\n",num);
  else
    printf("%d is not a Strong num\n",num);
}
