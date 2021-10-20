#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <unistd.h>
#include <errno.h>

#define MAX_BUF 2560

void print_hex (char *buf, int size)
{
  int a;
  
  for (a = 0; a < size; a++) 
    printf("0x%02X ", buf[a]);
  printf("\n");
}

int main(){
    struct sockaddr_in addr;
    int sock;
    char len = 0;
    char recv_buf[MAX_BUF];
    char header[MAX_BUF*2];
    int err = 0;

    SSL *ssl;
    SSL_CTX *ctx;

    if((sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)) == -1){
        perror("socket");
        return 1;
    }

    addr.sin_family = AF_INET;
    addr.sin_port = htons(1080);
    addr.sin_addr.s_addr = inet_addr("192.168.10.102");

    printf("[+] Target = %s:%d\n", inet_ntoa(addr.sin_addr), ntohs(addr.sin_port));

    if(connect(sock, (struct sockaddr *)&addr, sizeof(addr)) == -1){
        perror("connect");
        return 1;
    };

    char step_one_request[] = {
        0x05, /* socks version */
        0x01, /* auth list num */
        0x00  /* unencessary authentication */
    };

    send(sock, step_one_request, sizeof(step_one_request), 0);

    printf("[+] SENDED STEP ONE REQUEST (%d) = ", sizeof(step_one_request));
    print_hex(step_one_request, sizeof(step_one_request));

    len = recv(sock, recv_buf, MAX_BUF, 0);
    if( len > 0 ){
        printf("[+] RECVED DATA(%d): ", len);
        print_hex(recv_buf, len);

        if(recv_buf[0] != 0x05){
            printf("[!] Invalid socks version\n");
            goto CONNECTION_END;
        }
        if(recv_buf[1] != 0x00){
            printf("[!] Invalid authentication method\n");
            goto CONNECTION_END;
        }

        char step_two_request [MAX_BUF] = {
            0x05, /* socks version */
            0x01, /* connect method */
            0x00, /* reserved */
            0x01  /* ip v4 */
        };

        addr.sin_port = htons(443);
        addr.sin_addr.s_addr = inet_addr("202.16.128.23");

        memcpy(step_two_request + 4, &addr.sin_addr.s_addr, 4);
        memcpy(step_two_request + 8, &addr.sin_port, 2);
        send(sock, step_two_request, 10, 0);
        printf("[+] SENDED STEP TWO REQUEST (%d) = ", sizeof(step_two_request));
        print_hex(step_two_request, sizeof(step_two_request));

        memset(recv_buf, '\0', MAX_BUF);

        len = recv(sock, recv_buf, 10, 0);
        if ( len > 0 ){
            printf("[+] RECVED DATA(%d): ", len);
            print_hex(recv_buf, len);

            SSL_load_error_strings();
            SSL_library_init();
            ctx = SSL_CTX_new(SSLv23_client_method());
            ssl = SSL_new(ctx);
            err = SSL_set_fd(ssl, sock);
            SSL_connect(ssl);

            sprintf(header, "GET /~tagami/cgi-bin/proxychk/env.cgi HTTP/1.1\r\n"
                            "Host: www.cc.sojo-u.ac.jp\r\n\r\n"); 
            SSL_write(ssl, header, strlen(header));

            int buf_size = 256;
            char buf[buf_size];
            int read_size;

            do {
                read_size = SSL_read(ssl, buf, buf_size);
                write(1, buf, read_size);
            } while(read_size > 0);

            printf("%s\n", buf);

            SSL_shutdown(ssl);
            SSL_free(ssl);
            SSL_CTX_free(ctx);
            ERR_free_strings();

        }
    }

CONNECTION_END:
    close(sock);

    return 0;
}

