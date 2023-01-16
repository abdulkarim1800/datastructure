class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None
class Slinkedlist:
    def __init__(self):
        self.headval = None
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
list = Slinkedlist()
list.headval = Node("Sat")
e2 = Node("Mon")
e3 = Node("Tus")
e4 = Node("Wen")

list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
list.listprint()             

                

        