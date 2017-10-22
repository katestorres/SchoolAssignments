//Function review with triangles, Spring 2017
/* **************************
	menu
	Ask for choice from menu
	1-4, accept int 1-4
***************************** */
int menu()
{
	int choice;
	cout << "What triangle do you want to draw?\n";
	cout << "1 - Left-Top-Big\n2 - Left-Bottom-Big\n";
	cout << "3 - Right-Top-Big\n4 - Right-Bottom-Big\n";

	do {
		cin >> choice;
		if (choice >= 1 && choice <= 4) return choice;
		else
		{
			cout << "Illegal choice, try again: ";
		}
	} while (choice < 1 || choice > 4);
}
/* **************************
	getSize
	Ask for choice from 1-10,
	repeat until 1-10 is 
	recieved
***************************** */
int getSize()
{
	int choice;
	cout << "Please enter the maximum size(1-10): ";
	do {
		cin >> choice;
		if (choice >= 1 && choice <= 10) return choice;
		else
		{
			cout <<"Size must be in the range 1-10, please try again: ";
		}
	} while (choice < 1 || choice > 10);

}
/* **************************
	getRepeatChoice
	Ask for choice y or n,
	repeat until y or n is
	recieved
***************************** */
char getRepeatChoice()
{
	char choice;
	cout << "Draw another?(Y/N) ";
	do {
		cin >> choice;
		switch(toupper(choice))
		{
		case 'Y': case 'N': return choice; break;
		default:cout << "Please enter Y for yes or N for no: ";
		}
	} while (choice != 'Y' || choice != 'N');
}
/* **************************
	leftTopBig
	Draw a triangle with left
	top big
***************************** */
void leftTopBig(int a)
{
	int i, j;
	for(i=a; i>0;i--)
	{
		for (j = i; j > 0; --j) cout << "* ";
		cout << endl;
	}
}
/* **************************
	leftBotBig
	Draw a triangle with left
	bottom big
***************************** */
void leftBotBig(int a)
{
	int i, j;
	for (i = 1; i <= a; i++)
	{
		for (j = 1; j <= i; j++) cout << "* ";
		cout << endl;
	}
}
/* **************************
	rightTopBig
	Draw a triangle with right
	top big
***************************** */
void rightTopBig(int a)
{
	int i, j, k;
	for (i = a; i > 0; i--)
	{
		for (k = 0; k < a-i; k++) cout << "  ";
		for (j = i; j > 0; j--) cout << "* ";
		cout << endl;
	}
}
/* **************************
	rightBotBig
	Draw a triangle with right
	bottom big
***************************** */
void rightBotBig(int a)
{
	int i, j, k;
	for (i = 0; i <= a; i++)
	{
		for (k = 0; k < a-i; k++) cout << "  ";
		for (j = 1; j <= i; j++) cout << "* ";
		cout << endl;
	}
}
