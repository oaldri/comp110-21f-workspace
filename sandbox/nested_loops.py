"""nested loops."""

i = 0 
total: int = 0 
while i < 10:
    count: int = 0 
    while count < 5:
        total = total + 1 
        count = count + 1 
    i = i + 1 
print(total)
