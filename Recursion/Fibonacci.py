#O(2^N) T and O(N) S

####Finonacci Series 


def find_fib(n):
   if n == 1:
      return 0
   elif n == 2:
      return 1
   else :
      return find_fib(n-1) + find_fib(n-2)
