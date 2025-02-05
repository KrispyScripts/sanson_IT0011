def pattern_b():
    i = 1
    while i <= 7:  # Loop through 1 to 7, but skipping even rows (2nd and 4th)
        if i % 2 == 0:  # Skip even rows (2nd, 4th)
            i += 1
            continue  # Skip this iteration
        
        print(str(i) * i)  # Print the number `i`, `i` times
        i += 1

pattern_b()
