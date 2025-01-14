#==============================================================================================
        
#Airline NEA By Sam Powsney
        
#==============================================================================================

#==============================================================================================

#Variable Database Section

#==============================================================================================

#Plane Models
plane1 = 'Medium narrow body'
plane1run = '8'
plane1range = '2650'
plane1cap = '180'
plane1minfirst = '8'
#=============
plane2 = 'Large narrow body'
plane2run = '7'
plane2range = '5600'
plane2cap = '220'
plane2minfirst = '10'
#=============
plane3 = 'Medium wide body'
plane3run = '5'
plane3range = '4050'
plane3cap = '406'
plane3minfirst = '14'

#UK Airports
ukairport1 = 'Liverpool John Lennon'
ukairport1code = 'LPL'
#=============
ukairport2 = 'Bournemouth International'
ukairport2code = 'BOH'

#Overseas Airports
overseasairport1 = 'John F Kennedy International'
overseasairport1code = 'JFK'
overseasairport1lpl = '5326'
overseasairport1boh = '5486'
#===================
overseasairport2 = 'Paris-Orly'
overseasairport2code = 'ORY'
overseasairport2lpl = '629'
overseasairport2boh = '379'
#===================
overseasairport3 = 'Adolfo Suarez Madrid- Barajas'
overseasairport3code = 'MAD'
overseasairport3lpl = '1428'
overseasairport3boh = '1151'
#===================
overseasairport4 = 'Amsterdam Schiphol'
overseasairport4code = 'AMS'
overseasairport4lpl = '526'
overseasairport4boh = '489'
#===================
overseasairport5 = 'Cairo International'
overseasairport5code = 'CAI'
overseasairport5lpl = '3779'
overseasairport5boh = '3584'

#User Inputs
ukairportchoicecode = ''
#====================
overseasairportchoicecode = ''
#====================
planechoice = ''
#====================
firstyes = 'n'
#====================
firstdoneyes = 'n'

#Saved Flight Database
flight1 = 'No Flight Scheduled.'
#====================
flight1uk = 'N/A'
#====================
flight1ukcode = 'N/A'
#====================
flight1ukcodelwr = 'N/A'
#====================
flight1os = 'N/A'
#====================
flight1oscode = 'N/A'
#====================
flight1oscodelwr = 'N/A'
#====================
flight1planechoice = 'N/A'
#====================
flight1standard = 'N/A'
#====================
flight1first = 'N/A'
#====================
flight1distance = 'N/A'
#====================
flight1firstyes = 'n'
#====================
flight1set = 'n'
#====================
flight2 = 'No Flight Scheduled.'
#====================
flight2uk = 'N/A'
#====================
flight2ukcode = 'N/A'
#====================
flight2ukcodelwr = 'N/A'
#====================
flight2os = 'N/A'
#====================
flight2oscode = 'N/A'
#====================
flight2oscodelwr = 'N/A'
#====================
flight2planechoice = 'N/A'
#====================
flight2standard = 'N/A'
#====================
flight2first = 'N/A'
#====================
flight2distance = 'N/A'
#====================
flight2firstyes = 'n'
#====================
flight2set = 'n'
#====================
flight3 = 'No Flight Scheduled.'
#====================
flight3uk = 'N/A'
#====================
flight3ukcode = 'N/A'
#====================
flight3ukcodelwr = 'N/A'
#====================
flight3os = 'N/A'
#====================
flight3oscode = 'N/A'
#====================
flight3oscodelwr = 'N/A'
#====================
flight3planechoice = 'N/A'
#====================
flight3standard = 'N/A'
#====================
flight3first = 'N/A'
#====================
flight3distance = 'N/A'
#====================
flight3firstyes = 'n'
#====================
flight3set = 'n'

#==============================================================================================

#Main Menu

#==============================================================================================

def mainmenu():
    
    print("Main Menu:")
    
    print("Enter '1' To Enter Airport Details")
    print("Enter '2' To Enter Flight Details")
    print("Enter '3' To Enter Price Plan And Calculate Profit")
    print("Enter '4' To View Save Slots")
    print("Enter '5' To Update Database File (With Current Program Data)")
    print("Enter '6' To Clear Data (ONLY Program Data)")
    print("Enter '7' To Clear Database File (ONLY Database File)")
    print("Enter '8' To Quit")
    
    print("")
    
    mainmenuchoices()
    
