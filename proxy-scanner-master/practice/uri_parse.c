#include <stdio.h>
#include <regex.h>

int main(){
    char uri[] = "https://localhost.net/hogehoge/hogehoge/";
    const char *re = "^([^/]+?)://([^/]+?)/(.*)$";
    regex_t regbuf;
    regmatch_t regmatch[4];
    int i,j;
    regcomp(&regbuf, re, REG_EXTENDED);
    regexec(&regbuf, uri, 4, regmatch, 0 );

    for(i=0; i<sizeof(regmatch)/sizeof(regmatch[0]); i++){
        if (regmatch[i].rm_so >= 0 && regmatch[i].rm_eo >= 0) {
            for (j = regmatch[i].rm_so ; j < regmatch[i].rm_eo; j++) {
                putchar(uri[j]);
            }
            printf("\n");
        }
    }

    return 0;
}


