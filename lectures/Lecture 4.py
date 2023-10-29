#q1 -->Even Numbers
test_list = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]
def is_even_num(lis):
    even_num = []
    for n in lis:
        if n % 2 == 0:
            even_num.append(n)
    return even_num

is_even_num(test_list)
print(is_even_num(test_list))

#q2 -->Squared Elements
#Print a list only if the value of the square is greater than 150
list = [2,3,12,14,20,21,25,13,15]
new_list = [x**2 for x in list if x**2>150]
print(f'the new list contains values of squares greater than 150 which is as follows:{new_list}')