def mainmenuchoices():
    
    menuuser=input("Enter option here: ")
    
    if menuuser.isdigit():
        
        print("")
        
    else:
        
        print("Invalid Input! You have to enter a number for this question. Please try again...")
        print("")
        
        mainmenuchoices()
    
    if menuuser == '1':
        
        airportdetails()
        
    elif menuuser == '2':
        
        flightdetails()
        
    elif menuuser == '3':
        
        priceplan()
        
    elif menuuser == '4':
        
        viewsaveslot()
        
    elif menuuser == '5':
        
        filehandlesection()
        
    elif menuuser == '6':
        
        cleardata()
        
    elif menuuser == '7':
        
        fileclear()
        
    elif menuuser == '8':
        
        quitsec()
        
    else:
        
        print("Invalid Input! Please Try Again With A Listed Number.")
        print("")
        
        mainmenuchoices()
        
#==============================================================================================
        
#Airport Details
        
#==============================================================================================
        
def airportdetails():
    
    global ukairportchoice
    global ukairportchoicecode
    
    def airportdetailsnext():
        
        global distance
        global overseasairportchoice
        global overseasairportchoicecode
        
        print("You have selected " +ukairportchoice+ ".")
        print("")
        
        overseasairportchoicenon=input("Enter Overseas Airport Code: ")
        
        if overseasairportchoicenon.isdigit():
            
            print("Invalid Input! Airport codes are THREE LETTERS. (Example - JFK) Please try again...")
            print("")
            
            mainmenu()
            
        else:
            
            print("")
            
        overseasairportchoicenon = overseasairportchoicenon.upper()
        
        if overseasairportchoicenon == overseasairport1code:
            
            overseasairportchoicecode = overseasairport1code
            
            overseasairportchoice = overseasairport1
            
            if ukairportchoicecode == ukairport1code:
                
                distance = overseasairport1lpl
                
            elif ukairportchoicecode == ukairport2code:
                
                distance = overseasairport1boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport2code:
            
            overseasairportchoicecode = overseasairport2code
            
            overseasairportchoice = overseasairport2
            
            if ukairportchoicecode == ukairport1code:
                
                distance = overseasairport2lpl
                
            elif ukairportchoicecode == ukairport2code:
                
                distance = overseasairport2boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport3code:
            
            overseasairportchoicecode = overseasairport3code
            
            overseasairportchoice = overseasairport3
            
            if ukairportchoicecode == ukairport1code:
                
                distance = overseasairport3lpl
                
            elif ukairportchoicecode == ukairport2code:
                
                distance = overseasairport3boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()

            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport4code:
            
            overseasairportchoicecode = overseasairport4code
            
            overseasairportchoice = overseasairport4
            
            if ukairportchoicecode == ukairport1code:
                
                distance = overseasairport4lpl
                
            elif ukairportchoicecode == ukairport2code:
                
                distance = overseasairport4boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()

            airportdetailsfinal()
            
        elif overseasairportchoicenon == overseasairport5code:
            
            overseasairportchoicecode = overseasairport5code
            
            overseasairportchoice = overseasairport5
            
            if ukairportchoicecode == ukairport1code:
                
                distance = overseasairport5lpl
                
            elif ukairportchoicecode == ukairport2code:
                
                distance = overseasairport5boh
                
            else:
                
                print("Error! Please try again. Somethings gone wrong from our side...")
                
                print("")
                mainmenu()
            
            airportdetailsfinal()
            
        else:
        
            print("Invalid Input. Please check the code and try again.")
            print("")
        
            mainmenu()
                
    def airportdetailsfinal():
        
        print("You have selected " +overseasairportchoice+ ".")
        print("")
        
        mainmenu()
    
    ukairportchoicenon=input("Enter UK Airport Code: ")
    
    if ukairportchoicenon.isdigit():
            
        print("Invalid Input! Airport codes are THREE LETTERS. (Example - LPL) Please try again...")
        print("")
        
        mainmenu()
            
    else:
            
        print("")
        
    ukairportchoicenon = ukairportchoicenon.upper()
    
    if ukairportchoicenon == ukairport1code:
        
        ukairportchoicecode = ukairport1code
        
        ukairportchoice = ukairport1

        airportdetailsnext()
        
    elif ukairportchoicenon == ukairport2code:
        
        ukairportchoicecode = ukairport2code
        
        ukairportchoice = ukairport2

        airportdetailsnext()
        
    else:
        
        print("Invalid Input. Please check the code and try again.")
        print("")
        
        mainmenu()
        
