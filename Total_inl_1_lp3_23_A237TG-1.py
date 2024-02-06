#biblioteks importering av godkända tillgångar för inlämningsuppgiften
import csv
import matplotlib.pyplot as plt

#globala listor:
MasterData = []
kpiData = []
tjansteData = []
livsmedelData = []

#Deluppgift 1;_________________________________________________________________
# Rensad, enligt kommentar: "rensa bort all kod som du inte längre använder".
def avg_KPI(input_list1):
    kpiMedelTemp=[]
    for y in range(len(input_list1)):
        templist_1=input_list1[y][1:]
        templist_1=list(map(float,templist_1))    
        templist_1=round(sum(templist_1)/len(templist_1), 2)
        #templist_1=templist_1
        kpiMedelTemp.append(templist_1) #appendar sedan t ill en egen lista
    return(kpiMedelTemp)

def Find_Min(input_list):
    min_index = []
    #definierar största och minsta värdet för varje rad "abc" indexet i for-loopen.
    for abc in range(len(input_list)):
        min_value = min(input_list[abc])
        #går igenom hela "abc" raden tills den hittar ett index på raden som har samma "minimum" värde som tidigare definierats i första nestlade for-loopen.rad "abc", index "x"
        for x in range(len(input_list[abc])):
            if input_list[abc][x] == min_value:
                min_index.append(x+1) #tillsätter ett index värde +1 för att definiera vilken månad som hade detta min värde.
                break #break här för att ifall det skulle finnas fler med samma värde (skapar för många index)
    return(min_index)

def Find_Max(input_list):
    max_index = []
    #definierar största och minsta värdet för varje rad "abc" indexet i for-loopen.
    for abc in range(len(input_list)):
        max_value = max(input_list[abc])
        #går igenom hela "abc" raden tills den hittar ett index på raden som har samma "maximum" värde som tidigare definierats i första nestlade for-loopen.rad "abc", index "y"
        for y in range(len(input_list[abc])):
            if input_list[abc][y] == max_value: 
                max_index.append(y+1) #tillsätter ett index värde +1 för att definiera vilken månad som hade detta min värde.
                break #break här för att ifall det skulle finnas fler med samma värde (skapar för många index)
    
    return(max_index)

# Deluppgift 2a_____________________________________________________________________________________________________
def read_file(csvfile):
    inData = [] #tilldelar nestlade listorna till globala listor, mest för definition i funktionens fall (hålla enklare reda på)
        
    with open (csvfile, 'r', encoding="utf8") as file:
        csv_reader = csv.reader(file, delimiter = ';') # från föreläsning, filobjektet 'csv_reader' med ; delimitter
        for rad in csv_reader:                      
            inData.append(rad) # Läs in rad för rad från filen och spara i 'inData' listan
    
    for n in range(2):
        print(inData[n]) #printar ut 2 första raderna
    return(inData) #retunerar listan

# Deluppgift 2b____
#*********Deluppgift 1:s Modifierad AVG_KPI funktionen för uppgift 2b.
def avg_kpi_modified(inputlist1):
    #egen lista i funktionen som "rätt svar" ska sparas i för senare användning.
    ValuesList1 = [[],[]]
    #slicear bort årtalen, row 1.
    templista=inputlist1[1:] 
    
    #slicear och transformerar listan önskvärt, lägger sedan till genom ".append" till min "valueslist" alla uträkningar för dessa.
    #Ska sedan retuneras i nästa funktion til en string format som ska kunna plocka direkt från resultat (values) listan.
    for u in range(1, len(inputlist1)):
        templista=inputlist1[u][1:]
        increase=round(float(inputlist1[u][-1])-100, 2)
        templista=list(map(float,templista))
        ValuesList1[0].append(round((sum(templista[1:])/(len(templista)-1)),2))
        ValuesList1[1].append(increase)
    return(ValuesList1)


