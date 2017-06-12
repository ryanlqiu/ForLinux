#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

//Manacher algorithm

char* longestPalindrome(char* s) {
	int length=strlen(s);
	char* new_s=(char*)malloc(sizeof(char)*(2*length+3));//Rebuild Array
	int *P=(int*)malloc(sizeof(int)*(2*length+2));
	int imaxright_edge_center=0,maxright_edge=0,i=0;
	int max=0,imax=0,j=0;
	int start;
	int end;
	char*results;
	//�ع��ַ��� ����[0]Ϊ'!' ����Ϊ 2*length+1
	new_s[0]='!';
	for(i=1;i<2*length;i=i+2)
	{
		new_s[i]='#';
		new_s[i+1]=s[(i+1)/2-1];
	}
	new_s[2*length+1]='#';
	new_s[2*length+2]='\0';
	for(i=0;i<(2*length+2);i++)
	{
	if(i < maxright_edge)
	{
		//��� i < maxright_edge
		//�� maxright_edge-i > P[2*imaxright_edge_center - i]
		if((maxright_edge-i) > P[2*imaxright_edge_center - i])
		{
			P[i] = P[2*imaxright_edge_center - i];
		}
		else
		{
			//��� maxright_edge-i < P(2*imaxright_edge_center - i)
			P[i] = P[2*imaxright_edge_center - i];
			//���ڴ���maxright_edge �Ĳ��� ������һƥ��
			while((new_s[i-P[i]]!='!')&&(new_s[i+P[i]]!='\0'))
			{
				P[i]=P[i]+1;
				if(new_s[i-P[i]]==new_s[i+P[i]])
				{
				}
				else
				{
					P[i]=P[i]-1;
					break;
				}
		
			}
			if((i+P[i])>maxright_edge)//����imaxright_edge_center �� maxright_edge
			{
				imaxright_edge_center=i;
				maxright_edge=i+P[i];
			}

		}
	}

	else
	{

		//��� i > maxright_edge
		P[i]=0;
		while((new_s[i-P[i]]!='!')&&(new_s[i+P[i]]!='\0'))
			{
				P[i]=P[i]+1;
				if(new_s[i-P[i]]==new_s[i+P[i]])
				{
				}
				else
				{
					P[i]=P[i]-1;
					break;
				}
		
			}
			if((i+P[i])>maxright_edge)//����imaxright_edge_center �� maxright_edge
			{
				imaxright_edge_center=i;
				maxright_edge=i+P[i];
			}
	}
}//end for
	
	for(i=0;i<2*length+2;i++)
	{
		if(P[i]>max)
		{
			max=P[i];
			imax=i;
		}
	}

	results=(char*)malloc(sizeof(char)*(max+1));
	start=imax-max;
	end= imax+ max;
	for(i=start;i<=end;i++)
	{
		if(new_s[i]!='#')
		{
			results[j]=new_s[i];
			j++;
		}
	}
	results[j+1]='\0';
	return results;


}
