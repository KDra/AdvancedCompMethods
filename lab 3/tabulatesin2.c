#include <stdio.h>
#include <math.h>

#define XMIN 1.0

#define XMAX 10.0

#define N 10

int main(void){
	int i;
	float x, y, z;
	for (i=0; i<N; i=i+1){
		x = XMIN + (XMAX - XMIN)/(N-1)*((float)i);
		y = sin(x);
		z = cos(x);
		printf("%f %f %f\n", x, y, z);
	}
	return 0;
}
