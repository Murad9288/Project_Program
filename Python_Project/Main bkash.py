
import datetime

while True:
    a=input("Please enter your USSID Number:\n")
    if a=="*247#":
        print("--------------- Carrier info ---------------\n")
        print("1 Send Money")
        print("2 Send Money to Non-bkash User")
        print("3 Mobile Recharge")
        print("4 Paymant")
        print("5 Cash out")
        print("6 Pay Bill")
        print("7 Get Tk 25 bonus now!!")
        print("8 My bkash")
        print("9 Reset PIN")
        
#----------------------Send Money------------------------------------
        op = int(input("Please enter your option number:\n"))
        if op== 1:
            print("--------------- Carrier info ---------------\n")
            num = int(input("Enter Receiver bkash Account Number:\n"))
            print("--------------- Carrier info ---------------\n")
            amt = int(input("Enter The Amount:\n"))
            print("--------------- Carrier info ---------------\n")
            re = input("Enter the Reference:\n")
            print("--------------- Carrier info ---------------\n")
            print("Send Money.")
            print("To:",num)
            print("Amount:Tk",amt)
            print("Reference:",re)
            pin=int(input("Enter Menu PIN to confirm:\n"))
            if pin == 2222:
                print("\n >>>Send Money Tk",amt,"to",num,"successful.Ref 11. Fee Tk 5.00. TrxID 5JQ1I589L at",datetime.datetime.now())
            else:
                print("Sorry,Wrong your PIN number.")
#--------------------------------------Send Money to Non-bkash User-----------------------
        elif op == 2:
            print("--------------- Carrier info ---------------\n")
            num = int(input("Enter Receiver bkash Account Number:\n"))
            print("--------------- Carrier info ---------------\n")
            amt = int(input("Enter The Amount:\n"))
            print("--------------- Carrier info ---------------\n")
            re = input("Enter the Reference:\n")
            print("--------------- Carrier info ---------------\n")
            print("Send Money to Non-bkash User")
            print("To:",num)
            print("Amount:Tk",amt)
            print("Reference:",re)
            pin=int(input("Enter Menu PIN to confirm:\n"))
            if pin == 2222:
                print("\n >>>Send Money to Non-bkash User Tk",amt,"to",num,"successful.Ref 11. Fee Tk 5.00. TrxID 5JQ1I589L at",datetime.datetime.now())
            else:
                print("Sorry,Wrong your PIN number.")
                
