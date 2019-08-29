import pprint
message = 'It was a bright cold day in April, and the clocks were striking thriteen'

count = {} #empty set to store data in 

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] +1

pprint.pprint(count)

#This was written not dictated by Alex Foster