#! /usr/bin/env python3
print("*****this is my first python program*****")
print('hello, python')
#input("\n\n press enter to exit")
import sys; x = "runoob"; sys.stdout.write(x+"\n")
y = "aaaa"
z = "bbbb"

print(y, end="" )
print(z)

#isinstanse(y, int)

a = 2j
b = 3.4
c = 'abc'

print(a+b)
print(c*2)

list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]

print(list)

def reverseWords(input):
    inputWords = input.split(" ")
    inputWords=inputWords[-1::-1]
 
    output = ' '.join(inputWords)
     
    return output
 
if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)


sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Google'}

print(sites)

if "Facebook" in sites :
	print("yes")
else :
	print("no")

aa = set('asdfasdfasdf')
bb = set(';lkja;lkja')

print(aa)
print(bb)

'''
这也是注释
'''

"""
注释
"""

def a():
	'''this is document'''
	pass

print(a.__doc__)

bbb = 10**3
print(bbb)

a = "abcdefghijklmn"

print(a[0])
print(a[3:7])
print(a[5:])
print(a[:6])

print("\a")

a = 4
b = 2
c = "马田❤️福丫"
if a > b:
	print("good!!!")
if c == "马田❤️福丫":
	aa = "Good !!! 是真爱 !!!"
	print(aa.center(80,"*"))

thisset = set(("Google", "Runoob", "Taobao"))
print(thisset.pop())
print(thisset)

print(len(thisset))
thisset.clear()
print(thisset)























