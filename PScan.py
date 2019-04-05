#!/usr/bin/env python
# Created By ybenel
import socket
import _thread
import time
class bcolors:
          ##############################3
          Green="\033[1;33m"
          Blue="\033[1;34m"
          Grey="\033[1;30m"
          Reset="\033[0m"
          yellow="\033[1;36m"
          Red="\033[1;31m"
          purple="\033[35m"
          Light="\033[95m"
          cyan="\033[96m"
          stong="\033[39m"
          unknown="\033[38;5;82m"
          unknown2="\033[38;5;198m"
          unknown3="\033[38;5;208m"
          unknown4="\033[38;5;167m"
          unknown5="\033[38;5;91m"
          unknown6="\033[38;5;210m"
          unknown7="\033[38;5;165m"
          unknown8="\033[38;5;49m"
          unknown9="\033[38;5;160m"
          unknown10="\033[38;5;51m"
          unknown11="\033[38;5;13m"
          unknown12="\033[38;5;162m"
          unknown13="\033[38;5;203m"
          unknown14="\033[38;5;113m"
          unknown15="\033[38;5;14m"
          ###############################3
class Core(object):
    ipurl=0
    mode=1024
    menu1=False
    f=None
    network_speed="LAN"
    menu2=False
    print("        "+bcolors.unknown12+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+bcolors.unknown12+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+bcolors.unknown12+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+bcolors.unknown14+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
    print("        "+bcolors.unknown14+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
    print("        "+bcolors.unknown14+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
    print("        "+bcolors.unknown14+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
    print("        "+bcolors.unknown14+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
    print("        "+bcolors.unknown14+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
    print("        "+bcolors.unknown14+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
    print("        "+bcolors.unknown14+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
    print("        "+bcolors.unknown14+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
    print("        "+bcolors.unknown14+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
    print("        "+bcolors.unknown14+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
    print("        "+bcolors.unknown14+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
    print("        "+bcolors.unknown14+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
    print("        "+bcolors.unknown14+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
    print("        "+bcolors.unknown14+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
    print("        "+bcolors.unknown14+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
    print("        "+bcolors.unknown14+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
    print("        "+bcolors.unknown13+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+bcolors.unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+bcolors.unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+bcolors.unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+bcolors.unknown13+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+bcolors.Blue+"                   "+bcolors.unknown+"["+bcolors.unknown15+"PScan"+bcolors.unknown+"]"+bcolors.unknown+"         ")
    print("     "+bcolors.purple+"             "+bcolors.unknown+"["+bcolors.unknown9+"Created By ybenel"+bcolors.unknown+"]"+bcolors.unknown+"    "+bcolors.Reset+"\n")
    def GetData(self, url):
        self.url = url
        try:
            self.ipurl = socket.gethostbyname(self.url)
        except Exception as e:
            print ("Invalid URL or IP")
            exit(0)
        Core.ipurl=self.ipurl
        print (bcolors.Red,58*"-")
        print (22*" ",bcolors.Red,"Choices",bcolors.Red)
        print (60*"-")
        while Core.menu1 is not True:
            choice = input("\n1 - simple \n2 - extended\n")
            if choice == "1":
                Core.mode=1024
                menu=True
                break
            elif choice == "2":
                Core.mode=64000
                menu = True
                break
            else:
                print("Incorrect answer, choose 1 or 2")
        print (bcolors.Red,58*"-")
        print (22*" ",bcolors.Red,"Choices(2)",bcolors.Red)
        print (60*"-")
        while Core.menu2 is not True:
            choice = input("\n1 - LAN \n2 - Global Network\n")
            if choice == "1":
                Core.network_speed=0.05
                menu2=True
                break
            elif choice == "2":
                Core.network_speed=0.3
                menu2 = True
                break
            else:
                print("Incorrect answer, choose 1 or 2")

    def Start_Scan(self, port_start, port_end):
        Core.f = open(Core.ipurl, "a")
        try:
            for x in range(port_start,port_end):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                res = sock.connect_ex((Core.ipurl,x))
                if res is 0:
                    tmp="Port",x,"is open", socket.getservbyport(x)
                    tmp1=str(tmp[0])+" "+str(tmp[1])+" "+str(tmp[2])+" "+str(tmp[3])
                    print(bcolors.Red,tmp1)
                    Core.f.write(str(tmp)+"\n")
            Core.f.close()
        except Exception as e:
            print (e)
try:
    scan = Core()
    scan.GetData(input("Type IP or address\n"))
    print(bcolors.Red,"Range:",Core.mode,"\n Target:",Core.ipurl,"\n Scanning speed:",Core.network_speed,bcolors.Red)
    print(bcolors.Red,"Please wait...",bcolors.Red)
    for count in range(0,Core.mode):
        #print (Core.mode)
        time.sleep(Core.network_speed)
        _thread.start_new_thread(scan.Start_Scan, (count,count+1))
        if count > Core.mode:
            exit(0)
except Exception as e:
    print (e)
