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
