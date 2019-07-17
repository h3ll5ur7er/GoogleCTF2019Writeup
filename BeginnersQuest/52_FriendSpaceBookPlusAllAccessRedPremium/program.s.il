mov	acc1, 0
push	acc1
mov	acc1, 17488
push	acc1
mov	acc1, 16758
push	acc1
mov	acc1, 16599
push	acc1
mov	acc1, 16285
push	acc1
mov	acc1, 16094
push	acc1
mov	acc1, 15505
push	acc1
mov	acc1, 15417
push	acc1
mov	acc1, 14832
push	acc1
mov	acc1, 14450
push	acc1
mov	acc1, 13893
push	acc1
mov	acc1, 13926
push	acc1
mov	acc1, 13437
push	acc1
mov	acc1, 12833
push	acc1
mov	acc1, 12741
push	acc1
mov	acc1, 12533
push	acc1
mov	acc1, 11504
push	acc1
mov	acc1, 11342
push	acc1
mov	acc1, 10503
push	acc1
mov	acc1, 10550
push	acc1
mov	acc1, 10319
push	acc1
mov	acc1, 975
push	acc1
mov	acc1, 1007
push	acc1
mov	acc1, 892
push	acc1
mov	acc1, 893
push	acc1
mov	acc1, 660
push	acc1
mov	acc1, 743
push	acc1
mov	acc1, 267
push	acc1
mov	acc1, 344
push	acc1
mov	acc1, 264
push	acc1
mov	acc1, 339
push	acc1
mov	acc1, 208
push	acc1
mov	acc1, 216
push	acc1
mov	acc1, 242
push	acc1
mov	acc1, 172
push	acc1
mov	acc1, 74
push	acc1
mov	acc1, 49
push	acc1
mov	acc1, 119
push	acc1
mov	acc1, 113
push	acc1
mov	acc1, 119
push	acc1
mov	acc1, 106
push	acc1
mov	acc2, 1

:label_func01
pop acc1
push	acc2
push	acc1
mov	acc1, 389
push	acc1
push	acc2
jmp label_func04
xor
print
mov	acc1, 1
push	acc1
add
pop acc2
push acc1
if_not_zero
jmp label_func01
endif

mov	acc1, 98426
push	acc1
mov	acc1, 97850
push	acc1
mov	acc1, 97604
push	acc1
mov	acc1, 97280
push	acc1
mov	acc1, 96815
push	acc1
mov	acc1, 96443
push	acc1
mov	acc1, 96354
push	acc1
mov	acc1, 95934
push	acc1
mov	acc1, 94865
push	acc1
mov	acc1, 94952
push	acc1
mov	acc1, 94669
push	acc1
mov	acc1, 94440
push	acc1
mov	acc1, 93969
push	acc1
mov	acc1, 93766
push	acc1
mov	acc2, 99

:label_func02
pop acc1
push	acc2
push	acc1
mov	acc1, 568
push	acc1
push	acc2
jmp label_func04
xor
print
mov	acc1, 1
push	acc1
add
pop acc2
if_not_zero
jmp label_func02
endif

mov	acc1, 101141058
push	acc1
mov	acc1, 101060206
push	acc1
mov	acc1, 101030055
push	acc1
mov	acc1, 100998966
push	acc1
mov	acc1, 100887990
push	acc1
mov	acc1, 100767085
push	acc1
mov	acc1, 100707036
push	acc1
mov	acc1, 100656111
push	acc1
mov	acc1, 100404094
push	acc1
mov	acc1, 100160922
push	acc1
mov	acc1, 100131019
push	acc1
mov	acc1, 100111100
push	acc1
mov	acc1, 100059926
push	acc1
mov	acc1, 100049982
push	acc1
mov	acc1, 100030045
push	acc1
mov	acc1, 9989997
push	acc1
mov	acc1, 9981858
push	acc1
mov	acc1, 9980815
push	acc1
mov	acc1, 9978842
push	acc1
mov	acc1, 9965794
push	acc1
mov	acc1, 9957564
push	acc1
mov	acc1, 9938304
push	acc1
mov	acc1, 9935427
push	acc1
mov	acc1, 9932289
push	acc1
mov	acc1, 9931494
push	acc1
mov	acc1, 9927388
push	acc1
mov	acc1, 9926376
push	acc1
mov	acc1, 9923213
push	acc1
mov	acc1, 9921394
push	acc1
mov	acc1, 9919154
push	acc1
mov	acc1, 9918082
push	acc1
mov	acc1, 9916239
push	acc1
mov	acc2, 765

:label_func03
pop acc1
push	acc2
push	acc1
mov	acc1, 1023
push	acc1
push	acc2
jmp label_func04
xor
print
mov	acc1, 1
push	acc1
add pop acc2
if_not_zero
jmp label_func03
endif
exit

:label_func04
mov	acc1, 2
push	acc1

:label_func05
jmp label_func09

:label_func06
if_zero
pop_void
jmp label_func08
endif
pop_void
jmp label_func11

:label_func07
if_zero
pop_void
jmp label_func08
endif
pop_void
pop acc1
mov	acc2, 1
push	acc2
sub
if_zero
pop_void
pop acc2
push	acc1
push	acc2
break
endif
push	acc1

:label_func08
mov	acc2, 1
push	acc2
add
jmp label_func05

:label_func09
clone
mov	acc1, 2
push	acc1

:label_func10
sub
if_zero
pop_void
mov	acc1, 1
push	acc1
jmp label_func06
endif
pop_void
clone
push	acc1
mod
if_zero
jmp label_func06
endif
pop_void
clone
push	acc1
mov	acc1, 1
push	acc1
add
clone
pop acc1
jmp label_func10

:label_func11
clone
clone
mov	acc2, 0
push	acc2

:label_func12
mov	acc1, 10
push	acc1
mul
pop acc2
push	acc1
mod
push	acc2
add
pop acc2
pop acc1
clone
push	acc2
sub
if_zero
pop_void
mov	acc2, 1
push	acc2
jmp label_func07
endif
pop_void
push	acc1
mov	acc1, 10
push	acc1
div
if_zero
jmp label_func07
endif
clone
push	acc2
jmp label_func12
