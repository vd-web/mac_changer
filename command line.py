import subprocess
import optparse


def get_Argrument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change mac addresss")
    parser.add_option("-m", "--new_mac", dest='new_mac', help="new mac address")
    (options, arugruments) = parser.parse_args()
    if not options.interface:
        parser.error("please specify interface,use help for more information")
    else  :
        parser.error("please specify an new mac address,use help for more information")
    return options


def change_mac(interface, new_mac):
    print("[!]changing mac addresss for " + interface + "to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


option = get_Argrument()
# change_mac(option.interface,option.new_mac)

# ifconfig_result = subprocess.check_output(['ifconfig',options.interface])


