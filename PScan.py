##########################################
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
##########################################
import socket
import _thread
import time
class bcolors:
    Red = '\033[1;31m'
class Core(object):
    ipurl=0
    mode=1024
    menu1=False
    f=None
    network_speed="LAN"
    menu2=False

    print("        "+unknown5+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown5+"MMMMMMMMMMNKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown5+"MMMMMMMMMNc.dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown8+"MMMMMMMMWd. .kWMMMMMMMMMMMMMMMMMMMMMMW0KMMMMMMMMMM")
    print("        "+unknown8+"MMMMMMMMk:;. 'OMMMMMMMMMMMMMMMMMMMMMWx.,0MMMMMMMMM")
    print("        "+unknown8+"MMMMMMMK:ok.  ,0MMMMMMMMMMMMMMMMMMMWO. .cXMMMMMMMM")
    print("        "+unknown8+"MMMMMMNl:KO.   ;KWNXK00O0000KXNWMMWO' .c;dWMMMMMMM")
    print("        "+unknown8+"MMMMMMx,xNk.    .;'...    ....';:l:.  ,0l,0MMMMMMM")
    print("        "+unknown8+"MMMMMK;,l;. .,:cc:;.                  .dx,lWMMMMMM")
    print("        "+unknown8+"MMMMWo    ,dKWMMMMWXk:.      .cdkOOxo,. ...OMMMMMM")
    print("        "+unknown8+"MMMM0'   cXMMWKxood0WWk.   .lkONMMNOOXO,   lWMMMMM")
    print("        "+unknown8+"MMMWl   ;XMMNo.    .lXWd. .dWk;;dd;;kWM0'  '0MMMMM")
    print("        "+unknown8+"kxko.   lWMMO.      .kMO. .OMMK;  .kMMMNc   oWMMMM")
    print("        "+unknown8+"X0k:.   ;KMMXc      :XWo  .dW0c,lo;;xNMK,   'xkkk0")
    print("        "+unknown8+"kko'     :KMMNkl::lkNNd.   .dkdKWMNOkXO,    .lOKNW")
    print("        "+unknown8+"0Kk:.     .lOXWMMWN0d,       'lxO0Oko;.     .ckkOO")
    print("        "+unknown8+"kkkdodo;.    .,;;;'.  .:ooc.     .        ...ck0XN")
    print("        "+unknown8+"0XWMMMMWKxc'.          ;dxc.          .,cxKK0OkkOO")
    print("        "+unknown8+"MMMMMMMMMMMN0d:'.  .'        .l'  .;lxKWMMMMMMMMMN")
    print("        "+unknown8+"MMMMMMMMMMMMMMMN0xo0O:,;;;;;;xN0xOXWMMMMMMMMMMMMMM")
    print("        "+unknown6+"MMMMMMMMMMMMMMMMMMMMMMWWWWWMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown6+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown6+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown6+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+unknown6+"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("        "+Blue+"                   "+unknown+"["+unknown7+"PScan"+unknown+"]"+unknown+"         ")
    print("     "+purple+"             "+unknown+"["+unknown9+"Created By ybenel"+unknown+"]"+unknown+"    "+Reset+"\n")
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
