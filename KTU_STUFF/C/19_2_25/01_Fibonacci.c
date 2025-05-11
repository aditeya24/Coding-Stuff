#include <stdio.h>
void main() 
{
int n,i,a=0,b=1,c=0;
printf("Enter n: ");
scanf("%d",&n);
for(i=0;i<n;i++)
{
printf("%d ",c);
a=b;
b=c;
c=a+b;
}
printf("\n");
}
