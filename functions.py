import values
def connectedLetters(a):
	ln = len(a)
	startArr = []
	endArr = []
	connectedLettersType = []
	connectedLettersList = []
	end = -2
	start = -2
	i = 1
	full = []
	while i<ln:
		if a[i]==u'\u09CD':
			if i+2<ln and a[i+2]==u'\u09CD':
				startArr += [i-1];
				endArr += [i+3]
				connectedLettersType += [3]
				cl = []
				cl+=[a[i-1]]
				cl+=[a[i+1]]
				cl+=[a[i+3]]
				connectedLettersList += [cl]
				i = i+4
				full += [[3,cl]]
			else:
				startArr += [i-1];
				endArr += [i+1]
				connectedLettersType += [2]
				cl = []
				cl+=[a[i-1]]
				cl+=[a[i+1]]
				connectedLettersList += [cl]
				i = i+2
				full += [[2,cl]]
		else:
			full += [[1,a[i]]]
			i = i+1

	result = []
	result += [startArr]
	result += [endArr]
	result += [connectedLettersType]
	result += [connectedLettersList]
	result += [full]

	return result



def convertIntoInteger(value_set_array):
	print(len(value_set_array))
	print '\n'
	print '\n'
	print '\n'
	print '\n'
	data_set = []
	for value_set in value_set_array:
		val = 0
		if value_set[0] == 1:
			for value in values.valueOne:
				if value[0] == value_set[1]:
					val = value[1]
					print value
		elif value_set[0] == 2:
			for value in values.valueTwo:
				if value[0] == value_set[1][0] and value[1] == value_set[1][1]:
					val = value[2]
					print value
		elif value_set[0] == 3:
			for value in values.valueThree:
				if value[0] == value_set[1][0] and value[1] == value_set[1][1] and value[2] == value_set[1][2]:
					val = value[3]
					print value

		if val:
			data_set += [val]
	print '\n'
	print '\n'
	print '\n'
	print '\n'
	return data_set


def writeSubstructResult(resulted_data):
	resulted_data.sort(reverse=True)
	print resulted_data
	if not len(resulted_data):
		pre_data = 0
	else:
		pre_data = resulted_data[0]
		resulted_data.pop(0)
	for data in resulted_data:
		f = open('out.txt','a')
		f.write(str(pre_data-data))
		f.close()
		pre_data = data