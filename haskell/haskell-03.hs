--- Lesson 3 : Function on list and Recursion 

a = [1 .. 10]

first_a = head(a)
last_a = last(a)
tail_a = tail(a)
init_a = init(a)

my_first :: [a] -> a
my_first (x:t) = x

my_tail :: [a] -> [a]
my_tail (x:t) = t

--- (:) (++)

-- Exercise 1 Zdvojte první prvek seznamu.
exercise_1 :: [a] -> [a]
exercise_1 s = (head s):s

exercise_1_1 :: [a] -> [a]
exercise_1_1 x = [head x]++[head x]++tail(x)
exercise_1_2 x = [head x]++x

--exercise_1_2 :: [a] -> [a]
--exercise_1_2 x = (head a):(head a):[]++tail(a)


-- Zduplikujte seznam a na konec přidejte první prvek.
exercise_2 :: [a] -> [a]
exercise_2 s = s++s++[head s]
exercise_2_1 s = s++s++(head a):[]

-- Prohoďte první dva prvky seznamu.
exercise_3 :: [a] -> [a]
exercise_3 s = (head (tail s)):head s:tail(s)

exercise_3_1 (x:y:t) = y:x:t

-- Prohoďte první a poslední prvek seznamu.
exercise_4 :: [a] -> [a]
exercise_4 s = last s:tail (init s)++[head s]
exercise_4_1 s = (last s:[])++(tail (init s))++(head s:[])


-- Rozhodněte, zda je seznam palindrom.
-- aky tip
exercise_5 s = s == reverse s


-- Na neprázdných seznamech typu Num a => [a] definujte
-- funkci, která rozhodne, zda je součet prvků seznamu větší, než
-- součin.

exercise_6 :: Num a => [a] -> Bool 
exercise_6 s = sum a > product a

-- Dlzka rovnaka ako sucet prvkov 
exercise_6_1 s = toInteger(length s) == sum  s

-- let f x= x**2 in map f [4,5,6]

-- Rozhodněte, zda je seznam typu Integral a => [a] tvořen
-- pouze sudými čísly.

exercise_7 :: Integral a => [a] -> Bool
exercise_7 s = and (map odd s)

-- Úkol 6
-- Definujte funkci, která vrátí délku zadaného seznamu, tak,
-- abyste nepoužili funkci length .

exercise_8 s = sum (let f x = 1 in map f s)

-- Pro seznam dvojic, zaměňte první složku každé dvojice za
--druhou a naopak. Funkci definujte s použitím klíčového slova
--where .

b = [(1,2),(5,4)]

exercise_9 s = map fnuk s where fnuk (x,y) = (y,x)
exercise_9_1 s = let fnuk1 (x,y) = (y,x) in map fnuk1 s


fn :: Ord a => [a] -> Bool 
fn s = and ( map f ( zip s (head s:s))) where f (a,b) = a>=b 

--- my lenght function 

my_len :: [a] -> Int
my_len [] = 0
my_len (_:s) = 1 + my_len s

---- my lenght function 

my_factorial :: Integer -> Integer
my_factorial 0 = 1
my_factorial x = x * my_factorial(x-1)




--- my reverse funciton 
my_reverse :: [a] -> [a]
my_reverse (x:[]) = [x]
my_reverse  (x:s) = my_reverse s ++ [x]


