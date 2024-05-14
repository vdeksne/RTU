i = 1 
total = 0 
while i < 1000:
    total += i #gauss
    #show updates every 100
    if i % 200 == 0:
        print(f"iteration No. {i} total is now {total}")
    i+=1
print(f"Final total {total}, iteration {i}")
