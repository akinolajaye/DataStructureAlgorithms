class Node:
    def __init__(self,data,next):
        self.data=data #sets the data at the front of node
        self.next=next # initilise at none because first node will be the only node and the head

class LinkedList:
    def __init__(self):
        
        self.head=None

    def insert_at_end(self,data):
        node=Node(data,None)

        if self.head is None:
            self.head=node
            return

        itr=self.head
        while itr.next:
             
            itr=itr.next

        itr.next=node

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

    def insert_at_front(self,data):
        node=Node(data,self.head) #adds the inserted data by chaning head to next
        self.head=node 


    def print_list(self):
        if self.head is None:
            print("Linked List empty")
            return

        itr=self.head
        
        linked_list_str=""
        while itr:
            linked_list_str += str(itr.data) + ' --> '
            itr=itr.next


        print(linked_list_str)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1

        return count


class solution:


    def mergeklists(self,lists):

        linklist=LinkedList() #initiate linked list
        linklist.insert_values(lists[0]) #insert initial values
        
        for i in range(1,(len(lists))):#loop based on the amount of linked lists
            itr=linklist.head#set the linklist to head
            
            count=j=k=0# set counters
            
            while j <(len(lists[i])): #while j is less than the amount of nodes
                
                if itr.data > lists[i][j]:
            
                    linklist.insert_at(count,lists[i][j])#insert if the data on node is greater than data in nodelistarray
                    count=0 #reset the counter
                    itr=linklist.head# reset the linklist back to the head
                    
                    j+=1
                    k+=1
                    
                if itr.next is not None:#if next is not at the end of list

                    itr=itr.next
                
               
                if itr.next is None and itr.data <= lists[i][j]:#if at the end of list and the list nodes are greater than nodes on the linked list
                
                    
                    j=len(lists[i])#breaks the loop
                
                count+=1#increments the counter to index the linklist
                 

            while k < (len(lists[i])):
                
                linklist.insert_at_end(lists[i][k])#assuming listarrraynodes are sorted, inserts the remaining nodes at end of linklist
                k+=1

           
        linklist.print_list()



lists=[[1,4,5,11],[1,3,5,9,10],[2,4,6,721]]
s=solution()
s.mergeklists(lists)



                

              



            