#==============================================================================================
        
#Flight Details
        
#==============================================================================================
    
def flightdetails():
    
    global maxrange
    global capallstandard
    global planechoice
    global planechoicerun
    global planechoicerange
    global planechoicecap
    global planechoiceminfirst
    global firstclassseatsmax
    
    def flightdetailsnext():
        
        global firstclassseats
        global firstclassseatsnon
        global standardseatsnumb
        global firstclassseatsnon
        global firstyes
        
        print("")
        
        firstclassseatsnon=input("Number of First Class Seats? ")
        
        if firstclassseatsnon.isdigit():
            
            print("")
            
            firstclassseatsnon=float(firstclassseatsnon)
            
        else:
            
            print("Invalid Input! You have to enter a number for this question. Please try again...")
            print("")
            
            mainmenu()
        
        if float(firstclassseatsnon) == 0:
            
            firstyes = 'n'

            flightdetailscalc()
            
        else:
            
            if float(firstclassseatsnon) < float(planechoiceminfirst):
                print("Invalid Input. There must be more than " +planechoiceminfirst+ " for this specific aircraft.")
                print("")

                mainmenu()
                
            elif float(firstclassseatsnon) > float(firstclassseatsmax):
                
                print("Invalid Input. There must be " +str(firstclassseatsmax)+ " or less first class seats for this aircraft type.")
                print("")

                mainmenu()
                
            else:
                
                firstyes = 'y'
                
                flightdetailscalc()
            
    def flightdetailscalc():
        
            global firstclassseats
            global standardseatsnumb
            global firstdoneyes
        
            firstclassseats = firstclassseatsnon
            standardseatsnumb = float(planechoicecap) - float(firstclassseats) * 2
            
            firstdoneyes = 'y'
            
            mainmenu()
    
    global firstdoneyes
    
    firstdoneyes = 'n'
    
    print("What type of aircraft would you like to be used?")
    
    print("Enter '1' for " +plane1+ ".")
    print("Enter '2' for " +plane2+ ".")
    print("Enter '3' for " +plane3+ ".")
    
    planechoicenon=input("Enter number: ")
    
    print("")
    
    if planechoicenon.isalpha():
        
        print("Invalid Input! Please use a number above instead of a letter/word.")
        print("")
        
        mainmenu()
    
    if planechoicenon == '1':
        
        print("Run Cost for each Seat (Each 100km) - £" +plane1run)
        print("Maximum Flight Range - " +plane1range+ " KM")
        print("Maximum Amount of Seats - " +plane1cap)
        print("Minimum First Class Seats (If Applicable) - " +plane1minfirst)
        
        planechoice = plane1
        planechoicerun = plane1run
        planechoicerange = plane1range
        planechoicecap = plane1cap
        planechoiceminfirst = plane1minfirst
        
        maxrange = planechoicerange
        
        capallstandard = planechoicecap
        
        firstclassseatsmax = float(planechoicecap) / 2
        
        flightdetailsnext()
        
    elif planechoicenon == '2':
        
        print("Run Cost for each Seat (Each 100km) - £" +plane2run)
        print("Maximum Flight Range - " +plane2range+ " KM")
        print("Maximum Amount of Seats - " +plane2cap)
        print("Minimum First Class Seats (If Applicable) - " +plane2minfirst)
        
        planechoice = plane2
        planechoicerun = plane2run
        planechoicerange = plane2range
        planechoicecap = plane2cap
        planechoiceminfirst = plane2minfirst
        
        maxrange = planechoicerange
        
        capallstandard = planechoicecap
        
        firstclassseatsmax = float(planechoicecap) / 2
        
        flightdetailsnext()
        
    elif planechoicenon == '3':
        
        print("Run Cost for each Seat (Each 100km) - £" +plane3run)
        print("Maximum Flight Range - " +plane3range+ " KM")
        print("Maximum Amount of Seats - " +plane3cap)
        print("Minimum First Class Seats (If Applicable) - " +plane3minfirst)
        
        planechoice = plane3
        planechoicerun = plane3run
        planechoicerange = plane3range
        planechoicecap = plane3cap
        planechoiceminfirst = plane3minfirst
        
        maxrange = planechoicerange
        
        capallstandard = planechoicecap
        
        firstclassseatsmax = float(planechoicecap) / 2
        
        flightdetailsnext()
        
    else:
        
        print("Invalid Input! We cannot find that aircraft type, please try again.")
        print("")
        
        mainmenu()
        
