#include<stdio.h>
void main()
{
int num,temp,rem,sum=0,sq;
printf("Enter num: ");
scanf("%d",&num);
sq=num*num;
temp=sq;
while(temp>0)
{
rem=temp%10;
temp=temp/10;
sum+=rem;
}
if(sum==num)
printf("%d is a Neon number\n",num);
else
printf("%d is a not Neon number\n",num);
}
