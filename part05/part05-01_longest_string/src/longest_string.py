# Write your solution here
# Write your solution here





def longest(strings):
    longest=""
    for word in strings:
        if len(word)>len(longest):
            #remove the previously stored value
            longest=""
            longest+=word



    return longest




if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))