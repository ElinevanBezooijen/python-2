'''Print welkomstboodschap
print de titel
kies een woord

herhaal steeds:
  tekengalg
  print even veel streepjes als er letters in het gekozen woord zitten
  vraag een letter
  verwerken letter: 
    check of de letter in het woord zit
  als juist: invullen bij streepjes. 
  als onjuist: invullen bij "onjuiste letters" en teken de galg verder
  totdat er te veel fouten gemaakt zijn of het woord compleet is

vraag of de speler het spel nog een keer wil spelen
als ja: speel het programa weer af
als nee: niets
'''
import random
from lijst import galgen
from lijst import lijst_woorden

def print_welkom():
    print("Welkom bij galgje!")
  
def kies_woord():
    global woord
    woord = random.choice(lijst_woorden)
  
def check_de_letter(gekozen_letter):
  global goede_invoer
  if (len(gekozen_letter)) == "1":
    goede_invoer = True
  if gekozen_letter in "abcdefghijklmnopqrstuvwxyz":
    goede_invoer = True
  if gekozen_letter not in juiste_letters:
    goede_invoer = True
  if gekozen_letter not in onjuiste_letters:
    goede_invoer = True
  else:
    goede_invoer = False
  return goede_invoer
  
def galg_streepjes_invoer():
  doorgaan = True 
  lengte = len(woord)
  streepjes = "_"*lengte
  beurten = 5
  global teller_galgen
  teller_galgen = 0
  global onjuiste_letters
  onjuiste_letters = ""
  global juiste_letters
  juiste_letters = ""
  print(streepjes)
  global gekozen_letter
  while doorgaan:
    gekozen_letter = input("Kies een letter: ")
    if check_de_letter(gekozen_letter) == True:
      if gekozen_letter in woord:
        print("Deze letter zit in het woord")
        juiste_letters = juiste_letters + gekozen_letter
        for i in range(lengte):
          if gekozen_letter == woord[i]:
            streepjes = streepjes[:i] + gekozen_letter + streepjes[i+1:] 
      else: 
        beurten -= 1
        teller_galgen += 1     
        print("Deze letter zit niet in het woord, je hebt nog", beurten, "beurt(en) over")  
        onjuiste_letters = onjuiste_letters + gekozen_letter

    elif check_de_letter(gekozen_letter) == False:
        print ("Deze invoer is niet mogelijk of al gebruikt.")
    print(galgen[teller_galgen])
    print(streepjes)
    print("De onjuiste letters:", onjuiste_letters)  
    if beurten <= 0:
      doorgaan = False
      print("Helaas, je hebt verloren. Het goede antwoord was: ", woord)
    if streepjes == woord:
      print("Gefeliciteerd! Je hebt gewonnen!")
      doorgaan = False
    if doorgaan == False: 
      opnieuw = input("Wil je het spel nog een keer spelen? ")
      if opnieuw.lower() == "ja":
        alle_functies()
        doorgaan = True
      else:
        doorgaan = False

def alle_functies():
  print_welkom()  
  print(galgen[0])
  kies_woord()
  galg_streepjes_invoer()
alle_functies()
