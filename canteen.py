name = input("Enter your canteen name: ")
print("🥥"*25,f"{name} canteen","🥥"*25)
food_items = {40:["Idly","Dosa","poori"],60:["manchuria","noodles","fried rice"],30:"Ice-cream",20:["cool-drinks","water"],12:"Tea",10:["chocolate","samosa"],100:"Chicken Biryani",80:"Meals"} 
prices_list = []
for k in food_items.keys():
    prices_list.append(k)
prices_list.sort()
while(True):
    print("Enter P: prices\t M: Menu\t F: food-items\t B: Budget ")
    option = input("ENTER YOUR OPTION: ")
    if option=='P':
        print("Prices : ")
        for k in food_items.keys():
            print(k,end=" ")
    elif option=='M':
        print("Menu : ")
        for i in prices_list:
            print("MRP: ",i," Items: ",food_items[i])
    elif option=="F":
        print("Food items available: ")
        for v in food_items.values():
            print(v)
    elif option=="B":
        budget = int(input("Enter your budget: "))
        for i in prices_list:
            if i<=budget:
                print("MRP : ",i," items :",food_items[i])
    else:
        print("Thank YOU!!!")
        break


# for k,v in food_items.items():
#     print("MRP : ",k," Items : ",v)