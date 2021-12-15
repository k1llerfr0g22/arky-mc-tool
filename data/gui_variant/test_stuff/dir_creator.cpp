#include <fstream>
#include <string>
#include <stdio.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <physfs.h>
#include <sys/types.h>
#include <thread>
#include <cstdlib>
using namespace std;

string lol = "/home/k1llerfr0g/code/c++/projects/mc-server-tool/test_stuff/lol12345";

int main()
{
	//system("mkdir lol1234");
	//system("mkdir " + char(lol));	
	mkdir("/home/k1llerfr0g/code/c++/projects/mc-server-tool/test_stuff/loooool", 0700);
	mkdir(lol, 0700);
}