#läser in listan från argumentet i huvudprogram delen.
def prisutv_procent(inputlist):
    ValuesList=avg_kpi_modified(inputlist)
    templista=inputlist[1:]
    
    #if beroende på vilken lista som går in för att rubrikerna ska vara rätt
    if inputlist == livsmedelData:
        print('+{:-<40}+{:-<15}+{:-<15}+'.format("", "", ""))
        print('|{:<40}|{:<15}|{:<15}|'.format('Kategorier av livsmedel', 'Medelvärde', 'Totalt'))
        print('+{:=<40}+{:=<15}+{:=<15}+'.format("", "", ""))
    
    elif inputlist == tjansteData:
        print('+{:-<40}+{:-<15}+{:-<15}+'.format("", "", ""))
        print('|{:<40}|{:<15}|{:<15}|'.format('Kategorier av varor och tjänster', 'Medelvärde', 'Totalt'))
        print('+{:=<40}+{:=<15}+{:=<15}+'.format("", "", ""))
    
    #Hur de skall sedan skrivas ut baserat på for satsens input lista[x][y] där x (0 eller 1) blir medelvärdet eller då ökningeen, y blir indexet på raden
    for v in range(len(templista)):
        print('|{:<40}|{:<15}|{:<15}|'.format(templista[v][0], ValuesList[0][v], ValuesList[1][v]))
        print('+{:-<40}+{:-<15}+{:-<15}+'.format("", "", ""))
        
    return()
#Deluppgift 3__________________________________________________________________________________________________________

#läser in listan från definitionen i huvudprogram delen.
def plotta_data(inputData, inputheader): #inputData blir inputlistan, det vi kör in här definierar vad för lista som ska plottas.
    years=[]
    for abc in inputData[0][1:]: #års "row" med kolumnindexet för vilka år från listan.
        years.append(int(abc))
        
    for s,t in zip(range(len(inputData)), range(1,len(inputData))): #"dubbelräknare" ena (s) för indexet 0 till antalet rows, andra (t) för 1 till antalet rows.
        utveckling = [float(z) for z in inputData[t][1:]] #indexar alla värden i listan, slicear kortfattat bort "row" namnet.
        header = inputData[t][0] #definierar vad namnet på linjen blir, är alltid första i "row" indexet, det man undersöker helt enkelt.
        plt.plot(years, utveckling, label = header) #plt.plot, kalkylerar grafen genom "years" , "utveckling", tar in färg variabeln (som blivit en string med definierad färg i funktionen), och sätter en "label" på linjen.
        
    plt.title(inputheader) #titeln på hela grafen
    plt.grid() #ger oss en grid view på plotten
    plt.xlabel('År') #ger x-axeln namnet "år
    plt.ylabel('Prisutvecklingen') #ger y-axeln namnet "prisutveckling"
    plt.legend() #ger en informations ruta angående labels i plotten (linjens namn), visualiserar definitionen genom de definierade färger och namn för de.

    plt.show() #visar plotten".
    return()
    
# Deluppgift 4___________________________________________________________________________________________________________
def monthcheck(month_nr): #input som retunerar en string som definieras av plt.plot funktionen som färg sedan i grafen
            month_nr = month_nr-1        
            if month_nr == 0:
                month='januari'
            elif month_nr == 1:
                month='februari' 
            elif month_nr == 2:
                month='mars'
            elif month_nr == 3:
                month='april'
            elif month_nr == 4:
                month='maj'
            elif month_nr == 5:
                month='juni'
            elif month_nr == 6:
                month='juli'
            elif month_nr == 7:
                month='augusti'
            elif month_nr == 8:
                month='september'
            elif month_nr == 9:
                month='oktober'
            elif month_nr == 10:
                month='november'
            elif month_nr == 11:
                month='december'
            else:
                #retunerar "404" ifall man inte angett ett giltligt månads index:
                month=404
                print('Enter a valid month index number, please try again')
            return(month)

