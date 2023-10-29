#q1 --> Weekly pay
#Notes:
# <=35hours -->51.45/hr
# >35hours  -->88.9/hr

hours = input('Enter number of hours you worked this week: ')
hours = int(hours)
normal_pay = 51.45
overtime_pay = 88.9
if hours > 35:
 weekly_pay = (35 * normal_pay) + ((hours - 35) * overtime_pay)
else :
 weekly_pay = hours * normal_pay

print(f'This weekly payment is: {weekly_pay}')

 #Output for 12 hours:
 #Enter number of hours you worked this week: 12
 #This weekly payment is: 617.4000000000001

 #Output for 45 hours:
 #Enter number of hours you worked this week: 45
 #This weekly payment is: 2689.75

#q2 --> largest number

numbers = [3,9,1,5,7,2,11,0,3,12,3,15]
num_largest = None
print('Before', num_largest)
#creating a loop
for number in numbers:
 if num_largest is None:
     num_largest = number
 elif number > num_largest:
     num_largest = number
 print(number, num_largest)

print(f'The largest value is {num_largest}')


