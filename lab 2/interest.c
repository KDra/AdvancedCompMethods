#include <stdio.h>

int main(void)
{
	/* code */
	int m;
	float s, debt, rate, interest, total_interest;
	s = 1000;
	debt = s;
	rate = 0.03;
	total_interest=0.0;
	for (m=1; m<25; m = m+1){
		interest = debt * rate;
		debt = debt + interest;
		total_interest = total_interest + interest;
		printf("month %2d: debt=%7.2f, interest=%7.2f, total_interest=%7.2f, frac=%7.2f%%\n",\
				m, debt, interest, total_interest, total_interest/s*100);
	}
	return 0;
}