def konsumentprisindex(inputlista_1):
    inputlista_1 = inputlista_1[1:] # slicear bort första raden i listan

    kpiMedel = []
    MonthKpiMedel = []
    years_1=[]

    #"monads" input , sparar denna variabeln , och ska definiera vilket index i raderna jag vill plocka ut senare
    monad = int(input('Ange vilken månad som ska presenteras: '))

    #month text som ska köras in i månads funktionen för att retunera en string med månads namnet per input indexet
    month_txt = monthcheck(monad)

    #skapar kpiMedel listan med alla värden (enbart) genom index från for loopen och slicear bort årtalet (element 0 i alla rader)
    kpiMedel = avg_KPI(inputlista_1)
    
    #skapar års listan (min "header" på listorna)
    for a in range(len(inputlista_1)):
        templist_1=int(inputlista_1[a][0])
        years_1.append(templist_1)

    #definierar en andra årslista för senare användning (ifall den behöver ändras)
    years_2 = years_1

    # en if sats ifall man skrivit in ett otgiltligt månads index:
    if not month_txt == 404:
    #skapar min månadslista med värden för varje månad genom en for loop med indexet som "monads" input från tidigare
        for e in range(len(inputlista_1)):    
            #försöker ifall indexet finns, vilket det inte gör för 2022:s alla månader.
            try: 
                templist_2=inputlista_1[e][monad] #lita e i for loopen, till månads index input.
                templist_2=float(templist_2) #konverterar till float
                MonthKpiMedel.append(templist_2) #appendar sedan t ill en egen lista

            #finns inte indexet skapar den en separat year lista utan de åren som inte har ett månads index.
            except:
                years_2 = years_1[1:] #slicear bort första årtalet, kommer alltid funka då det går frammåt i tiden, ökar årtalet och index inmatningen tar den bara bort senaste året igen.
                years_2.reverse()


    #"reverse" alla listor så att det går från "0 / 100" så det visualiserar ökningen:
    kpiMedel.reverse()
    years_1.reverse()
    MonthKpiMedel.reverse()

    #plottar medelKpi:n i bar och linje form:
    plt.bar(years_1, kpiMedel, color = 'lightblue', label = 'kpiMedel')
    #plot för månads kpi med en if sats ifall man skrivit in ett otgiltligt månads index:
    if not month_txt == 404:
        plt.plot(years_2, MonthKpiMedel, color = 'red', label = 'linjediagram för ' + month_txt)
    #plot för årligt kpi:
    plt.plot(years_1, kpiMedel, color = 'black', label = 'Linjediagram för medelkpi')



    #PLOT VIEWER    
    inputheader_1 = "Konsumentprisindex under åren 1980 – 2022." #mitt header/namn på grafen (plotten)
    plt.title(inputheader_1) #titeln på hela grafen

    plt.xlim(1980, 2023) #view:n på x-led
    plt.ylim(100, 400) ##view:n på y-led
    plt.xticks(rotation=90)
    plt.grid() #ger oss en grid view på plotten
    plt.xlabel('År') #ger x-axeln namnet "år"
    plt.ylabel('Konsumentprisindex') #ger y-axeln namnet "prisutveckling"
    plt.legend() #ger en informations ruta angående labels i plotten (linjens namn), visualiserar definitionen genom de definierade färger och namn för de.
    plt.show()
    return()

# Deluppgift 5__________________________________________________________________________________________
#*********Deluppgift 1:s funktion av att hitta min och max values samt indexarar dessa.


#Här börjar "Deluppgift 5" funktionen._________________
def KPI_Max_Min(KPI_LIST_INPUT):
    #definition av importerad lista samt slicear bort första raden (radnamnen (jan,feb,mars...))
    inputlist_KPI = KPI_LIST_INPUT
    inputlist_KPI = inputlist_KPI[1:]
    #listor för funktionen
    value_list = []
    years_KPI = []
    
    #skapar en temporär lista som slicear bort första columnen på varje rad (årtalet, 2022, 2021...)
    #och importerar raderna till en ny lista: value_list
    for xy in range(len(inputlist_KPI)):
            templist_xy=inputlist_KPI[xy][1:]
            templist_xy=list(map(float,templist_xy))
            value_list.append(templist_xy)
    #skapar en temporär lista som slicear bort allt förrutom först columnen på varje rad
    #och importerar raderna till en ny lista: years_KPI
    for bc in range(len(inputlist_KPI)):
        templist_bc=inputlist_KPI[bc][0]
        templist_bc =int(templist_bc)
        years_KPI.append(templist_bc)
    
    #från uppgift 1, hittar min och max, indexar dessa i varsina 2 listor.
    min_index=Find_Min(value_list)
    max_index=Find_Max(value_list)

    #skapar plot för KPI av max samt min indexena, med årslistan och attributer definierat till (färg och namn)
    plt.scatter(max_index, years_KPI, color='blue',label='Årsmax') 
    plt.scatter(min_index, years_KPI, color='red',label='Årsmin')

    #PLOT VIEWER    
    KPI_inputheader = "Månad med högsta resp. lägsta årsvärde av KPI under åren 1980 - 2022" #mitt header/namn på grafen (plotten)
    plt.title(KPI_inputheader) #titeln på hela grafen
    plt.grid() #ger oss en grid view på plotten
    plt.xlabel('Månad') #ger x-axeln namnet "månad"
    plt.ylabel('År') #ger y-axeln namnet "år"
    plt.legend() #ger en informations ruta angående labels i plotten (linjens namn), visualiserar definitionen genom de definierade färger och namn för de.
    plt.show() #visar plotten
    
    return()

