
class Node:
    #This node class serves as heap min tree, so keep that in mind while evaluating the insert and delete dunctions below
    def __init__(self,data):
        self.data = data
        self.parent = self.child = self.left = self.right = None
        self.degree = 0
        self.mark = False
class FibonacciHeap:
    def __init__(self):
        self.Hmin = None
        self.root_list = None
        self.count = 0
        self.tail = None




    #this is the actual function of fibonacci heap which uses a wrapper function of insertatend that serves as insert for min heap tree.
    def Insert(self, data):
        n = Node(data)
        n.left = n.right = n
        #self.tail = n
        self.Insertatend(n)
        if self.Hmin is None or n.data < self.Hmin.data:
            self.Hmin = n
        self.count+= 1







    #these below are supporting functions for the delete function whch is too a wrapper function,not related to fibonacci heap class but mandatory
    def DeleteatFirst(self):
        if self.root_list == None and self.tail == None:
            raise ListEmpty("The list is empty")
        if self.root_list== self.tail:
            self.root_list,self.tail = None,None
        else:
            x = self.root_list
            self.root_list = self.root_list.right
            self.root_list.left=None
            x = None

    def DeleteatEnd(self):
        if self.root_list == None and self.tail == None:
            raise ListEmpty("The list is empty")
        if self.root_list == self.tail:
            self.root_list,self.tail = None,None
        else:
            x = self.tail
            self.tail = self.tail.left
            self.tail.right = None
            x = None
    def DeletebyValue(self,value):
        x = self.root_list
        print(x.right)
        while (x!=None) and (x.data!=value.data):
            x = x.right
        if x  == None:
            raise ItemNotFound("Item not found in the list")
        elif x == self.root_list:
            self.DeleteatFirst()
        elif x == self.tail:
            self.DeleteatEnd()
        else:
            x.left.right = x.right
            x.right.left = x.left
            x = None


    #this is a function that only returns the minimum value in O(1).
    def Minimum(self):

        return self.Hmin.data

    '''def remove_from_root_list(self, node):
        if node == self.root_list:
            self.root_list = node.right
        node.left.right = node.right
        node.right.left = node.left'''




    #Union function for merging two heaps
    def Fib_Heap_Union(self,H1,H2):
        global H

        H = FibonacciHeap()

        #H = H1
        H.Hmin = H1.Hmin

        H.root_list = H1.root_list




        #H.root_list, H.Hmin = root_list, Hmin

        last = H2.root_list.right
        H2.root_list.left = H.root_list.right
        H.root_list.left.right = H2.root_list
        H.root_list.left =last
        H.root_list.left.right = H.root_list

        # update min node if needed
        if H2.Hmin.data < H.Hmin.data:
            H.Hmin = H2.Hmin
        # update total nodes

        H.total_nodes = H1.count + H2.count

        self.count = H.total_nodes

        self.root_list = H.root_list
        c = 0
        current = H.root_list

        print('Keys after union of two heaps:')
        while c != H.total_nodes:
            print(current.data, end='  ')
            current = current.right
            c += 1




        #print('\n','Total nodes after union',H.total_nodes)
    #another wrapper function to traverse through the min heap tree
    def iterate(self, head):
        if head is None:
            #Stops further iteration,learnt from google.
            raise StopIteration()
        result = head
        head = head.right

        yield result

        '''node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right'''

    def iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.right
    #the function for which fibonacci heap is famous for.


    def extract_min(self):
        children = []
        z = self.Hmin

        if z is not None:
            if z.child is not None:
