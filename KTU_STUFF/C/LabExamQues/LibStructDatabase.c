#include <stdio.h>
#include <string.h>
int main()
{
int N,i,j;
struct stud
{
 int adno;
 char name[50];
}s[100],t;
printf("enter no of students..N <100::");
scanf("%d",&N);
printf("Enter Admission no and Name of %d students\n",N);
for(i=0;i<N;i++)
{
scanf("%d %s",&s[i].adno,s[i].name);
}
//sorting the list according to name
for(i=0;i<N-1;i++)
{
    for(j=0;j<N-1-i;j++)
    {
        if(strcmp(s[j].name,s[j+1].name)>0)
        {
            t=s[j];
            s[j]=s[j+1];
            s[j+1]=t;
        }
    }
}
 
    //printing the roll list in the order of name
printf("Name....Admission Number\n");
for( i=0;i<N;i++)
printf("%-20s%5d\n",s[i].name,s[i].adno);
}