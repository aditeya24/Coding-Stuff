#include<stdio.h>
void main()
{
int i,temp,rem,sum=0;
for(i=100;i<400;i++)
{
temp=i;
sum=0;
while(temp>0)
{
rem=temp%10;
temp/=10;
sum+=rem;
}
printf("%d\n",sum);
}
}
