#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
//���ر���ɹ���Leetcode�ϣ���ʾRunTime Error:sysmalloc:.....

//ʹ�������ҹ���ʵ��
//��0��Ϊ ��ʼ����0 + ���2*��n-1��;����n��������
//��1��Ϊ ��ʼ����1 + ���2*��n-2��;����n��������
//��2��Ϊ ��ʼ����2 + ���2*��n-3��;����n��������
//������������������
//��n-2�� Ϊ��ʼ����n-2 + ���2*��n-(n-1)��;����n��������
//��n-1�� Ϊ��ʼ����n-1 + ���2*��n-1��;����n��������

//1����������Ϊstrlen(s)������ָ�룬�洢�任����
//�����������飬����Ϊ����n��
//���1������
#define Array_Row  (numRows-1)

char* convert(char* s, int numRows) {
	int *CommenDiff=(int*)malloc(sizeof(int)*numRows);//��������
	int length=strlen(s);
	char*ConvertionArray=(char*)malloc(sizeof(char)*length);//�任����
	int CommenDiff_Flag=0,Row=0,CommenDiff_Choose=0;
	int s_i=0,j=0;//��������ĽǱ�
	static int i=0;
//	ConvertionArray[0]=s[0];
	//�������齨��
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
	//n-1 ��
	CommenDiff[j]=2*(numRows-1);
	//�������
	while(Row<numRows)
	{
		for(s_i=Row;s_i<strlen(s);s_i=s_i+CommenDiff[CommenDiff_Choose],i++)//����ʱ i�ĽǱ�Ϊ��һ�еĵ�һλ�Ǳ�
		{
	//s_i=s_i+CommenDiff[CommenDiff_Choose];//s�Ǳ����
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
