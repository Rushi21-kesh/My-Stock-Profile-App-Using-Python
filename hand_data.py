import pymongo
import main_app
import admin_access
print('\n\t {} MY STOCK DATA PROFILE {}'.format((' * ')*10,' * '*10))

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = client['project0']
mycol = mydb['clientdata']

def add_data():
    choice = int(input("\n\t\t\t1) Client User \t\t\t2) Admin\t\t\t3)Exit"))
    if choice==1:
        main_app.mail_very()
    elif choice==2:
        admin_access.admin_val()
    elif choice == 0:
        exit()
    else:
        print("\nplease choose right option .....")
        add_data()

add_data()