#==============================================================================================
        
#Price Plan
        
#==============================================================================================
    
def priceplan():
    
    def priceplancheck1():
        
        if ukairportchoicecode == ukairport1code or ukairportchoicecode == ukairport2code:
            
            if overseasairportchoicecode == overseasairport1code:
            
                priceplancheck2()
                
            elif overseasairportchoicecode == overseasairport2code:
                
                priceplancheck2()
                
            elif overseasairportchoicecode == overseasairport3code:
                
                priceplancheck2()
                
            elif overseasairportchoicecode == overseasairport4code:
                
                priceplancheck2()
                
            elif overseasairportchoicecode == overseasairport5code:
                
                priceplancheck2()
                
            else:
                
                print("You need to enter all the details for the airports before continuing.")
                print("")
                mainmenu()
            
        else:
            
            print("You need to enter all the details for the airports before continuing.")
            print("")
            mainmenu()
        
    def priceplancheck2():
        
        if planechoice == plane1:
            
            priceplancheck3()
            
        elif planechoice == plane2:
            
            priceplancheck3()
            
        elif planechoice == plane3:
            
            priceplancheck3()
            
        else:
            
            print("You need to enter all the details about the aircraft before continuing.")
            print("")
            mainmenu()
        
    def priceplancheck3():
        
        if firstdoneyes == 'y':
        
            if firstclassseats == '':
                
                print("You need to enter all the details (Including About First Class) before continuing.")
                print("")
                mainmenu()
                
            else:
                
                priceplancheck4()
                
        elif firstdoneyes == 'n':
            
            print("You need to enter all the details (Including About First Class) before continuing.")
            print("")
            mainmenu()
            
        else:
            
            print("Sorry! Something has gone wrong from our side, please try again!")
            print("")
            
            mainmenu()
        
    def priceplancheck4():
        
        if int(maxrange) == int(distance):
            
            print("You need to select a different aircraft! It isn't possible/unsafe* to complete the route with the selected aircraft.")
            print("")
            print("Your Aircrafts Maximum Range is " +planechoicerange+ "km!")
            print("Your Selected Journey Length is " +distance+ "km!")
            print("")
            print("*Routes can't be close OR the exact same to the maximum distance of the selected aircraft for safety reasons.")
            
            print("")
            mainmenu()
            
        elif int(maxrange) < int(distance):
            
            print("You need to select a different aircraft! It isn't possible to complete the route with the selected aircraft.")
            print("")
            print("Your Aircrafts Maximum Range is " +planechoicerange+ "km!")
            print("Your Selected Journey Length is " +distance+ "km!")
            
            print("")
            mainmenu()
            
        else:
            
            priceplannext()
        
    def priceplannext():
        
        global pricestandard
        global pricefirst

        pricestandard=input("Price of a Standard ticket: £")
        
        if pricestandard.isdigit():
            
            if firstyes == 'y':
            
                pricefirst=input("Price of a First Class ticket: £")
                
            elif firstyes == 'n':
                
                priceplancalc()
                
            else:
                
                print("")
                print("Sorry! Something has gone wrong from our side, please try again...")
                print("")
                mainmenu()
            
            if pricefirst.isdigit():
                
                priceplancalc()
                
            else:
                
                print("Invalid Input! You have to enter a number for this question. Please try again...")
                
                print("")
                priceplannext()
        
        else:
            
            print("Invalid Input! You have to enter a number for this question. Please try again...")
            
            print("")
            priceplannext()
        
    def priceplancalc():
        
        global flightcostperseat
        global flightcost
        global flightincome
        global flightprofit
        global pricefirst
        
        if firstyes == 'n':
        
            pricefirst = '0'
        
        flightcostperseat = float(planechoicerun) * float(distance) / 100
        
        flightincome = float(firstclassseats) * float(pricefirst) + float(standardseatsnumb) * float(pricestandard)
        
        flightcost = float(flightcostperseat) * (float(firstclassseats) + float(standardseatsnumb))
        
        flightprofit = flightincome - flightcost
        
        priceplanfinal()
        
    def priceplanfinal():
        
        print("")
        print("Uk Airport - " +ukairportchoice)
        print("Overseas Airport - " +overseasairportchoice)
        print("Distance - " +distance+ " KM")
        print("Plane Type - " +planechoice)
        print("Maximum Flight Range - " +maxrange+ " KM")
        print("Flight Cost For Each Seat (Per 100KM) - £" +str(flightcostperseat))
        print("Capacity (If all are Standard) - " +planechoicecap)
        print("Number of First Class Seats - " +str(firstclassseats))
        print("Number of Standard Seats - " +str(standardseatsnumb))
        print("Standard Ticket Price - £" +pricestandard)
        
        if firstyes == 'y':
            
            print("First Ticket Price - £" +pricefirst)
            
        print("Flight Cost (Per Seat) - £" +str(flightcostperseat))
        print("Flight Cost - £" +str(flightcost))
        print("Flight Income - £" +str(flightincome))
        print("Flight Profit - £" +str(flightprofit))
        print("")
        
        priceplancheckpoint=input("Enter anything to continue: ")
        print("")
        
        savecheckpoint()
        
    def savecheckpoint():
        
        print("Enter '1' to return to the main menu.")
        print("Enter '2' to save a flight.")
        
        print("")
        saveflightcheckpoint=input("Enter choice here: ")
        print("")
        
        if saveflightcheckpoint == '1':
        
            mainmenu()
            
        elif saveflightcheckpoint == '2':
        
            saveflight()
            
        else:
            
            print("Invalid Input! Please try again...")
            print("")
            
            savecheckpoint()
            
    priceplancheck1()
    
