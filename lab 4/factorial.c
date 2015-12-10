#include <stdio.h>
#include <limits.h>
#include <math.h>

long maxlong(void){
	return LONG_MAX;
}

double upper_bound(long n){
	if (n>=6){
		return pow((double)n / 2, n);
	}
	else{
		return pow((double)n / 2 + 0.5, n);
	}
}

long factorial(long n){
	if (n < 0){
		return -2;
	}
	if (upper_bound(n) > LONG_MAX){
		return -1;
	}
	if (n==1 || n==0){
		return 1;
	}
	return n * factorial(n-1);
}

int main(void) {
    long i;

    /* The next line should compile once "maxlong" is defined. */
    printf("maxlong()=%ld\n", maxlong());

    /* The next code block should compile once "upper_bound" is defined. */

    
    for (i=0; i<10; i++) {
        printf("upper_bound(%ld)=%g \t result is = %ld\n", i, upper_bound(i), factorial(i));
    }
    
    return 0;
}


