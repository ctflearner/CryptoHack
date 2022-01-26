
text="label"
flag=""
for i in text:
    flag += chr(ord(i)^13)

print(f"crypto{{{flag}}}")

