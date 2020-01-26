# Fibonacci-Heap
This is a group project for the subject Data Structures and Algorithms.

# What is Fibonacci Heap
In computer science, a Fibonacci heap is a data structure for priority queue operations, consisting of a collection of heap-ordered trees.
It has a better amortized running time than many other priority queue data structures including the binary heap and binomial heap.

# Descriptions About the project
1. Firstly it will create a Node class which will serve as a min heap tree, evaluating the insert and delete funtions.
2. Secondly in the Node it will set the parent, child and their left and right to None.
3. Then a class of Fibonacci Heap has been created where root tail and min are set to None.
4. Insert Function will add a value to the left or right of the tree. This will use a wrapper function InsertAtEnd which is not a part of fibonacci heap.
5. DeleteAtFirst, DeleteAtEnd, DeleteByValue are also the wrapper functions which are not directly linked with the Fibonacci Heap but are mandatory.
6. Minimun Function will return the minimum value in the heap.
7. FibHeapUnion. It will give union of two heaps.
8. Extract Min. It will delete the value of minimum
9. Consolidate it is also a wrapper function and it traverse the heap
10. Decrease Key. it will decrease the key to desired value. And it is made for the delete function to make the key -infinity and can delete it easily.
11. Delete function will delete the value 
12. Show Keys function will show you the keys in the fibonacci heap.

# How To Call Functions:

There is a function in the code named ASK where you will get to know how to run the cut but cut short i will tell you how the function will work and their arrangements and technicalities.
The arrangment for running Fibonacci heap's code is:
  a.)Make Heap
  b.)Insert
  c.)Return Min
  d.)Extract Min
  e.)Decrease Key
  f.)Delete
  g.)Union
  h.)Show Keys
# Make Heap:-
  It will create a heap.
# Insert:-
  It will insert a value to the left or right of the tree.
# Return Min:-
  It will return you the minimun element of the list
# Extract Min:-
  It will delete the value of the minimum and will shift the pointer to the next      
  minimum
 # Decrease Key:-
  It will decrease the key to the desired value. It is also an helpful function for   
  delete because it makes the key negative infinity and is easy to delete.
 # Show Keys:
  This function will show the keys present in the fibonacci heap.
 # Union(IMPORTANT):
  This will give you Union of two heaps.
  Now in union Function if you will directly run Union form our interface it will give 
  you union of our heaps.This will be a proof that our union is working. But after that 
  extract min and other functiosns will not be of our union function. They will be of 
  the first heap created in the start. But if you want to run extract min and other  
  functions on our unioned heap create two heaps for example H1 and H2 and third object 
  for e.g F and then after finding out the union make that F go for extract min and 
  other things.
