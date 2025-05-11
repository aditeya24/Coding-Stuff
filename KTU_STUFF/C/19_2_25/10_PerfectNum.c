#include<stdio.h>
void main()
{
int num,sum=0,i;
printf("Enter num: ");
scanf("%d",&num);
for(i=1;i<num;i++)
{
if(num%i==0)
sum+=i;
}
if(sum==num)
printf("%d is a Perfect Number\n");
else
printf("%d is not a Perfect Number\n");
}
