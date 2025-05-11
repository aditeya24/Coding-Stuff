#include<stdio.h>
int main()
{
int start,end,i,temp,rem,sum=0,cube=1;
printf("Enter start and end of range:\n");
scanf("%d%d",&start,&end);
printf("Armstrong numbers:\n");
for(i=start;i<=end;i++)
{
temp=i;
sum=0;
while(temp>0)
{
rem=temp%10;
temp=temp/10;
cube=rem*rem*rem;
sum+=cube;
}
if(sum==i)
printf("%d\n",i);
}
return 0;
}
