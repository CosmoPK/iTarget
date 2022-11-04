import sys, getopt
import sys #interact with os
import os  #
import urllib.request as urllib2 #handle urls
import json #store & exchange data
import socket

argsList = sys.argv[1:] #remove 1st arg
options = "hi:u:f:" #option list
longOptions = ["Help", "IPAddress", "URL", "PhoneNumber"]  

def ipFromUrl(url):
    print("Your target website address: ", url)
    ip= socket.gethostbyname(url)        #targe ip
    url="http://ip-api.com/json/"        #source id
    response=urllib2.urlopen(url+ip)     #get url request response in varialbe
    data=response.read()                 #get meaningful data from response
    values=json.loads(data)              #load all values from data

    print("IP: "+values["query"], "\n")
    print("City: "+values["city"])
    print("ISP: "+values["isp"])
    print("Country: "+values["country"])
    print("Region: "+values["region"])
    print("Timezone: "+values["timezone"])

    #print("\n", values)

    #print(os.system('ipconfig'))
    
def main(argv):
    try:
        # Parsing argument
        arguments, values = getopt.getopt(argsList, options, longOptions)
             
        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--Help"):
                print ("Displaying Help")
                 
            elif currentArgument in ("-i", "--IPAddress"):
                print ("Displaying ipaddress:", currentValue)
                 
            elif currentArgument in ("-u", "--URL"):
                ipFromUrl(currentValue)

            elif currentArgument in ("-f", "--PhoneNumber"):
                print("ip address from phone number: ")
                
    except getopt.error as err:
        print(str(err))
        print ("Displaying Help")
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
