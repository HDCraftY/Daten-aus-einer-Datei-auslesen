
woerter = {}
woerter1 = {}                                             
woerter2 = {"Beenden": "Sie haben das Programm beendet."}
#Datentyp Dictionary. Einen für Deutsch-Englisch, einen für Englisch-Deutsch Übersetzungen
#und einen dritten, um das Programm zu beenden. Sprich wenn der Schlüssel "Beenden" eingegeben
#wird, wird "Sie haben das programm beendet." ausgegeben.

fobj = open("woerterbuch.txt", "r")
#Mit der Funktion "open" wird der Folgende Pfad geöffnet. Der zweite Parameter "r" gibt an
#das wir die Datein lesen wollen (Lesemodus).

for line in fobj:                    #"line" referenziert auf eine Zeile. 
    line = line.strip()
    zuordnung = line.split(" ")
    woerter[zuordnung[0]] = zuordnung[1]
    woerter1[zuordnung[1]] = zuordnung[0]
fobj.close()
#Hier wird mit der iterierenden for-Schleife die in der Textdatei angegebenen Zeilen ausgegeben.
#Mit der Methode "strip" werden Whitespacezeichen (z.B. Zeilenumbrüche entfernt).

#Mit der Methode "split" wird die eingelesene Zeile in zwei Teile aufgespalten, damit ein Wörterbuch
#gebildet werden kann (links (0) und rechts (1) vom Leerzeichen in der Textdatei)

#Dazu gibt es eine Zuordnung im Datentyp Dictionary. Dem Schlüssel zuordnung[0] wird ein
#neuer Wert zugeweisen zuordnung[1]. Das bedeutet, dem englischen Wort wird eine deutsche Über-
#setzung zugeordnet. Hier wurde das ein zweites Mal getan, um einem deutschen Wort ein englisches Wort
#zuzuweisen.

#mit der Methode close() wird das Auslesen der Datei beendet.


while True:

    wort = input("Geben Sie ein Wort ein: ")
   
    if wort in woerter:
        print("Die Übersetzung lautet: ", woerter[wort])
    
    elif wort in woerter1:
        print("Die Übersetzung lautet: ", woerter1[wort])

    elif (wort not in woerter or woerter1) and (wort not in woerter2):
        print("Das eingegebene Wort ist entweder falsch geschrieben oder nicht in der Datenbank.")
        
    elif (wort in woerter2):
        print(woerter2[wort])
        break  
        
             
#In einer Endlosschleife wird zuerst gefragt, welches Wort man eingeben möchte.
#Anschließend wird jeweils die if Anweisung ausgeführt die Wahr ist.
#Dabei wird geprüft, ob das eingegebene Wort in dem Dictionary woerter, woerter1 oder woerter2 ist.
#Ist der "schlüssel" richtig, wird der entsprechende "wert" ausgegeben.

    

   





   



        
        
    


    
        

