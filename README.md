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
