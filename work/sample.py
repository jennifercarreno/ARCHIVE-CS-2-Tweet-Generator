from json.tool import main
import random
import histogram

def sample(histogram):
    words = list(histogram.items())
    rand_word = random.choice(words)

    return print(rand_word[0])

def weighted_sample():
    global one_count
    global fish_count
    global two_count
    global red_count
    global blue_count
    dart = random.uniform(0,8)
    # print(dart)
    for i in range(8):
        if 0 <= dart <= 1:
            one_count += 1
            return print("one")
        if 1 <= dart <= 5:
            fish_count +=1
            return print("fish")
        if 5 <= dart <= 6:
            two_count+=1
            return print("two")
        if 6 <= dart <= 7:
            red_count+=1
            return print("red")
        if 7 <= dart <= 8:
            blue_count+=1
            return print('blue')
        else:
            return print (f"else, dart = {dart}")

def sample_test(weighted_sample):
    global one_count
    global fish_count
    global two_count
    global red_count
    global blue_count

    print(one_count)

    for i in range(10000):
        weighted_sample()
    return(print(f"one: {one_count}, two:{two_count}, red:{red_count}, blue:{blue_count}, fish: {fish_count}"))

if __name__ == "__main__":
    # histogram_dict = histogram.histogram("minimal.txt")
    # sample(histogram_dict)
    one_count = 0
    fish_count = 0
    two_count = 0
    red_count = 0
    blue_count= 0

    # weighted_sample()
    sample_test(weighted_sample)