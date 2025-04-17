
# Write your solution here:
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        
        
        if not name in self.__persons:
            person=Person(name)
           
            self.__persons[name]=person
        
        person=self.__persons[name]  # fetch the person using name
        person.add_number(number) # add the number to the numbers list
        

    def add_address(self,name:str,addrs:str):
        if not name in self.__persons:
            person=Person(name)
            self.__persons[name]=person
        
        person=self.__persons[name]  # fetch the person using name
        person.add_address(addrs)
     
    
    
    
    def get_entry(self, name: str):
        
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)


    def add_address(self):
        name = input("name: ")
        addrs = input("address: ")
        self.__phonebook.add_address(name,addrs)

    def search(self):
        name = input("name: ")
        numbers=self.__phonebook.get_entry(name)
        address=self.__phonebook.get_entry(name)

        if numbers!=None and address!=None:
            numbers=self.__phonebook.get_entry(name).numbers()
            if numbers==[]:
                numbers=None
            address=self.__phonebook.get_entry(name).address()

      
        if numbers == None:
            print("number unknown") 
             
        else:
            for number in numbers:
                print(number)


        if address==None:
            print("address unknown")
            return 

        print("address",address)       

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()

            elif command=="3":
                self.add_address()
            else:
                self.help()
class Person:
    def __init__(self,name):
        self._name=name
        self._numbers=[]
        self._address=""

    
    def name(self):
        return self._name

    def numbers(self):
        # if len(self._numbers)==0:
        #     return None
        
        return self._numbers
    
    def address(self):
        if len(self._address)==0:
            return None
        return self._address
      

    def add_number(self,value:str):
        self._numbers.append(value)

    def add_address(self,addrs:str):
        self._address=addrs


# person = Person("Eric")
# print(person.name())
# print(person.numbers())
# print(person.address())
# person.add_number("040-123456")
# person.add_address("Mannerheimintie 10 Helsinki")
# print(person.numbers())
# print(person.address())

# phonebook = PhoneBook()
# phonebook.add_number("Eric", "02-123456")
# phonebook.add_number("Eric", "02-133456")
# print(phonebook.get_entry("Eric"))
# print(phonebook.get_entry("Emily"))

# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
