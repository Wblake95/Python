# had trouble getting my pattern to work, but got help
# https://stackoverflow.com/questions/76949942/python-re-findall-returns-empy-strings

import re, pyclip

phonePattern = re.compile(r'(?m)(?:\(?\d{3}\)?[-.\s])?\d{3}[-.\s]\d{4}', re.DOTALL)
emailPattern = re.compile(r'(?m)[\w.%+-]+@(?:[\w-]+\.)+\w{2,}', re.DOTALL)

print("This will be searched", pyclip.paste(text=True))

phone= phonePattern.findall(pyclip.paste(text=True))
print("Phone numbers found:", phone)

email = emailPattern.findall(pyclip.paste(text=True))
print("emails found: ", email)