#==============================================================================================
        
#Clear Data
        
#==============================================================================================
    
def cleardata():
    
    def cleardatafinal():
        
        global ukairportchoice
        global overseasairportchoice
        global distance
        global planechoice
        global maxrange
        global runcost
        global capallstandard
        global firstclassseats
        global standardseatsnumb
        global pricestandard
        global pricefirst
        global flightcostperseat
        global flightcost
        global flightincome
        global flightprofit
        global flight1
        global flight1uk
        global flight1ukcode
        global flight1os
        global flight1oscode
        global flight1planechoice
        global flight1standard
        global flight1first
        global flight1distance
        global flight1firstyes
        global flight1set
        global flight2
        global flight2uk
        global flight2ukcode
        global flight2os
        global flight2oscode
        global flight2planechoice
        global flight2standard
        global flight2first
        global flight2distance
        global flight2firstyes
        global flight2set
        global flight3
        global flight3uk
        global flight3ukcode
        global flight3os
        global flight3oscode
        global flight3planechoice
        global flight3standard
        global flight3first
        global flight3distance
        global flight3firstyes
        global flight3set
        global firstdoneyes
        
        ukairportchoice = ''
        overseasairportchoice = ''
        distance = ''
        planechoice = ''
        maxrange = ''
        runcost = ''
        capallstandard = ''
        firstclassseats = ''
        standardseatsnumb = ''
        pricestandard = ''
        pricefirst = ''
        flightcostperseat = ''
        flightcost = ''
        flightincome = ''
        flightprofit = ''
        flight1 = 'No Flight Scheduled.'
        flight1uk = 'N/A'
        flight1ukcode = 'N/A'
        flight1os = 'N/A'
        flight1oscode = 'N/A'
        flight1planechoice = 'N/A'
        flight1standard = 'N/A'
        flight1first = 'N/A'
        flight1distance = 'N/A'
        flight1firstyes = 'n'
        flight1set = 'n'
        flight2 = 'No Flight Scheduled.'
        flight2uk = 'N/A'
        flight2ukcode = 'N/A'
        flight2os = 'N/A'
        flight2oscode = 'N/A'
        flight2planechoice = 'N/A'
        flight2standard = 'N/A'
        flight2first = 'N/A'
        flight2distance = 'N/A'
        flight2firstyes = 'n'
        flight2set = 'n'
        flight3 = 'No Flight Scheduled.'
        flight3uk = 'N/A'
        flight3ukcode = 'N/A'
        flight3os = 'N/A'
        flight3oscode = 'N/A'
        flight3planechoice = 'N/A'
        flight3standard = 'N/A'
        flight3first = 'N/A'
        flight3distance = 'N/A'
        flight3firstyes = 'n'
        flight3set = 'n'
        firstdoneyes = 'n'
        
        print("Your data has now been cleared!")
        print("")
        
        mainmenu()
    
    clearuser=input("Are you sure you want to clear your current data? (y/n) ")
    
    if clearuser == 'y' or clearuser == 'Y':
        
        print("")
        cleardatafinal()
        
    elif clearuser == 'n' or clearuser == 'N':
        
        print("Operation stopped! Returning you back to the main menu...")
        print("")
        mainmenu()
        
    else:
        
        print("Invalid Input! Please try again.")
        print("")
        
        cleardata()
        
