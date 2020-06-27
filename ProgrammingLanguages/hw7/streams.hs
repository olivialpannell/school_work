main = putStrLn "hello world"


ones = 1 : ones

intList n = n : intList (n + 1)

test = intList 5
 
takeN n (e1:e2) = if n == 0 then [] 
					else e1 : takeN (n - 1) e2

test2 = takeN 4 (intList 5)