class C




is_running = True



while is_running:
    print("Enter add, remove, show or quit")
    selection = input()
    if selection == 'quit':
        is_running = False
        
    if  selection == 'add':
        print('what items do you want add')
    if selection == 'remove':
        print('type remove if you want to remove items')
    if selection == 'show':
       print('hre are your add')        