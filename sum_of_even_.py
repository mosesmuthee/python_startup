numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
sum_of_even=0
for number in numbers:
    if number %2 == 0:
        sum_of_even += number
print(f"The sum of even numbers is {sum_of_even}")

# sum
sum_of_all_numbers=0
for sum2 in numbers:
    if sum2 %1 ==0:
        sum_of_all_numbers += sum2
print(f"The sum of all numbers is {sum_of_all_numbers}")