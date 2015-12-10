/* Laboratory 6, SESG6025, 2013/2014, Template */

#include <stdio.h>

/* Function void rstrip(char s[])
modifies the string s: if at the end of the string s there are one or more spaces,
then remove these from the string.

The name rstrip stands for Right STRIP, trying to indicate that spaces at the 'right'
end of the string should be removed.
*/

void rstrip(char s[]) {
    /* to be implemented */
    int l=0;
    while (s[l] != '\0'){
		if (s[l] != ' '){
			break;
		}
		l++;
	}
	int i=0;
	char temp[1000000000];
	temp=*s;
	while (s[i] != '\0'){
		 temp[i] = s[first_char + i +1];
		 i++;
	}
	temp[i] = '\0';
	s = temp;
}


int main(void) {
  char test1[] = "Hello World   ";

  printf("Original string reads  : |%s|\n", test1);
  rstrip(test1);
  printf("r-stripped string reads: |%s|\n", test1);

  return 0;
}
