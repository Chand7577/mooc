# Write your solution here:


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


  


# t1 = Task("program hello world", "Eric", 3)
# print(t1.id, t1.description, t1.programmer, t1.workload)
# print(t1)
# print(t1.is_finished())
# t1.mark_finished()
# print(t1)
# print(t1.is_finished())
# t2 = Task("program webstore", "Adele", 10)
# t3 = Task("program mobile app for workload accounting", "Eric", 25)
# print(t2)
# print(t3)

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

        return len(finished),len(unfinished),sum(finished),sum(unfinished)

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]


    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]




if __name__=="__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
