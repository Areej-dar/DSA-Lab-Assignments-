# -*- coding: utf-8 -*-
"""200901008-LAB-05

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16cenabf9bUzyQzrI8IGr1ad8_bZk9sih
"""

import numpy as np
class Queue:
  def __init__(self):
    self.array=np.arange(6)

  def enqueue(self,data):
    x=np.append(self.array,data)
    return x

  def dequeue(self):
    self.array=np.delete(self.array,0)

  def isempty(self):
    return (len(self.array)==0)

q=Queue()

q.enqueue(6)

q.dequeue()

from collections import deque
l=deque()

l.append(1)
l.append(2)
l.append(3)
l.append(4)

print(l)

l.appendleft(6)

print(l)

l.pop()

print(l)

l.popleft()

print(l)

l.clear()

print(l)