// ------------- INCLUDES ------------- //

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


//---------------- IDK --------------- //

using namespace std;


// --------------- COLORS ------------- //

#define RESET   "\033[0m"
#define BLACK   "\033[30m"      /* Black */
#define RED     "\033[31m"      /* Red */
#define GREEN   "\033[32m"      /* Green */
#define YELLOW  "\033[33m"      /* Yellow */
#define BLUE    "\033[34m"      /* Blue */
#define MAGENTA "\033[35m"      /* Magenta */
#define CYAN    "\033[36m"      /* Cyan */
#define WHITE   "\033[37m"      /* White */
#define BOLDBLACK   "\033[1m\033[30m"      /* Bold Black */
#define BOLDRED     "\033[1m\033[31m"      /* Bold Red */
#define BOLDGREEN   "\033[1m\033[32m"      /* Bold Green */
#define BOLDYELLOW  "\033[1m\033[33m"      /* Bold Yellow */
#define BOLDBLUE    "\033[1m\033[34m"      /* Bold Blue */
#define BOLDMAGENTA "\033[1m\033[35m"      /* Bold Magenta */
#define BOLDCYAN    "\033[1m\033[36m"      /* Bold Cyan */
#define BOLDWHITE   "\033[1m\033[37m"      /* Bold White */

// --------------- COMMENTS ------------- //
/*

FUNCTIONS:

getchar()             WAIT'S UNTIL I HIT A KEY
get_backup_number()   FIND'S OUT NUMBER OF BACKUPS AND PUT THE NUMBER IN VAR: final_backup_count
add_backup_number()
cout_backup_number()  COUT'S THE NUMBER OF BACKUPS
permanent_backup()    CREATES A BACKUP


COLORS:

EXAMPLE:
cout << pc_prompt << RED << "hello world" << RESET << endl;


*/
// -------------- VARIABLES ------------- //

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

//  ------------ FUNCTIONS ------------ //

void reset_backup_count()
{
  backup_count = 0;
  system("rm backup_count.txt");
  system("touch test.txt");
  fstream myFile;
  myFile.open("backup_count.txt", ios::out);
  myFile << backup_count << endl;
  myFile.close();
}


/*
void auto_backup(auto_backup)
{
  while(auto_backup == true)
  {
    sleep(5000);

    backup_count += 1;
    system("rm backup_count.txt");
    system("touch test.txt");
    fstream myFile;
    myFile.open("backup_count.txt", ios::out);
    myFile << backup_count << endl;
    myFile.close();

    system("cd /home/k1llerfr0g/code/c++/projects/mc-server-tool/ && python3 backup.py");

  }
}*/


void test_backup_system()
{
  system("cd ~/code/server/minecraft/aternos/ && cp world -r ~/code/server/minecraft/aternos/backup/lol");
  system("ls ~/code/server/minecraft/aternos/backup/lol");
}

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

/*void create_backup()
{

  system("/home/k1llerfr0g/code/c++/projects/mc-server-tool && python3 backup.py");
}*/

// THE FUNCTION create_backup DOES'NT WORK IDK WHY...

void cout_backup_number()
{
  cout << final_backup_count << endl;
};

void use_permanent_backup()
{
  system("cd ~/code/server/minecraft/aternos && rm -rf world");
  system("cd ~/code/server/minecraft/aternos/backup/permanent_backup && cp world/ -r ~/code/server/minecraft/aternos/");
};

void show_servers()
{
  system("cd ~/code/server/minecraft && ls");
};

void edit_server_probs()
{
  system("cd ~/code/server/minecraft/aternos/ && nano server.properties");
};

void permanent_backup()
{
  system("cd ~/code/server/minecraft/aternos/backup/permanent_backup && rm -rf world/");
  system("cd ~/code/server/minecraft/aternos/ && cp world/ -r ~/code/server/minecraft/aternos/backup/permanent_backup/");
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


void welcome()
{
  cout << "Hello, welcome to my program" << endl;
  system("clear");
};


void clear()
{
  system("clear");
};


void list_backups()
{
  system("ls ~/code/server/minecraft/aternos/backups");
};

void setup()
{
  // HERE ALL GET FUNCTIONS!!!!
  get_backup_number();
  get_backup_name();
}

void command()
{
  if (command_var == "add_backup_number")
  {
    add_backup_number();
    cout << pc_prompt << BOLDGREEN << "BACKUP COUNT ADDED SUCCSESFULL" << RESET << endl;

  }

  if (command_var == "lol")
  {
    cout << pc_prompt << "lollll" << endl;
  }

  if (command_var == "create_backup")
  {
    // add_backup_number();
    // create_backup();

    backup_count += 1;
    system("rm backup_count.txt");
    system("touch test.txt");
    fstream myFile;
    myFile.open("backup_count.txt", ios::out);
    myFile << backup_count << endl;
    myFile.close();

    system("cd /home/k1llerfr0g/code/c++/projects/mc-server-tool/ && python3 backup.py");
  }

  if (command_var == "stop")
  {
    running = false;
  }

  if (command_var == "make_simple_backup")
  {
    permanent_backup();
    cout << pc_prompt << BOLDGREEN << "BACKUP CREATED SUCCSESFULL" << RESET << endl;
  }

  if (command_var == "backup_name")
  {
    get_backup_name();
    get_backup_number();
    cout << pc_prompt << "name of new backup would be: " << backup_name << endl;
    cout << backup_name;
  }

  if (command_var == "backup_count")
  {
    get_backup_number();
    cout << pc_prompt << "the count of backups are: " << backup_count << endl;
  }

  if (command_var == "edit_server_config")
  {
    edit_server_probs();
  }

  if (command_var == "reset_backup_count")
  {
    reset_backup_count();
  }

  if (command_var == "list_backups")
  {
    cout << pc_prompt << "availible backups are" << endl;
    list_backups();
  };

};


//  ------------ THE START ----------- //

int main()
{
  clear();
  setup();
  while (running == true) // MAINLOOP
  {
    setup();
    cout << user_prompt;
    cin >> command_var;
    command();
  }
}
