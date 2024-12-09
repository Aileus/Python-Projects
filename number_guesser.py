import random as rd

def randomguesser():
    
    rd_no = rd.randint(1,100)
    print(rd_no)
    
    if rd_no-11 < 0:
        start = 1
    else:
        start = rd_no-6
        
    numbers = [i for i in range(start,rd_no+6)]
    close_number = [ i for i in range(rd_no - 2 , rd_no + 3)]
    print(close_number)
    
    print(numbers)
    while True:
        guess = int(input("Enter your guess: "))
        
        if guess in numbers and not close_number and guess != rd_no:
            print("Close!")
            
        elif guess in close_number and guess != rd_no:
            print("Pretty Close!!")            
            
        elif guess == rd_no:
            print("You have guessed the number!")
            break
        else:
            print("Far")
            
# randomguesser()

def comp_guesser(x):
    print(x)
    numbs = [ i for i in range(x-10,x+11)]
    print(numbs)
    y = 40
    while True:
        guess = rd.randint(1, x + y)
        
        if guess == x:
            print("You have guessed correctly!")
            break
        elif guess not in numbs:
            print("Far")
        elif guess in numbs:
            print("Pretty Close!")
# comp_guesser(30)

def comp_guess_v2(x):
    rg = rd.randint(1,x)
    low = x - rg
    high = x + rg
    while True:
        
        print(low,high)
        
        guess = rd.randint(low,high)
        print(guess)
        
        if guess > x :
            print("Too high!\n")
            high -= 1
            print(high)
            
        elif guess < x:
            print("Too Low!\n")
            low += 1
            print(low)
            
        elif guess == x:
            print("Guessed correctly!\n")
            break
        
comp_guess_v2(392)