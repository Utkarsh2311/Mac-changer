#!usr/bin/env python3
import subprocess
import optparse
import re

def change_mac(inter,add):
    subprocess.call(["ifconfig" ,inter,"down"])
    subprocess.call(["ifconfig",inter,"hw","ether",add])
    subprocess.call(["ifconfig",inter,"up"])

    if inter=="eth0" or inter=="wlan0":
        print("[+] changing mac adress of "+ inter + " to "  + add)


def get_args():
    parse=optparse.OptionParser()
    parse.add_option("-i","--interface",dest="inter",help="interface for chnging mac adrress")  
    parse.add_option("-m","--mac",dest="add",help="Enter new mac address")
    (options,arguments)=parse.parse_args()
    if not options.inter:
        parse.error("[-]Please secify an interface")
    elif not options.add:
        parse.error("[-]Plz specify a mac adrress to be entered")
    return options

def current_mac(inter):
    ifconfig_result=subprocess.check_output(["ifconfig", inter])
    mac_add_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if mac_add_result:
        return mac_add_result.group()
    else:
        print("[-]no mac adrees found")

options1=get_args()
current_mac_=current_mac(options1.inter)
print("Current MAC "+ str(current_mac_))
change_mac(options1.inter,options1.add)
new_mac=options1.add
if current_mac_!= new_mac:
    print("[+]MAC adres was succesfully changed to " + new_mac)
else:
    print("[-]MAC adress was not changed")  