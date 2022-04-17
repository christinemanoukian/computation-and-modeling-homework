complicatedList n = length[(x,y) | x <- [-n..n], y <- [-n..n], -n <= x, y <= n, x-y <= (x*y)/2, (x*y)/2 <= x+y, x `notElem` [-2, -1, 0, 1, 2], y `notElem` [-2, -1, 0, 1, 2]]

main = print(complicatedList 50)
