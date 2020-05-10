#include <stdio.h>

int main()
{
    int n,t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        scanf("%d",&n);
        if(n==2010 || n==2015 || n==2016 || n==2017 || n==2019)
            printf("HOSTED");
        else
            printf("NOT HOSTED");
        if(i!=t-1)
            printf("\n");
    }
    return 0;
}
