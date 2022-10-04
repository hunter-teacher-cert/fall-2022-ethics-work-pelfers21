Patti (Patricia) Elfers-Wygand



import re


def find_name(line):
 
    #First Name Last Name 
    pattern=r'[A-Z]\w*\s[A-Z]\w*'
    result = re.findall(pattern,line)

    #First Name Last Name 
    pattern=r'[A-Z]\w*\s[A-Z]\w*'
    result = re.findall(pattern,line)

    #Mrs. Last expression
    pattern=r'Mrs.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)

    #Ms. S. Last 
    #pattern=r'Ms.\s[A-Z]\.\s[A-Z]\w*'
    #result = result + re.findall(pattern,line)

    #Mrs. S. Last name 
    pattern=r'Mrs.\s[A-Z]\.\s[A-Z]\w*'
    result = result + re.findall(pattern,line)
    return result

f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)

 
