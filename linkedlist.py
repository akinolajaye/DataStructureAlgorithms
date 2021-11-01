class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next


class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_front(self,data):
        node=Node(data,self.head) #adds the inserted data by chaning head to next
        self.head=node 

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return

        itr =self.head
        while itr.next:#loops to go to the end of the list
            itr=itr.next

        itr.next=Node(data,None)


    def print_list(self):
        if self.head is None:
            print("Linked List empty")
            return

        itr=self.head
        print(itr.data,itr.next)
        linked_list_str=""
        while itr:
            linked_list_str += str(itr.data) + ' --> '
            itr=itr.next


        print(linked_list_str)


    def insert_values(self,data_list):
        
        for data in data_list:
            self.insert_at_end(data)



    def insert_at(self,index,data):
        if index < 0 or index >self.get_length():
            raise Exception("invalid error")

        if index==0:
            self.insert_at_front(data)
            return

        count =0
        itr=self.head
        while itr:
            if count == index-1:
                node =Node(data,itr.next)
                itr.next=node
                break

            itr=itr.next
            count+=1


    def remove_at(self,index):
        if index < 0 or index >self.get_length():
            raise Exception("invalid error")

        if index==0:
            self.head=self.head.next


        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1       

        

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1

        return count
            

x=LinkedList()
x.insert_values(["banana","mango","grapes"])
x.insert_values(["cheese","bread","apple"])

x.print_list()
x.remove_at(4)
x.print_list()
