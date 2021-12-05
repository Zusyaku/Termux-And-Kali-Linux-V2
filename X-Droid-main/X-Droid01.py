print("""
__  __     ____            _     _
\ \/ /    |  _ \ _ __ ___ (_) __| |         
 \  /_____| | | | '__/ _ \| |/ _` |    
 /  \_____| |_| | | | (_) | | (_| |
/_/\_\    |____/|_|  \___/|_|\__,_|v0.1®

""")
db = {}
print('Welcome!, I am X~Droid v0.1\nDesigned by Myth for data storage\n')
while True:
    r = input( 'Shall we begin?\n(Y/N) >>> ')
    if r == 'N':
        print('Alright, Watch out for v0.2 with a new feature....Bye!')
        break
    elif r == 'Y':
        print('\nGreat!')
        print('So, what do you want to do?')
        break
while True:
        print('\nInput (S) to Save, (O) to Open already saved data, (L) to List all saved data') 
        print('or (Q) to Quit\n')
        a = input('>>>')
        if a == 'S':
            n = input('Data name: ')
            i = input('Data info: ')
            db[n] = i
        elif a == 'O':
            n = input('Data name: ')
            if not n in db:
                print('No such Data name!')
            else:
                print('Your Data info: '+db[n]+'\n')
        elif a == 'L':
            print('Lists of Data names:')
            print(db)
        elif a == 'Q':
            print('Thank you for using X~Droid, v0.2 will be out soon with a new feature, stay tuned...Bye!')
            break
exit()
