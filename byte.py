#unhexlify: Return the binary data represented by the hexadecimal string hexstr.hexstr must contain an even humber of hexadecimal digits(Which can be upper or lower case),otherwise an Error exception is raised
#raise: The "raise" keyword is used to raise an exception,we can define what kind of error to raise, and text to print the user p
#importing the unhexlify from binascii 
from binascii import unhexlify   
import string

def single_byte_xor(input, key):
    if len(chr(key)) != 1:
       raise "Key Length Exception: In Single_byte_xor key must be 1 byte long"
    output = b''
    for b in input:
        output=output+bytes([b ^ key])
        
    try:
       return output.decode("utf-8")
    except:
       return "Cannot Decode Some bytes"
   
   
data="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded=unhexlify(data)
print("[-] HEX_DECODE:{}\n".format(decoded))            

result={}
for i in range(256):
    result[i]=(single_byte_xor(decoded,i))
   
print("[*] FLAG: {}".format([s for s in result.values() if "crypto" in s]))   