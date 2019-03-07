#/bin/bash
#Author name: Kate Torres
#Program name: Sum of an Array
#Assignment number: 2
rm *.o, *.lis, *.out

echo "Assemble the X86 file h2arith.asm"
nasm -f elf64 -l h2arith.lis -o h2arith.o h2arith.asm

echo "Assemble the C++ file h2driver.cpp"
gcc -c -m64 -Wall -l h2driver.lis -o h2driver.o -fno-pie -no-pie h2driver.cpp

echo "Link the 'O' files h1driver.o and h1arith.o"
gcc -m64 -fno-pie -no-pie -o h.out h2driver.o h2arith.o

echo "Run the Startying out with X86 Program"
./h.out