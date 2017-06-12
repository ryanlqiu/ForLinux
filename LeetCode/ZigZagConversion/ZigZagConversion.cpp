#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
//本地编译成功，Leetcode上，显示RunTime Error:sysmalloc:.....

//使用数组找规律实现
//第0行为 起始坐标0 + 公差：2*（n-1）;其中n代表行数
//第1行为 起始坐标1 + 公差：2*（n-2）;其中n代表行数
//第2行为 起始坐标2 + 公差：2*（n-3）;其中n代表行数
//。。。。。。。。。
//第n-2行 为起始坐标n-2 + 公差：2*（n-(n-1)）;其中n代表行数
//第n-1行 为起始坐标n-1 + 公差：2*（n-1）;其中n代表行数

//1、建立长度为strlen(s)的数组指针，存储变换数据
//建立公差数组，长度为行数n。
//存第1行数据
#define Array_Row  (numRows-1)

char* convert(char* s, int numRows) {
	int *CommenDiff=(int*)malloc(sizeof(int)*numRows);//公差数组
	int length=strlen(s);
	char*ConvertionArray=(char*)malloc(sizeof(char)*length);//变换数组
	int CommenDiff_Flag=0,Row=0,CommenDiff_Choose=0;
	int s_i=0,j=0;//两个数组的角标
	static int i=0;
//	ConvertionArray[0]=s[0];
	//公差数组建立
	if(Array_Row==0)
	{
		ConvertionArray=s;
		i=length+1;
	}
	else
	{
	for(j=0;j<(Array_Row);j++)//0- n-2
	{
		CommenDiff[j]=2*(numRows-(j+1));
	}
	//n-1 行
	CommenDiff[j]=2*(numRows-1);
	//建立完毕
	while(Row<numRows)
	{
		for(s_i=Row;s_i<strlen(s);s_i=s_i+CommenDiff[CommenDiff_Choose],i++)//结束时 i的角标为新一行的第一位角标
		{
	//s_i=s_i+CommenDiff[CommenDiff_Choose];//s角标计算
			ConvertionArray[i]=s[s_i];
			if(CommenDiff_Flag==0)
			{
				CommenDiff_Choose=Array_Row -Row;
				CommenDiff_Flag=1;
			}
			else
			{
				CommenDiff_Choose=Row;
				CommenDiff_Flag=0;
			}
		}
		Row++;
	}
	ConvertionArray[i]='\0';
	}
	return ConvertionArray;  
}
