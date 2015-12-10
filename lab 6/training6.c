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
    int last_char;
    while (s[l] != '\0'){
		if (s[l] != ' '){
			last_char = l;
		}
		l++;
	}
	s[last_char + 1] = '\0';
}


int main(void) {
  char test1[] = "Hello World   ";
  char test2[] = "iaofnlsdhgs;goojiziodaomkf;lsdfl;mmgxklnfs s fsd    sfpsog;sdg    ";

  printf("Original string reads  : |%s|\n", test1);
  rstrip(test1);
  printf("r-stripped string reads: |%s|\n", test1);
  printf("Original string reads  : |%s|\n", test2);
  rstrip(test2);
  printf("r-stripped string reads: |%s|\n", test2);

  return 0;
}
