import os
import math
import random
import smtplib

def otp_genrator(emailid):

    digits="0123456789"
    global OTP
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    otp = (OTP + " is your OTP")
    msg= otp
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login("wifiplot8@gmail.com", "cjdu qaru cerb ywzg")
   # emailid = input("Enter your email: ")

    BODY = "\r\n".join((
                "From: %s" % "wifiplot8@gmail.com",
                "To: %s" % emailid,
                "Subject: %s" % "otp login" ,
                "",
                msg
                ))

    s.sendmail("wifiplot8@gmail.com",emailid,BODY)

def otp_verifier(otp):

    if otp == OTP:
        print("Verified")
        
    else:
        print("Please Check your OTP again")
        
otp_genrator("rj8277129592@gmail.com")
otp = input("Enter Your OTP >>: ")
otp_verifier(otp)
