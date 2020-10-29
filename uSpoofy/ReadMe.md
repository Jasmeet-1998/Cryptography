Author-Jasmeet Singh Bali

ProjectName-uSpoofer


#Features->
uSpoofer On Target Machine Can ->

-Capture System Info

-Capture Clipboard Info

-Record Device Microphone

-Take Screenshot After Equal Intervals .

-Encrypting all the Logs/Info Of the Victim

-Finally Sending Email From the Victim Device to Invoker temporary mail via SMTP.


#To Make It Work

1.)U Need to Refactor the both DecryptFile and Generatekey In Cryptography Directory.
 Remember the Key Must be Same For Both Decryption and Encryption.

2.)Replace the Variable Value With Your App Password,emailaddress,toaddress
in keylogger.py

3.)Replace the File Path variable in keylogger.py
With the File Path where The Whole Project is Situated.
For instance if u Cloned this Repo in Spoofer folder then file_path will be
C:\\Users\\user\\Desktop\\Spoofer\\uSpoofy\\Project 

Execute the keylogger.py Script

-----Thats It-------

#Problems u may Stumble Upon->

-Email Sending Problem

THE EMAIL PART to make it work either
ALLOW LESS TRUSTED APPS TO ON IN YOUR GOOGLE SETTINGS

or do the below

You  Need to Enable Two Factor authentication

FOR THE GMAILL ACCOUNT U USE FOR SENDING THIS MAIL
AND GENERATE APP PASSWORD SO AS TO USE ALLOW THIS CODE TO SEND MAILS ON BEHALF OF YOUR ACCOUNT

SET 16 DIGIT APP PASSWORD AND USE THAT PASSWORD IN THE KEYLOGGER.PY FILE.

#Sources->
1.)https://gist.github.com/tylermakin/d820f65eb3c9dd98d58721c7fb1939a8#:~:text=Multipart%20email%20strings%20are%20composed,for%20their%20email%20clients'%20capabilities.

2.)https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/

3.)https://docs.python.org/2/library/email.mime.html

and Other Python Docs for the respective Used Modules/packages in this Project.




