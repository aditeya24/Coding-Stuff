#include <stdio.h>
int main()
{
  int temp,i,n;
  printf("Enter len: ");
  scanf("%d",&n);
  int arr[n];
  printf("Enter array:\n");
  for(i=0;i<n;i++)
    scanf("%d",&arr[i]);
  for(i=0;i<n/2;i++)
  {
    temp=arr[i];
    arr[i]=arr[n-i-1];
    arr[n-i-1]=temp;
  }
  printf("Reversed array:\n");
  for(i=0;i<n;i++)
    printf("%d ",arr[i]);
  printf("\n");
}
