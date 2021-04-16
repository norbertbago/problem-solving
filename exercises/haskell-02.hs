
-- add   ()
add_numbers :: Integer -> Integer -> Integer
add_numbers a b = a + b

-- sub  
sub_numbers :: Integer -> Integer -> Integer
sub_numbers a b = a - b 

-- multi 
multi_numbers :: Integer -> Integer -> Integer
multi_numbers a b = a * b 

-- div 
div_numbers :: Integer -> Integer -> Integer 
div_numbers a b = (div) a b 

-- product 
power_two :: Integer  -> Integer 
power_two a = (^) a 2  

x :: (Ord a, Integral b) => (a,b) -> a
x (a,b) = a 

-- t: odd
-- clear - ctr + l
-- quit  - ctr + d 

-- Lists 
a = 1:2:3:[]
b = (:) 1 ((:) 2 ((:) 3 []))


-- Napiste funkci ktera vrati druhy prvek seznamu pokud je aplikovana na seznam delky alespon dva 

-- pomocou pojmoveho vzoru @
f (a@(x:y:z)) = y

-- klasicky zapis funkcie 
be :: [a] -> a 
be (x:y:z) = y