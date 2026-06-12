



while True:
    print('What is your name?')
    name = input()
    #print(str(name)+' '+'is a lovely name')
    if name.lower() not in ['thumbi','tigger']:
        print('Not permitted')
        continue
    print('Do you want to know how many letters '+str(name)+' has? (Y?N)')
    ans=input()
    if ans == 'Y'or ans == 'y':
        print(len(name))
        break
    elif ans == 'N'or ans == 'n':
        print('Alright then')   
        break
    else:
        print('Error, try again')
        continue

