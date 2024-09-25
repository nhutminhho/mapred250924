#!/usr/bin/python3
import sys 

prev_word = None # tu truoc do 
prev_count = 0   # so luong tu truoc do
word = None     # tu hien tai 

for line in sys.stdin: 
	line = line.strip()
	word, count = line.split('\t')
	count = int(count)

	if word == prev_word:
		prev_count += count
	else:
		if prev_word:
			print('{0}\t{1}'.format(prev_word, prev_count))
		prev_word = word
		prev_count = count
if prev_word == word:
	print('{0}\t{1}'.format(prev_word, prev_count))

