# Write your solution here



class Task:
    id=0
    def __init__(self,desc,programmer,workload):
        Task.id+=1
        self.description=desc
        self.programmer=programmer
        self.workload=workload
        self.id=Task.id
        self.task_done=False


    def is_finished(self):
        return self.task_done


    def mark_finished(self):
        self.task_done=True
        return self.task_done


    def __repr__(self):
        work_status="NOT FINISHED" if  not self.task_done else "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {work_status}"


  

class OrderBook(Task):
    def __init__(self):
        self.orders=[]


    def add_order(self,desc,programmer,workload):
        task=Task(desc,programmer,workload)
        self.orders.append(task)
    
    def all_orders(self):

        return [task for task in self.orders]


    def programmers(self):
        return list(set([task.programmer for task in self.orders]))


    def mark_finished(self,id:int):
        
        for order in self.orders:
            if order.id==id:
                order.mark_finished()
                return
        
        raise ValueError()


    def status_of_programmer(self,programmer:str):
        finished=[]
        unfinished=[]
        found=False
        for order in self.orders:
            if order.programmer==programmer:
                found=True
                if order.is_finished():
                    finished.append(order.workload)
                        
                else:
                    unfinished.append(order.workload)

        if not found:
            raise ValueError()

        return f"tasks: finished {len(finished)} not finished {len(unfinished)}, hours: done {sum(finished)} scheduled {sum(unfinished)}"

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]


    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]

    def __iter__(self):
        self.current=0
        return self

    def __next__(self):
        if (self.current)<len(self.orders):
            task=self.orders[self.current]
            self.current+=1
            return task

        else:
            raise StopIteration



def get_task_info(orders:OrderBook):
    try:
        desc=input("description:")
        programmer,workload=input("programmer and worload estimate:").split()
        orders.add_order(desc,programmer,int(workload))
        print("added!")

    except ValueError:
        print('erroneous input ')

def get_finished_tasks(orders:OrderBook):
    
    if len(orders.finished_orders())==0:
        print("no finished tasks")


    else:
        for order in orders.finished_orders():
                print(order)

    
def get_unfinished_tasks(orders:OrderBook):
    if len(orders.unfinished_orders())==0:
        print("no finished tasks")


    else:
        for order in orders.unfinished_orders():
                print(order)   


def mark_as_finished(orders:OrderBook):
    try:
        id=int(input("id:"))
        orders.mark_finished(id)
        print('marked as finished')
    except ValueError:
        print("erroneous input")

def getProgrammers(orders:OrderBook):
    for programmer  in orders.programmers():
        print(programmer)


def getStatus(orders:OrderBook):
    try:
        programmer=input("programmer:")
        return orders.status_of_programmer(programmer)

    except ValueError:
        return "erroneous input"

def main():
    print('commands:')
    print('0 exit')
    print('1 add order')
    print('2 list finished tasks')
    print('3 list unfinished tasks')
    print('4 mark task as finished')
    print('5 programmers')
    print('6 status of programmer')
    orders=OrderBook() # initalizing the class OrderBook,holds reference to the current instance of class OrderBook

    while True:
        command=int(input('command:'))

        if command==1:
            get_task_info(orders)

        elif command==2:
            get_finished_tasks(orders)

        elif command==3:
            get_unfinished_tasks(orders)

        elif command==4:
            mark_as_finished(orders)


        elif command==5:
            getProgrammers(orders)

        elif command==6:
            print(getStatus(orders))
            
        elif command==0:
            break
            

main()
    # orders = OrderBook()
    # orders.add_order("program webstore", "Adele", 10)
    # orders.add_order("program mobile app for workload accounting", "Adele", 25)
    # orders.add_order("program app for practising mathematics", "Adele", 100)
    # orders.add_order("program the next facebook", "Eric", 1000)

    # orders.mark_finished(1)
    # orders.mark_finished(2)

    # status = orders.status_of_programmer("Adele")
    # print(status)
