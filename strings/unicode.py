#返回单个字符的unicode 代码点 （十进制）
print(ord('A'))
##将十进制转为十六进制 # 输出 '0x41'
print(hex(ord('A')))

print("\u0041")   #\u要求4个十六禁止数  \U是8位置

print("\u03B1")  # 输出: α
print("\N{dog}")  


print(ord('🐍'))
print(hex(128013))
print("\U0001F40D") 
"""
- [A] https://www.compart.com/en/unicode/U+0041  
- [α] https://www.compart.com/en/unicode/U+03B1  
- [🐍] https://www.compart.com/en/unicode/U+1F40D
"""

print(ord('α'))       #945  unicode代码点，十进制
print(hex(ord('α')))  #0x3b1  十六进制

print(int('3B1', 16))    #十六进制转为十进制

# Latin Capital Letter              拉丁文大写字母
# Greek Small Letter Alpha          希腊文小字母 Alpha

var = "\N{Latin Capital Letter A}lways look on the bright side of life."  

print(var)


print("\N{Face Massage}")
