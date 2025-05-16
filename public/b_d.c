#include <stdio.h>

int binaire_decimal(int x){
    int d=0 ,rem =0,i=1;
    while(x !=0)
    {
        rem=x%10;
        d+=rem*i;
        x=x/10;
        i=i*2;

    }
    return d;
}

int main()
{
    int x;
    printf("veuillez entrer un nombre binaire:");
    scanf("%d",&x);
    printf("la decimal de %d est %d" , x,binaire_decimal(x));
}