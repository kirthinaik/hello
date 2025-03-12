queue = []

size = int(input("Enter the size of the queue:"))

def Enqueue(data):
    if(isFull()):
        
        print("Queue is Full")
        
        return
    
    else:
            
        queue.append(data)
    
def isFull():
    
    return len(queue) == size

def isEmpty():
    
    return len(queue) == 0

def Dequeue():
    
    if(isEmpty()):
        
        print("Stack is Empty")
        
        return
    else:
        
        return queue.pop(0)
    
def Peek():
    
    return queue[0]

def display():
    
    print("Queue elements are:")
    
    for i in queue:
        
        print(i,end=" ")
    print()   

while(True):
    
    print("Queue operations performed are:")
    
    print("1.Enqueue")
    
    print("2.Dequeue")
    
    print("3.Display")
    
    print("4.Peek")
    
    print("5.Exit")
    
    ch = int(input("Enter your choice:"))
    
    if(ch == 1):
        
        data = int(input("Enter the data to be inserted:"))
        
        Enqueue(data)
        
    elif(ch == 2):
        
        print("Element deleted is: ",Dequeue())
        
    elif(ch == 3):
        
        display()
        
    elif(ch == 4):
        
        print("Peek element of queue is:",Peek())
        
    elif(ch == 5):
        
        print("Exiting Program ...")
        
        break
    
    else:
        
        print("Invalid input re-enter")
        
    