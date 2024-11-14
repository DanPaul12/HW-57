class Queue:
    def __init__(self):
        self.orders = []

    def addOrder(self, order):
        self.orders.append(order)

    def completedOrder(self):
        self.orders.pop(0)

    def readOrders(self):
        for order in self.orders:
            print(order)


order1 = {'customer':'steve', 'order': 'steak and eggs'}
order2 = {'customer':'dan', 'order': 'buttermilk pancakes'}
order3 = {'customer':'joyce', 'order': 'fruit smoothie'}

queue = Queue()
queue.addOrder(order1)
queue.addOrder(order2)
queue.addOrder(order3)
queue.completedOrder()
queue.readOrders()

#-----------------------------------------------------------------------------------

class Stack:
    def __init__(self):
        self.pages = []

    def addPage(self,page):
        self.pages.append(page)

    def removePage(self):
        self.pages.pop()

    def readPages(self):
        for page in self.pages:
            print(page)

    def isEmpty(self):
        return len(self.pages) == 0
    
    def countPages(self):
        count = len(self.pages)
        print("Histoy has " + str(count) + " pages")

page1 = "Home"
page2 = "About"
page3 = "Store"

stack = Stack()
stack.addPage(page1)
stack.addPage(page2)
stack.addPage(page3)
stack.removePage()
stack.readPages()
stack.countPages()
print(stack.isEmpty())
