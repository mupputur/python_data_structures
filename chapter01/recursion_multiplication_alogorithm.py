'''
4 (multiplier)* 6 (multipliant)

4 + 4 + 4 + 4+ 4 + 4
'''

def multiply_alog(mr, mt):
    result = 0
    for i in range(mt):
        result = result + mr
    return result

def recursion_multiply_alog(mr, mt):
    if mt == 1:
        return mr
    else:
        return recursion_multiply_alog(mr, mt-1) + mr



#print(multiply_alog(4, 6))

print(recursion_multiply_alog(4, 6))
#recursion_multiply_alog(2, 6)
#recursion_multiply_alog(1, 6)