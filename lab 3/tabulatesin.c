#include <stdio.h>
#include <math.h>

#define XMIN (float)1

#define XMAX (float)10

#define N (float)10

int main(void){
	int i;
	float x, y;
	for (i=0; i<N; i=i+1){
		x = XMIN+(XMAX-XMIN)/(N-1)*((float)i);
		y = sin(x);
		printf('%f %f\n', x, y);
	}
}
