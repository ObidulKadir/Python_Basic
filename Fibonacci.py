def fib(n):
  first_num = 0
  
  second_num = 1
 
  count = 0
  if(n>=0):
    while(count<n): 
        print(first_num) 
        next_value = first_num + second_num
        first_num, second_num = second_num,next_value
        count = count + 1

  else:
    print("Please Enter the positive Number: ")

n = int(input('Enter the sequence number: '))
fib(n)
    