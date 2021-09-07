introduction=input("introduce yourself: ")
character_count=0
word_count=1
for character in introduction :
    character_count=character_count+1
    if (character == " "):
        word_count=word_count+1

print (character_count)
print( word_count)
