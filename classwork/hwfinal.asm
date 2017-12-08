;Bryer Jeannotte sunyat asm assignment
;Borrowed some of Prof. Confers code examples
;such as print string and read letter

; specify .variable and .constant shit
;make labels like this !main


;ask for 'number 0-255: [user enters num]
;take in literally number at a time
;perform alg. to change its base and shit
;print back 'same as: 0x[hex addr]

;-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

.constant	TERM	0xFF	;terminal addr

	jmp	!main

.variable	key
.variable	left_hex
.variable	right_hex

!prompt
.variable	prompt0	'n'
.variable	prompt1	'u'
.variable	prompt2	'm'
.variable	prompt3	'b'
.variable	prompt4	'e'
.variable	prompt5	'r'
.variable	prompt6	' '
.variable	prompt7	'0'
.variable	prompt8	'-'
.variable	prompt9	'2'
.variable	prompt10 '5'
.variable	prompt11 '5'
.variable	prompt12 ' ' 
.variable	prompt13 0xD 
.variable	prompt14 0xA
.variable	prompt15 0

!output
.variable	output0	's'
.variable	output1	'a'
.variable	output2	'm'
.variable	output3	'e'
.variable	output4	' '
.variable	output5	'a'
.variable	output6	's'
.variable	output7	':'
.variable	output8	' '
.variable	output9	'0'
.variable	output10 'x'
.variable	output11 0

!hex
.variable	hex0 '0'
.variable	hex1 '1'
.variable	hex2 '2'
.variable	hex3 '3'
.variable	hex4 '4'
.variable	hex5 '5'
.variable	hex6 '6'
.variable	hex7 '7'
.variable	hex8 '8'
.variable	hex9 '9'
.variable	hex10 'A'
.variable	hex11 'B'
.variable	hex12 'C'
.variable	hex13 'D'
.variable	hex14 'E'
.variable	hex15 'F'

;remember to add our hex plus 0

;-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
!main
	mov	R7	!prompt
	call	!print_string
	call	!read_letters

	mov	R7	!output
	call	!print_string

	load	R0	key	;this is total
	call	!hex_conv

	ret

!main_end

!print_string
	push R6
	push R7

;print until null or while(mem[R7]!=0){print(mem[R7];R7++} in c

;-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
!while_ps
	loadp	R6	R7
	cmp	R6	0
	jeq	!while_ps_end
	stor	TERM	R6
	add	R7	1
	jmp	!while_ps

!while_ps_end
	pop	R7
	pop	R6
	ret

!print_string_end

;-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
;take in keystrokes then apply base change algorithm

!read_letters
	push	R0
	push 	R5
	mov	R5	0	;total
		
!do_rl
	load	R0	TERM
	
!do_rl_while
	cmp	R0	0xD
	jeq	!do_rl_end
	cmp	R0	0xA
	jeq	!do_rl_end

	cmp	R0	'0'
	jls	!do_rl ;ctrl characters before chars in ascii
	jeq	!alg
	cmp	R0	'9'
	jgr	!do_rl
	jeq	!alg

!alg
	sub	R0	'0'
	mul	R5	10
	add	R5	R0
	jmp 	!do_rl

!alg_end

!do_rl_end
	stor	key	R5
	pop	R5
	pop	R0
	ret

!read_letters_end

;-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

!hex_conv
; ** im so upset that this doesnt have a bit shift instruction or modulo**
!h_c
	push	R0
	push	R1
	load	R0	key
	mov	R1	R0
	mov	R6	!hex

	cmp	R0	16
	jls	!one_num
	jmp	!two_num

!one_num
	mov	R0	0
	and	R1	0xF	;crap way for bit mask::R hexnum
	jmp	!array_lookup
	
!two_num
	div	R0	16	;leftmost hex num
	and	R1	0xF	;Rightmost num
	jmp	!array_lookup

!array_lookup
	;loadp	R5	R6	;iterates through array
	mov	R3	0	;counter
	jmp	!do_a_l1

!do_a_l1
	mov	R6	!hex
	loadp	R5	R6
	mov	R3	0

!do_shit
	loadp	R5	R6
	cmp	R0	R3
	jeq	!do_a_l2
	add	R3	1
	add	R6	1
	jmp	!do_shit

!do_a_l2
	mov	R6	!hex	
	stor	TERM	R5
	loadp	R5	R6	;iterates through array
	mov	R3	0	;counter

!do_while_thing
	loadp	R5	R6
	cmp	R1	R3
	jeq	!h_c_end
	add	R3	1
	add	R6	1
	jmp	!do_while_thing

!h_c_end
	stor	TERM	R5
	pop	R1
	pop	R0
	ret


!hex_conv_end
