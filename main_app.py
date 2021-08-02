import datetime
import re
import numpy
import pymongo
import login
from send_mail import mail_send

#connecting string
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
mydb = client['project0']
mycol = mydb['clientdata']

def mail_very():
    """This function helps mail verification """
    name = input("Enter full name : ")
    email = input("Enter email id : ")
    r = r'\b[A-Za-z0-9.-_]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
    if re.match(r, email):
        all_mails = [i['_id'] for i in mycol.find({}, {'_id': 1})]
        if email not in all_mails:
            otp = numpy.random.randint(1000, 9999)
            mail_send(email,otp)
            check = int(input("Enter OTP : "))
            if otp==check:
                print("Email verified successfully...... \nStart Creating your account ")
                return create_profile(name,email)
            else:
                print('you entered an wrong otp ....\n\tplease try again ...')
                mail_very()
        else:
            print("You already responded.... \n\tPlease login")
            otp = numpy.random.randint(1000, 9999)
            mail_send(email, otp)
            check = int(input("Enter OTP : "))
            if otp==check:
                print("You logged in.....\n\t")
                login.opetion(email)
    else:
        print('oops!!! please check valid email....')

def create_profile(name,email):
    try :
        record = {}
        date_entry = input("Enter DOB (DD MM YYYY) : ")
        day, month, year = map(int, date_entry.split())
        dob = datetime.date(year, month, day)
        mobile = int(input("Enter mobile number : "))
        other = input("Enter other details but make sure data is in key value pair and seprated by ' ' : ")
        key = ['_id','Name','Contact','Date of Birth','Other']
        val = [email,name, mobile, str(dob), other]
        for k,v in zip(key,val):
            record[k] = v
        i = iter(other.split())
        d = dict(zip(i,i))
        record['Other']=d
        mycol.insert_one(record)
        return login.opetion(email)
    except Exception as e:
        print(e)
