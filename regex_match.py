'''
This program is used to find if words in a line
'''
import re

text= 'arn:aws:iam::110013012092:user/samir.sapkota'
pattern= r'11001301a22092'

match=re.search(pattern,text)

if match:
    print("AWS account id matches")
else:
    print("No account id matched")
