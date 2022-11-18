import random
import time
import binascii
import CryptFunction as CF

# opening input file
inp_file = open(r"01-input.txt", "r")
inp_str = inp_file.read()
# (inp_str)
inp_file.close()

# convert string to binary
inp_str_bin = "".join([format(y, '08b') for y in [ord(x) for x in inp_str]])
# print(inp_str_bin)
# print(type(inp_str_bin))

# divide binary into 2 parts
n = int(len(inp_str_bin) // 2)
L1 = inp_str_bin[0:n]
R1 = inp_str_bin[n::]


def rand_key(p):
    temp_key = ""

    for i in range(p):
        temp = random.randint(0, 1)
        temp = str(temp)
        temp_key = temp_key + temp

    return temp_key


# generate the random keys and write into the file
m = int(len(R1))
key_1 = rand_key(m)
key_2 = rand_key(m)

key_gen_file = open(r"output/02-key.txt", "w+")
key_gen_file.write(key_1)
key_gen_file.write("\n")
key_gen_file.write(key_2)
key_gen_file.close()


def feistel(a, b):
    # x = CF.com_or_num(a, b)
    # y = CF.com_and_num(a, b)
    # print(CF.xor_num(a, b))
    # return CF.com_xor_num(x, y)
    return CF.comjfun(a,b)


# generating L2 & R2 from given input (first round for feistel)
feistel_str_1 = feistel(R1, key_1)
R2 = CF.xor_num(feistel_str_1, L1)
L2 = R1

# generating L3 & R3 from given input (second round for feistel)
feistel_str_2 = feistel(R2, key_2)
R3 = CF.xor_num(feistel_str_2, L2)
L3 = R2

# whole encrypted string in binary
binary_str = L3 + R3
# print(len(L3))
# print(len(R3))
normal_str = ''

# whole encrypted string in ascii characters
for i in range(0, len(binary_str), 7):
    temp_data = binary_str[i:i + 7]
    decimal_data = int(temp_data, 2)
    normal_str = normal_str + chr(decimal_data)

# writing binary and normal encrypted output to the file
ciph_out_file = open(r"output/03n-cipher_normal_output.txt", "w")
ciph_out_file.write(normal_str)
ciph_out_file.close()
bciph_out_file = open(r"output/03b-cipher_binary_output.txt", "w")
bciph_out_file.write(str(len(L3)))
bciph_out_file.write('\n')
bciph_out_file.write(binary_str)
bciph_out_file.close()
print("encryption done!!")
# print("encrypted Text is : ", normal_str)

time.sleep(3)

# read keys from the file for decryption part
key_file = open(r"output/02-key.txt", "r")
key_3 = key_file.readline()
key_4 = key_file.readline()
# print(key_3)
# print(key_4)
key_file.close()

# read encrypted binary from the file for decryption part
b_data_file = open(r"output/03b-cipher_binary_output.txt", "r")
L3_size = int(b_data_file.readline())
binary_str_from_file = b_data_file.read()
# print(L3_size)
# print(binary_str_from_file)
# print(binary_str)
b_data_file.close()

L3_from_file = binary_str_from_file[0:L3_size]
# print(L3)
# print(L3_from_file)
R3_from_file = binary_str_from_file[L3_size::]
# print(len(R3_from_file))

# first round for the decryption
L4 = L3_from_file
R4 = R3_from_file
feistel_str_3 = feistel(L4, key_4)
L5 = CF.xor_num(R4, feistel_str_3)
R5 = L4

# second round for the decryption
feistel_str_4 = feistel(L5, key_3)
L6 = CF.xor_num(R5, feistel_str_4)
R6 = L5

# decrypted binary string
inp_str1 = L6 + R6

# converting decrypted binary string to the normal ascii values for original output
decrypted_str = (binascii.unhexlify('%x' % int(inp_str1, 2))).decode()
plain_out_file = open(r"output/04-plain_output.txt", "w")
plain_out_file.write(decrypted_str)
plain_out_file.close()
print("decryption done!!")
# print("decrypted text is: ", decrypted_str)
