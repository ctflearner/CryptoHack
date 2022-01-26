from pwn import xor
#Below are the keys that are given in the challenge
#first converting all the key1 value to bytes where the given strings are in hex format,for this we use " bytes.fromhex(given_string) "
key1= bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key2_1= bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_3= bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
flag_123= bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
#Solving for the individual value
key2=xor(key2_1 , key1)
key3=xor(key2_3 , key2)
key1_2_3= xor(key2_1 , key3)
flag=xor(flag_123 , key1_2_3)
print(flag.decode())