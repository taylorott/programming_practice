#!/usr/bin/env python 
# import os,sys,inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# sys.path.insert(0,os.path.dirname(os.path.dirname(currentdir)))
# path = currentdir

import sys


#extracts a list of integers from a string
def extract_ints_from_string(str_in):
    list_out = []

    count1 = 0
    while count1<len(str_in):
        test1 = '0'<=str_in[count1] and str_in[count1]<='9'
        test2 = count1+1<len(str_in) and str_in[count1]=='-' and '0'<=str_in[count1+1] and str_in[count1+1]<='9' 
        if test1 or test2:
            count2 = count1+1
            while count2<len(str_in) and ('0'<=str_in[count2] and str_in[count2]<='9'):
                count2+=1
            list_out.append(int(str_in[count1:count2]))
            count1 = count2
        else:
            count1+=1

    return list_out

def parse_input(fname=None):
    myInput = None


    if fname is not None:
        load_name = os.path.join(path,fname)
        myInput = open(load_name)

    else:
        myInput = sys.stdin

    l = extract_ints_from_string(myInput.readline().strip('\n'))
    n, m, q = l[0], l[1], l[2]
    A = extract_ints_from_string(myInput.readline().strip('\n'))
    B = extract_ints_from_string(myInput.readline().strip('\n'))

    x_list = []

    for i in range(q):
        x_list.append(extract_ints_from_string(myInput.readline().strip('\n'))[0])

    myInput.close()

    return A, B, x_list



def generate_dicts(A, B):
    #takes a motal of max (len(A),len(B)) at most
    dictA = dict()
    dictB = dict()

    sumA = sum(A)
    sumB = sum(B)

    for i in range(len(A)):
        dictA[sumA-A[i]] = i 

    for j in range(len(B)):
        dictB[sumB-B[j]] = j

    return dictA, dictB


def check_X(dictA,dictB, x):
    q = 1
    #takes a total sqrt(x) iterations at most
    while (q-1)*(q-1)<=abs(x):
        if x%q == 0:
            r = x/q

            test1 = r in dictA and q in dictB
            test2 = -r in dictA and -q in dictB
            test3 = q in dictA and r in dictB
            test4 = -q in dictA and -r in dictB

            if test1 or test2 or test3 or test4: return True
        q+=1

    return False

def solution(fname=None):
    A, B, x_list = parse_input(fname)

    dictA, dictB = generate_dicts(A, B)

    for x in x_list:
        if check_X(dictA,dictB, x):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    solution()
    # solution('Input01.txt')
    # solution('Input02.txt')
    