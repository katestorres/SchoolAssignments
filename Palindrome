//Palindrome checker using loops, Fall 2016
#include <iostream>
#include <string>
using namespace std;
char Check(string name)
{
	int lower=0, lengths;
	char answer='Y';
	string temp;
	lengths = name.length();
	lengths--;
	do{
		if(tolower(name[lower])==tolower(name[lengths]))
		{
			lower++;
			lengths--;
		}
		else { answer = 'N'; return answer; }
	} while (lengths>=0);
	return answer;
}
int main()
{
//Ask for the word
	string name;
	char answer;
	cout << "Enter a word: ";
	getline(cin, name);
//Check
	answer = Check(name);
//Palindrome?
	if(answer == 'Y')
	{
		cout << name << " is a palindrome\n";
	}
	else
	{
		cout << name << " is not a palindrome\n";
	}
//Terminate program
	system("pause");
	return 0;
}
