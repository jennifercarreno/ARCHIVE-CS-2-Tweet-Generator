
import random
histogram_dict = {

    }

def histogram(source_text):
    #todo: split into words
    text = source_text
    words = text.split()
    # print(len(words))

    
    #todo: count each time the word appears 
    for i in range(len(words)):
        # print(words.count(words[i]))
        histogram_dict[words[i]]= words.count(words[i])
        


    return print(histogram_dict)

def unique_words(histogram):
    return

if __name__ == "__main__":
    histogram("one two three three four four four")