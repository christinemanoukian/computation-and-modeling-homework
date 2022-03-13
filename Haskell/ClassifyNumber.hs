classifyNumber x = if x<0 then "negative" else "nonnegative"
main = print(classifyNumber 5)