#==============================================================================================
        
#Quit Section
        
#==============================================================================================
    
def quitsec():
    
    def quitsecfinal():
    
        print("You have ended the program! Your data has also been cleared automatically.")
        exit()
        
    quituser=input("Are you sure you want to quit? (y/n) ")
    
    if quituser == 'y' or quituser == 'Y':
        
        print("")
        quitsecfinal()
        
    elif quituser == 'n' or quituser == 'N':
        
        print("Operation stopped! Returning you back to the main menu...")
        print("")
        mainmenu()
        
    else:
        
        print("Invalid Input! Please try again.")
        print("")
        
        quitsec()
        
    quitsec()
    
#==============================================================================================
        
#Save Flight
        
#==============================================================================================
    
def saveflight():
    
    print("Flight saving: " +ukairportchoice+ " - " +overseasairportchoice+ "")
    
    print("Current save slots: ")
    print("")
    
    print("Slot 1: " +flight1)
    print("Slot 2: " +flight2)
    print("Slot 3: " +flight3)
    
    print("")
    savecheckpoint=input("Which save slot would you like to use? (Enter '0' to cancel) ")
    print("")
    
    if savecheckpoint.isalpha():
        
        print("Invalid Input! You have to enter a number for this question. Please try again...")
        print()
        
        mainmenu()
    
    if savecheckpoint == '0':
        
        print("Canceled!")
        print("")
        
        mainmenu()
        
    elif savecheckpoint == '1':
        
        def next1():
            
            next2()
            
        def next1override():
            
            flight1checkpoint=input("Are you sure you would like to override the save slot? (y/n) ")
            print("")
            
            if flight1checkpoint == 'y' or flight1checkpoint == 'Y':
                
                next2()
                
            elif flight1checkpoint == 'n' or flight1checkpoint == 'N':
                
                print("Operation stopped!")
                print("")
                
                saveflight()
                
            else:
                
                print("Invalid Input! Please try again...")
                print("")
                
                next1override()
                
        def next2():
            
            global flight1
            global flight1uk
            global flight1ukcode
            global flight1os
            global flight1oscode
            global flight1planechoice
            global flight1standard
            global flight1first
            global flight1firstyes
            global flight1set
            
            flight1=(ukairportchoice+ " - " +overseasairportchoice+ "")
            
            flight1uk=ukairportchoice
            
            flight1ukcode=ukairportchoicecode
            
            flight1os=overseasairportchoice
            
            flight1oscode=overseasairportchoicecode
            
            flight1planechoice=planechoice
            
            flight1standard=pricestandard
            
            flight1first=pricefirst
            
            flight1firstyes=firstyes
            
            flight1set = 'y'
            
            next3()
            
        def next3():
            
            filehandlesection()
        
        if flight1 == 'No Flight Scheduled.':
            
            next1()
            
        else:
            
            next1override()
            
    elif savecheckpoint == '2':
        
        def next1():
            
            next2()
            
        def next1override():
            
            flight2checkpoint=input("Are you sure you would like to override the save slot? (y/n) ")
            print("")
            
            if flight2checkpoint == 'y' or flight2checkpoint == 'Y':
                
                next2()
                
            elif flight2checkpoint == 'n' or flight2checkpoint == 'N':
                
                print("Operation stopped!")
                print("")
                
                saveflight()
                
            else:
                
                print("Invalid Input! Please try again...")
                print("")
                
                next1override()
                
        def next2():
            
            global flight2
            global flight2uk
            global flight2ukcode
            global flight2os
            global flight2oscode
            global flight2planechoice
            global flight2standard
            global flight2first
            global flight2firstyes
            global flight2set
            
            flight2=(ukairportchoice+ " - " +overseasairportchoice+ "")
            
            flight2uk=ukairportchoice
    
            flight2ukcode=ukairportchoicecode
            
            flight2os=overseasairportchoice
            
            flight2oscode=overseasairportchoicecode
            
            flight2planechoice=planechoice
            
            flight2standard=pricestandard
            
            flight2first=pricefirst
            
            flight2firstyes=firstyes
            
            flight2set = 'y'
            
            next3()
            
        def next3():
            
            filehandlesection()
        
        if flight2 == 'No Flight Scheduled.':
            
            next1()
            
        else:
            
            next1override()
            
    elif savecheckpoint == '3':
        
        def next1():
            
            next2()
            
        def next1override():
            
            flight3checkpoint=input("Are you sure you would like to override the save slot? (y/n) ")
            print("")
            
            if flight3checkpoint == 'y' or flight3checkpoint == 'Y':
                
                next2()
                
            elif flight3checkpoint == 'n' or flight3checkpoint == 'N':
                
                print("Operation stopped!")
                print("")
                
                saveflight()
                
            else:
                
                print("Invalid Input! Please try again...")
                print("")
                
                next1override()
                
        def next2():
            
            global flight3
            global flight3uk
            global flight3ukcode
            global flight3os
            global flight3oscode
            global flight3planechoice
            global flight3standard
            global flight3first
            global flight3firstyes
            global flight3set
            
            flight3=(ukairportchoice+ " - " +overseasairportchoice+ "")
            
            flight3uk=ukairportchoice
        
            flight3ukcode=ukairportchoicecode
            
            flight3os=overseasairportchoice
            
            flight3oscode=overseasairportchoicecode
        
            flight3planechoice=planechoice
            
            flight3standard=pricestandard
            
            flight3first=pricefirst
            
            flight3firstyes=firstyes
            
            flight3set = 'y'
            
            next3()
            
        def next3():
            
            filehandlesection()
        
        if flight3 == 'No Flight Scheduled.':
            
            next1()
            
        else:
            
            next1override()
        
    else:
        
        print("Invalid Input! Please try again...")
        print("")
        
        saveflight()
        
