
class Suitcase:
    def __init__(self,max_weight):
        self.suitCase=[]
        self.max_weight=max_weight
        self.total_weight=0
        


    def add_item(self,item:Item):
        
        if item._weight+self.total_weight<=self.max_weight:

            self.suitCase.append(item)
            self.total_weight+=item._weight
            
           

    def __str__(self):
        if len(self.suitCase)==1:
            return f"{len(self.suitCase)} item ({self.total_weight} kg)"

        return f"{len(self.suitCase)} items ({self.total_weight} kg)" 


    def print_items(self):
        for item in self.suitCase:
            print(item)
         
    
    def weight(self):
        return self.total_weight

    
    def heaviest_item(self):
        heavy_weight=-1
        heaviest_item=-1 
        if len(self.suitCase)==0:
            return None
        
        else:
            for item in self.suitCase:
                if item._weight>heavy_weight:
                    heavy_weight=item._weight
                    heaviest_item=item
        
        return heaviest_item


class CargoHold:
    def __init__(self,max_weight):
        self.cargo=[]
        self.max_weight=max_weight
        
       

    def add_suitcase(self,case:Suitcase):
        combined_weight=0
        if combined_weight+case.weight()<=self.max_weight:
            self.cargo.append(case)
            combined_weight+=case.weight()
            
            self.max_weight=(self.max_weight-combined_weight)
           
           


    def __str__(self):
        if len(self.cargo)==1:

            return f"{len(self.cargo)} suitcase, space for {self.max_weight} kg"    

        return f"{len(self.cargo)} suitcases, space for {self.max_weight} kg"    



    def print_items(self):
        for case in self.cargo:
            for item in case.suitCase:
                print(f"{item._name} ({item._weight} kg)")




if __name__=="__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
