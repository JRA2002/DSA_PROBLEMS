import re

with open('story.txt','r') as file:
    story = file.read()


text = set(re.findall(r"<\w+>", story))
print(text)

changes = {}
for i in text:
    user = input(f'enter the word for {i} :' )
    changes[i] = user

for i in text:
    story = story.replace(i,changes[i])

print(story)


    
        