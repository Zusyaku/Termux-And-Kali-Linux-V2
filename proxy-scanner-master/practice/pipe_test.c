#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(void){
    pid_t pid;
    char buffer[10], result[10];
    int pp[2], qq[2];
    int a, b, c;

    pipe(pp);
    pipe(qq);

    pid = fork();

    if( pid == 0){
        close(pp[0]);
        close(qq[1]);

        printf("a = ");
        fgets(buffer, 10, stdin);
        write(pp[1], buffer, strlen(buffer)+1);

        printf("b = ");
        fgets(buffer, 10, stdin);
        write(pp[1], buffer, strlen(buffer)+1);

        read(qq[0], result, 10);

        printf("a + b = %s\n", result);
        close(qq[0]);
        close(pp[1]);
    }else{
        close(qq[0]);
        close(pp[1]);

        read(pp[0], buffer, 256);
        a = atoi(buffer);

        read(pp[0], buffer, 256);
        b = atoi(buffer);

        c = a + b;
        sprintf(buffer, "%d", c);

        write(qq[1], buffer, strlen(buffer) + 1);
        
        close(pp[0]);
        close(qq[1]);
    }

    return(0);
}

