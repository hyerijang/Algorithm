# linkedList --> List
# def nodeToList(head): lst = [] while head: lst.append(head.val) head = head.next return lst ## List --> linkedList def listToNode(lst): head = None while lst: head = ListNode(lst.pop(), head) # reversed linked list when pop(0) return head ## linkedList -- > string def nodeToString(head): word = '' while head: word +=str(head.val) head = head.next return word
