import re

str = "purple alice-vgb@google.com monkey dish*washer"
match = re.split(r'[!@#$%^&*(){}_+-=.\s]',str)
print(match)

#output
#['purple', 'alice', 'vgb', 'google', 'com', 'monkey', 'dish', 'washer']