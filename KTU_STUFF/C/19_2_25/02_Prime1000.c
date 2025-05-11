#include<stdio.h>
void main()
{
int i,j,flag;
for(i=2;i<1000;i++)
{
flag=0;
for(j=2;i<i;i++)
{
if(i%j==0)
flag=1;
}
if(flag==0)
printf("%d\n",i);
}
}
