//Dice rolling in Spring 2017
/* **********************
	Katy Torres
	Wednesday Lab
	Program #2
   ********************** */
#include <iostream>
#include <ctime>
#include <iomanip>
using namespace std;
int main()
{
	srand(time(0));

	int tries, goal=0, i, total=0, die1, die2, diet;
	double average;

	do 
	{ 
		cout << "Enter a number between 2 and 12: ";
		cin >> goal;
	} while (goal < 2 || goal > 12 );
	do
	{
		cout << "How many tries do you want? ";
		cin >> tries;
	} while (tries < 1);

	for(i=0; i<tries; i++)
	{
		die1 = (rand()) % 5 + 1;
		die2 = (rand()) % 5 + 1;
		diet = die1 + die2;
		total += diet;
		cout << "found " << goal << " on roll " 
			<< diet << endl;
	}
	average = double(total) / tries;
	cout << fixed << showpoint << setprecision(1);
	cout << "In " << tries << " tries, found " << goal
		<< " in an average of " << average << " rolls\n";
	return 0;
}
