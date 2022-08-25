#ex1.1

#city = 'London'
#print(city)

#ex1.2
"""
city = 'berlin'
population = '3645000'

print(city.capitalize(),":",population)
"""
#ex1.3

"""
city = 'London'
population = '9000000'

print("City:",city,"("+str(city.isalpha())+")")
print("Population:", population)
"""

#ex1.4
"""
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

print("capital:",text.find("capital"))
"""


#ex1.5
"""
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."


print(text.split())

"""

#ex1.6
"""
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

print(text.replace("capital", "capital of Germany"))
"""


#ex2.1
"""
text = "Berlin is a world city of culture, politics, media and science."

print(len(text))

"""
#ex2.2!!!!
"""
text = "Berlin is a world city of culture, politics, media and science."
print(text[0],text[62])
"""

#ex2.3
"""
text = "Berlin is a world city of culture, politics, media and science."
text = text.upper()
print(text[0:3])
"""

#ex2.4
"""
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital"

print("B appears:", text.count("B"),"times")

"""

#ex2.5

"""
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."

print(text[len(text)-10:len(text):])

"""

#ex.2.6
"""
text = '---Python programming---'

print(text.replace("-",""))

"""

#ex2.7

"""
firstname = "Mary"
lastname = "Mat"

print("Firstname:",firstname,"\nLastname:",lastname)
"""

#ex3

"""
secret = input("*secret*")
name = input("*name*")
year = input("*year*")

if len(secret) >= 8:
  print(((secret+name)[::-1])+year)
else:
  print("False! Secret should be at least 8 characters")
"""

#ex4
"""
line = str(input("print something:  "))
print(len(line))
if len(line) % 2 == 0:
  print("the length of the string is even")
else:
  print("the length of the string is odd")
"""

#ex5
"""
inp = str(input("Enter a word:"))
print("The length of the word: ", len(inp))
print(inp+"inator "+str(len(inp)*1000))

"""

#ex6



# given_string = """One morning, when Gregor Samsa woke from troubled dreams, 
# he found himself transformed in his bed into a horrible vermin.
#  He lay on his armour-like back, and if he lifted his head a 
# little he could see his brown belly, slightly domed and divided by 
# arches into stiff sections. The bedding was hardly able to cover 
# it and seemed ready to slide off any moment. His many legs, pitifully 
# thin compared with the size of the rest of him, waved about helplessly 
# as he looked."""
# print(given_string.find("Gregor"))
# print(given_string[18:24:])
# print(given_string.index("He"))
# print(given_string.index("ll"))
# print(given_string.index("o"))
# print(given_string[124:126]+given_string[217:219]+given_string[5]+given_string[17:24])

#ex7

ogstring = str(input("Enter your string: "))

print(ogstring.upper())
print(ogstring.lower())