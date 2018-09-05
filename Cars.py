import csv

def average(cyl,reader):    #function for finding average mileage
    total=0
    count=0
    for row in reader:
        if row[7]==cyl:
            count+=1
            total+=int(row[10])
    print("The average highway mileage of cars with ", cyl," cylinders is ","%.2f" % (total/count))

def maximum(cyl,reader):    #function for finding max mileage
    maxHWY=-1
    for row in reader:
        if row[7]==cyl and int(row[10])>maxHWY:
            maxHWY=int(row[10])
    print("The maximum highway mileage of cars with ", cyl," cylinders is", maxHWY)
    

def minimum(cyl,reader):    #function for finding min mileage
    minHWY=100
    for row in reader:
        if row[7]==cyl and int(row[10])<minHWY:
            minHWY=int(row[10])
    print("The minimum highway mileage of cars with ", cyl," cylinders is", minHWY)

def carline(carDesc,reader):    #function for analysis of carline statistics
    mileage= input("What is the minimum highway mileage of the cars in this description that you are trying to analyze? ")
    print()
    print("STATISTICS OF VEHICLES WITH DESCRIPTION OF: ",carDesc)

    
    print("CITY MILEAGE       ","HIGHWAY MILEAGE    ", "MAKE               ", "MODEL") #context
    stats=[]
    for row in reader:  #reading in data for chosen carline class description
        if row[69]==carDesc and row[10]>=mileage:
            line=[]
            line.append(row[9])
            line.append(row[10])
            line.append(row[2])
            line.append(row[3])
            # pretty printing
            cols=4
            split=[line[x:x+len(line)//cols] for x in range(0,len(line),len(line)//cols)]
            for row in zip(*split):
                print("".join(str.ljust(x,20) for x in row))
    print()

def drilldown(carType,reader): #function for analysis of percentage 
    total=0
    count=0
    perc=input("Which highway mileage percentage are you wanting to analyze? ")

    for row in reader:  #iteration for analysis 
        if row[69]==carType:
            total+=1
            if row[10]==perc:
                count+=1
    print("The percentage of ",carType," vehicles with a highway mileage of ",perc," is: ","%.2f" % (count/total),"%")
            
    

def main(reader): #main function where all of the parameters/variables are inputted and passed to other functions
    print("-----AGGREGATION-----")
    
    while True: #call for robust input
        cyl=input("How many cylinders? (3/4/5/6/8/10/12/16) ")
        if cyl=="3" or cyl=="4" or cyl=="5" or cyl=="6" or cyl=="8" or cyl=="10" or cyl=="12" or cyl=="16":
            break
        print("Sorry, you must enter a valid input. :(")
        
    while True: #call for robust input
        ques= input("Would you like to find the average/minimum/or maximum highway mileage? (avg/min/max) ")
        if ques=="avg" or ques=="max" or ques=="min":
            break
        print("Sorry, you must enter a valid input. :(")
    

    if ques=="avg": #calls for functions depending on input
        average(cyl,reader)
    if ques=="max":
        maximum(cyl,reader)
    if ques=="min":
        minimum(cyl,reader)
    
     
    print()
    print("-----SLICING-----")
    prev=reader[1][69]  #used for creating list of different carline class descriptions
    check=[]
    print(prev)
    check.append(prev)
    for desc in reader:
        if prev != desc[69]:
            prev=desc[69]
            check.append(prev)
            print(prev)
    print("----------------------------------------")

    while True: #call for robust input
        carDesc=input("Choose a carline class descirption from the list above to analyze (enter exactly as typed above): ")
        if carDesc in check:
            break
        print("Sorry, you must enter a valid input. :(")
    

    carline(carDesc,reader) #call for function with chosen carline class description and array for iteration 

    print("-----DRILL-DOWN-----")
    while True: #call for robust input 
        carType= input("Choose another carline description from the same list to analyze: ")
        if carType in check:
            break
        print("Sorry, you must enter a valid input. :(")

    drilldown(carType,reader) #call for function with chosen carline class description with array
        
                       
#--------------------------------------------------------------------------


with open('2015FEGuide.csv') as csvfile: #"with" opens file during use, but is closed automatically after use
    readCSV= csv.reader(csvfile, delimiter=",")

    reader=[] #array for file data
    
    for row in readCSV: #data passing into array 
        reader.append(row)
        
    answer="Y"
    while answer =="y" or answer =="Y": #continues program if requested
        main(reader)
        print()
        answer=input("Would you like to answer more questions? (Y/y/n) " )


