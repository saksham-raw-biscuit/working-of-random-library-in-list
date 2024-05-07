import random

list_1 = ['Violet','Indigo','Blue','Green','Yellow','Orange','Red']

print(random.choice(list_1))      ##This will give you a random item form the list
## The random.choice is the alternative to
print(list_1[random.randint(0,len(list_1)-1)])

random.shuffle(list_1)            ##This will shuffle the items from list into random order
print(list_1)

print(random.shuffle(list_1))
    #output : None

    ##random.shuffle id alternate to 
def shuffle(list_2):

    shuffle_list = []

    for i in range (0,len(list_2)):

        # print(list_2)
        length = len(list_2)
        
        rand_choice = random.randint(0,length-1)
        item = list_2[rand_choice]
        shuffle_list.append(item)
        # del list_2[rand_choice] #using del to delete, del uses the index
        list_2.remove(item)         #using remove to remove, remove uses the item
        
    return shuffle_list

print(shuffle(list_1))

