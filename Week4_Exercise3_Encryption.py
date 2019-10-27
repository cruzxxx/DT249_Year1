''' Encryption program

To encrypt a string, we reverse it and add 1 to the ASCII code for each character.
To decrypt a string we do the opposite. We reverse the order again, but this time
subtracting 1 from the ASCII code for each character in the string.

Need to know:
ord("A") order - yields number that represents A in utf-8
65

chr("65") character - yields character that represents 65 in uft-8
A

'''

phrase = input("Enter a random text: ")

# encrypt

encrypt_str = "" #stores the letter that is running through the loop
for next_letter in phrase: #for an element in the collection of strings
    encrypt_str += chr(ord(next_letter) + 1) #ORD is a number, add + 1 to it to ecrypt. CHR converts ORD to the str that represents the number. ENCRYPT_STR is str and is added to itselt
    # print (encrypt_str, end="")

print (f" The encrypted version of {phrase} is {encrypt_str}")

# decrypt

decrypt_str = ""
for letter in encrypt_str:
    decrypt_str += chr(ord(letter) - 1)
    # print (encrypt_str, end="")

print (f" Now we are decrypting {encrypt_str}, returning to be what it was {decrypt_str}")

