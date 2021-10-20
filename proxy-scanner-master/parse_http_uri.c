/*
parse_http_uri.c

Author:
luismartingil
+ https://github.com/luismartingil
+ www.luismartingil.com

Description:
Basic HTTP Uri parser using C libraries. Used as a proof of concept.
Better use a pure http library such as http://www.w3.org/Library/src/HTParse.
Use at your own risk.

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
  char *tests[5];
  tests[0] = "http://123.233.124.232:8090/foo_page/5566443377228811";
  tests[1] = "http://123.233.124.232/foo_page/5566443377228811";
  tests[2] = "<http://123.233.124.232:8090/foo_page/5566443377228811>;attr=blaBla";
  tests[3] = "http://123.233.124.232:8090";
  tests[4] = "http://123.233.124.232";

  int succ_parsing = 0; // Whether the parsing has been
  char ip[100]; // IP field of the HTTP uri
  int port;  // Port field of the HTTP uri if found
  char page[200]; // Page field of the uri if found

  char* host; // Will be the ip and page joined in one char*
  char tmp_inside_lower[1000]; // Tmp variable if the uri contains < and >
  char* tmp_source; // Points to the source to parse
  size_t i = 0;

  for(i = 0; i < sizeof(tests) / sizeof(tests[0]); i++)
    {
      memset(ip, 0, 100);
      memset(page, 0, 200);
      memset(tmp_inside_lower, 0, 1000);
      port = 80;
      succ_parsing = 0;

      // Set the proper tmp_source char*
      int n1 = sscanf(tests[i], "<%999[^>]>", tmp_inside_lower);
      if (n1 > 0) { tmp_source = tmp_inside_lower;}
      else { tmp_source = tests[i];}

      // Parsing the tmp_source char*
      if (sscanf(tmp_source, "http://%99[^:]:%i/%199[^\n]", ip, &port, page) == 3) { succ_parsing = 1;}
      else if (sscanf(tmp_source, "http://%99[^/]/%199[^\n]", ip, page) == 2) { succ_parsing = 1;}
      else if (sscanf(tmp_source, "http://%99[^:]:%i[^\n]", ip, &port) == 2) { succ_parsing = 1;}
      else if (sscanf(tmp_source, "http://%99[^\n]", ip) == 1) { succ_parsing = 1;}

      // Properly attaching the ip+page to a host
      if (succ_parsing) {
        if ((page != NULL) && (strlen(page) > 0)) { asprintf(&host, "%s/%s", ip, page); }
	else { asprintf(&host, "%s", ip); }

	// Some printing
	printf("--------------------- \n");
	printf("test = \"%s\"\n", tests[i]);
	printf("Success. \n");

	printf("tmp_source = \"%s\"\n", tmp_source);
	printf("*ip = \"%s\"\n", ip);
	printf("*page = \"%s\"\n", page);
	printf("*port = \"%d\"\n", port);
	printf("\n+host = \"%s\" \n+port = \"%d\" \n\n\n", host, port);

	free(host);
      }	else {
	printf("--------------------- \n");
	printf("test = \"%s\"\n", tests[i]);
	printf("Error. \n");
      }
    }

  return 0;
}