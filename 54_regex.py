#Regular Expressions
#Regex

#Standart re kütüphanesi kullanılır
#import re

# findall()
# search()
# split()
# sub()

# [] 	Karakter seti 	"[a-l]"
# \ 	Özel karakter ayrımı 	"\d"
# . 	Herhangi bir karakter 	"he..o"
# ^ 	Başlayan kelime-harf 	"^hello"
# $ 	Biten kelime-harf 	"world$"
# * 	Hiç tekrar etmiş mi 	"aix*"
# + 	En az bir defa tekrar 	"aix+"
# {} 	Belirtilen sayıda tekrar etmiş mi	"al{2}"
# | 	Veya 	"falls|stays"

"""
[arn] 	Returns a match where one of the specified characters (a, r, or n) are present
[a-n] 	Returns a match for any lower case character, alphabetically between a and n
[^arn] 	Returns a match for any character EXCEPT a, r, and n
[0123] 	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
[0-9] 	Returns a match for any digit between 0 and 9
[0-5][0-9] 	Returns a match for any two-digit numbers from 00 and 59
[a-zA-Z] 	Returns a match for any character alphabetically between a and z, lower case OR upper case
[+] 	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

\A 	Returns a match if the specified characters are at the beginning of the string 	"\AThe"
\b 	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string") 	r"\bain"
r"ain\b"

\B 	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string") 	r"\Bain"
r"ain\B"

\d 	Returns a match where the string contains digits (numbers from 0-9) 	"\d"
\D 	Returns a match where the string DOES NOT contain digits 	"\D"
\s 	Returns a match where the string contains a white space character 	"\s"
\S 	Returns a match where the string DOES NOT contain a white space character 	"\S"
\w 	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) 	"\w"
\W 	Returns a match where the string DOES NOT contain any word characters 	"\W"
\Z 	Returns a match if the specified characters are at the end of the string 	"Spain\Z"

"""

import re

s = "kartal kalkar dal sarkar, " \
    "dal sarkar kartal kalkar "

a = re.findall("[ark]{3}",s)
print(a)
print(len(a))

a = re.search("kar",s)
print(a)

a = re.findall("[^alr]",s)
print(a)

a = re.findall("\d",s)
print(a)

a = re.split("r",s)
print(a)

a = re.sub("\s","-",s)
print(a)

a = re.sub("kar","yağmur",s)
print(a)





