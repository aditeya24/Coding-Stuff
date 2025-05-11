#include<stdio.h>
void main()
{
int i=0,sum=0,count=0;
while(count<10)
{
if(i%2!=0)
sum+=i;
count++;
i++;
}
printf("Sum: %d\n",sum);
}
