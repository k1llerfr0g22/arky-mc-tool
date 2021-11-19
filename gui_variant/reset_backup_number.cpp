#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int backup_count;

void get_backup_number()
{
	fstream myFile;
	myFile.open("backup_count.txt", ios::in);
	myFile >> backup_count;	
};

int main()
{
	get_backup_number();
	backup_count = 0;
	system("rm backup_count.txt");
	system("touch test.txt");
	fstream myFile;
	myFile.open("backup_count.txt", ios::out);
	myFile << backup_count << endl;
	myFile.close();
}
