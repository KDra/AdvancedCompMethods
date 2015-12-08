#include <stdio.h>

int main(void)
{
	/* code */
	int c;
	for (c=-30; c<=30; c=c+2){
		printf("%3d = %5.1f\n", c, (float)c * 9/5 + 32);
	}
	return 0;
}
