#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char* mix(char *s1, char *s2){
	char *r;
	int i;
	int len = strlen(s1) + strlen(s2);
	r = (char*)malloc(len);
	if (r == NULL){
		return r;
	}else{
		for (i = 0; i < len; i+=2){
			r[i] = s1[i];
			r[i+1] = s2[i];
		}
		return r;
	}
}

int main(void){
	char s1[] = "Hello World";
    char s2[] = "1234567890!";

    printf("s1 = %s\n", s1);
    printf("s2 = %s\n", s2);
    printf("r  = %s\n", mix(s1, s2));
	return 0;
}
