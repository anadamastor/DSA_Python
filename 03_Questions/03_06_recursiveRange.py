'''
A function chich accepts a number and adds 
up all the numbers from 0 to the bumber passed
'''

def recursiveRange(num):
    assert num >= 0 and int(num) == num, "Need positive integer"
    if num == 1:
        return 1
    else:
        return num + recursiveRange(num - 1)

print(recursiveRange(2.1))