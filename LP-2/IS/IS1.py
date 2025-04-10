string = input("Enter String: ")
result_and = ""
result_xor = ""
for char in string:
    # Bitwise AND with 127
    and_val = ord(char) & 127
    # Bitwise XOR with 127
    xor_val = ord(char) ^ 127 
    result_and += chr(and_val)
    result_xor += chr(xor_val)

print("Original string: ", string)
print("AND result: ", result_and)
print("XOR result: ", result_xor)

