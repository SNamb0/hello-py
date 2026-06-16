import os
import matplotlib.pyplot as plt #type: ignore
# pyrefly: ignore [missing-import]
os.system('cls')
# Write your Fibonacci code here:
print("How many numbers in the Fibonacci series do you want?")
n = int(input())
#print(first_number := 0)
#print(second_number := 1)
first_number = 0
second_number = 1
fibonacci_list = [first_number,second_number]
for i in range(n-2):
    
    #print(total := first_number+second_number)
    total = first_number+second_number
    first_number=second_number
    second_number=total
    fibonacci_list.append(total)

#print("My array is",fibonacci_list)
plt.plot(fibonacci_list,color='green',marker='o')
plt.xlabel("Index")
plt.ylabel("Fibonacci number")
plt.show()


    
