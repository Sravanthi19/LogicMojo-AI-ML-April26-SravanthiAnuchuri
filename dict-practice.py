
#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

cart = {}
for shop in (freelancers,antiques,pet_shop):
   buy_item = input(f'welcome to{shop["name"]} what do u eant to buy.! :{shop}')
   cart.update({buy_item:shop.pop(buy_item)})
print(f'u purchased {list(cart.keys())} todau it\'s all free')

#################################another program##################

def pro_crypto():
# create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz!'
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    print(keys)
    print(values)
# create two dictionaries
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))
# OR create 1 and then flip 
   
#user input 'the message' and mode
    msg = input("enter your message : ")
    msg1 = input("your message should be encode as (e) or decode as 'd' : ")
# run encode or decode
    if msg1.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
# return result
    return new_msg.capitalize()
# clean and beautify the code msg
print(pro_crypto())










#loop through stores/dicts
# for shop in (freelancers,antiques) :
#     #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
#     buy_item = input(f'Welcome to {shop["name"]}! what do you want to buy: {shop}').lower()
#     #update the cart
#     cart.update({buy_item:shop.pop(buy_item)}) # use pop...
# print(f'You Purchased {", ".join(list(cart.keys()))} Today it is all free. Have a nice day of mayhem!')
# Find
# No Results

Console
