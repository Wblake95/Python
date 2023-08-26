# had trouble getting my pattern to work, but got help
# https://stackoverflow.com/questions/76949942/python-re-findall-returns-empy-strings

import re, pyclip

phonePattern = re.compile(r'(?m)(?:^[\w]\(?\d{3}\)?[-.\s\\])?\d{3}[-.\s\\]\d{4}', re.DOTALL)
# multi line search
# if () and ### area code
# separators - . or space
# 3 digits and 4 digits
emailPattern = re.compile(r'(?m)[\w.%+-]+@(?:[\w-]+\.)+\w{2,}', re.DOTALL)
# multi line search
# a word of anylength
# the @ symbole
# if there is a wordafter @
# .com or .xyz

# print("This will be searched", pyclip.paste(text=True))

phone= phonePattern.findall(pyclip.paste(text=True))
print("Phone numbers found:", phone)

email = emailPattern.findall(pyclip.paste(text=True))
print("emails found: ", email)
