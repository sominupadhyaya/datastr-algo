def reverse_words_in_str(string):
    reverse = ""
    
    for i in reversed(range(len(string))):
        reverse += string[i]
    print(reverse)

reverse_words_in_str("Hello there")