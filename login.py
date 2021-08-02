# required libraries
from datetime import date
import pymongo
from send_mail import mail_send
import pprint
import numpy
from bson.json_util import dumps

# connecting string
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = client['project0']
mycol = mydb['clientdata']

def opetion(email):
    try:
        choice = int(input("\n\t\t1) Insert Data\t\t2) Update Data\t\t3) Delete Data\t\t4) Show Data\t\t"))
        if choice==1:
            print("\nYou choosed insertion of data ...")
            insert_data(email)
        elif choice==2:
            print("\nYou choosed updation of data ...")
        elif choice==3:
            print("\nYou choosed deletion of data ...")
            delete_data(email)
        elif choice==4:
            print("\nTake a look into your data ...")
            show(email)
        elif choice==0:
            return exit()
        else:
            print("\nPlease choose right one")
            return opetion(email)
    except Exception as e:
        print(e)
    return opetion(email)

# function which helps to add data
def insert_data(email):
    try:
        do = email.split('@')[0]
        mycol = mydb[do]
        record={}
        name = input("Company Name : ")
        ticker = input("Stock Ticker : ")
        price = input("Stock Price : ")
        dt = date.today()
        other = input("Enter Other data separated by ' ' and must be key and value : ")
        key = ['Company', 'Ticker','Date of entry', 'Other']
        val = [name, ticker,str(dt), other]
        for k, v in zip(key, val):
            record[k] = v
        i = iter(other.split())
        d = dict(zip(i, i))
        record['Other'] = d
        record = {'data':record}
        mycol.insert_one(record)

    except Exception as e:
        print(e)

def update(email):
    pass

def delete_data(email):
    do = email.split('@')[0]
    col = mydb[do]
    choose = int(input("\n\t\t1)Delete Account\t\t2)Drop Data\t\t3)Delete record"))

    if choose==1:
        otp = numpy.random.randint(1000, 9999)
        mail_send(email, otp)
        check = int(input("Enter otp :"))
        if otp==check:
            col.drop()
            mycol.delete_one({'_id':email})
            print("\nYour account deleted successfully ...".format(' * '*10))
        return exit()

    elif choose == 2:
        otp = numpy.random.randint(1000, 9999)
        mail_send(email, otp)
        check = int(input("Enter otp :"))
        if otp == check:
            col.drop()
            print("\nYour data dropped successfully ...".format(' * ' * 10))
        return opetion(email)

    elif choose == 3:
        ticker = input("Enter the ticker :")
        if ticker in [i['data']['Ticker'] for i in col.find()]:
            col.delete_one({'data.Ticker':ticker})
            print("\nRecord deleted successfully ...".format(' * ' * 10))
            return opetion(email)
        else:
            print("\nTicker is not in your data .....".format(' * '*10))
            return opetion(email)
    else:
        print("\nPlease choose right one ....")
        return delete_data(email)

# function fetch data from database and show
def show(email):
    col = mydb[email.split('@')[0]]
    for i in col.find({},{'_id':0}):
        pprint.pprint(i)
    down =  input("\nPress D for download data else press any key..... ")
    if down.upper() =='D':
        dowload(email,col)
    else:
        opetion(email)

# create ajson file using database
def dowload(email,col):
    file = open(email.split('@')[0]+".json", "w")
    file.write("[")
    for rec in col.find():
        file.write(dumps(rec))
        file.write(",\n")
    file.write("]")
    print("\nDownload Successfully ......")

#
def exit():
    print("\n\t{}\tThank you for using me \t{}".format(10*' * ',10*' * '))