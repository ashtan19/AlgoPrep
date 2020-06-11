# Decrypt Message
# An infamous gang of cyber criminals named “The Gray Cyber Mob”, which is behind many hacking attacks and drug trafficking, has recently become a target for the FBI. After intercepting some of their messages, which looked like complete nonsense, the agency learned that they indeed encrypt their messages, and studied their method of encryption.

# Their messages consist of lowercase latin letters only, and every word is encrypted separately as follows:

# Convert every letter to its ASCII value. Add 1 to the first letter, and then for every letter from the second one to the last one, add the value of the previous letter. Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII. Convert the values back to letters.

# For instance, to encrypt the word “crime”

# Decrypted message:	c	r	i	m	e
# Step 1:	            99	114	105	109	101
# Step 2:	            100	214	319	428	529
# Step 3:	            100	110	111	116	113
# Encrypted message:	d	n	o	t	q
# The FBI needs an efficient method to decrypt messages. Write a function named decrypt(word) that receives a string that consists of small latin letters only, and returns the decrypted word.

# Explain your solution and analyze its time and space complexities.

# Examples:

# input:  word = "dnotq"
# output: "crime"

# input:  word = "flgxswdliefy"
# output: "encyclopedia"
# Since the function should be used on messages with many words, make sure the function is as efficient as possible in both time and space. Explain the correctness of your function, and analyze its asymptotic runtime and space complexity.

# Note: Most programing languages have built-in methods of converting letters to ASCII values and vica versa. You may search the internet for the appropriate method.

# Constraints:

# [time limit] 5000ms

# [input] string word

# The ASCII value of every char is in the range of lowercase letters a-z.
# [output] string


# Attempt 1 O(n) O(1)
def decrypt(word):
    if word == '' or word == None:
        return ''
    firstletter = ord(word[0]) - 1
    result = [chr(firstletter)]
    salt = ord(word[0])-97

    for i in range(1, len(word)):
        encoded = ord(word[i]) - 97
        decodedAscii = (encoded - 19-salt) % 26
        salt += 19 + decodedAscii
        result.append(chr(decodedAscii + 97))

    return ''.join(result)
