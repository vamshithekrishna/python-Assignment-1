'''
Create the below pattern using nested for loop in Python.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
s=''
s1=''
for i in range(5):
    s+='*'
    print(s)
    if i==4:
        for j in range(5,0,-1):
            s1=s[0:j-1]
            print(s1)

