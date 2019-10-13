import argparse
import socket
import time
import csv
import sys
parser=argparse.ArgumentParser(description="Site Connectivity Checker")
parser.add_argument('-c','--check',metavar='',required=False,help="Check the this site")
parser.add_argument('-i','--interval',metavar='',required=False,help="The interval time")
parser.add_argument('-d','--add',metavar='',required=False,help="Add This Site to Checker Sites")
parser.add_argument('-de','--delete',metavar='',required=False,help="Delete from the site from data")
parser.add_argument('-ca','--checkall',metavar='',required=False,help="check all host in the data")
args=parser.parse_args()

def addsite():
        if args.add:
            site=args.add
            with open('sites.csv',mode='a') as file:
                site_write=csv.writer(file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
                site_write.writerow([site])
            file.close()

def sites_arrayf():
    sites_array=[]
    with open('sites.csv','r') as file:
        the_sites=csv.reader(file)
        for row in the_sites:
            sites_array.append(row[0])
        return sites_array

def deletedata():
    if args.delete:
        site=args.delete
        sites_array=[]
        sites_array=sites_arrayf()
        if site in sites_array:
            print("here")
            sites_array.remove(site)
        with open('sites.csv','w') as file:
            the_sites=csv.writer(file,delimiter=',')
            for row in sites_array:
                the_sites.writerow([row])
        file.close()
def site_tryf(thearray):
    while True:
        for element in thearray:
            if args.interval:
                timee=args.interval
                try:
                    socket.create_connection((element,80))
                    print("site:"+element+" Online")
                    time.sleep(timee)
                except socket.error as e:
                    print("Error:{}".format(e))
                    print("site:"+element+" Offline")
                    time.sleep(timee)
            else:
                try:
                    socket.create_connection((element,80))
                    print("site:"+element+" Online")
                except socket.error as e:
                    print("Error:{}".format(e))
                    print("site:"+element+" Offline")

def checkalls():
    if args.checkall:
        sites_array=[]
        sites_array=sites_arrayf()
        site_tryf(sites_array)

def checkifsiteexist(name):
    key=False
    site_array=sites_arrayf()
    if name in site_array:
        key=True
    return key
if __name__=='__main__':
    site=args.check
    if (len(sys.argv))<2:
        print("type: python file -h")
    elif args.checkall:
        checkalls()
    elif args.add:
        name=args.add
        if not checkifsiteexist(name):
            addsite()
        else:
            print("Site Is Already Exist")
    elif args.delete:
        deletedata()

    else:
        while True:
            try:
                socket.create_connection((site,80))
                print("online")
                break
            except socket.error as e:
                if args.interval:
                    timee=args.interval
                    timee=int(timee)
                    print("offline")
                    print("The Problem :{}".format(e))
                    time.sleep(timee)
                else:
                    print("offline")
                    print("The Problem :{}".format(e))
                                                                          #By Miss.Robot
