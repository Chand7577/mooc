# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.rooms=[]
        

    def add(self,person:Person):
        
        self.rooms.append(person)

    def is_empty(self):
        return len(self.rooms)==0

    def print_contents(self):
        combined_height=0
        for person in self.rooms:
            combined_height+=person.height

        print(f"There are {len(self.rooms)} persons in the room, and their combined height is {combined_height} cm")
        
        for person in self.rooms:
            print(f"{person.name} ({person.height}cm)")


    def shortest(self):
        if not self.is_empty():
            shortest_person=-1
            min_height=10000000000
            for person in self.rooms:
                if min_height>person.height:
                    min_height=person.height
                    shortest_person=person
            
            return shortest_person
        return None

    def remove_shortest(self):
       
        if not self.is_empty():
            short_person=self.shortest()
            if short_person:
                self.rooms.remove(short_person)
                return short_person        
            
        return None


if __name__=="__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    # print()

    removed = room.remove_shortest()
    # print(removed)
    # print(f"Removed from room: {removed.name}")

    # print()

    room.print_contents()