#inserting all the children of z in a list first
                #self.display(z.child)
                children = [x for x in self.iterate(z.child)]

            for i in range(len(children)):
                self.Insertatend(children[i])
                children[i].parent = None

            self.DeletebyValue(z)
            if z == z.right:
                self.Hmin = self.root_list= None
            else:
                self.Hmin = z.right
                self.Consolidate()
            self.count-=1
        return z.data


    #a wrapper function of extract min that is used for maintaining the right degrees through out.
    def Consolidate(self):
        A = [None for i in range(self.count)]


        nodes = [w for w in self.iterate(self.root_list)]



        for w in range(len(nodes)):
            x = nodes[w]
            d = x.degree
        while A[d]!= None:
            y = A[d]
            if x.data > y.data:
                temp = x
                x,y = y,temp
            self.heap_link(y,x)
            A[d] = None
            d+=1
            A[d] = x

        for i in range(len(A)):
            if A[i] is not None:

                if A[i].data < self.Hmin.data:
                    self.Hmin = A[i]

    def heap_link(self, y, x):
        self.DeletebyValue(y)
        y.left = y.right = y
        self.MakeChild(x, y)
        x.degree += 1
        y.parent = x
        y.mark = False
    #in the extract min function when consolidate works we have to make the minimum node from the same rank tree a child, for which the below function is used
    def MakeChild(self,x,y):
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node

    def Insertatend(self, node):
        if self.root_list is None:
            self.root_list = node
        else:
            node.right = self.root_list.right
            node.left = self.root_list
            self.root_list.right.left = node
            self.root_list.right = node
    # this function uses two method wrapper method actually to decrease a key of given to desired value, actually it was made for delete function of Fheaps so it decrease the key to - infinity and extract min can delete it easily.
    def DecreaseKey(self,v,k):
        x = Node(v)

        if k>x.data:
            raise Exception('Invalid key')
        x.data= k
        y = x.parent
        if y is not None and x.data<y.data:
            cut(x,y)
            cascadingcut(y)
        if x.data< self.Hmin.data:
            self.Hmin = x
    def cut(self,x,y):
        if x.child == x.child.right:
            x.child = None
        elif x.child == y:
            x.child = y.right
            y.right.parent = parent
        y.left.right = y.right
        y.right.left = y.left
        y.degree-=1
        self.Insertatend(x)
        x.parent = None
        x.mark = False
    def cascadingcut(self,y):
        z = y.parent
        if z is not None:
            if y.mark == False:
                y.mark = True
            else:
                cut(y,z)
                cascadingcut(z)
    def Delete(self,v):
        x = Node(v)
        g = x.data
        g2 = float(g)
        self.DecreaseKey(g,-float('inf'))
        self.extract_min()
    def ShowKeys(self):
        c = 0
        current = self.root_list

        print('Keys:')
        while c!= self.count:

            print(current.data, end='  ')
            current = current.right
            c+=1






global lst

if __name__ == '__main__':





    print( '\t'*10, 'This is an implementation of Fibonacci Heap:')

    def Ask():


        print('\n\nDisclaimer : First you have to make heap , there\'s no choice.\n\n')
        print('Disclaimer : Select options by numbers and enter Done when you want to terminate!')
        print('1) Make Heap')
        print('2) Insert')
        print('3) Return Min')
        print('4) Extract Min')
        print('5) Decrease Key')
        print('6) Union')
        print('7) Show keys')
        ask = input('What do you want to do?')
        if ask == '1':
            global H1
            H1 = FibonacciHeap()
            print('Heap Created')
            Ask()
        if ask == '2':
            ask_many = int(input('how many values :'))
            for i in range(ask_many):
                ask2 = int(input('Enter value to be inserted: '))

                H1.Insert(ask2)
            Ask()
        if ask == '3':

            print('Min value is:', H1.Minimum())
            Ask()
        if ask == '4':
            print('Extracted value is ',H1.extract_min())
            Ask()
        if ask == '5':
            ask4 = int(input('Key to be decreased : '))
            ask5 = int(input('Desired decreasing value: '))
            H1.DecreaseKey(ask4,ask5)
            Ask()



        if ask == '6':
            lst = 7
            print(lst)
            global f


            f = FibonacciHeap()
            print('Insert values into the second heap you want to make union of:')
            H2 = FibonacciHeap()
            ask_many = int(input('how many values :'))
            for i in range(ask_many):
                ask2 = int(input('Enter value to be inserted: '))

                H2.Insert(ask2)

            f.Fib_Heap_Union(H1,H2)




            Ask()
        if ask == 'Done':
            print('Okay.')
        if ask == '7':
            print('Before Union : ')
            H1.ShowKeys()
            Ask()
    Ask()

c = FibonacciHeap()
c.Insert(2)
c.extract_min()


















