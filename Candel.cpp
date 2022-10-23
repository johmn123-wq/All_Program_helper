#include<iostream>
using namespace std;
int main()
{

int len;	
cout << "Enter number of rows: ";
cin >> len;


for(int i=0;i<len;i++){
	cout<<" ";
}

cout<<"*\n";

for(int i = 1; i <= len; i++)
{
	
	for (int s = i; s < len; s++)
	
	 if(s/2==len){
	 	
	 	for(int k = 1; k < len; k++){
	 		cout<<"*";
	 	}
	 	
	 }
	 else{
	    cout << " ";
		//for loop to print star
		for(int j = 1; j <= (2 * len - 1); j++)
		{
			if(i == len || j == 1 || j == 2*i - 1)
			cout << "*";
			else
			cout << " ";
		}
		
		cout << "\n";
	 }
}
return 0;
}