##############################################################

#__________________Huvudprogram med Meny______________________

##############################################################

while True: #initierar menyn
    print("\nMeny \n \n1. Läser in csv-filerna. \n2. Konsumentprisindex under åren 1980 – 2022. \n3. Prisutvecklingen för de olika kategorierna 1980 – 2021. \n4. Prisutvecklingen i procentform för de olika kategorierna 1980 – 2021. \n5. Jämförelse mellan olika kategorier under åren 1980 – 2021. \n6. Avsluta programmet.\n")
    Meny_val=input("\nVälj ett menyalternativ (1 - 6): ")
    if Meny_val == "":
        pass
    else:
        Meny_val=(int(Meny_val))
    #beroende på vad inputten blir, definierar jag genom if satserna hur jag fortsätter programmet.
    
#1. Läs in filer.
    if Meny_val == 1:
        csvfil=input("\nAnge filnamn eller tryck bara Enter för kpi.csv: ") or 'kpi.csv'
        if csvfil == "":
            kpiData=read_file('kpi.csv') #tilldelar nestlade listorna till globala listor
        else:
            kpiData=read_file(csvfil)

        csvfil=input("\nAnge filnamn eller tryck bara Enter för tjanster.csv: ") or 'tjanster.csv'
        if csvfil == "":
            tjansteData =read_file('tjanster.csv') #tilldelar nestlade listorna till globala listor
        else:
            tjansteData=read_file(csvfil)
            
        csvfil=input("\nAnge filnamn eller tryck bara Enter för livsmedel.csv: ") or 'livsmedel.csv'
        if csvfil == "":
            livsmedelData = read_file('livsmedel.csv') #tilldelar nestlade listorna till globala listor
        else:
            livsmedelData=read_file(csvfil)
            
        
#2. Konsumentprisindex under åren 1980 - 2022.
    elif Meny_val == 2:
        konsumentprisindex(kpiData)

#3. Diagram över prisutvecklingen för de olika kategorierna 1980 - 2021.
    elif Meny_val == 3:
        meny3_val = input("\nUndermeny\nVälj vilken/vilka listor vill du få diagram från:\n1. livsmedelData\n2. tjansteData\n3. både livsmedelData och tjansteData\n\nVälj ett menyalternativ (1 - 3): ")
        meny3_val=(int(meny3_val))
        
        if meny3_val == 1:
            plotta_data(livsmedelData, "Prisutvecklingen för olika livsmedel 1980 – 2021.")
            
        elif meny3_val == 2:
            plotta_data(tjansteData, "Prisutvecklingen för olika kategorier av varor och tjänster 1980 – 2021.")
            
        elif meny3_val == 3:
            plotta_data(livsmedelData, "Prisutvecklingen för olika livsmedel 1980 – 2021.")
            print('\n')
            plotta_data(tjansteData, "Prisutvecklingen för olika kategorier av varor och tjänster 1980 – 2021.")
            
        else:
            print("Enter a valid number 1-3, returning to main menu.")
        
#4. Tabell över prisutvecklingen för de olika kategorierna 1980 - 2021.
    elif Meny_val == 4:
        #matar in argumentet, funktionen kör med listan
        prisutv_procent(livsmedelData)
        #snyggare med avskiljda listor
        print("\n\n\n")
        #matar in argumentet, funktionen kör med listan
        prisutv_procent(tjansteData)
        
#5. Diagram över högsta och lägsta årskpi under åren 1980 - 2022.
    elif Meny_val == 5:
        KPI_Max_Min(kpiData)
        
#6. Avsluta programmet.
    elif Meny_val == 6:
        print("Tack för denna gång. Programmet avslutas.")
        break
        Meny_val =0
    
    else:
        print("Felaktigt val försök igen!")
    Meny_val =0