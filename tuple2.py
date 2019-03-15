
def randomword(word):
    vowels=['a','e','i','o','u']

    #gets the vowels and removes duplicates and puts them into a string
    vowel_word=set([x for x in word if x in vowels])
    my_string="".join(vowel_word)

    #gets the letters of the original string that appear more than once and removes duplicates
    duplicates=set([x for x in word if word.count(x)>1])

    #returns a tuple with a string of vowels and the number of letters that are duplicates
    my_tuple= my_string,len(duplicates)
    print(my_tuple)

randomword('dahdah')