from Crypto.Cipher import AES
import base64
import os
def decryption(encryptedString):
	PADDING = '{'
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	#Key is FROM the printout of 'secret' in encryption
	#below is the encryption.
	encryption = encryptedString
	key = 'h4ckth1sk3yp4d16'
	cipher = AES.new(key)
	decoded = DecodeAES(cipher, encryption)
	print decoded
print decryption("Ap1MyUc1PI9mQ+q97LLbTVJPWwaPhaby/i1omIW6riU=")
