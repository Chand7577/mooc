# Write your solution here


def no_vowels(sentence):
    new=""
    for char in sentence:
        if char not in ["a","e","i","o","u"]:
            new+=char

    

    return new


if __name__=="__main__":

    print(no_vowels("this is an example"))