#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(int argc, char *argv[],char*envp[])
{
	char ** ptr;
	for(ptr=envp;*ptr!=0;ptr++)
	{
		printf("env is :%s\n",*ptr);
	}
	
	printf("\n\n---------------My environment variable---------\n\n");
	printf("USERNAME is :%s\n",getenv("USERNAME"));
	putenv("USERNAME=Ryanqiu");
	printf("USERNAME is :%s\n",getenv("USERNAME"));
	setenv("USERNAME","RyanQiu",0);
	
	printf("USERNAME is :%s\n",getenv("USERNAME"));
	setenv("USERNAME","RyanQiu",1);
	printf("USERNAME is :%s\n",getenv("USERNAME"));
	return 0;
}
