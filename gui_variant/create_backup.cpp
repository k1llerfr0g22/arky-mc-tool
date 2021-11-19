#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <physfs.h>
#include <sys/types.h>
#include <thread>
#include <cstdlib>
#include <chrono>
using namespace std;


int backup_count;
int final_backup_count;
int one = 1;

bool running = true;
bool auto_backup;

string command_var;
string user_prompt = "   \e[1mUSER:\e[0m  ";
string pc_prompt = "   \e[1mPC:\e[0m    ";
string three_spaces = "   ";
string backup_name;
string backup_;

void get_backup_name()
{
  backup_name = "backup_" + backup_ + to_string(backup_count);
};

void get_backup_number()
{
  fstream myFile;
  myFile.open("backup_count.txt", ios::in);
  myFile >> backup_count;
  final_backup_count = one + backup_count;
};

void add_backup_number()
{
  backup_count += 1;
  system("rm backup_count.txt");
  //system("touch test.txt");
  fstream myFile;
  myFile.open("backup_count.txt", ios::out);
  myFile << backup_count << endl;
  myFile.close();
};

void setup()
{
  // HERE ALL GET FUNCTIONS!!!!
  get_backup_number();
  get_backup_name();
}

int main()
{
	get_backup_number();
	get_backup_name();
	add_backup_number();

    backup_count += 1;
    system("rm backup_count.txt");
    //system("touch test.txt");
    fstream myFile;
    myFile.open("backup_count.txt", ios::out);
    myFile << backup_count << endl;
    myFile.close();

    system("cd /home/k1llerfr0g/code/c++/projects/mc-server-tool/ && python3 backup.py");
}