#==============================================================================================
        
#View Saved Flights & Available Flights
        
#==============================================================================================
        
def viewsaveslot():
    
    print("Flight Slot 1: " +flight1)
    print("Flight Slot 2: " +flight2)
    print("Flight Slot 3: " +flight3)
    
    print("")
    print("(NOTE - Enter 'y' to see saved flights in more detail)")
    checkgo=input("Enter anything else to continue: ")
    print("")
    
    if checkgo == 'y' or checkgo == 'Y':

        availflights()
        
    else:
        
        mainmenu()
    
def availflights():
    
    print("Current Saved Flights: (IN DETAIL)")
    print("")
    
    print("Flight 1:")
    print("-----------------------------------------------------------")
    print("")
    
    print("FROM:")
    print(flight1uk+ " (" +flight1ukcode+ ")")
    print("TO:")
    print(flight1os+ " (" +flight1oscode+ ")")
    print("")
    print("Plane Model - " +flight1planechoice)
    print("")
    print("Economy Class - Starting at: £" +flight1standard)
    
    if flight1set == 'n':
        
        print("First Class - Starting at: £N/A")
        
    elif flight1set == 'y':
    
        if flight1firstyes == 'y':
    
            print("First Class - Starting at: £" +flight1first)
    
    print("")
    print("Flight 2:")
    print("-----------------------------------------------------------")
    print("")
    
    print("FROM:")
    print(flight2uk+ " (" +flight2ukcode+ ")")
    print("TO:")
    print(flight2os+ " (" +flight2oscode+ ")")
    print("")
    print("Plane Model - " +flight2planechoice)
    print("")
    print("Economy Class - Starting at: £" +flight2standard)
    
    if flight2set == 'n':
        
        print("First Class - Starting at: £N/A")
        
    elif flight2set == 'y':
    
        if flight2firstyes == 'y':
    
            print("First Class - Starting at: £" +flight2first)
    
    print("")
    print("Flight 3:")
    print("-----------------------------------------------------------")
    print("")
    
    print("FROM:")
    print(flight3uk+ " (" +flight3ukcode+ ")")
    print("TO:")
    print(flight3os+ " (" +flight3oscode+ ")")
    print("")
    print("Plane Model - " +flight3planechoice)
    print("")
    print("Economy Class - Starting at: £" +flight3standard)
    
    if flight3set == 'n':
        
        print("First Class - Starting at: £N/A")
        
    elif flight3set == 'y':
    
        if flight3firstyes == 'y':
    
            print("First Class - Starting at: £" +flight3first)
    
    print("")
    print("-----------------------------------------------------------")
    print("")
    
    viewflightscheckpoint=input("Enter anything to continue: ")
    print("")
    
    mainmenu()
    
