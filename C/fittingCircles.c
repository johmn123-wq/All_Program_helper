#include <stdio.h>
#include <math.h>
int main()
{
	int T;
	scanf("%d", &T);
	while(T--)
	{
		long int cir,a,b,rec,n=0;
		scanf("%ld %ld", &a,&b);
		if(a>b) printf("%ld\n",a/b);
		else if(a<b) printf("%ld\n",b/a);
		else printf("%ld\n",a/b);
	}
	return 0;
}
