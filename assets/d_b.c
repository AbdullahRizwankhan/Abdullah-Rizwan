#include <stdio.h>

int decimal_to_binaire(int x)

{
    if (x==0)
{
    printf("0");
    return 0;
}
    if(x>0)
    {decimal_to_binaire(x/2);
    printf("%d", x % 2);
    
    }
}

int main()
{int x;

printf("veuillez entrer un nombre decimal:");
scanf("%d",&x);
printf("Le nombre binaire de %d est : ", x);
decimal_to_binaire(x);
return 0;
}



