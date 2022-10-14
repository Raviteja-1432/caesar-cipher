def encode(text, shift):
    	encrypted_password =""
	for i in text:
		encrypted_password =encrypted_password+chr(ord(i)+shift)
	return encrypted_password

def decode(text, shift):
	decrypted_password=""
	for i in text:
		decrypted_password =decrypted_password+chr(ord(i)-shift)
	return decrypted_password

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

if direction=="encode":
	print(encode(text, shift))
elif direction=="decode":
	print(decode(text, shift))
else:
	print("Wrong command")

while (5>3):
	y=input("Type yes you want to do again? otherwise no\n").lower()
	if y == "yes":
		direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
		text = input("Type your message:\n")
		shift = int(input("Type the shift number:\n"))
		if direction=="encode":
			print(encode(text, shift))
		elif direction=="decode":
			print(decode(text, shift))
		else:
			print("Wrong command")
	else:
		exit()