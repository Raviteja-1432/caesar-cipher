# Algorithm
# 	Step-1 :- consider an input from user (ciphertext,shift)
# 	Step-2 :- user selects encryption or decryption
# 	Step-3 :- if encryption then perform an mathematical expression value and shift to that value i.e, E = (x + n) % 26
# 	Step-4 :- if decryption then perform an mathematical expression value and shift to that value i.e, E = (x - n) % 26
# 	Step-5 :- if the shift value is doesnot know that means we have to bruteforce using the shift values from 0-25
# 	Step-6 :- the output of the encryption or decryption will be displayed

L = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def select(c):
	if c == 'encryption':
		ciphertext = input('Enter the text to encrypt : ')
		shift = int(input('Enter the shift value : '))
	if c == 'decryption':
		ciphertext = input('Enter the text to decrypt : ')
		shift = input('Enter the shift value (For bruteforce method type "None") : ')
		if shift.isdigit() == True:
			shift = int(shift)
	return ciphertext,shift

def encryption(ciphertext,shift):
	encryption_text = ''
	for i in ciphertext:
		if i.isdigit:
			E = i
		if i.isupper():
			e = (L.index(i) + shift) % 26
			E = L[e]
		if i.islower():
			e = (L.index(i.upper()) + shift) % 26
			E = L[e].lower()
		encryption_text += E
	return encryption_text


def decryption(ciphertext,shift):
	decryption_text = ''
	if shift == 'None':
		for shift in range(0,26):
			decryption_text = ''
			for i in ciphertext:
				if i.isdigit:
					E = i
				if i.isupper():
					e = (L.index(i) - shift) % 26
					E = L[e]
				if i.islower():
					e = (L.index(i.upper()) - shift) % 26
					E = L[e].lower()
				decryption_text += E
			print(f'The decrypted text with a shift {shift} is : {decryption_text}')
		exit()
	if shift != 'None':
		for i in ciphertext:
			if i.isupper():
				e = (L.index(i) - shift) % 26
				E = L[e]
			if i.islower():
				e = (L.index(i.upper()) - shift) % 26
				E = L[e].lower()
			decryption_text += E
		return decryption_text


c = input("Encryption or Decryption : ").lower()
ciphertext,shift = select(c)
if c == 'encryption':
	t = encryption(ciphertext,shift)
	print(f'The encrypted text is : {t}')
if c == 'decryption':
	t = decryption(ciphertext,shift)
	print(f'The decrypted text with a shift {shift} is : {t}')
