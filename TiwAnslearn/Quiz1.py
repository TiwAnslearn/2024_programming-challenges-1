numbers_list = []
for _ in range(5):
        number = int(input("Enter list number: "))
        numbers_list.append(number)

ans = int(input("Enter number do u Need: "))

length = len(numbers_list)

for i in range(length):
        for y in range(i + 1,len(numbers_list)):
                sum = numbers_list[i] + numbers_list[y]
                if sum == ans:
                    print("[",numbers_list[i] ,numbers_list[y], "]")
