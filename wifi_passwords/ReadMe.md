#Wifi-Password and Network information Extractor Snippet.

##Note- Education Purposes Only the following script was implemented on a network that was completely owned by me 
##Dont try to use it to extract info of the networks u dont own . only you will be responsible for your own actions if u are using this method in any malicious way.
 
#below are the things automated via the python script in this mini-project.

1.)In Windows cmd open as admin.

2.)enter 'netsh wlan show profiles'
will show all the Wifi-networks to which the current system has been connected to.  

3.) 'netsh wlan show profile profilename' replace profile name with the name of the network u want to get info of.

4.)'netsh wlan show profile profilename key=clear' will display the password of the wifi network.

'python main.py' in the cmd in the wifi_passwords directory to display ssid and password of the wifi 
n/w to which the current system has ever been connected to. 