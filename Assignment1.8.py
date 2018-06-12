'''
Write a Python Program to print the given string in the format specified in the sample
output.
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens
Sample Output:
WE, THE PEOPLE OF INDIA,
    having solemnly resolved to constitute India into a SOVEREIGN, !
        SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
         and to secure to all its citizens:
'''


print(r'WE, THE PEOPLE OF INDIA,{0} {1}'
      r'having solemnly resolved to constitute India into a SOVEREIGN, !'
      r'{2}{3}{4}SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC{5} {6} {7} and to secure to all its citizens:'.
      format('\n','\t','\n','\t','\t','\n','\t','\t'))