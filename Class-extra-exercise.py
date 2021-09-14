numbers= [[1,4,7,5],[8,5,1,11]]

even = 0 #count for even numbers

odd = 0 #count for odd numbers

for i in range(len(numbers)):

  for j in range(len(numbers[i])): #loop visit value in matrix

    if(numbers[i][j]%2==0): #if the number is even add +1 to the counter

      even +=1

    else:

      odd+=1

#print output

print(even)

print(odd)