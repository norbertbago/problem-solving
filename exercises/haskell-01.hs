square :: Float -> Float
square x = x * x

pyth :: Float -> Float -> Float
pyth a b = sqrt( square a + square b )

one_or_two :: Integer -> Bool
one_or_two 1 = True
one_or_two 2 = True
one_or_two _ = False

to_int :: Float -> Integer
to_int a = round a

-- Skladanie funcii
-- (one_or_two . to_int . square) 5

a_div_b :: Integer -> Integer -> String
a_div_b a b = do {
    if (*) ((div) a b) b == a
      then (show a) ++ " je delitelne cislom " ++ (show b)
      else (show a) ++ " nie je delitelne cislom " ++ (show b) };

my_even :: Integer -> Bool
my_even n = (mod) n 2 == 0









 
