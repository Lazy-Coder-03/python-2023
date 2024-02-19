class myQueue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self.queue.pop(0)
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def show_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue)
    
def main():
    print("Queue operations")
    q = myQueue()
    while True:
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            item = int(input("Enter the item: "))
            q.enqueue(item)
            q.show_queue()
        elif choice == 2:
            if q.is_empty():
                print("Queue is empty")
            else:
                q.dequeue()
                q.show_queue()
        elif choice == 3:
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()            