for i in range (1,90):
    
    print(i)
    
    if(i != 10):
        continue # Skips the iteration
    else:
        break # Break this iteration
    
# The logic here is that until i is 10, the iteration will continue but will break as soon as i = 10.
# So it should print 1 to 10