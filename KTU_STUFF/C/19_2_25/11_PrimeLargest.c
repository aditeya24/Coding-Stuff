#include<stdio.h>
void main()
{
int a,b,c,flag=0,max,i;
printf("Enter a,b,c: \n");
scanf("%d%d%d",&a,&b,&c);
if(a>b)
{
if(a>c)
max=a;
else
max=c;
}
else
{
if(b>c)
max=b;
else
max=c;
}
for(i=2;i<max;i++)
{
if(max%i==0)
flag=1;
}
if(flag==0)
printf("Largest number %d is Prime\n",max);
else
printf("Largest number %d is not Prime\n",max);
}
