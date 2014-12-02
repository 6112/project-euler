# encoding=utf-8
## SOLVED 20/10/14
## 107359

# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange). For
# example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to
# ASCII, then XOR each byte with a given value, taken from a secret key. The
# advantage with the XOR function is that using the same encryption key on the
# cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107
# XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text
# message, and the key is made up of random bytes. The user would keep the
# encrypted message and the encryption key in different locations, and without
# both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified
# method is to use a password as a key. If the password is shorter than the
# message, which is likely, the key is repeated cyclically throughout the
# message. The balance for this method is using a sufficiently long password
# key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower
# case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
# a file containing the encrypted ASCII codes, and the knowledge that the plain
# text must contain common English words, decrypt the message and find the sum
# of the ASCII values in the original text.

from helpers.file import flattened_list_from_file
import re

def euler():
    xs = flattened_list_from_file("data/059.txt", separator = ",")
    letter_range = range(ord('a'), ord('z') + 1)
    common_chars_rx = re.compile("[ a-zA-Z.,']")
    the_rx = re.compile("\\bthe\\b")
    for a in letter_range:
        for b in letter_range:
            for c in letter_range:
                key = [a, b, c]
                decrypted = "".join(chr(x ^ key[i % len(key)]) for i,x in enumerate(xs))
                chars = len(decrypted)
                common_chars = len(common_chars_rx.findall(decrypted))
                thes = len(the_rx.findall(decrypted))
                if common_chars >= 0.95 * chars and thes >= 3:
                    return sum(ord(c) for c in decrypted)
    return None
