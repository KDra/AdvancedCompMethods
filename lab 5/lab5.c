#include <stdio.h>
#define MAXLINE 1000 /* maximum length of string */

/* function prototype */
void reverse(char source[], char target[]);
int string_length(char s[]);

int main(void) {
  char original[] = "This is a test: can you print me in reverse character order?";
  char reversed[MAXLINE];

  printf("%s\n", original);
  reverse(original, reversed);
  printf("%s\n", reversed);
  return 0;
}

/* reverse the order of characters in 'source', write to 'target'.
   Assume 'target' is big enough. */
void reverse(char source[], char target[]) {
	int i = 0;
	int j = string_length(source)-1;
	while (j>=0){
		target[i] = source[j];
		i++;
		j--;
	}
}

int string_length(char s[]){
	int i = 0;
	i = 0;
	while (s[i] != '\0'){
		i++;
	}
	return i;
}
