//Author name: Kate Torres
//Program title: Starting out with X86
//Files in this program: h1driver.c, h1arith.asm, h1bash.sh
//Course number: CPSC 240
//Assignment number: 1
//Required delievery date: Feb 4, 2019 before 11:59pm
//Purpose: learn how to embed C library functions calls in an X86 module.
//Language of this module: C
//Compile this module: gcc -c -m64 -Wall -l h1driver.lis -o h1driver.o -fno-pie -no-pie h1driver.c
//Link object files: gcc -m64 -fno-pie -no-pie -o h.out h1driver.o h1arith.o
//Exectute: ./h.out

#include <stdio.h>
#include <stdlib.h>

long int h1arith();

int main(int argc, char* argv[]){
	long int remainder;
	printf("Welcome to Starting out with X86\n");
	printf("This program was created by Kate Torres\n");
	printf("and completed on January 31, 2019\n");
	
	remainder = h1arith();

	printf("The driver function has recieved this number: %4ld",remainder);
	printf("\rThe driver will now return 0 to the operating system. Have a nice day.\r");
	return 0;
}