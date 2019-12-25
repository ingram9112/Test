#import os
#url = '//www.jb51.net/images/logo.gif'
#filename = os.path.basename(url)
#print(filename)

import os
urls = ["http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png" ]

counta = 0
countb = 0
countc = 0
countd = 0
for i in urls:
    filename = os.path.basename(i)

    
    if filename == "a.txt":
        counta += 1
    if filename == "b.txt":
        countb += 1
    if filename == "c.jpg":
        countc += 1
    if filename == "haha.png":
        countd += 1

print("a.txt" , counta)
print("b.txt" , countb)
print("c.txt" , countc)
