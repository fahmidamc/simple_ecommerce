cart = []
while True:
    print("--------WELCOME TO FLIPKAD---------")

    print("1.LOGIN")
    print("2.REGISTRATION")
    print("3.EXIT")
    choice = input("SELECT^")

    if choice == '1':
        print("-----LOGIN-----")
        user = input("Enter Login id")
        pas = input("Enter Password")
        if pas == pswd and user == loginid:
            print("Login success!!!")
            print("                     ")
            input("Press enter to continue")

        else:
            print("login failed")
            input("press enter to continue")
            continue

        # print(val)

        # input("Press Enter to continue")

        print("-----SHOP NOW----")
        while True:
            print("1.LIST OUT ITEMS")
            print("2.CHECK OUT")
            print("3.LIST CART")
            print("4.EXIT")
            choic = int(input("Choose Option : ^"))
            itemset = [{'item_id': 1, 'item_name': '1.Pen', 'item_price': 10},
                       {'item_id': 2, 'item_name': '2.Book', 'item_price': 20},
                       {'item_id': 3, 'item_name': '3.Pencil', 'item_price': 5}]
            if choic == 1:
                lis = []
                for value in itemset:
                    lis.append(value['item_name'])
                for i in lis:
                    print(i)
                while True:
                    ch = int(input("CHOOSE ANY ITEM ID^"))
                    flag = 0
                    for item in itemset:

                        if ch == item["item_id"]:
                            # print(ch)
                            #flag = 1
                            cart.append(item)
                            print("Cart items are : ", cart)
                            print("Item added to cart")
                            input("Press enter to continue shopping or to exit")

                    else:
                        print("Item not found")

                    break

            elif choic == 2:
                if len(cart) > 0:

                    print("order placed! ", cart)

                    total = 0
                    for item in cart:
                        total = total + item["item_price"]
                    print(" The amount will be : ", total)

                else:
                    print("empty cart")
            elif choic == 4:
                print("thanks for visting us")
                break
            elif choic == 3:
                c = int(input("Do u want to clear cart (yes or no(1/0))"))
                if c == 1:
                    cart.clear()
                    print("cart cleared!",cart)
                elif c == 0:
                    print("cart not cleared",cart)
                    input("Press enter to continue")
            else:
                break

    elif choice == '2':
        print("_____REGISTRATION_____")
        loginid = input("enter your name")
        pswd = input("enter your password")
        cpswd = input("enter your password again")
        if cpswd != pswd:
            print("password do not match!!")
        else:
            print("                     ")
            print("Registered!!")
            print("                     ")
            input("Press enter to continue")
            continue

    elif choice == '3':
        break
