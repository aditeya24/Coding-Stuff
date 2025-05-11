#include<stdio.h>
void main()
{
int num,temp,count=0;
printf("Enter num: ");
scanf("%d",&num);
temp=num;
while(temp>0)
{
temp/=10;
count++;
}
printf("Number of digits: %d\n",count);
}
