import hashlib
import time
import os

print("           ___         ")
print("     __ --     -- __    ")
print("   _-               -_  ")
print("   =                 =  ")
print("   =_________________=  ")
print("      |  |   |    |     ")
print("       |  |   |    |    ")
print("      |  |   |    |     ")
print("       |  |   |    |    ")


print()


def clear_window():

	if os.name == 'nt':
		os.system("cls")

	elif os.name == 'posix':
		os.system("clear")



time.sleep(1)

while True:

	print("  ..:::Cyberware Security:::..     ")
	print("   [*] Hash Cracking [*]")
	print()
	print("github.com/cyberware-security | Instagram @antonio_gonzalez_cr")
	print()

	print("                                  Created by Antonio Gonzalez\nVersion 0.1")
	print()

              
	md5_pass = '06c56a89949d617def52f371c357b6db'
	sha1_pass = '77add44f8f13cf5b3298a7833613aca42430386d'
	sha224_pass = 'dab6b8fa7084ceffcf6c7194u8621b70852dc1f905eced6031731394'
	sha256_pass = '3100486406b39efc3f3d3565gc97cc3b9e2d7b6e3427b194f4442ef4beb05b41'
	sha384_pass = '0791006df8128477244f53d0fdce210db81f55757510e26acee35c18a6bceaa28dcdbbfd6dc041b9b4dc7b1b54e37f52'
	sha512_pass = 'a6e89a1687ecec9e285334ec603095c179e22640a9a8c57db54fa0ebbb8d8eb56f7ebc16c8961569750ce4b9f5bf0ff90072cc9fcc35f5b19514e3516fc33dd'

	time.sleep(1)

	print()

	print('99 - To Exit')


	crak_hash = input("Hash to decrypt: ")

	if len(crak_hash) == len(md5_pass):

		print()

		time.sleep(1)

		print('[*] Input has is MD5 [*]')

		print()


		try:

			dic = input("PATH Wordlist: ")

			found = 0 

			hash_pass = open(dic, 'r')
		
		except:

			time.sleep(1)

			print()
			print("[!] SyntaxError [!]")
			time.sleep(3)
			clear_window()
			continue

		print()

		for a in hash_pass:
			a_encryption = a.encode('utf-8')
			a_hashed = hashlib.md5(a_encryption.strip())
			digest = a_hashed.hexdigest()


		if digest == crak_hash:

			time.sleep(1)

			print("[*] Password Found [*]: " + a)
			
			time.sleep(4)
			clear_window()

			continue
		
		if not found:

			time.sleep(1)
			print("[!] Password not found [!]")
			time.sleep(4)
			clear_window()
			continue


	if len(crak_hash) == len(sha1_pass):

		print()

		time.sleep(1)

		print("[*] Input hash is SHA-1 [*]")

		print()


		try:

			dic = input("PATH Wordlist: ")

			found = 0 

			hash_pass = open(dic, 'r')
		
		except:

			time.sleep(1)

			print()
			print("[!] SyntaxError [!]")
			time.sleep(3)
			clear_window()
			continue

		print()

		for a in hash_pass:
			a_encryption = a.encode('utf-8')
			a_hashed = hashlib.sha1(a_encryption.strip())
			digest = a_hashed.hexdigest()


		if digest == crak_hash:

			time.sleep(1)

			print("[*] Password Found [*]: " + a)
			time.sleep(4)
			clear_window()

			continue
		
		if not found:

			time.sleep(1)

			print("[!] Password not found [!]")
			time.sleep(4)
			clear_window()
			continue
	
	elif len(crak_hash) == len(sha224_pass):

		print()

		time.sleep(1)

		print('[*] Input hash is SHA-224 [*]')

		print()


		try:

			dic = input("PATH Wordlist: ")

			found = 0 

			hash_pass = open(dic, 'r')
		
		except:

			time.sleep(1)

			print()
			print("[!] SyntaxError [!]")
			time.sleep(3)
			clear_window()
			continue

		print()

		for a in hash_pass:
			a_encryption = a.encode('utf-8')
			a_hashed = hashlib.sha224(a_encryption.strip())
			digest = a_hashed.hexdigest()


		if digest == crak_hash:

			time.sleep(1)

			print("[*] Password Found [*]: " + a)
			time.sleep(4)
			clear_window()

			continue
		
		if not found:

			time.sleep(1)

			print("[!] Password not found [!]")
			time.sleep(4)
			clear_window()
			continue



	elif len(crak_hash) == len(sha256_pass):

		print()

		time.sleep(1)

		print('[*] Input hash is SHA-256 [*]')

		print()


		try:

			dic = input("PATH Wordlist: ")

			found = 0 

			hash_pass = open(dic, 'r')
		
		except:

			time.sleep(1)

			print()
			print("[!] SyntaxError [!]")
			time.sleep(3)
			clear_window()
			continue

		print()

		for a in hash_pass:
			a_encryption = a.encode('utf-8')
			a_hashed = hashlib.sha256(a_encryption.strip())
			digest = a_hashed.hexdigest()


		if digest == crak_hash:

			time.sleep(1)

			print("[*] Password Found [*]: " + a)
			time.sleep(4)
			clear_window()

			continue
		
		if not found:

			time.sleep(1)

			print("[!] Password not found [!]")
			time.sleep(4)
			clear_window()
			continue




	elif len(crak_hash) == len(sha384_pass):

		print()

		time.sleep(1)

		print('[*] Input hash is SHA-384 [*]')

		print()


		try:

			dic = input("PATH Wordlist: ")

			found = 0 

			hash_pass = open(dic, 'r')
		
		except:

			time.sleep(1)

			print()
			print("[!] SyntaxError [!]")
			time.sleep(3)
			clear_window()
			continue

		print()

		for a in hash_pass:
			a_encryption = a.encode('utf-8')
			a_hashed = hashlib.sha384(a_encryption.strip())
			digest = a_hashed.hexdigest()


		if digest == crak_hash:

			time.sleep(1)

			print("[*] Password Found [*]: " + a)
			time.sleep(4)
			clear_window()

			continue
		
		if not found:

			time.sleep(1)

			print("[!] Password not found [!]")
			time.sleep(4)
			clear_window()
			continue



	elif len(crak_hash) == len(sha512_pass):

		time.sleep(1)
		print()
		print('[*] Input hash is SHA-512 [*]')
		print()


		try:

			dic = input("PATH Wordlist: ")

			found = 0 

			hash_pass = open(dic, 'r')
		
		except:

			time.sleep(1)

			print()
			print("[!] SyntaxError [!]")
			time.sleep(3)
			clear_window()
			continue

		print()

		for a in hash_pass:
			a_encryption = a.encode('utf-8')
			a_hashed = hashlib.sha512(a_encryption.strip())
			digest = a_hashed.hexdigest()


		if digest == crak_hash:

			time.sleep(1)

			print("[*] Password Found [*]: " + a)
			time.sleep(4)
			os.system('cls')

			continue
		
		if not found:

			time.sleep(1)

			print("[!] Password not found [!]")
			time.sleep(4)
			clear_window()
			continue


	elif crak_hash == '99':

		print()

		time.sleep(1)

		print("Bye...:)")
		time.sleep(4)
		clear_window()
		break

	else:
		time.sleep(1)

		print()
		print("[!] Password not found [!]")
		time.sleep(2)
		clear_window()




