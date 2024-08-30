with open('note.txt', 'r') as file:
    content=file.read() # Reading the entire content of the file.
    print(f"Contents of the file is:\n{content}")
    word=content.split() # Splitting the content into individual words.
 
set1=set()
set2=set()
for word in words:
 # Converting word to lowercase to avoid case mismatch.
    word=word.lower()
 # Removing punctuation and symbols from the word.
    word=word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~') 
 # check if word is not an empty string and word is not numeric.
    if word and not word.isnumeric: 
        if word not in set1:
            #storing the word in a set
            set1.add(word) 
        else:
            set2.add(word) 
unique=set1.difference(set2)
print("\nUnique words in the file are:\n", unique)
