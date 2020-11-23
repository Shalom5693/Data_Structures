#O(2^N) T and O(N) S

####Finonacci Series 

# 1st Approach
def find_fib(n):
   if n == 1:
      return 0
   elif n == 2:
      return 1
   else :
      return find_fib(n-1) + find_fib(n-2)

   # 2nd Approach
   #O(N) T and O(N) S
   
   
   def find_fib(n,memory = {1:0,2:1}):
      if n in memory:
         return memory[n]
      else:
         memory[n] = find_fib(n-1,memory) + find_fib(n-2,memory)
         return memory[n]
      
   # 3rd Approach (Efficient Method)
   
   def find_fib(n):
      last_two = [0,1]
      counter = 3
      while counter <= n:
      new_fib = last_two[0] + last_two[1]
      last_two[0] = last_two[1]
      last_two[1] = new_fib
      counter +=1
      return last_two[1] for i in last_two > 0 else: return last_two[1]
      
      
      
      
      
      
  
  

         
