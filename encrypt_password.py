import sys
import crypt

password = sys.argv[1]

print crypt.crypt(password, "$1$ansible$")
