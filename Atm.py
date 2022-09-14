val=True
balance=500
slist=list()
def credit():
    global balance,slist
    ac=int(input("enter creadit amount"))
    if ac>0:
        balance+=ac
        slist.append("credit amount {}".format(ac))
        print("amount creadited")
    else:
        print("cannot credit 0 amont")
def debit():
    global balance,slist
    ad=int(input("enter debit amount"))
    if ad>balance:
        print("low balance")
    else:
        balance-=ad
        slist.append("debit amount {}".format(ad))
        print("amount debited")
def check():
    global balance
    print("Current Amount is {}".format(balance))
def statement():
    global slist
    for ele in slist:
        print(ele)
while val:
    opt=int(input("1.credit 2.debit 3.checkbalance 4.statement 5.exit"))
    if opt==1:
        credit()
    elif opt==2:
        debit()
    elif opt==3:
        check()
    elif opt==4:
        statement()
    elif opt==5:
        val=False