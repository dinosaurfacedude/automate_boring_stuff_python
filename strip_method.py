#author: Daniel Jones
#last edited Aug 20 12:54 PM
#Text editor: Nano

#rem short for remove
def stripmeth(word, rem):
	if word == None:
		print('no word given.')
		exit()
	elif rem == '':
		word = word.replace(' ', '')
		print(word)
		exit()
	else:
		word = word.replace(rem, '')
		print(word)
		exit()


inword = input('What word do you wish to strip?\n')

remw = input('which character do you wish to remove?\n')

stripmeth(inword, remw)
