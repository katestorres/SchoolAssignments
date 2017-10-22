//Reviewing structs, Spring 2017
/* ************************
	Katy Torres
	Wednesday Lab
***************************	*/
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;
struct Employee
{
	string name;
	float salary;
	int years;
};
const int ARRSIZE = 5;
Employee getData();
void total(Employee[], int, float&, float&);
void print(Employee[], int, float, float);

int main()
{
	Employee employees[5];
	char repeat = 'Y';
	float averagey = 0, averages = 0;
	int datasize = 0;
	do
	{
		employees[datasize] = getData();
		cout << "Enter another employee? ";
		cin >> repeat;
		datasize++;
		if (toupper(repeat) != 'Y' && toupper(repeat) != 'N')
			do
			{
				cout << "Enter Y for yes or N for no: ";
				cin >> repeat;
			} while (toupper(repeat) != 'Y' && toupper(repeat) != 'N');
	} while (repeat == 'Y' && datasize < ARRSIZE);
	total(employees, datasize, averagey, averages);
	print(employees, datasize, averagey, averages);
	system("pause");
	return 0;
}
/* ***********************
getData
gets employee information
************************** */
Employee getData()
{
	Employee temp;
		cout << "Enter employee name: \n";
		getline(cin, temp.name);
		cout << "Enter years of service: ";
		cin >> temp.years;
		if (temp.years < 0)
		{
			do
			{
				cout << "Please enter a positive value: ";
				cin >> temp.years;
			} while (temp.years < 0);
		}
		cout << "Enter salary: ";
		cin >> temp.salary;
		if (temp.salary < 0)
		{
			do
			{
				cout << "Please enter a positive value: ";
				cin >> temp.salary;
			} while (temp.salary < 0);
			cin.ignore();
		}
	return temp;
}
	/* ***********************
	total
	gets average years and salary
	************************** */
	void total(Employee employees[], int d, float& years, float& salary)
	{
		float totaly = 0, totals = 0;
		for (int i = 0; i < d; i++)
		{
			totaly += employees[i].years;
			totals += employees[i].salary;
		}
		years = totaly / d;
		salary = totals / d;
	}
	/* ***********************
	print
	print results
	************************** */
	void print(Employee employees[], int d, float y, float s)
	{
		cout << fixed << showpoint;
		cout << "Employee data\n\n";
		cout << left << setw(15) << "Name" << right << setw(6) << "Years"
			<< setw(10) << "Salary\n";
		for (int i = 0; i < d; i++)
		{
			cout << left << setw(15) << employees[i].name << right << setw(6)
				<< setprecision(0) << employees[i].years << setw(10) << setprecision(2)
				<< employees[i].salary << endl;
		}
		cout << endl;
		cout << left << setw(15) << "Average" << right << setw(6) << setprecision(1)
			<< y << setw(10) << setprecision(2) << s << endl;
	}
