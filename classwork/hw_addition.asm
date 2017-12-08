;confer algorithm

;iterate through and copy stage

!0
	alpha "10+=$XAB"
	left
	bra !1

!1
	draw '$', R
	bra !2

!2
	bra 'A', !2_AB
	bra 'B', !2_AB
	bra '+', !2_+
	bra '0', !2_0
	bra '1', !2_1
	
!2_AB
	right
	bra !2
!2_+
	left
	bra !3
!2_0
	draw 'A', r
	bra !4
!2_1
	draw 'B', r
	bra !5
!3	; can be more efficient
	bra ^'$', !3_^$
	bra '$', !3_$
!3_^$
;	right
	left
	bra !3
!3_$
	right
	bra !11
; come back here and continue off to 11

!4	;can be more efficient
	bra ^blank, !4_^b
	bra !4_b
!4_^b
	right
	bra !4
!4_b
	draw '0', L
	bra !6
!5	;can be more efficient
	bra ^blank, !5_^b
	bra !5_b
!5_^b
	right 
	bra !5
!5_b
	draw '1', L
	bra !6	
!6	; can be more efficient
	bra ^'=', !6_^=
	bra !6_=
!6_^=
	left
	bra !6
!6_=
	left
	bra !7
!7
	bra 'A', !7_AB
	bra 'B', !7_AB
	bra '0', !7_0
	bra '1', !7_1
!7_AB
	left
	bra !7
!7_0
	draw 'A', L
	bra !8
!7_1
	draw 'B', L
	bra !9
!8
	bra ^blank, !8_^b
	draw '0', r
	bra !10
!8_^b
	left
	bra !8
!9
	bra ^blank, !9_^b
	draw '1', r
	bra !10
!9_^b
	left
	bra !9
!10
	bra ^'$', !10_^$
	right
	bra '$', !10_$
!10_$
	right
	bra !2
!10_^$
	right 
	bra !10
!11
	bra 'A', !11_AX
	bra 'X', !11_AX
	bra '+', !11_+
	bra 'B', !11_B
	right
	bra !17
;continue this branch at 17
!11_AX
	draw 'X', r
	bra !11
!11_B
	right
	bra !12	
!11_+
	right 
	bra !17
!12
	bra ^'+', !12_^+
	left
	bra !13
!12_^+
	right
	bra !12
!13
	bra 'A', !13_A
	draw 'A', L
	bra !14
!13_A
	draw 'B', L
	bra !13
!14
	bra ^'$', !14_^$
	left
	bra !15
!14_^$
	left 
	bra !14
!15
	bra '1', !15_1
	bra blank, !15_b0
	bra '0', !15_b0
!15_1
	draw '0', L
	bra !15
!15_b0
	draw '1', r
	bra !16
!16
	bra ^'$', !16_^$
	right
	bra !11
!16_^$
	right
	bra !16
!17
	bra ^blank, !17_^b
	left
	bra !18
!17_^b
	right
	bra !17
!18
	bra '0', !18_0
	bra '1', !18_1
	left
	bra !21
!18_1
	draw blank, L
	bra !20
!18_0
	draw blank, L
	bra !19
!19
	bra ^'X', !19_^X
	draw '0', r
	bra !17
!19_^X
	left
	bra !19
!20
	bra ^'X', !20_^X
	draw '1', r
	bra !17
!20_^X
	left
	bra !20
!21
	bra 'B', !21_B
	bra 'A', !21_A
	left
	bra !22
!21_B
	draw '1', L
	bra !21
!21_A
	draw '0', L
	bra !21
!22
	bra ^blank, !22_^b
	right
	bra !23
!22_^b
	left
	bra !22
!23
	bra '0', !23_0
	bra '1', !23_1
	draw blank, r
	halt
!23_0
	draw blank, r
	bra !24
!23_1
	draw blank, r
	bra !25
!24
	bra ^blank, !24_^b
	draw '0', L
	bra !22
!24_^b
	right 
	bra !24
!25
	bra ^blank, !25_^b
	draw '1', L
	bra !22
!25_^b
	right
	bra !25
