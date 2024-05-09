from os import system
garden2d = [

    ['⛅','⛅','⛅','⛅','⛅','⛅'],
    ['⛅','⛅','⛅','⛅','⛅','⛅'],
    ['⛅','⛅','⛅','⛅','⛅','⛅'],
    ['⛅','⛅','⛅','⛅','⛅','⛅'],
    ['⛅','⛅','⛅','⛅','⛅','⛅'],
    ['🌰','🌰','🌱','🌰','🌱','🌰'],
]

action = 0 
note = ''
print()
while action !=3:
    system ("cls")
    count = 0
    plants =0
    for ri in range(len(garden2d)):
        for pi in range(len(garden2d[ri])):
            plants +=len(garden2d[ri][pi])
            if garden2d[ri][pi] =="v":
                count +=1
            print (garden2d[ri][pi], ' ', end="")
        print("m"+str(len(garden2d) - ri), end="")
        print()
        if ri == len(garden2d)-1:
            for i in range(len(garden2d[ri])):
                print(' '+str(i)+'  ', end="")
     
    plants = count*100/plants
    print(note)
    print(f"Fruit:{plants:3.0f}%")
    print ("ACTION:\n1. watering\n2. collect\n3. exit")
    action = int(input("> "))
    if action  == 1:
        idx = int(input("Where: "))
        for ir in reversed(range(len(garden2d))):
            if garden2d[ir][idx] == '.':
                garden2d[ir][idx] = 'v' 
                note = ''
                break
            else: 
                note = 'The growth limit on position '+str(idx)+' has been exhausted'     
    elif action  == 2:
        idx = int(input("Where: "))
        for ir in range(len(garden2d)):
            if garden2d[ir][idx] == 'v':
                garden2d[ir][idx] = '.'
                note ='' 
                break
            else:
                note = 'There are no more fruits in the position '+str(idx)   
print()    