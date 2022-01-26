QUESTION
---------------------------------------------------
XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret ^ used instead.

We can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character.




---------------------------------------------------
SOLUTION
--------------------------------------------------
text="label"
flag=""
for i in text:
    flag += chr(ord(i)^13)     

print(f"crypto{{{flag}}}")


---------------------------------------------------------

