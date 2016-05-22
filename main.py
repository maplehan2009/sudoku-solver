# -*- coding: utf-8 -*-
"""
Created on Sun May 22 13:54:02 2016

@author: Jingtao
"""

import numpy as np
from functools import reduce
from numpy import NaN

def read_sudoku():
    table = np.array([[0, 4, 3, 0, 8, 0, 2, 5, 0],
                      [6, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 0, 9, 4],
                      [9, 0, 0, 0, 0, 4, 0, 7, 0],
                      [0, 0, 0, 6, 0, 8, 0, 0, 0],
                      [0, 1, 0, 2, 0, 0, 0, 0, 3],
                      [8, 2, 0, 5, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 5],
                      [0, 3, 4, 0, 9, 0, 7, 1, 0]])
    return table

def small_table(table, i, j):
    i_topleft = (i / 3) * 3
    j_topleft = (j / 3) * 3
    return table[i_topleft:i_topleft+3, j_topleft:j_topleft+3].flatten()

def possible_candidates(table, i, j):
    list_all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row = table[i, :]
    column = table[:, j]
    palace = small_table(table, i, j)
    return np.setdiff1d(list_all, reduce(np.union1d, (row, column, palace)))
  
def initialization_of_table(table):
    # reference of the address of the table
    flag = False
    while(not flag):
        for i in range(9):
            for j in range(9):
                if table[i, j] == 0:
                    possible_cdd = possible_candidates(table, i, j)
                    if possible_cdd.size == 1:
                        table[i , j] = possible_cdd[0]
                        flag = True
        flag = not flag       
 
def has_empty_case(table):
    for i in range(9):
        for j in range(9):
            if table[i, j] == 0:
                return True, (i, j)
    return False, (NaN, NaN)

def test_this_case(table):
        
    
    pass

if __name__=='__main__':
    mytable = read_sudoku()
    print '\ninitial table: '
    print mytable
    
    initialization_of_table(mytable)
    
    print
    print 'after initialization: '
    print mytable
    
    
    