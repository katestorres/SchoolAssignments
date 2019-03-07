//Author name: Kate Torres
//Proram name: Sum of a Sequence
//Names of the files in this programming: h2arith.asm, h2bash.sh, h2driver.cpp
//Course number: CPSC 240
//Scheduled delivery date: February 18, 2019
//Program purpose: Computer the sum of an sequence of signed integers
//Status: In progress
//Date of last modification: February 10, 2019
//============================================
//Information about this module:
//This module purpose: Driver for Sum of a Sequence
//File name of this module: h2driver.cpp
//Compile this module: gcc -c -m64 -Wall -l h2driver.lis -o h2driver.o -fno-pie -no-pie h2driver.cpp
//Link this module with other objects: gcc -m64 -fno-pie -no-pie -o h.out h2driver.o h2arith.o

#include <stdio.h>
#include <stdlib.h>

extern "C" long int h2arith();

int main(int argc, char* argv[]){
	long int sum;
	printf("Welcome to summing a sequence of integers.\n");
	printf("This program was brought to you by Kate Torres.\n");

	sum = h2arith();

	printf("This program recieved this number: %4ld\n", sum);
	printf("Main will now return 0 to the operating system. Have a nice day\n");
	return 0;
}