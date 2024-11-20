#varible number of agrument using variable length argument

def sum(*args):
    total=0
    for i in args:
        total+=i
    return total

print(sum(1,2,3,4,5))