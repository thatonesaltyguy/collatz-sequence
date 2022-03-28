print ("what is number?")
def collatz(number):
 if (number % 2 == 0):
  return number // 2
 else:
      result = (3 * number + 1)
      return result
 return number 


n = int(input())
while n != 1:
   n = collatz(n) 
   print(n)

Exception(ValueError())

   
   



