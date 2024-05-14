
i = 0 
while i < 10: 
    print(i)
    i += 1
    if i % 2 == 0:
        print("even number going back to start", i)
        continue
    print("doing sometging with odd number", i)

