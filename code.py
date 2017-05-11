import codecs
from functions import connectedLetters, convertIntoInteger, writeSubstructResult
foo = codecs.open('in.txt', encoding='utf-16')
f = open('out.txt', 'w')
f.close()
for line in foo:
	aa = line.split()
	# for a in aa:
	# 	for i in range(len(a)):
	# 		f = open('out.txt', 'a')
	# 		if a[i]==u'\u09CD':
	# 			f.write(a[i].encode('utf16'))
	# 			f.write( ' '.encode('utf16'))
	# 			f.close()
	# print repr(line)
	print connectedLetters(line)[4]
	print '\n'
	print '\n'
	print '\n'
	print '\n'
	resulted_data = convertIntoInteger(connectedLetters(line)[4])
	writeSubstructResult(resulted_data)