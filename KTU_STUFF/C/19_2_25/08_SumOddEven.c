#include<stdio.h>
void main()
{
int n,i,temp,odd=0,even=0;
printf("Enter n: ");
scanf("%d",&n);
printf("Enter numbers:\n");
for(i=0;i<n;i++)
{
scanf("%d",&temp);
if(temp%2==0)
even+=temp;
else
odd+=temp;
}
printf("Even Sum: %d\nOdd Sum: %d\n",even,odd);
}
