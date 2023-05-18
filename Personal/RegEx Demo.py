import re

#s = "quick brown 111 22 333-444 fox jumps_over 666 777 the lazy_dog."

# print(re.match("quick",s))

# print(re.match("fox",s))  # will return None as it matching if string start with fox

# print(re.search("dog.$", s))

# print(re.search("l..y", s))

# print(re.findall("l..y",s))  # It will return list of words which matching the pattern

# print(re.findall("..zy",s))

# print(list(re.finditer("..zy",s)))

# print(list(re.finditer("\d",s)))  # It will print all the digits in the string separately

# print(list(re.finditer("\d{3}",s))) # It will print all digits string with length 3

# print(list(re.finditer("[a-z]*_[a-z]",s))) # It will print all words with full_word_first_letter_of_word

# print(list(re.finditer("[a-z]*_[a-z]*",s))) # It will print all words with word_word

# print((list(re.finditer("\d{3}-\d{3}",s)))) # It will print all digit string with length 3 separated by -

# s1 = "I am happy"
# print(list(re.finditer("[a-z]{2}",s1)))  #It will print am, ha, pp means 2 set of characters from string

# s2 = "I am happy, coppy, mappy"
# print(list(re.finditer("[a-z]+[p]{2}[a-z]+",s2))) # it will print all words with set of char+pp+set of char in it

# print(re.split(" ",s1))  # It will return list of words

# print(re.sub("am", "AM", s1))  # It will return string after replacing values

p="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"
pattern = re.compile(p)
s="Email addresses can be on servers on a subdomain as in john@server.com  All of the above regexes match this email address, because I included a dot in the character class after the @ symbol. But the above regexes also match john@aol...com which is not valid due to the consecutive dots."
re.findall(pattern,s)
