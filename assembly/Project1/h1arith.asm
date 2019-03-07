;Author name: Kate Torres
;Program title: Starting out with X86
;Files in this program: h1driver.c, h1arith.asm, h1bash.sh
;Course number: CPSC 240
;Assigment number: 1
;Required delievery date: Feb 4, 2019 before 11:59pm
;Purpose: Learn how to embed C library function calls in an X86 module.
;Language of this module: X86 with Intel syntax
;Compile this module: nasm -f elf64 -l h1arith.lis -o h1arith.o h1arith.asm

extern printf				;Be able to use C function printf
extern scanf				;Be able to use C function scanf
global h1arith				;Enable program to be called from outside the function
segment .data				;Initialize data here

;===================Declare messages===============


firstprompt db "Please enter the first integer:", 10, 0

secondprompt db "Please enter the second integer:", 10, 0

product db "The product of these two integers is: %ld", 10, 0

quotient db "The quotient of these two integeres is %ld with the remainder %ld:", 10,0

goodbye db "This assembly function will now return to the driver", 10, 0

stringformat db "%s", 0			;General string format

eightbyteformat db "%ld", 0		;General 8 byte format

;--------------------------------------------------

segment .bss 

;This section is empty

;==================================================
;====================Begin=========================
;==================================================

segment .text				;Executable instructions
 
h1arith:				;Execution begins here

;Next two instruction required
push	rbp				;Marks the start of a new stack
mov	rbp, rsp			;rbp holds the addresses of the stack frame

push 	qword 0				;Ints are qwords

;---------------------------------------------------

;Print firstprompt
;Not understanding why it's outputting 19Torres here

mov qword 	rax, 0			;No data from SSE will be printed
mov		rdi, stringformat	;"%s"
mov		rsi, firstprompt	;Push firstprompt into the stack
call		printf			;Print firstprompt

;Scan first integer
push qword	0			;push 64 0's onto stack
mov qword	rdi, 0			;SSE is not involved in this operation
mov 		rdi, eightbyteformat	;"%ld"
mov		rsi, rsp		;Give scanf a pointer to the reserved space
call 		scanf			;get input
pop 		r12			;store input to r12

;Print secondprompt
;Segmentation fault here xFIXED
mov qword 	rax, 0			;No data from SSE will be printed
mov		rdi, stringformat	;"%s"
mov		rsi, secondprompt	;Push secondprompt into the stack
call		printf			;Print secondprompt

;Scan second integer
;Issue here, not letting me read the second input, says 0 instead
;throwing error that you can't divide by 0
push qword	0			;push 64 0's onto stack
mov qword	rdi, 0			;SSE is not involved in this operation
mov 		rdi, eightbyteformat	;"%ld"
mov		rsi, rsp		;Give scanf a pointer to the reserved space
call 		scanf			;get input
pop 		r14			;store input to r14

;pop		rax			;Open up space used by scanf

;Multiply integers
mov		r15, r12		;copy r12 into r15 for later
imul		r12, r14		;multiply r12 by r14, store in r12

;Display product
mov qword 	rax, 0			
mov		rdi, product		;move product statement to rdi
mov		rsi, r12		;move product answer to rsi
call		printf			;Print product statement

;Divide integers
mov		rax, r15		;mov r15 into rax
cqo					;extend rax to rdx
idiv		r14			;divide rax by r14, store in rdx and rax
mov		r9, rax			;store quotient in r9
mov		r15, rdx		;move remainder to r15

;Display quotient and remainder
mov qword 	rax, 0			
mov		rdi, quotient		;move quotient statement to rdi
mov		rsi, r9 	    	;move quotient answer to rsi
mov		rdx, r15		;move remainder answer to rsp
call		printf			;Print quotient

;Exit statement
mov qword 	rax, 0			
mov		rdi, goodbye 		;move goodbye statement to rdi
pop		rax
call 		printf			;print goodbye


;Copy number to rax
;mov		rax, r15 		;is already there?	

;Return to driver
pop		rbp			;return stack to start
ret					;return to driver