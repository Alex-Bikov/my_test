# def task(array):
#     return array.index('0')
#
# print(task("111111111110000000000000000"))

def task(array):
    count = 0
    for i in array:
        if i == '0':
            break
        count += 1
    return count

print(task("111111111110000000000000000"))