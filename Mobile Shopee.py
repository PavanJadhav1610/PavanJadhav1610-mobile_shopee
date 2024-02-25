class mobile:

    def __init__(self):
        self.user_details=[]
    
    def user_registration(self):
        print("\n Welcome to User registration Page\n")
        name=input("Enter your name:")
        if name not in self.user_details:
             self.Email=input("Enter your Email:")
             if "@gmail.com" in self.Email:
                  self.passw=int(input("Enter your password :"))
                  mob=int(input("enter your mobile no :"))
                  b=str(mob)
                  if len(b)>10 or len(b)<10:
                       print("...enter the valid mobile number...")
                  if len(b)==10:
                    address=input("Enter your Address:")
                    if len(address)>=10:
                       self.user_details.append(name)
                       self.user_details.append(self.Email)
                       self.user_details.append(self.passw)
                       self.user_details.append(mob)
                       self.user_details.append(address)
                       print("-----------------------------------")
                       print("***User Registered successfully***")
                       print("------------------------------------")
                    else:
                       print("\n ....Enter correct address....\n")
             else:
                  print("\n ....Enter valid emai....\n")  
        else:
             print("\n ....User already registered....\n")

            
    def user_login(self):
        print("....login your self by giving registered name and gmail and save with pasword....")
        
        Email1=input("Enter your Email:")
        if Email1==self.Email:
                  passw=int(input("Enter your password:"))
                  if passw==self.passw:
                        while(True):
                            print("\n 1.See available mobiles \n 2.My purchase \n 3.Add to my cart \n 4.Payment \n 5.Exit \n")
                            choice=int(input("Enter your choice:"))
                        
                            if choice==1:
                                 self.see_mobiles()
                            elif choice==2:
                                self.my_purchase()
                            elif choice==3:
                              self.my_cart()
                            elif choice==4:
                              self.payment()
                            elif choice==5:
                              break
                            else:
                              print("Enter valid choice")
                  else:
                        print("Enter Valid Password")
        else:
            print("Enter Valid Email or Email not Registered")
             
    def see_mobiles(self):
            print("----here we have some products related to your search----")
            while(True):
                print("1.redmiA1 \n2.redmiA2 \n3.redmiB1 \n4.redmiB2 \n5.redmiC1 \n6.redmiC2 \n7.redmiD1 \n8.back to main menu")
                var3=int(input("enter your selection number select number for see details of product :"))
                if var3==1:
                    print("***this is redmiA1 you looking for*** \n>-redmiA1 has features as listed below. \n ram:2gb \nstorage:32gb \n battery:3100maH \n camera:8 mp \n price:8000rs|- \n 1 year warranty")
                elif var3==2:
                    print("***this is redmiA2 you looking for*** \n>-redmiA2 has features as listed below. \n ram:3gb \n storage:32gb \n battery:3100maH \n camera:8mp+2mp \n price:8500rs|-\n 1 year warranty ")
                elif var3==3:
                    print("***this is redmiB1 you looking for*** \n>-redmiB1 has features as listed below. \n ram:4gb \nstorage:64gb \n battery:4100maH \n camera:13mp \n supports fast charging 13W \n price:10000rs|- \n 1 year warranty")
                elif var3==4:
                    print("***this is redmiB2 you looking for*** \n>-redmiB2 has features as listed below. \n ram:4gb \n storage:64gb \n battery:5000maH \n camera:13+13mp \n supports fast charging 18W \n price:12000rs|- \n 1 year warranty")
                elif var3==5:
                    print("***this is redmiC1 you looking for*** \n>-redmiC1 has features as listed below. \n ram:6gb \n storage:128gb \n battery:5000maH \n camera:13+2+13mp \n supports fast charging 25W\n price:14000rs|- \n 1 year warranty")
                elif var3==6:
                    print("***this is redmiC2 you looking for*** \n>-redmiC2 has features as listed below. \n ram:6gb \nstorage:128gb \n battery:6000maH \n camera:64+2+13mp \n supports fast charging 28W \n price:15500rs|- \n 1 year warranty")
                elif var3==7:
                    print("***this is redmiD1 you looking for*** \n>-redmiD1 has features as listed below. \n ram:8gb \nstorage:256gb \n battery:7000maH \n camera:64+64+13+13+2mp \n supports fast charging 64W \n price:19000rs|- \n 1 year domestic warranty")
                elif var3==8:
                      break
                else:
                    print("<please enter a valid selection number>")
    
    def my_purchase(self):
            print("...enter the choice number to purchase from list you saw...")
            while(True):
                print("1.redmiA1:8000rs \n2.redmiA2:8500rs \n3.redmiB1:10000rs \n4.redmiB2:12000rs \n5.redmiC1:14000rs \n6.redmiC2:15500rs \n7.redmiD1:19000rs \n8.back to main menu")
                var4=int(input("select the above choice number to buy your product"))
                if var4==1:
                    print(" ----your selected product redmiA1 has price 8000rs----")    
                elif var4==2:
                    print(" ----your selected product redmiA2 has price 8500rs----")                    
                elif var4==3:
                    print(" ----your selected product redmiB1 has price 10000rs----")
                elif var4==4:
                    print(" ----your selected product redmiB2 has price 12000rs----")
                elif var4==5:
                    print(" ----your selected product redmiC1 has price 14000rs----")
                elif var4==6:
                    print(" ----your selected product redmiC2 has price 15500rs----")
                elif var4==7:
                    print(" ----your selected product redmiA1 has price 19000rs----")
                elif var4==8:
                    break
                else:
                    print("...please select valid number of product...")

    def my_cart(self):
            while(True):
                print("1.redmiA1 \n2.redmiA2 \n3.redmiB1 \n4.redmiB2 \n5.redmiC1 \n6.redmiC2 \n7.redmiD1 \n8.back to main menu")
                self.var5=(int(input("...please re-conform your product to buy and proceed further to payment :")))
                if self.var5==1:
                        print("----your redmiA1 is added to your cart sucessfully----")
                elif self.var5==2:
                        print("----your redmiA2 is added to your cart sucessfully----")
                elif self.var5==3:
                        print("----your redmiB1 is added to your cart sucessfully----")
                elif self.var5==4:
                        print("----your redmiB2 is added to your cart sucessfully----")
                elif self.var5==5:
                        print("----your redmiC1 is added to your cart sucessfully----")
                elif self.var5==6:
                        print("----your redmiC2 is added to your cart sucessfully-----")
                elif self.var5==7:
                        print("----your redmiD1 is added to your cart sucessfully----")
                elif self.var5==8:
                     break
                else:
                        print("please enter valid choice number to proceed for payment option")
                        print("--------------------**--------------------")

    def payment(self):
                print("...we prefer cash on delivery for customer satisfaction...")
                print("..< enter the payment mode you want >..\n1.i want cash on delivery>..")
                print("2.online payment")
                var6=int(input("enter the number for payment method:"))
                if var6==1:
                        print("---------------------------------------------------------------------------------------")
                        print("congratulations we received your order and will be delivered soon at your given adress.")
                        print("your name is:",self.user_details[0])
                        print("your mail is :",self.user_details[1])
                        print("your contact no is :",self.user_details[3])   
                        print("your delivery adress is:",self.user_details[4])
                        print("----------------------------------------------------------------------------------------")   
                elif var6==2:
                    b=int(input("enter the card number:"))
                    c=str(b)    
                    if len(c)>16:
                            print("...you entered too long card number...")
                            print("...go to the payment payment option and try agian...")
                    elif len(c)<16:
                            print("...we find some missing characters while you entering card details...")
                            print("...go to the payment payment option and try agian...")
                            
                    else:
                        print("you entered the valid card number.")
                        if len(c)==16:
                        
                            d=int(input("enter the card cvv:"))
                            e=str(d)
                            if len(e)>3:
                                print("you entered too long cvv number.")
                            elif len(e)<3:
                                print("we find some missing characters while you entering cvv details.")
                            else:
                                print("you entered a valid cvv number and it is verified")  
                                if len(c)==16 and len(e)==3:
                                    print("--------------------------------------------")
                                    print("       ***your payment is sucessfull*** \n\n----following are your order details----")
                                    print("your order details are as follow :-")
                                    print("your name is:",self.user_details[0])
                                    print("your mail is :",self.user_details[1])
                                    print("your contact no is :",self.user_details[3])
                                    print("your delivery adress is:",self.user_details[4])
                                    print("---------------------------------------------")
                else:
                        print("enter valid payment choice only from above :")
                        print("--------------------------**-------------------------")
            
    def gallary(self):
            print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
            print("        ****> Welcome to Balaji Shopee <****")
            print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=")
            while(True):
                print("1.For user registration \n2.User_login \n3.Exit")
                choice=int(input("Enter your choice : "))
                if choice==1:
                    self.user_registration()    
                elif choice==2:
                    self.user_login()
                elif choice==3:    
                    break
                else:
                    print("....you entered wrong choice select only from above.....") 

object=mobile()
object.gallary()
