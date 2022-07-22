from pprint import pprint as pp
import sys
import requests
# import slug_party
# from simplecrypt import encrypt, decrypt
# pp(sys.modules)
# print(sys.modules.get('practice_module')) # None
# import practice_module
# print(practice_module.s) # 1
# print(sys.modules.get('practice_module')) # <module 'practice_module' from 'C:\\Users\\kiril\\Desktop\\Job\\tree-of-knowledge\\Python\\python_base_and_use_stepik\\2_\\practice_module.py'>

# pp(sys.path)
print(requests)
# print(encrypt)
# print(decrypt)
pp(sys.path)

# не работает, потому что почему-то не импортируется библиотека simplecrypt
# из консоли, если включить виртуальное окружение - работает

# from simplecrypt import decryp, DecryptionException
# with open('task_2_2_9/passwords.txt', 'r') as f:
# 	fr = f.read()
# 	passwords = fr.split('\n')

# with open("task_2_2_9/encrypted.bin", "rb") as f:
# 	data = f.read()

# count = 0
# while not info:
# 	try:
# 		info = decrypt(passwords[count], data)
# 	except DecryptionException:
# 		if count == len(passwords) - 1:
# 			print('password not found')
# 			break
			
# 		count += 1
# print(info) # b'Alice loves Bob'