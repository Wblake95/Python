# I want to copy something from my clipboard and find emails;phone numbers from it.
# 1. Get thetext off the clipboard
#   - Find out what clipboard I have: Wayland clipboard
#   - How to access that clipboard: wl-copy/wl-paste
# 2. Find all phone numbers and email addressses in the clipboard
# 3. Paste them back into the clipboard

# Pyperclip is not an option (wayland is not supported). Use Subprocess to run wl-copy/wl-paste

import re, subprocess

phone = re.compile(r'(\d{3})?(\W)?\d{3}(\W)?\d{4}')
email = re.compile(r'\w+[.]?(\w+)?@(/w+).com')
x = subprocess.run("wl-paste", capture_output=True, text=True)

# phone.search(x.stdout).group()
# email.search(x.stdout).group()
try:
    phone1 = phone.search('925-819-3408')
    print(phone1.group())
except:
    pass
finally:
    print("no phone numbers") 
try:
    email1 = email.search('wesleyblake95@gmail.com')
    email1.group()
except:
    pass
finally:
    print("no emails") 
