#PROGRAM DESCRIPTION
#Author: Adam Sparkes
#Date(s): 2024-03-20 to 2024-03-24
import datetime
import FormatValues as FV

#DEFAULTS


PolicyNum = 1944
BasicPrem = 869.00
AddCarsDis = .25
ExtraLiabCost = 130.00
GlassCoverCost = 86.00
LoanCarCost = 58.00
HSTRate = .15
ProssFee = 39.99



CurDate = datetime.datetime.now()



#PROGRAM FUNCTIONS

def CalcPremium():
    Premium = BasicPrem + (CarAmt - 1) * (BasicPrem* AddCarsDis)
    TotExtraCost = 0
    if ExtraLiab == 'Y':
        TotExtraCost += ExtraLiabCost * CarAmt
    if GlassCover == 'Y':
        TotExtraCost += GlassCoverCost * CarAmt
    if LoanCar == 'Y':
        TotExtraCost += LoanCarCost * CarAmt
    Premium += TotExtraCost
    return Premium

def CalcTotPrem():
    TotPremium = Premium + (Premium * HSTRate)
    return TotPremium

def CalcMonthlyPay():
    if DownPayment > 0:
        RemainingCost = TotPremium - DownPayment
    else:
        RemainingCost = TotPremium
    MonthlyPay = (RemainingCost + ProssFee) / 8
    return MonthlyPay


#PROGRAM INPUTS
while True:
    print()
    print()
    CustFirstName = input("Enter customer's first name: (END To Quit) ").title()
    if CustFirstName == "End":
        break
    CustLastName = input("Enter customer's last name: ").title()
    StAdd = input("Enter customer's street address: ").title()
    City = input("Enter the customer's City: ")

    Provlist = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']

    Prov = input("Enter customer's province (2-letter abbreviation): ").upper()
    while Prov not in Provlist:
        print("Invalid province abbreviation. Please enter a valid 2-letter abbreviation.")
        Prov = input("Enter customer's province (2-letter abbreviation): ").upper()

    PostalCode = input("Enter customer's postal code: ")

    PhNum = input("Enter customer's phone number: ")
    print()
    CarAmt = int(input("Enter the number of cars being insured: "))
    ExtraLiab = input("Do you want extra liability coverage? (Y/N): ").upper()
    GlassCover = input("Do you want glass coverage? (Y/N): ").upper()
    LoanCar = input("Do you want loaner car coverage? (Y/N): ").upper()
    print()
    PayList = ['Full', 'Monthly', 'Down Payment']
    PayMethod = input("How do you want to pay? (Full/Monthly/Down Payment): ").title()
    while PayMethod not in PayList:
        print("Invalid payment method. Please enter 'Full', 'Monthly', or 'Down Payment'.")
        PayMethod = input("How do you want to pay? (Full/Monthly/Down Payment): ").title()

    DownPayment = 0
    if PayMethod == 'Down Payment':
        DownPayment = float(input("Enter the amount of the down payment: "))
    
    #PROGRAM CALCULATIONS
    CustFullName = CustFirstName + " " + CustLastName

    Premium = CalcPremium()
    
    TotPremium = CalcTotPrem()

    MonthlyPay = CalcMonthlyPay()

    HST = Premium * HSTRate

    ClaimNums = []
    ClaimDates = []
    ClaimAmts = []

    ClaimNumber = input("Please enter the 4-digit Claim Number: ")
    ClaimNums.append(ClaimNumber)
    ClaimDate = CurDate
    ClaimDates.append(ClaimDate)
    ClaimAmt = TotPremium
    ClaimAmts.append(ClaimAmt)
    
    #PROGRAM OUTPUTS
    print()
    print()
    print("====== Previous Claims ======")
    print("Claim #   Claim Date   Amount")
    print("--------------------------------")
    for i in range(len(ClaimNums)):
        print(f"{ClaimNums[i]:>4s}      {FV.FDateS(ClaimDates[i]):>10s}  {FV.FDollar2(ClaimAmts[i]):>10s}")


    print()
    print()
    print("           One Stop Insurance")
    print("-------------------------------------")
    
    print("Customer Details: ")
    print(CustFullName)
    print(f"{StAdd}, {City}, {Prov}")
    print(f"Phone Number : {PhNum}")
    print("-------------------------------------")
    print(f"Number of Cars Insured:            {CarAmt}")
    print(f"Extra Liability Coverage:          {ExtraLiab}")
    print(f"Glass Coverage:                    {GlassCover}")
    print(f"Loaner Car Coverage:               {LoanCar}")
    print(f"Payment Method:         {PayMethod:>12s}")
    if PayMethod == 'Down Payment':
        print(f"Down Payment:             {FV.FDollar2(DownPayment):>10s}")
    print("------------------------------------")
    print(f"Premium:                  {FV.FDollar2(TotPremium):>10s}")
    print(f"HST :                     {FV.FDollar2(HST):>10s}")
    print(f"Total Cost:               {FV.FDollar2(TotPremium):>10s}")
    if PayMethod != 'Full':
        print(f"Monthly Payment:          {FV.FDollar2(MonthlyPay):>10s}")
    print(f"------------------------------------")
    print(f"Invoice Date:            ", FV.FDateS(CurDate))

   

    
    


