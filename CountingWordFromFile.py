def count_words():
    file_name="test.txt"
    number_of_words=0
    file_handler=open(file_name,"r")
    for line in file_handler:
        words=line.split()
        number_of_words=number_of_words+len(words)
    
    print("This text is from file 6 ")


count_words()