#==============================================================================================
        
#File Air-Routes Database
        
#==============================================================================================
    
def filehandlesection():
    
    file = open('airlineflights.txt','w')
    file.write("Saved Flights:""\n")
    file.write("" "\n")
    
    file.write("FROM:""\n")
    file.write(flight1uk+ " (" +flight1ukcode+ ") \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write(flight1os+ " (" +flight1oscode+ ") \n")
    file.write("" "\n")
    file.write("Aircraft model = " +flight1planechoice+ "\n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £" +flight1standard+ "\n")
    
    if flight1set == 'n':
        
        file.write("First Class Ticket Price = £N/A" "\n")
        
    if flight1set == 'y':
    
        if flight1firstyes == 'y':
    
            file.write("First Class Ticket Price = £" +flight1first+ "\n")
        
    file.write("" "\n")
    file.write("-------------------------------------------""\n")
    
    file.write("" "\n")
    file.write("FROM:""\n")
    file.write(flight2uk+ " (" +flight2ukcode+ ") \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write(flight2os+ " (" +flight2oscode+ ") \n")
    file.write("" "\n")
    file.write("Aircraft model = " +flight2planechoice+ "\n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £" +flight2standard+ "\n")
    
    if flight2set == 'n':
        
        file.write("First Class Ticket Price = £N/A" "\n")
        
    if flight2set == 'y':
    
        if flight2firstyes == 'y':
    
            file.write("First Class Ticket Price = £" +flight2first+ "\n")
        
    file.write("" "\n")
    file.write("-------------------------------------------""\n")
    
    file.write("" "\n")
    file.write("FROM:""\n")
    file.write(flight3uk+ " (" +flight3ukcode+ ") \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write(flight3os+ " (" +flight3oscode+ ") \n")
    file.write("" "\n")
    file.write("Aircraft model = " +flight3planechoice+ "\n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £" +flight3standard+ "\n")
    
    if flight3set == 'n':
        
        file.write("First Class Ticket Price = £N/A" "\n")
        
    if flight3set == 'y':
    
        if flight3firstyes == 'y':
    
            file.write("First Class Ticket Price = £" +flight3first+ "\n")
        
    file.write("" "\n")
    file.write("-------------------------------------------""\n")
    
    file.close()
    
    print("The database file has been updated! Please completely close the file and open it again for the updated version.")
    
    print("")
    mainmenu()
    
#==============================================================================================
        
#File Clear
        
#==============================================================================================
    
def fileclear():
    
    print("Please Note - Your data will NOT be cleared, only the file will be reset to its default state.")
    print("")
    
    fileclear2()
    
def fileclear2():
    
    checkfileclear=input("Are you sure you want to clear the file? (y/n) ")
    print("")
    
    if checkfileclear == 'y' or checkfileclear == 'Y':
        
        fileclear3()
        
    elif checkfileclear == 'n' or checkfileclear == 'N':
        
        print("Clear stopped! Returning you back to the main menu...")
        print("")
        
        mainmenu()
        
    else:
        
        print("Invalid Input! Please try again...")
        print("")
        
        fileclear2()
        
def fileclear3():
    
    file = open('airlineflights.txt','w')
    file.write("Saved Flights:""\n")
    file.write("" "\n")
    
    file.write("FROM:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("Aircraft model = N/A \n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £N/A \n")
    file.write("First Class Ticket Price = £N/A \n")
    file.write("" "\n")
    file.write("-------------------------------------------""\n")
    
    file.write("" "\n")
    file.write("FROM:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("Aircraft model = N/A \n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £N/A \n")
    file.write("First Class Ticket Price = £N/A \n")
    file.write("" "\n")
    file.write("-------------------------------------------""\n")

    file.write("" "\n")
    file.write("FROM:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("TO:""\n")
    file.write("N/A \n")
    file.write("" "\n")
    file.write("Aircraft model = N/A \n")
    file.write("" "\n")
    file.write("Economy Ticket Price = £N/A \n")
    file.write("First Class Ticket Price = £N/A \n")
    file.write("" "\n")
    file.write("-------------------------------------------""\n")
    
    file.close()
    
    print("The database file has been cleared and set back to its default! Please completely close the file and open it again for the updated version.")
    
    print("")
    mainmenu()

mainmenu()
