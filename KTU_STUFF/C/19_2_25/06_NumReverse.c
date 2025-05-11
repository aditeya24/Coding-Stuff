#include<stdio.h>
void main()
{
int num,temp,rem,rev=0;
printf("Enter num: ");
scanf("%d",&num);
temp=num;
while(temp>0)
{
rem=temp%10;
temp=temp/10;
rev*=10;
rev+=rem;
}
printf("%d\n",rev);
}
