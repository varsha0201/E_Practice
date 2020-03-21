# import sys
# print(sys.argv)
# # print(sys.winver)
# print(sys.flags)

# import os
# os.mkdir("Test")
# os.getcwd()
# os.rmdir("Test")

# import math

# print(math.ceil(10.25))
# print(math.cos(10))

# import random

# no = random.randrange(101,500)
# print(no)

# import datetime

# print(datetime.tzinfo())

# import json

# data = {"name":"varsha", "age":40}
# json_string = json.dumps(data)
# print(json_string)

import re
# print(re.sub('[ab]','*','abscd abd aab sssab abbaab'))

# print(re.sub('abc','*','abc abcdgbabc'))

print(re.sub(r'[abcd][1234]','*','a1+b2+d3+e4'))