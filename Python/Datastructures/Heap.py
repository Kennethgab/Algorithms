# Heap datastructure, put from an array
# root: index 0
# left: 2i, right: 2i+1 , parent: i//2
#  Max-heap invariant: both children smaller or equal to parent.
import math
class Heap:
    heap_size = 0
    heap = []


    def __init__(self,array = None):




        pass
        # takes array and builds a heap out of it of all indexes from 0 to n//2
    def build_heap(self,array):
        self.heap = array
        for i in range(0, len(array)//2):
            print(i)
            self.max_heapify(i)






    def insert(self, value: int):
        pass



    def max_heapify(self, i):

        value = self.heap[i]
        left = self.heap[2*i]
        right = self.heap[2*i+1]
        # left node is bigger

        # need to perform max_heapify on node
        if left > value or right > value:

            # left node is bigger than right node
            if left > right:
                self.heap[2*i] = value
                self.heap[i] = left

            # right node is bigger than left node
            else:
                self.heap[2*i +1] = value
                self.heap[i] = right

            # recurse upward
            self.max_heapify(i//2)


array = [10, 20, 30, 40, 50, 60]

heap = Heap()

heap.build_heap(array)

print(heap.heap)
