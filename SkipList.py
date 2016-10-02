#Skip list and Skip list objects
class SkipList(object):
  def __init__(self, head=None, tail=None):
    self.head = SkipListNode(float("-inf"), None, None, None, None)
    self.tail = SkipListNode(float("inf"), None, None, None, None)
    self.head.setNext(tail)
    self.tail.setPrev(head)
    self.height = 0
    self.entries = 0

  def find(self, key):  #searches through till it finds key
    temp = self.head
    found = False
    turn = True
    while not found:
      while (temp.next != None and turn):
        if(temp.next.key < key):
          temp = temp.next
        else:
          turn = False
      if (temp.down):
        temp = temp.down
      else:
        found = True
    return temp

  #this method adds a top layer that connects from head to tail
  def addHeadTail(self):
    head = SkipListNode(float("-inf"), None, None, None, None)
    tail = SkipListNode(float("inf"), None, None, None, None)
    head.setNext(tail)
    head.setDown(self.head)
    tail.setPrev(head)
    tail.setDown(self.tail)
    self.head.setUp(head)
    self.tail.setUp(tail)
    self.head = head
    self.tail = tail
    height += 1

  def insert(self, key):
    temp, node = self.find(key), SkipListNode(key, None, None, None, None)
    if(temp.key != key):
      node.prev = temp
      node.next = temp.next
      temp.next.prev = node
      temp.next = node

      count, data = 0, random.random()
      while(data < 1):
        if(count >= self.height):
          self.addHeadTail()
        while(temp.up == None):
          temp = temp.prev
        temp = temp.up
        curr = SkipListNode(key, None, None, None, None)
        curr.prev = temp
        curr.next = temp.next
        curr.down = node
        
        temp.next.prev = curr
        temp.next = curr
        node.up = curr

        node = curr
        

class SkipListNode(object): 
  def __init__(self, key=None, prev=None, next=None, up=None, down=None):
    self.key = key
    self.prev = prev
    self.next = next
    self.up = up
    self.down = down

  def setNext(self, node):
    self.next = node

  def setPrev(self, node):
    self.prev = node

  def setUp(self, node):
    self.up = node

  def setDown(self, node):
    self.down = node

