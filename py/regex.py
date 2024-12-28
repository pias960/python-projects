import re 

a = """Hi my name is pias 
    i am 20 years old and i 30  love coding"""



words = re.findall(r'[]{2}', a)
print(words)