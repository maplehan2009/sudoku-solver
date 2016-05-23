# -*- coding: utf-8 -*-
"""
Created on Sun May 22 13:54:02 2016

@author: Jingtao
"""

import numpy as np
from functools import reduce
from numpy import NaN

def read_sudoku():
    '''read the puzzle. 0 represents empty case'''
    table = np.zeros([9, 9])
    
    print 'Please input the puzzle line by line. Using 0 to represent the empty case'
    print 'Example of the format: '
    print '0 4 3 0 8 0 2 5 0'
    print 'Note: do not write space in the beginning nor in the end of the input'
    
    for i in range(9):
        line = raw_input('line ' + str(i+1) + ': ')
        line = np.array([int(x) for x in line.split()])
        table[i] = line
    return table

def read_sudoku_example():
    '''this is a testing example'''
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
    '''return the list of the numbers in the small nine cases table
    where lies the position (i, j)'''
    i_topleft = (i / 3) * 3
    j_topleft = (j / 3) * 3
    return table[i_topleft:i_topleft+3, j_topleft:j_topleft+3].flatten()

def possible_candidates(table, i, j):
    '''Given a position (i, j), return all the possible candidates for this case'''
    list_all = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    row = table[i, :]
    column = table[:, j]
    palace = small_table(table, i, j)
    return np.setdiff1d(list_all, reduce(np.union1d, (row, column, palace)))
  
def initialization_of_table(table):
    '''Initialization of the table: 
    fill in the cases with just one possible candidate'''
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
    '''Check whether the table has an empty case
    True means yes so we continue 
    while False means no empty case so we finish the procedure'''
    for i in range(9):
        for j in range(9):
            if table[i, j] == 0:
                return True, (i, j)
    return False, (NaN, NaN)

def test_this_case(table):
    '''main body of the code: with the recurrence idea, 
    we test simply all the possibilities of all the unfilled cases'''
    flag, (i, j) = has_empty_case(table)
    
    # check if the table is completely filled
    if flag == False:
        return True
    
    # check the possible value of the empty case (i, j)
    possible_cdd = possible_candidates(table, i, j)
    
    # if this case has no candidates. Absurd. So we return False to indicate wrong
    if possible_cdd.size == 0:
        return False
    
    # if this case has some candidates, we test them one by one
    for x in possible_cdd:
        table[i, j] = x
        if test_this_case(table):
            return True
        else:
            table[i, j] = 0
            
    # if the code runs until here. This means that we have tried all the 
    # possible values of this case but all fail in the end. So we return False
    # because the precedent must be wrong            
    return False

    
if __name__=='__main__':
    mytable = read_sudoku_example()
    #mytable = read_sudoku()
    
    print '\ninitial table: '
    print mytable
    
    initialization_of_table(mytable)
    
    if test_this_case(mytable):
        print '\nSuccess, the answer is: '
        print mytable
    else:
        print '\nFailed, this puzzle might have no answer.'
    
    
    