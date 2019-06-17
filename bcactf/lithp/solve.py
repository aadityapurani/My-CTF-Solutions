#!/usr/bin/python
# Ref: https://arxiv.org/pdf/1507.05956.pdf
# Lowkey Interpreter in Python
# <3 from knapstack - helping dcua-school

# DEBUG
#ins="caddadddddr"
#(( !\"#$%&'\(\)*+,-./)(0123456789)(:;<=>?@)(ABCDEFGHIJKLMNOPQRSTUVWXYZ)(\[\\\]^_`)(abcdefghijklmnopqrstuvwxyz)(\{|\}~))


boxes = ["!\"#$%&'\(\)*+,-./", "0123456789", ":;<=>?@", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "\[\\\]^_`", "abcdefghijklmnopqrstuvwxyz", "\{|\}~"]
ins_list =['cadadddddr', ' caddadddddr', ' caadddddr', ' caddadddddr', ' cadddddddddddddddddddadddddr', ' cadddddadddddr', ' caaddddddr', ' cadddddddddddadddr', ' cadadr', ' cadddddadr', ' cadddddddadr', ' caddddaddddr', ' caddddddddadr', ' caddddadr', ' cadddddadr', ' cadddadr', ' cadddadddddr', ' caddddaddddr', ' cadddddddddddddddadddddr', ' cadddddddddddddddddadddr', ' caadr', ' caddddddadddddr', ' cadddddddddddddddddadddr', ' caddddadr', ' caddddddddddddadddr', ' caddddddddddddadddddr', ' cadadr', ' cadddddddddddddadddddr', ' caddddddadddr', ' caddddaddddr', ' cadadr', ' cadddddadr', ' caddddaddddr', ' caddddadr', ' caddddddddddddddddddddddadddddr', ' cadddadr', ' caddddddddddddddddddadddr', ' caadr', ' caddddddddddddadddr', ' caddddadddddr', ' cadar', ' caddaddddddr']


def lisp_translate(ins):
	inz_len = len(ins)
	j = inz_len
	index = 0
	temp=[]
	slow_ptr = 0
	accessed = 0
	ptr_idx = -2
	
	while j > 2:
		if ins[ptr_idx] == 'd':
			if len(temp) == 1:
				slow_ptr+=1
			else:
				index+=1
		elif ins[ptr_idx] == 'a':
			if not accessed:
				temp.append(boxes[index])
				accessed = 1
			else:
				return temp[0][slow_ptr]
		ptr_idx -=1
		j -=1

flag = ""
for i in ins_list:
	flag+=lisp_translate(i)

print flag.replace("]","_").replace("\\","{").replace("\"","!").replace("|","}")

#bcactf{L157_8453d_pR0gR4Mm1nG_15_4w3S0Me!}
