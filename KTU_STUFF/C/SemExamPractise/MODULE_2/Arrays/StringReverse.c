#include <stdio.h>
#include <string.h>
void main()
{
  char s[100];
  printf("Enter string: ");
  scanf("%s", s);
  int temp,n=strlen(s);
  for(int i=0;i<n/2;i++)
  {
    temp=s[i];
    s[i]=s[n-i-1];
    s[n-i-1]=temp;
  }
  printf("%s",s);
}
