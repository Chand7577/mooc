# Write your solution here
# Write your solution here

def addUserInfo(records):

    name=input("name:")
    number=(input("number:"))
    print("ok!")
    if name not in records:
        records[name]=[]
        records[name].append(number)
    else:
        records[name].append(number)



def searchByName(records):
    name=input("name:")
    for key in records.keys():
        if name not in records:
            return None
        if key==name:
            return records[key]


def run_phone_book_app():
    records={}

    while True:
        command=int(input(f"command (1 search, 2 add, 3 quit):"))

        if command==2:
                addUserInfo(records)

        elif command==1:
            phone_num=searchByName(records)
            
            if phone_num==None:
                print("no number")
            else:
                for number in phone_num:
                    print(number)

        elif command==3:
            print("quitting...")
            break









run_phone_book_app()
