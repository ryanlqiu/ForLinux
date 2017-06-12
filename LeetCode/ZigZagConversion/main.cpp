#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
extern char* longestPalindrome(char* s);
extern char* convert(char* s, int numRows); 

int main(void)
{
	char str[]="PAYPALISHIRING";
	char*q;
	cout<<str<<endl;
	q=convert("ABCDEF",5);
	cout<<q<<endl;
	getchar();
	return 0;
}