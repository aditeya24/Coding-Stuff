#include<stdio.h>
int main()
{
  int num,sum=0,temp,rem,start,end,fact=1,i,j;
  printf("Enter start and end of range:\n");
  scanf("%d%d",&start,&end);
  printf("Krishnamurthy Numbers:\n");
  for(i=start;i<=end;i++)
  {
    temp = i;
    sum=0;
    while(temp!=0)
    {
      rem=temp%10;
      temp=temp/10;
      for(j=rem;j>1;j--)
      {
        fact*=j;
      }
      sum+=fact;
      fact=1;
    }
    if(sum==i)
      printf("%d\n",i);
  }
  return 0;
}
