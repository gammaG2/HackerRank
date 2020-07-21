
import math
import os
import random
import re
import sys

class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.children = []
        self.isEnd = False
        self.counter=1
    
    def add(self, str_var):
        current_node = self
        
        for char in str_var:
            flag=False
            
            for child in current_node.children:
                if char == child.char:
                    flag=True
                    child.counter +=1
                    current_node=child
                    break
            if not flag:
                new_node = TrieNode(char)
                current_node.children.append(new_node)
                current_node=new_node
        current_node.isEnd = True
    
    def searchTrie(self,str_var):
        current_node = self
        # current_counter = 0
        
        for char in str_var:
            flag=False
            for child in current_node.children:
                if char == child.char:
                    flag=True
                    current_node=child
                    break
            if not flag:
                return 0
        # current_node.isEnd = True

        return current_node.counter

if __name__ == '__main__':
    n = int(input())
    root=TrieNode('')
    output_list=[]
    for n_itr in range(n):
        opContact = input().split()

        op = opContact[0]

        contact = opContact[1]
        if(op == 'add'):
            root.add(contact)
        else:
            output_list.append(root.searchTrie(contact))

    for i in output_list:
        print(i)
