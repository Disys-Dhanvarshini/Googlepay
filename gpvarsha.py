import random
import math


class Googlepay:
    bank = {"icici":{"Accno":"ICICI Bank 5579","type":"Savings","upi":"3455"},"SBI":{"Accno":"SBI Bank 5569","type":"Savings","upi":"3325"}}
    def __init__(self):
        self.Mobileno = input("Enter your mobile number:")
    def otpverify(self):
        if type(self.Mobileno) == str:
           if (len(str(self.Mobileno)) == 10 or len(str(self.Mobileno))!= None):
                    print("Enter OTP")
                    digits="0123456789"
                    OTP=""
                    for i in range(6):
                        OTP+=digits[math.floor(random.random()*10)]
                        otp = OTP + " is your OTP. Please dont share your OTP"
                        msg=otp
                    print(msg)
                    self.a = input()
                    if (self.a == OTP):
                            print("OTP verified")
                    else:
                        print("Invalid OTP")
        else:
                    raise ValueError("Please enter a valid phone number")
    def upiverification(self):
          bank = {"icici":{"Accno":"ICICI Bank 5579","type":"Savings","upi":"3455"},"SBI":{"Accno":"SBI Bank 5569","type":"Savings","upi":"3325"}}
          self.upi = input("Enter the upi")
          for i,j in bank.items():
                for k in j.values():
                      if(k==self.upi):
                           print("Account Verified")
                           print("Google Account Successfully Created")
    def Payment(self):
        contacts = {"Kavitha":"9234567380","Latha":"6748934678","Devi":"8946578490","Gokulraj":"9444120188","Malathi":"9444503390"}
        self.user = input("choose the person you want to pay")
        for i in contacts.keys():
            if(i==self.user):
                print("enter the amount")
                self.amount = input()
                if(len(str(self.amount != None))):
                     print("Payment done!")

on = Googlepay()
on.otpverify()
on.upiverification()
on.Payment()
