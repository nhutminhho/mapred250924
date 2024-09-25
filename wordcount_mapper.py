#!/usr/bin/python3
import sys # thu vien cung cap cac ham de lam viec voi stdin va stdout 

# doc tung dong du lieu tu dau vao chuan (stdin)
for line in sys.stdin:
	# su dung ham split() de tach dong van ban thanh list cac tu 
	# split() se tach dua vao khoang trang 
	words = line.split()

	for word in words: 
		# su dung ham print() de in ra 
		print('{0}\t{1}'.format(word,1))
