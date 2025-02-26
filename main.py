first_num = int(input("First num: "))
second_num = int(input("Second num: "))
if first_num > second_num:
    first_num, second_num = second_num, first_num

print("numbers in range:")
current_num = first_num
while current_num <= second_num:
    if current_num % 2 != 0:
        print(current_num, end=" ")  
    current_num += 1
print()  

count = 0
num = 100
while num <= 9999:
    num_str = str(num)
    is_count = True
    for digit in num_str:
        if num_str.count(digit) > 1:
            is_count = False
            break
    if is_count:
        count_digit += 1
    num += 1



print(f"Number DIGGIT in range 100-9999: {count_digit}")
