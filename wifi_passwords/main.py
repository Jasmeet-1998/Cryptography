import subprocess
#to use system commands
import re
#regular expression handling

#Step1 capture the output of the 1st command mentioned in Readme and decode it as the stdout attribute has the output in bytes so we convert it into string.
output_one=subprocess.run(["netsh","wlan","show","profiles"],capture_output=True).stdout.decode()

profile_names=(re.findall("All User Profile     : (.*)\r", output_one))

wifi_list=list()

if len(profile_names) !=0:
    for name in profile_names:
        wifi_profile=dict()
        profile_info=subprocess.run(["netsh","wlan","show","profile",name],capture_output=True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"]=name
            profile_info_pass=subprocess.run(["netsh","wlan","show","profile",name,"key=clear"],capture_output=True).stdout.decode()
            password=re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"]=None
            else:
                wifi_profile["password"]=password[1]
            wifi_list.append(wifi_profile)
for x in range(len(wifi_list)):
    print(wifi_list[x])