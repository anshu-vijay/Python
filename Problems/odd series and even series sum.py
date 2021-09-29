start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
odd_sum = 0
even_sum = 0
for num in range(start,end+1):
    if num%2 == 0:
        even_sum = even_sum + num
    else:
        odd_sum = odd_sum + num

print("odd: ",odd_sum,"even: ",even_sum)