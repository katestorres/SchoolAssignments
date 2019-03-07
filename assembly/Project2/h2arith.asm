;Author name: Kate Torres
;Program name: Sum of a Sequence
;Names of the files in this programming: h2arith.asm, h2bash.sh, h2driver.cpp
;Course number: CPSC 240
;Scheduled delivery date: February 18, 2019
;Program purpose: Computer the sum of an sequence of signed integers
;Status: In progress
;Date of last modification: February 10, 2019
;============================================
;Information about this module:
;File name of this module: h2arith.asm
;Lanugage of this module: X86 with Intel Syntax
;Compile this module: nasm -f elf64 -l h2arith.lis -o h2arith.o h2arith.asm
;============================================

extern printf				;Be able to use C function printf
extern scanf				;Be able to use C function scanf
global h2arith				;Enable program to be called from outside the function

;===================Declare messages===============

segment .data				;Initialize data here



mess1 db "The fast accumulator program written in X86 Intel language has begun", 10, 0

mess2 db "Instructions: Enter a sequence of integers. Include a white space between each number", 10, 0

mess3 db "To terminate press 'Enter' followed by Control+D", 10, 0

enterprompt db "Enter integer: ", 10, 0

messsum db "Thank you. You entered %ld numbers with a sum equal to %ld.", 10, 0

messex db "The X86 function will now return to the caller function. Bye.", 10, 0

stringformat db "%s", 0			;General string format

eightbyteformat db "%ld", 0		;General 8-byte format

;=================================================

segment .bss

;this segment is empty

;==================================================
;====================Begin=========================
;==================================================

segment .text				;Executable instructions
 
h2arith:				;Execution begins here

;Next two instruction required
push		rbp			;Marks the start of a new stack
mov		rbp, rsp		;rbp holds the addresses of the stack frame

push 		qword 0			;Ints are qwords

;---------------------------------------------------

;Print mess1
mov qword 	rax, 0			;No data from SSE will be printed
mov		rdi, stringformat	;"%s"
mov		rsi, mess1		;Push mess1 into the stack
call		printf			;Print mess1

;Print mess2
mov qword	rax, 0			;No data from SSE will be printed
mov		rdi, stringformat	;"%s"
mov		rsi, mess2		;Push mess2 into stack
call 		printf			;Print mess2

;Print mess3
mov qword	rax, 0			;No data from SSE will be printed
mov		rdi, stringformat	;"%s"
mov		rsi, mess3		;Push mess3 into stack
call		printf			;Push mess3

;Make variables
mov		r12, 0 			;total
mov		r13, 0			;counter

startofloop:

;Enter integers

;Print enterprompt
mov qword	rax, 0			;No data from SSE will be printed
mov		rdi, stringformat	;"%s"
mov		rsi, enterprompt	;Push enterprompt into the stack
call		printf			;Print enterprompt

;Take input
push qword	0			;Push 64 0's onto the stack
mov qword	rdi, 0			;SSE is not involved
mov		rdi, eightbyteformat	;"%ld"
mov		rsi, rsp		;Give scanf a pointer to reserved space
call		scanf			;Get input

;Check for control+D
cdq					;Place into rdx sign-extension of that 32 bit integer
shl 		rdx, 32			;Shift sign extension 32 bits to the left
or 		rax, rdx		;Perform the operation to rax = rax or rdx
cmp		rax, -1			;Compare with -1

je		endofloop		;End loop

pop		r15			;Store input to r15

;If integer input
inc		r13			;Increment counter by one
add		r12, r15		;Add r15 to r12
jmp 		startofloop		;return to start of loop


;Exit out of function
endofloop:				;Loop ends here
pop		rax			;Open space up used by scanf

;Print messsum
mov qword	rax, 0			;No data from SSE will be printed
mov		rdi, messsum		;Push messsum into stack
mov		rsi, r13		;Push counter into stack
mov		rdx, r12		;Push total into stack
call 		printf			;Print messsum

;Print messex
mov qword	rax, 0			;No data from SSE will be printed
mov		rdi, stringformat	;"%s"
mov		rsi, messex		;Push messex into stack
pop		rax			;match the top push rax
call 		printf			;Print messex

;Move total to rax
mov		rax, r12		;Move r12 to rax		

;Return to driver
pop		rbp			;Return stack to start
ret					;Return to driver