# Write your solution here

def getUserInfo():

    name=input("name:")
  
    number=(input("number:"))
    
    print("ok!")
    return [name,number]



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
                name,number=getUserInfo()
                records[name]=number

        elif command==1:

            phone_num=searchByName(records)
            
            if phone_num==None:
                print("no number")
            else:
                print(phone_num)

        elif command==3:
            print("quitting...")
            break









run_phone_book_app()
