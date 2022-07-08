import os



print("Witam w krótkim teście politycznym. " + "Wersja: 0.2")
print()

print("Naciśnij Enter by rozpocząć test.")
input()
os.system("cls")

x = 0
y = 0

for que in range(1,9):
    file = open(str(que) + ".txt")
    for line in file.readlines():
        print(line.strip())
    file.close

    rpt = 0

    while rpt == 0:
        ans = input("Odpowiedź: ")
        #A#
        if ans == "A" and que in range(1,5):
            x += 25
            y += 0
            rpt += 1
            os.system("cls")
        elif ans == "A" and que in range(5,9):
            x += 0
            y += 25
            rpt += 1
            os.system("cls")
        #B#
        elif ans == "B" and que in range(1,5):
            x += -25
            y += 0
            rpt += 1
            os.system("cls")
        elif ans == "B" and que in range(5,9):
            x += 0
            y += -25
            rpt += 1
            os.system("cls")  
        #C#
        elif ans == "C":
            rpt += 1
            os.system("cls")



os.system("cls")

print("Skala x100.")
print()
print("Oś ekonomiczna: " + str(x))
print("Oś obyczajowa: " + str(y))
print()

#Centryzm#
if x in range(-25, 26) and y in range(-25, 26):
    print("Centryzm")
#Wzdłuż osi y#
elif x in range(-25, 26) and y in range(50, 76):
    print("Nacjonalizm")
elif x in range(-25, 26) and y in range(-75, -49):
    print("Liberalizm")
elif x in range(-25, 26) and y == 100:
    print("Faszyzm")
elif x in range(-25, 26) and y == -100:
    print("Syndykalizm")
#Wzdłuż osi x#
elif x in range(50, 76) and y in range(-25, 26):
    print("Klasyczny liberalizm")
elif x in range(-75, -49) and y in range(-25, 26):
    print("Socjaldemokracja")
elif x == 100 and y in range(-25, 26):
    print("Neoliberatrianizm")
elif x == -100 and y in range(-25, 26):
    print("Socjalizm")
#Prawy dolny#
elif x in range(50, 76) and y in range(-75, -49):
    print("Libertarianizm")
elif x in range(50, 76) and y == -100:
    print("Anarchizm")
elif x == 100 and y in range(-75, -49):
    print("Minarchizm")
elif x == 100 and y == -100:
    print("Anarchokapitalizm")
#Lewy dolny#
elif x in range(-75, -49) and y in range(-75, -49):
    print("Socjal-libertarianizm")
elif x in range(-75, -49) and y == -100:
    print("Anarchokolektywizm")
elif x == -100 and y in range(-75, -49):
    print("Anarchosocjalizm")
elif x == -100 and y == -100:
    print("Anarchokomunizm")
#Lewy gorny#
elif x in range(-75, -49) and y in range(50, 76):
    print("Etatyzm")
elif x in range(-75, -49) and y == 100:
    print("Narodowy socjalizm")
elif x == -100 and y in range(50, 76):
    print("Leninizm")
elif x == -100 and y == 100:
    print("Komunizm")
#Prawy gorny#
elif x in range(50, 76) and y in range(50, 76):
    print("Neokonserwatyzm")
elif x in range(50, 76) and y == 100:
    print("Nacjonalizm wolnorynkowy")
elif x == 100 and y in range(50, 76):
    print("Paleolibertarianizm")
elif x == 100 and y == 100:
    print("Kapitalizm dyktatorski")

print()
input("Zakończ program Enterem.")


