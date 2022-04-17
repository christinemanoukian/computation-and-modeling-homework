recommendClothing :: (RealFloat a) => a -> String  
recommendClothing degreesCelsius  
    | degreesFahrenheit >= 80 = "I recommend wearing a shortsleeve shirt"
    | degreesFahrenheit >= 65 = "I recommend wearing a longsleeve shirt"
    | degreesFahrenheit >= 50 = "I recommend wearing a sweater"
    | otherwise = "I recommend wearing a jacket"
    where degreesFahrenheit = (degreesCelsius*(9/5))+32

main = print(recommendClothing 1)