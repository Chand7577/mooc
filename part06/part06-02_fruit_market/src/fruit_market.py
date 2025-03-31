# write your solution here



def read_fruits():
    fruits={}
    with open('fruits.csv') as file:
        
        for line in file:
            line=line.replace("\n","")
            line=line.split(";")

            fruits[line[0]]=float(line[1])

    return fruits


if __name__=="__main__":
    print(read_fruits())
    