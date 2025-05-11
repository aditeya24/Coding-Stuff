#include<stdio.h>
void main()
{
int num,sum=0,last,first,temp;
printf("Enter num: ");
scanf("%d",&num);
temp=num;
last=temp%10;
sum+=last;
while(temp>10)
{
temp=temp/10;
}
first=temp;
sum+=first;
printf("Sum: %d\n",sum);
}
