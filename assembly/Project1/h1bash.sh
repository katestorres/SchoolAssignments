#/bin/bash
#Author name: Kate Torres
#Program name: Starting out with X86
#Assignment number: 1
rm *.o, *.lis, *.out

echo "Assemble the X86 file h1arith.asm"
nasm -f elf64 -l h1arith.lis -o h1arith.o h1arith.asm

echo "Assemble the C file h1driver.c"
gcc -c -m64 -Wall -l h1driver.lis -o h1driver.o -fno-pie -no-pie h1driver.c

echo "Link the 'O' files h1driver.o and h1arith.o"
gcc -m64 -fno-pie -no-pie -o h.out h1driver.o h1arith.o

echo "Run the Startying out with X86 Program"
./h.out