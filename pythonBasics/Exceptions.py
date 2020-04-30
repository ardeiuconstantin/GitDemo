

ItemsInCart = 0

if ItemsInCart != 2: # raise Exception("Products Cart count not matching")
    pass

assert(ItemsInCart == 0)

try:
    with open('test.txt', 'r') as reader:
                reader.read()
except:
    print('There is a failure in the try block')

