import re
def check_aei (text):
  result = re.search(r"a..d", text)
  print(result)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

#m= check_aei("paramedic")
#print(m)

print(re.findall(r"cat|dog", "I like fluffy dogs, , small cat, big dogs, and mean cats."))

print(re.findall(r"racecar", "racecaracecar"))

print(re.findall(r"attack|tac", "cattack"))

print(re.findall(r"Py.+n", "Python Programmin"))

print(re.findall(r"o+l+", 'woolly goldfish'))

print(re.findall(r'(\w+) and (\d+)', 'set width=20 and height=10'))

print(re.findall(r"\b[a-zA-Z]{5}\b", "A little scary ghost appeared"))

print(re.sub(r"s*", "friendly", "A little scary ghost appeared"))