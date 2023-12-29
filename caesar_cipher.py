# Algorithm
# 	Step-1 :- consider an input from user (ciphertext,shift)
# 	Step-2 :- user selects encryption or decryption
# 	Step-3 :- if encryption then perform an mathematical expression value and shift to that value i.e, E = (x + n) % 26
# 	Step-4 :- if decryption then perform an mathematical expression value and shift to that value i.e, E = (x - n) % 26
# 	Step-5 :- if the shift value is doesnot know that means we have to bruteforce using the shift values from 0-25
# 	Step-6 :- the output of the encryption or decryption will be displayed

from os import system,name
from time import sleep
from pyfiglet import *


L = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def banner():
	heading = Figlet(font='big')
	banner_text = heading.renderText("Caesar Cipher\n")

	for line in banner_text.split('\n'):
	    print(colored(0, 213, 255, line))
	    sleep(0.1)

	sub = Figlet(font='digital').renderText("#written by D@rk_D3v1l\n")
	for line in sub.split('\n'):
	    print(colored(255, 0, 0, line))
	    sleep(0.1)


def contact():
	print(colored(0,200,255,"*************************\n"))
	print(colored(0,255,255,"https://www.linkedin.com/in/ravi-teja-188373250"))
	print(colored(0,255,255,"https://github.com/Raviteja-1234/caesar-cipher.git"))
	print(colored(0,200,255,"\n*************************\n"))
	sleep(0.5)


def input_banner():

	sub = Figlet(font='small').renderText("Input\n")

	for line in sub.split('\n'):
		print(colored(255, 100, 100, line))
		sleep(0.1)

def output_banner():

	sub = Figlet(font='small').renderText("output\n")

	for line in sub.split('\n'):
		print(colored(0, 255, 0, line))
		sleep(0.1)

def main():
	c = input("Encryption or Decryption\t:\t").lower()
	sleep(0.5)
	ciphertext,shift = select(c)
	sleep(0.5)
	if c == 'encryption':
		t = encryption(ciphertext,shift)
		sleep(0.5)
		print(colored(0,200,255,"\n*************************\n"))
		sleep(0.1)
		output_banner()
		print(f'The encrypted text is \t\t:\t{t}')
		sleep(0.1)
		print(colored(0,200,255,"\n*************************\n"))
		sleep(0.1)
	if c == 'decryption':
		t = decryption(ciphertext,shift)
		sleep(0.5)
		print(colored(0,200,255,"\n*************************\n"))
		sleep(0.1)
		output_banner()
		print(f'The decrypted text with a shift {shift} is\t\t:\t{t}')
		sleep(0.1)
		print(colored(0,200,255,"\n*************************\n"))
		sleep(0.1)

def select(c):
	if c == 'encryption':
		ciphertext = input('Enter the text to encrypt\t:\t')
		sleep(0.5)
		shift = int(input('Enter the shift value\t\t:\t'))
		sleep(0.5)
	if c == 'decryption':
		ciphertext = input('Enter the text to decrypt\t:\t')
		sleep(0.5)
		shift = input('Enter the shift value \n(For bruteforce type "None")\t:\t')
		sleep(0.5)
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
		print(colored(0,200,255,"\n*************************\n"))
		output_banner()
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
			print(f'The decrypted text with a shift {shift} is\t:\t{decryption_text}')
			sleep(0.1)
		print(colored(0,200,255,"\n*************************\n"))
		exit()
	if shift != 'None':
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
		return decryption_text

if __name__ == "__main__":
	sleep(2)
	clear()
	banner()
	contact()
	input_banner()
	main()
