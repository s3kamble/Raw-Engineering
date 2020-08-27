print("")
print("MANAGER:-Total money in account today ")
total = int(input("Enter the total amount you have:"))  
sum = 0

#Denominations Assumed:2000,500,100,50,10,1
denomAvail = {2000:0,500:0,100:0,50:0,10:0,1:0}
initAmt = denomAvail
print("Denominations:")

#Check denominations entered and available denominations
while sum != total:     
    for i,j in denomAvail.items():
        num = int(input("Enter the number of " + str(i) + " notes:"))
        sum = sum + (num*i)
        denomAvail[i] = num
        if(i==len(denomAvail) or sum > total ):
            print("Total and Denomination total mismatch try again")
            sum = 0
            denomAvail = initAmt
            break
        if sum == total:
            break
    if(sum < total):
        print("Please check Denominations")
    print(" ")


billAmt = int(input("Customer's Bill amount:")) 
amtPaid = int(input("Amount paid by the customer:"))

while amtPaid < billAmt:    
    if(amtPaid < billAmt):
        print("Not sufficient to pay the bill")
    amtPaid = int(input("Please enter the denomination you want to pay with :"))

returnAmount = amtPaid - billAmt
print("Amount to be returned : " + str(returnAmount))

#Returnimg Amt calculations
availDenoms = dict()    
for (key,val) in denomAvail.items():
    if(val>0 and key < returnAmount):
        availDenoms[key] = val

if(len(availDenoms.keys()) > 0):
    for (key,val) in availDenoms.items():
        if(returnAmount//key <= val):
            tempNum = returnAmount//key
            updateVal = val - tempNum
            print("Denominations to be returned ")
            print(str(key)+" :"+str(returnAmount//key))
            returnAmount = returnAmount % key
            availDenoms[key] = updateVal
            if(returnAmount == 0):
                break

    if(returnAmount > 0):
        # print("Transaction cannot be completed as denomination's of " +str(returnAmount) + " required aren't available.")
        print("Transaction cannot be completed as we do not have change of Rs " +str(returnAmount) )

else:
    print("No denominations available .")
