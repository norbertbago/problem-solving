arr = [1 .. 6]

sum_odd_elements :: [a] -> Int 
sum_odd_elements arr = sum ( filter odd arr)

len :: [a] -> Int
len [] = 0
len (_:arr) = 1 + len arr

update_list :: [a] -> [a]
update_list arr = map abs arr 

filter_array :: [a] -> [a]
filter_array n arr = filter fun arr where fun a = a < n