#---------------------------- Mobile Recharge-----------------------------------
        elif op== 3:         
            print("--------------- Carrier info ---------------\n")
            print("bkash")
            print("1 Robi")
            print("2 Airtel")
            print("3 Banglalink")
            print("4 Grameenphone")
            print("5 Teletalk")
            print("0 Main Menu")
            op = int(input("Please select your option:\n"))
            if op==1:
                print("--------------- Carrier info ---------------\n")
                print("bkash")
                print("1 prepaid")
                print("2 postpaid")
                print("0 Main Menu")
                op = int(input("Please select your option:\n"))
                if op==1 or 2:
                    print("--------------- Carrier info ---------------\n")
                    num=int(input("Enter Robi Mobile Number:\n"))
                    print("--------------- Carrier info ---------------\n")
                    amt=int(input("Enter Recharge Amount:\n"))
                    print("--------------- Carrier info ---------------\n")
                    print("Mobile Recharge.")
                    print("To:",num)
                    print("Amount:Tk",amt)
                    pin=int(input("Enter Menu PIN to confirm:\n"))
                    if pin == 2222:
                        print("\n >>>Received Recharge request of Tk",amt,"for",num,"successful. Fee Tk 0.00. TrxID 2JT25UK89D at",datetime.datetime.now(),".","wait for confirmation.")
                    else:
                        print("Sorry,Wrong your PIN number.")                      
            elif op==3:
                print("--------------- Carrier info ---------------\n")
                print("bkash")
                print("1 prepaid")
                print("2 postpaid")
                print("0 Mian Menu")
                op = int(input("Please enter your option number:\n"))
                if op==1 or 2:
                    print("--------------- Carrier info ---------------\n")
                    num=int(input("Enter Airtel Mobile Number:\n"))
                    print("--------------- Carrier info ---------------\n")
                    amt=int(input("Enter Recharge Amount:\n"))
                    print("--------------- Carrier info ---------------\n")
                    print("Mobile Recharge.")
                    print("To:",num)
                    print("Amount:Tk",amt)
                    pin=int(input("Enter Menu PIN to confirm:\n"))
                    if pin == 2222:
                        print("\n >>>Received Recharge request of Tk",amt,"for",num,"successful. Fee Tk 0.00. TrxID 2LQ28IK89T at",datetime.datetime.now(),".","wait for confirmation.")
                    else:
                        print("Sorry,Wrong your PIN number.")
            elif op==3:
                print("--------------- Carrier info ---------------\n")
                print("bkash")
                print("1 prepaid")
                print("2 postpaid")
                print("0 Mian Menu")
                op = int(input("Please enter your option number:\n"))
                if op==1 or 2:
                    print("--------------- Carrier info ---------------\n")
                    num=int(input("Enter Baglalink Mobile Number:\n"))
                    print("--------------- Carrier info ---------------\n")
                    amt=int(input("Enter Recharge Amount:\n"))
                    print("--------------- Carrier info ---------------\n")
                    print("Mobile Recharge.")
                    print("To:",num)
                    print("Amount:Tk",amt)
                    pin=int(input("Enter Menu PIN to confirm:\n"))
                    if pin == 2222:
                            print("\n >>>Received Recharge request of Tk",amt,"for",num,"successful. Fee Tk 0.00. TrxID 6WE25IK89D at",datetime.datetime.now(),".","wait for confirmation.\n")
                    else:
                        print("Sorry,Wrong your PIN number.")
            elif op==4:
                print("--------------- Carrier info ---------------\n")
                print("bkash")
                print("1 prepaid")
                print("2 postpaid")
                print("3 skitto")
                print("0 Mian Menu")
                op = int(input("Please enter your option number:\n"))
                if op==3:
                    print("--------------- Carrier info ---------------\n")
                    num=int(input("Enter Skitto Mobile Number:\n"))
                    print("--------------- Carrier info ---------------\n")
                    amt=int(input("Enter Recharge Amount:\n"))
                    print("--------------- Carrier info ---------------\n")
                    print("Mobile Recharge.")
                    print("To:",num)
                    print("Amount:Tk",amt)
                    pin=int(input("Enter Menu PIN to confirm:\n"))
                    if pin == 2222:
                            print("\n >>>Received Recharge request of Tk",amt,"for",num,"successful. Fee Tk 0.00. TrxID 5JQ2445IK89D at",datetime.datetime.now(),".","wait for confirmation.\n")
                if op==1 or 2:
                    print("--------------- Carrier info ---------------\n")
                    num=int(input("Enter Grameenphone Mobile Number:\n"))
                    print("--------------- Carrier info ---------------\n")
                    amt=int(input("Enter Recharge Amount:\n"))
                    print("--------------- Carrier info ---------------\n")
                    print("Mobile Recharge.")
                    print("To:",num)
                    print("Amount:Tk",amt)
                    pin=int(input("Enter Menu PIN to confirm:\n"))
                    if pin == 2222:
                            print("\n >>>Received Recharge request of Tk",amt,"for",num,"successful. Fee Tk 0.00. TrxID 3JQ25IK85A at",datetime.datetime.now(),".","wait for confirmation.\n")                
                    else:
                        print("Sorry,Wrong your PIN number.")
            elif op==5:
                print("--------------- Carrier info ---------------\n")
                print("bkash")
                print("1 prepaid")
                print("2 postpaid")
                print("0 Mian Menu")
                op = int(input("Please enter your option number:\n"))
                if op==0:
                    print("--------------- Carrier info ---------------\n")
                    print("1.Send Money")
                    print("2.Mobile Recharge")
                    print("3.Paymant")
                    print("4.Cash out")
                    print("5.Pay Bill")
                    print("6.My bkash")
                    print("7.Helpline")
                    op = int(input("Please enter your option number:\n"))
                if op==1 or 2:
                    print("--------------- Carrier info ---------------\n")
                    num=int(input("Enter Teletalk Mobile Number:\n"))
                    print("--------------- Carrier info ---------------\n")
                    amt=int(input("Enter Recharge Amount:\n"))
                    print("--------------- Carrier info ---------------\n")
                    print("Mobile Recharge.")
                    print("To:",num)
                    print("Amount:Tk",amt)
                    pin=int(input("Enter Menu PIN to confirm:\n"))
                    if pin == 2222:
                            print("\n >>>Received Recharge request of Tk",amt,"for",num,"successful. Fee Tk 0.00. TrxID 5JQ25IK89D at",datetime.datetime.now(),".","wait for confirmation.\n")
                    else:
                        print("Sorry,Wrong your PIN number.")
            elif op==0:
                print("--------------- Carrier info ---------------\n")
                print("1.Send Money")
                print("2.Mobile Recharge")
                print("3.Paymant")
                print("4.Cash out")
                print("5.Pay Bill")
                print("6.My bkash")
                print("7.Helpline")
                op = int(input("Please enter your option number:\n"))
        if op==4:
            print("--------------- Carrier info ---------------\n")
            num=int(input("Enter Marchant bkash Account Number:\n"))
            print("--------------- Carrier info ---------------\n")
            amt=int(input("Enter The Amount:\n"))
            print("--------------- Carrier info ---------------\n")
            re=int(input("Enter the Reference:\n"))
            print("--------------- Carrier info ---------------\n")
            co=int(input("Enter Counter Number:\n"))
            print("--------------- Carrier info ---------------\n")
            print("Payment.")
            print("To:",num)
            print("Amount:Tk",amt)
            print("Reference:",re)
            print("Counter No:",co)
            pin=int(input("Enter Menu PIN to confirm:\n"))
            if pin == 2222:
                print("\n >>> Welcome the received payment of Tk",amt,"for",num,"successful.TrxID 12JQ25IK459N at",datetime.datetime.now(),".","wait for confirmation.\n\t\t\t\t\t----------'Thank You'---------\n")
            else:
                print("Sorry,Wrong your PIN no.")
        if op==5:
            print("--------------- Carrier info ---------------\n")
            print("bkash\n 1 From Agent\n 2 From ATM\n 0 Main menu")
            op = int(input("Please select your option:\n"))
            if op==1:
                print("--------------- Carrier info ---------------\n")
                num=int(input("Enter Agent bkash Account Number:\n"))
                print("--------------- Carrier info ---------------\n")
                amt=int(input("Enter The Amount:\n"))
                print("--------------- Carrier info ---------------\n")
                print("Cash Out.")
                print("To:",num)
                print("Amount:Tk",amt)
                pin=int(input("Enter Menu PIN to confirm:\n"))
                if pin == 2222:
                    print("\n >>>Received Cash out Tk",amt,"To",num,"successful.TrxID 12JQ25IK85N at",datetime.datetime.now(),".\n")
                else:
                    print("Sorry,Wrong your PIN number.")
                    
            elif op==0:
                print("--------------- Carrier info ---------------\n")
                print("1.Send Money")
                print("2.Mobile Recharge")
                print("3.Paymant")
                print("4.Cash out")
                print("5.Pay Bill")
                print("6.My bkash")
                print("7.Helpline")
                op = int(input("Please enter your option number:\n"))

        if op==6:
            print("--------------- Carrier info ---------------\n")
            print("Pay Bill\n 1 Electricity\n 2 Gas\n 3 Internet,TV and Phone\n 4 Education\n 5 Holding Tax\n 6 Other\n 0 Main Menu")
            op = int(input("Please select your option:\n"))
            if op==0:
                print("--------------- Carrier info ---------------\n")
                print("1.Send Money")
                print("2.Mobile Recharge")
                print("3.Paymant")
                print("4.Cash out")
                print("5.Pay Bill")
                print("6.My bkash")
                print("7.Helpline")
                op = int(input("Please select your option:\n"))
            if op==1:
                print("--------------- Carrier info ---------------\n")
                print("Electricity\n 1 PALLI BIDYUT\n 2 NESCO\n 3 DESCO(PREPAID)\n 4 DESCO(POSTPAID)\n 5 DPDC(PREPAID)\n 6 DPDC(POSTPAID)\n 0 Main Menu ")
                op = int(input("Please select your option:\n"))
                if op==0:
                    print("--------------- Carrier info ---------------\n")
                    print("1.Send Money")
                    print("2.Mobile Recharge")
                    print("3.Paymant")
                    print("4.Cash out")
                    print("5.Pay Bill")
                    print("6.My bkash")
                    print("7.Helpline")
                    op = int(input("Please select your option:\n"))
                if op==1:
                    print("--------------- Carrier info ---------------\n")
                    print("PALLI BIDYUT\n 1 Check Bill\n 2 Make Payment\n 0 Main Menu\n")
                    op = int(input("Please select your option:\n"))
                    if op==0:
                        print("--------------- Carrier info ---------------\n")
                        print("1.Send Money")
                        print("2.Mobile Recharge")
                        print("3.Paymant")
                        print("4.Cash out")
                        print("5.Pay Bill")
                        print("6.My bkash")
                        print("7.Helpline")
                        op = int(input("Please select your option:\n"))
                    if op==1:
                        print("--------------- Carrier info ---------------\n")
                        print("Check Bill\n 1.Input SMS A/C number\n 2.Saved Accounts\n 0.Main Menu")
                        op = int(input("Please select your option:\n"))
                        if op==0:
                            print("--------------- Carrier info ---------------\n")
                            print("1.Send Money")
                            print("2.Mobile Recharge")
                            print("3.Paymant")
                            print("4.Cash out")
                            print("5.Pay Bill")
                            print("6.My bkash")
                            print("7.Helpline")
                            op = int(input("Please enter your option number:\n"))
                        if op==1:
                            print("--------------- Carrier info ---------------\n")
                            num=int(input("Enter SMS Account Number:\n"))
                            print("--------------- Carrier info ---------------\n")
                            date=int(input("Enter Bill Month and Year(MMYYYYY):\n"))
            elif op==2:
                print("--------------- Carrier info ---------------\n")
                print("Gas\n 1 Jalalabad Gas\n 0 Main Menu")
                op = int(input("Please select your option:\n"))
                if op==1:
                    print("--------------- Carrier info ---------------\n")
                    print("Jalalabad\n 1 Check Bill\n 2 Make Payment\n 0 Main Menu")
                elif op==0:
                    print("--------------- Carrier info ---------------\n")
                    print("1.Send Money")
                    print("2.Mobile Recharge")
                    print("3.Paymant")
                    print("4.Cash out")
                    print("5.Pay Bill")
                    print("6.My bkash")
                    print("7.Helpline")
                    op = int(input("Please enter your option number:\n"))
                    op = int(input("Please select your option:\n"))
                    if op==1:
                        print("--------------- Carrier info ---------------\n")
                        print("Check Bill\n 1.Input Bill A/C number\n 2.Saved Accounts\n 0.Main Menu")
                        op = int(input("Please select your option:\n"))
                        if op==1:
                            print("--------------- Carrier info ---------------\n")
                            num=int(input("Enter Customer Code Number:\n"))
                            print("--------------- Carrier info ---------------\n")
                            date=int(input("Enter Bill Month and Year(MMYYYYY):\n"))
                            op = int(input("Please select your option:\n"))
                        elif op==2:
                            print("--------------- Carrier info ---------------\n")
                            print("Sorry, there is no beneficatciary.")
                        elif op==0:
                            print("--------------- Carrier info ---------------\n")
                            print("1.Send Money")
                            print("2.Mobile Recharge")
                            print("3.Paymant")
                            print("4.Cash out")
                            print("5.Pay Bill")
                            print("6.My bkash")
                            print("7.Helpline")
                            op = int(input("Please enter your option number:\n"))
                            
                    op = int(input("Please select your option:\n"))
                    if op==2:
                        print("--------------- Carrier info ---------------\n")
                        print("Make Payment\n 1.Input SMS A/C number\n 2.Saved Accounts\n 0.Main Menu")
                        op = int(input("Please select your option:\n"))
                        if op==1:
                            print("--------------- Carrier info ---------------\n")
                            num=int(input("Enter SMS Account Number:\n"))
                            print("--------------- Carrier info ---------------\n")
                            date=int(input("Enter Bill Month and Year(MMYYYYY):\n"))
                        op = int(input("Please select your option:\n"))
                        if op==2:
                            print("--------------- Carrier info ---------------\n")
                            print("Sorry, there is no beneficatciary.")
                            op = int(input("Please select your option:\n"))
                        elif op==0:
                            print("--------------- Carrier info ---------------\n")
                            print("1.Send Money")
                            print("2.Mobile Recharge")
                            print("3.Paymant")
                            print("4.Cash out")
                            print("5.Pay Bill")
                            print("6.My bkash")
                            print("7.Helpline")
                            op = int(input("Please enter your option number:\n"))
    else:
        print("Sorry! wrong your USSID number.\n\t\t\tPlease try again.\n\n")
                                                    


                

           
        
                    
                    
            
            
        
        
           
                
                
                
            
                
            
