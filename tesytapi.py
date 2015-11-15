from urllib.request import urlopen

def printbill(kittens):
    f = str(kittens.read()).split(',')
    count = 0
    bills = []
    billinfo = {}
    while count < len(f):
        if "Electric" in f[count]:
            bills.append(f[count: count+5])
        count +=1
    for each in bills:
        billinfo[each[2].split(":")[1].strip('"')] = float(each[4].split(":")[1])
    print(billinfo)    

#Juliet's account 
kittens = urlopen('http://api.reimaginebanking.com/accounts/56241a14de4bf40b17112b19/bills?key=fddd3bd8c4f874dc2f2d5ff4efbfd263')
printbill(kittens)

#Arnies's account 
kittens = urlopen('http://api.reimaginebanking.com/accounts/56241a14de4bf40b17112b1b/bills?key=fddd3bd8c4f874dc2f2d5ff4efbfd263')
printbill(kittens)
