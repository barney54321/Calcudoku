l1=input()
l2=input()
l3=input()
l4=input()
l5=input()
l6=input()
l7=input()
file_lines=[l1,l2,l3,l4,l5,l6]
operator_line=l7
full_set=[]
for lines in file_lines:
	l=[]
	l=lines.split()
	for c in l:
		full_set.append(int(c))
grouping=[]
for a in range (0,max(full_set)+1):
	test=[]
	for i,x in enumerate(full_set):
		if x==a:
			test.append(i)
	grouping.append(test)
list_of_ops=operator_line.split()
ops=[]
for o in list_of_ops:
	whatever=[]
	try:
		whatever.append(int(o))
	except BaseException:
		whatever.append(o[:-1])
		whatever.append(o[-1])
	ops.append(whatever)

test=[1,2,3,4,5,6]
import itertools
g=grouping
all_com=list(itertools.permutations(test,6))
def test_ops(a_36,o,g):
	works=True
	for index,i in enumerate(g):
		run=True
		for b in i:
			if a_36[b]==0:
				run=False
		if run:
			if len(i)==1:
				if a_36[i[0]]!=o[index][0]:
					works=False
			elif o[index][1]=="-":
				difference=abs(a_36[i[0]]-a_36[i[1]])
				result=int(o[index][0])
				if difference!=result:
					works=False
			elif o[index][1]=="+":
				summ=0
				for b in i:
					summ+=a_36[b]
				if summ!=int(o[index][0]):
					works=False
			elif o[index][1]=="*":
				summ=1
				for b in i:
					summ=summ*a_36[b]
				if summ!=int(o[index][0]):
					works=False
			elif o[index][1]=="/":
				if a_36[i[0]]/a_36[i[1]]!=int(o[index][0]) and a_36[i[1]]/a_36[i[0]]!=int(o[index][0]):
					works=False
	return works
def find_most(line):
	f=True
	if line[0]==line[1]!=0 or line[0]==line[2]!=0 or line[0]==line[3]!=0 or line[0]==line[4]!=0 or line[0]==line[5]!=0 or line[1]==line[2]!=0 or line[1]==line[3]!=0 or line[1]==line[4]!=0 or line[1]==line[5]!=0 or line[2]==line[3]!=0 or line[2]==line[4]!=0 or line[2]==line[5]!=0 or line[3]==line[4]!=0 or line[3]==line[5]!=0 or line[4]==line[5]!=0:
		f=False
	return f
def check_36(_36):
	check=False
	c1=[_36[0],_36[6],_36[12],_36[18],_36[24],_36[30]]
	c2=[_36[1],_36[7],_36[13],_36[19],_36[25],_36[31]]
	c3=[_36[2],_36[8],_36[14],_36[20],_36[26],_36[32]]
	c4=[_36[3],_36[9],_36[15],_36[21],_36[27],_36[33]]
	c5=[_36[4],_36[10],_36[16],_36[22],_36[28],_36[34]]
	c6=[_36[5],_36[11],_36[17],_36[23],_36[29],_36[35]]
	if find_most(c1) and find_most(c2) and find_most(c3) and find_most(c4) and find_most(c5) and find_most(c6):
		check=True
	return check
row1,row2,row3,row4,row5,row6=[],[],[],[],[],[]
for a in all_com:
	if test_ops(list(a)+[0]*30, ops, grouping):
		row1.append(a)
	if test_ops([0]*6+list(a)+[0]*24, ops, grouping):
		row2.append(a)
	if test_ops([0]*12+list(a)+[0]*18, ops, grouping):
		row3.append(a)
	if test_ops([0]*18+list(a)+[0]*12, ops, grouping):
		row4.append(a)
	if test_ops([0]*24+list(a)+[0]*6, ops, grouping):
		row5.append(a)
	if test_ops([0]*30+list(a), ops, grouping):
		row6.append(a)
if len(row1)==0 or len(row2)==0 or len(row3)==0 or len(row4)==0 or len(row5)==0 or len(row6)==0:
	quit("No solution.")
def find_one(row,index):
	change=True
	only=row[0][index]
	for a in row:
		if a[index]!=only:
			change=False
	return change
def reduce_numbers(row,row1,row2,row3,row4,row5,row6):
	for w in range (0,6):
		if find_one(row,w):
			if row!=row1:
				row1=[item for item in row1 if item[w]!=row[0][w]]
			if row!=row2:
				row2=[item for item in row2 if item[w]!=row[0][w]]
			if row!=row3:
				row3=[item for item in row3 if item[w]!=row[0][w]]
			if row!=row4:
				row4=[item for item in row4 if item[w]!=row[0][w]]
			if row!=row5:
				row5=[item for item in row5 if item[w]!=row[0][w]]
			if row!=row6:
				row6=[item for item in row6 if item[w]!=row[0][w]]
	return row1,row2,row3,row4,row5,row6
row1,row2,row3,row4,row5,row6=reduce_numbers(row1,row1,row2,row3,row4,row5,row6)
row1,row2,row3,row4,row5,row6=reduce_numbers(row2,row1,row2,row3,row4,row5,row6)
row1,row2,row3,row4,row5,row6=reduce_numbers(row3,row1,row2,row3,row4,row5,row6)
row1,row2,row3,row4,row5,row6=reduce_numbers(row4,row1,row2,row3,row4,row5,row6)
row1,row2,row3,row4,row5,row6=reduce_numbers(row5,row1,row2,row3,row4,row5,row6)
row1,row2,row3,row4,row5,row6=reduce_numbers(row6,row1,row2,row3,row4,row5,row6)
for a in row1:
	all_36=list(a)+[0]*30
	for b in row2:
		all_36=all_36[0:6]+list(b)+[0]*24
		if test_ops(all_36,ops,grouping) and check_36(all_36):
			for c in row3:
				all_36=all_36[0:12]+list(c)+[0]*18
				if test_ops(all_36,ops,grouping) and check_36(all_36):
					for d in row4:
						all_36=all_36[0:18]+list(d)+[0]*12
						if test_ops(all_36,ops,grouping) and check_36(all_36):
							for e in row5:
								all_36=all_36[0:24]+list(e)+[0]*6
								if test_ops(all_36,ops,grouping) and check_36(all_36):
									for f in row6:
										all_36=all_36[0:30]+list(f)
										if test_ops(all_36,ops,grouping) and check_36(all_36):
											final_list=all_36
											print(final_list[0],final_list[1],final_list[2],final_list[3],final_list[4],final_list[5])
											print(final_list[6],final_list[7],final_list[8],final_list[9],final_list[10],final_list[11])
											print(final_list[12],final_list[13],final_list[14],final_list[15],final_list[16],final_list[17])
											print(final_list[18],final_list[19],final_list[20],final_list[21],final_list[22],final_list[23])
											print(final_list[24],final_list[25],final_list[26],final_list[27],final_list[28],final_list[29])
											print(final_list[30],final_list[31],final_list[32],final_list[33],final_list[34],final_list[35])
											quit()
print("No solution.")
