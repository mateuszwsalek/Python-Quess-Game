import random
import pyttsx3
engine=pyttsx3.init()
engine.setProperty('voice','com.apple.speech.voice.Victoria')
volume=engine.getProperty('volume')
engine.setProperty('volume',volume +0.75)
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-70)
engine.say('Napisz mi swoje imię')
print("Napisz mi swoje imię")
engine.runAndWait()
MyName=input()
MyName=MyName.upper()
Female=str(MyName[-1]).upper()
engine.say("Cześć "+ MyName +"\n spróbuj zgadnąć liczbę \n o której teraz myślę?")
print ("Cześć "+ MyName +" spróbujesz zgadnąć liczbę o której myślę")
engine.runAndWait()
QS= random.randint(1,10)
engine.say('Wybierz liczbę \n liczba musi być z zakresu od 1 do Dziesięciu')
print('Wpisz swoją liczbę\n liczba musi być z zakresu od 1 do 10')
engine.say('i Wpisz swoją liczbę')
engine.say('masz 6 prób odgadnięcia')
engine.runAndWait()


dict={          1:'pierwszej',
                2:'drugiej',
                3:'trzeciej',
                4:'czwartej',
                5:'piątej',
                6:'szóstej'
     }
def Mytry(i):
    return dict.get(i,"invalid try")

i=1

for i in range(6):
    MyNumber=input()
    engine.say('twoja liczba to' + MyNumber)
    engine.runAndWait()
    if int(QS) == int(MyNumber):
        engine.say('Brawo gratulacje')
        engine.runAndWait()
        break
    elif int(QS) > int(MyNumber):
        engine.say('Moja liczba jest większa \n spróbuj jeszcze raz')
        print('Moja liczba jest większa \n spróbuj jeszcze raz')
        engine.runAndWait()

    
    elif int(QS) < int(MyNumber):
        engine.say('Moja liczba jest mniejsza \n spróbuj jeszcze raz')
        print('Moja liczba jest mniejsza \n spróbuj jeszcze raz')
        engine.runAndWait()
    elif int(QS) - int(MyNumber) > 3:
        engine.say('Moja liczba jest dużo większa \n spróbuj jeszcze raz')
        print('Moja liczba jest dużo większa \n spróbuj jeszcze raz')
        engine.runAndWait()

    
    elif int(QS) - int(MyNumber) < 3:
        engine.say('Moja liczba jest dużo mniejsza \n spróbuj jeszcze raz')
        print('Moja liczba jest mniejsza \n spróbuj jeszcze raz')
        engine.runAndWait()

print(Mytry(i))
if Female=="A":
    print ('Liczba którą miałam na myśli to \n'+  str(QS)+ ' \n zgadłaś w '+ str(Mytry(i)) + ' próbie')
    engine.say ('Liczba którą miałam na myśli to \n'+ str(QS)+ '\n zgadłaś w '+ str(Mytry(i)) + ' próbie')
    engine.runAndWait()
else:
    print ('Liczba którą miałam na myśli to \n'+  str(QS)+ ' \n zgadłeś w '+ str(Mytry(i)) + ' próbie')
    engine.say ('Liczba którą miałam na myśli to \n'+ str(QS)+ '\n zgadłeś w '+ str(Mytry(i)) + ' próbie')
    engine.runAndWait()









