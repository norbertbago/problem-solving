"""
Print 
# #
# ##
# ###
# ##
# #
"""


n = 3
z = "#"

for i in range(1, 2*n+1):
    print(''.join(str(i*z if i<=n else (2*n-i)*z)))
