import sys
import string
import random

class fcolor:
    CReset='\033[0m'
    CBold='\033[1m'
    CDim='\033[2m'
    Red='\033[31m'
    Green='\033[32m'
    Yellow='\033[33m'
    Blue='\033[34m'
    Cyan='\033[36m'
    White='\033[37m'

print (fcolor.Red +    "                                     (                  " + fcolor.CBold + "    /    \ \ ")
print (fcolor.Red +    "               (             )       )\ )               " + fcolor.CBold + "   (UpdateLap)")
print (fcolor.Red +    "   (           )\ )    )  ( /(   (  (()/(     )         " + fcolor.CBold + "    \ \ _ /")
print (fcolor.Red +    "  ))\  `  )   (()/( ( /(  )\()) ))\  /(_)) ( /(  `  )   ")
print (fcolor.Red + "(_))( ((_)_\   _| |((_)_ | |_ (_))  | |   ((_)_ ((_)_\  ")
print (fcolor.Red +    "| || || '_ \)/ _` |/ _` ||  _|/ -_) | |__ / _` || '_ \) ")
print (fcolor.Red + " \_,_|| .__/ \__,_|\__,_| \__|\___| |____|\__,_|| .__/  ")
print (fcolor.Red +    "      |_|                                       |_|     ")
print (fcolor.Cyan + "Jafar abo Nada "  + fcolor.White + "  " + "   [11/2019] ")
print (fcolor.Cyan + "Word-List Generator : " +fcolor.White + " Token, Password, Recovery Code")
print ("")

#============ Word List Gen Start============#

minimum=int(input(fcolor.White + 'Please enter the' + fcolor.Red + ' Minimum' + fcolor.White + ' length of any give word to be generated: '))
maximum=int(input(fcolor.White + 'Please enter the' + fcolor.Red + ' Maximum' + fcolor.White + ' length of any give word to be generated: '))
wmaximum=int(input(fcolor.White +'Please enter the' + fcolor.Red + ' Max Number' + fcolor.White + ' of words to be generate in the dictionary: '))
wmaximumn =int(wmaximum)
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
strginT=''
string=''
size=0
FILE = open("wl.txt","w")
for count in range(wmaximumn):
    sys.stdout.write('\r'+'loading...  process '+str(count)+'/'+str(wmaximum)+' '+ '{:.2f}'.format(count/wmaximum*100)+'%')
    sys.stdout.flush()
    for x in random.sample(alphabet,random.randint(minimum,maximum)):
        string+=x
        size+= sys.getsizeof(string)
    Char_upper = 0
    Char_lower = 0

#============ Word List Filter Start ============#

    strginT =string
    for x in range(len(strginT)):
    	if strginT[x].isupper():
           Char_upper  += 1
    	elif strginT[x].islower():
           Char_lower += 1 
    if (Char_upper == 7) and (Char_lower == 3):
       FILE.write("1"+strginT+'\n')
    string=''
    strginT=''
FILE.close()

#============ Word List Filter End  ============#

#============ Size meter start ============#

power = 2**10
n = 1
Dic_powerN = {1:'Kilobytes', 2:'Megabytes', 3:'Gigabytes', 4:'Terabytes'}

if size <= power**2 :
   size /=  power
   print ('\r')
   print (fcolor.Cyan + "File Size = " + fcolor.Green + str(size) + " / " + Dic_powerN[n])
else: 
   while size   >  power :
         n  += 1
         size /=  power**n
   print ('\r')
   print (fcolor.Cyan + "File Size = " + fcolor.Green + str(size) + " / " + Dic_powerN[n])

#============ Size meter end ============#
