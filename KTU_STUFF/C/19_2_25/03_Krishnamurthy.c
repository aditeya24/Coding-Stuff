#include<stdio.h>
int fct(int n);
void main()
{
int num,sum=0,temp,rem;
printf("Enter num: ");
scanf("%d",&num);
temp = num;
while(temp>0)
{
rem=temp%10;
temp=temp/10;
sum+= fct(rem);
}
if(sum==num)
printf("%d is Krishnamurthy number\n",num);
else
printf("%d is not Krishnamurthy number\n",num);
}
int fct(int n)
{
int i,fact=1;
for(i=n;i>1;i--)
{
fact*=i;
}
return fact;
}
