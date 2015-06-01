#!/usr/bin/python
#filename = addr.py
import os,sys
import time
import cPickle as cp
class Card:
    def __init__(self,name,phonenumber,email,birthday,note = ""):
        self.name = name
        self.phonenumber = phonenumber
        self.email = email
        self.birthday = birthday
        self.note = note
    # def __del__(self):
        # print "%s have deleted from the directory"%self.name
        # print "info as follow :"
        # print """\
                # Phone Number:%d
                # E-mail      :%s
                # Birthday    :%s
                # Note        :%s
                # """%(self.phonenumber,self.email,self.birthday,self.note)
    def show_info(self):
         print """\
                Name        :%s
                Phone Number:%d
                E-mail      :%s
                Birthday    :%s
                Note        :%s
                """%(self.name,self.phonenumber,self.email,self.birthday,self.note)




def show_banner():
    print "###########################################"
    print "###########################################"
    print "###########################################"
    print "###########################################"
    print "###########################################"
    print "###########################################"
    print "###########################################"

def show_option():
    print "1: search"
    print "2: add"
    print "3: delete"
    print "4: modify"
    print "5: exit"

def load_card(card_list):
    filename = "card.txt"
    print "loading\n"
    if filename in os.listdir("."):
        f = file("card.txt")
        while 1:
            try:
                item = cp.load(f)
                print item
            #if len(item) == 0:
            #   break
            except EOFError:
                break
            else:
                card_class = Card(item['name'],item['phonenumber'],item['email'],item['birthday'],item['note'])
                card_list.append(card_class)
        f.close()
    
def dump_card(card_list):
    filename = "card.txt"
    if filename in os.listdir('.'):
        f =file("card.txt",'a')
    else:
        f = file("card.txt","w")
    dic = {}
    for item in card_list:
        dic['name'] = item.name
        dic['phonenumber'] = item.phonenumber
        dic['email'] = item.email
        dic['birthday'] = item.birthday
        dic['note'] = item.note
        cp.dump(dic,f)
   
    f.close()

def show_card(card_list):
    print "Now the card contain : "
    for content in card_list:
        print "======================"
        content.show_info()
        print "======================"
    

def add_card(card_list):
    confirm = 0
    while not confirm:
        name = raw_input("Enter the name: ")
        phonenumber = int(raw_input("Enter the phone: "))
        email = raw_input("Enter the email: ")
        birthday = raw_input("Enter the birthday: ")
        note = raw_input("Enter the note: ")
        
        print name + '\n' + str(phonenumber) + '\n' + email + '\n' + birthday + '\n' + note + '\n'

        confirm = int(raw_input("Confirm the Info? 1/0"))
            

    new_card = Card(name,phonenumber,email,birthday,note)
    card_list.append(new_card)
    
    confirm = raw_input("If you want to check the current card list ? Y/N")
    
    if confirm[0].lower() == 'y':
        show_card(card_list)
    time.sleep(2)

def del_card(card_list):
    
    return

def modify_card(card_list):

    return

def search_card(card_list):
    name = raw_input("The name you want to search: ")
    item = [item for item in card_list if name == item.name]
    if len(item) == 0:
        print "No such person"
    else:
        for i in item:
            i.show_info()
    time.sleep(2)

card_list = []
load_card(card_list)
while 1:
    #os.system('clear')
    show_card(card_list)
    show_banner()
    show_option()
    option = int(raw_input("Which operation do you want?"))
    if option == 1:
        search_card(card_list)
        print card_list
    elif option == 2:
        add_card(card_list)
        print card_list
    elif option == 3:
        delete_card(card_list)
    elif option == 4:
        modify_card(card_list)
    else:
        break
dump_card(card_list)
print "Exit Contacts system"

