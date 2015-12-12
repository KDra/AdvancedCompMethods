#include<stdio.h>
/* TIMING CODE BEGIN (We need the following lines to take the timings.) */
#include<stdlib.h>
#include<math.h>
#include <time.h>
clock_t startm, stopm;
#define RUNS 1
#define START if ( (startm = clock()) == -1) {printf("Error calling clock");exit(1);}
#define STOP if ( (stopm = clock()) == -1) {printf("Error calling clock");exit(1);}
#define PRINTTIME printf( "%8.5f seconds used .", (((double) stopm-startm)/CLOCKS_PER_SEC/RUNS));
/* TIMING CODE END */

double f(double x){
	return sqrt(1 - x*x);
}

double pi(long n){
	double a = -1;
	double b = 1;
	double s, x, h;
	int i;
	h = (b-a)/(double)n;
	s = 0.5 * f(a) + 0.5 * f(b);
	for (i=1; i<n; i++){
		x = a + i*h;
		s = s + f(x);
	}
	return s * h * 2;
}

int main(void) {
    /* Declarations */



    /* Code */
    START;               /* Timing measurement starts here */
    /* Code to be written by student, calling functions from here is fine
       if desired
    */
	printf("%20.19f\n", pi(1e7));


    STOP;                /* Timing measurement stops here */
    PRINTTIME;           /* Print timing results */
    return 0;
}
