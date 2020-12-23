class node():
    def __init__(self,value):
        self.value=value
        self.link=None

class linked_list():
    def __init__(self):
        self.start=None
    
    def add_at_end(self,value):
        
        NewNode = node(value)
        if self.start is None:
            self.start = NewNode
            return
        laste = self.start
        while(laste.link):
            laste = laste.link
        laste.link=NewNode
                
    def add_at_begin(self,value):
        if self.start is None:
            new_node=node(value)
            self.start=new-node
        else:
            new_node=node(value)
            new_node.link=self.start
            self.start=new_node
                    

    def display(self):
        p = self.start
        while p is not None:
            print (p.value," >" ,end= " " )
            p= p.link
        print()
    
    def find_value(self,x):
              
        current = self.start 
  
        # loop till current not equal to None 
        while current != None: 
            count=0
            if current.value == x: 
                count+=1
                print(x ,"at position ", count)
                return True # data found 
              
            current = current.link
            
        print("not found")
        return False # Data Not found 
                    
        
        
c=linked_list()

c.add_at_end(4)
c.add_at_end(5)
c.add_at_end(6)
c.add_at_end(7)
c.add_at_begin(77)
c.add_at_begin(68)
c.display()
            
c.find_value(6)
c.find_value(68)
c.find_value(79)