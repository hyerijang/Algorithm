class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None
        
class LinkedList : 
    def __init__(self) :
        self.head = Node(None)
    
    def append(self,data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next =  Node(data)
    
    def getByindex(self, index):
        node = self.head
        cnt = -1 # head의 인덱스 == -1
        while cnt < index:
            cnt += 1
            node = node.next 
        return node
    
    def delete(self, index):
        node = self.getByindex(index -1)
        if node.next is not None:
            node.next = node.next.next
    
        
    def insert(self, data, index):
        newNode = Node(data)
        
        node = self.getByindex(index-1)
        next_node = node.next        
        newNode.next = next_node
        node.next = newNode 
        return
    

    def print_all(self):
        cur = self.head
        while cur.next is not None :
            cur = cur.next
            print(cur.data, end= ' ')
        print()
        
    #코딩 인터뷰 연습문제 p141
    # 2-1중복 없애기
    def delete_all_duplicate(self):
        dic = dict()
        cur = self.head
        while cur.next is not None :
            before = cur
            cur = cur.next
            if cur.data in dic:
                before.next = cur.next;
            dic[cur.data] = True
        return
        
        
            
            
            
li = LinkedList()
li.append(0)
li.append(1)
li.print_all()
li.insert(9,1)
li.insert(0,1)
li.append(0)
li.print_all()
li.delete_all_duplicate()
li.print_all()
