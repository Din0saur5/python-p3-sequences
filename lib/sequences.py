#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = [0]
    if length == 0:
        print([])
    else:
        if length == 1:
            print(fib_list)
        else:
            fib_list.append(1)
            for num in range(1,length-1):
                nxt_num= fib_list[num]+fib_list[num-1]
                fib_list.append(nxt_num)
            print(fib_list)
         
         
        