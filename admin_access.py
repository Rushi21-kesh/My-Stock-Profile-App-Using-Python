import pprint

import pymongo
from send_mail import mail_send
import numpy
def admin_val():
    user_id = input("Enter used id : ")
    password = input("Enter your password : ")

    if (user_id == 'enter user id') and (password == 'enter password'):
        otp = numpy.random.randint(1000, 9999)
        mail_send(user_id, otp)
        check = int(input("Enter otp : "))
        if otp == check:
            admin_ac(user_id)
        else:
            print("Invalid otp ....... ")
            admin_val()
    else:
        print("Check user_id and password ..... ")
        admin_val()

def admin_ac(email):
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    mydb = client['project0']
    mycol = mydb['clientdata']
    choice = int(input("\n\t\t1)Check user info \t\t2)List of Collection\t\t3)Exit"))
    if choice==1:
        for i in mycol.find():
            pprint.pprint(i)
        admin_ac(email)
    elif choice==2:
        for i in mydb.list_collection_names():
            pprint.pprint(i)
        admin_ac(email)
    else:
        print("\n\t{}\tThank you for using me \t{}".format(10 * ' * ', 10 * ' * '))
        exit()
