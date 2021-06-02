def consecutive_zeros(string):
   n = string.split("1")
   n = [len(x) for x in n ]
   return max(n)
   
print(consecutive_zeros("1001101000110"))