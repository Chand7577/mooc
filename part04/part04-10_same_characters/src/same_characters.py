# Write your solution here
# You can test your function by calling it within the following block


def same_chars(word,index1,index2):


    if index1>len(word)-1:
        return False

    if index2>len(word)-1:
        return False

    if word[index1]==word[index2]:
        return True

    return False
if __name__ == "__main__":
    print(same_chars("coder", 1, 12))