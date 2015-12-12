#include <stdio.h>

int main(void){
	int n = 0;
int m = n;
n = m + 2;
for (m = 0; m < 3; m++)
  { n = n + 1; }
  printf("%d", n);
	return 0;
}
