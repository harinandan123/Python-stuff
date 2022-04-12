from itertools import cycle

f = input("Enter the path of the Cipher File: ")

Magic_Number = input("Enter the Magic-Numbers of the file-type you want with spaces: ").split(" ")
D_Magic_Number = []
for i in Magic_Number:
    D_Magic_Number.append(int(i,16))

f = open(f,"rb").read()

Cipher_File_Header = []
for i in range(8):
    Cipher_File_Header.append(f[i])

key = ''
for i in range(8):
    key += chr(Cipher_File_Header[i]^D_Magic_Number[i])
byte_key = key.encode()

def Multi_Byte_XOR(ct,key):
	return bytes(i^j for i,j in zip(ct,cycle(key)))

directory_and_name = input("Enter the Directory and name of the output file like path/to/file_name: ")
output = open(directory_and_name,"xb")
output.write(Multi_Byte_XOR(f,byte_key))
output.close()

print("Key:",key)
