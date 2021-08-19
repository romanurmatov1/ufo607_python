import random

print("\n\t'Yuqori yoki Past o'yini!'")
ch_c = random.randrange(1, 11, 2)


def game():
    g1 = input("\n\tIltimos raqam tanlang:  ")
    g = g1.replace(" ","")

    if g == "1" or g == "1" or g == "2" or g == "3" or g == "4" or g == "5" or g == "6" or g == "7" or g == "8" or g == "9" or g == "10":
        if int(g) < ch_c:
            print("\n\tMag'lubiyat!\n\tSiz "+str(g)+" ni tanladingiz Raxmatjon "+str(ch_c)+" ni tanladi.")
            again()
        elif int(g) > ch_c:
            print("\n\tG'alaba!\n\tSiz "+str(g)+" ni tanladingiz Raxmatjon "+str(ch_c)+" ni tanladi.")
            again()
        else:
            print("\n\tDurrang!\n\tSiz "+str(g)+" ni tanladingiz Raxmatjon "+str(ch_c)+" ni tanladi.")
            again()
    else:
        xato()

def xato():
    print("\n\tNoto'g'ri tanlov!")
    game()

def again():
    a1 = input("\n\tYana o'ynaysizmi:\n\t\tHa - 0\n\t\tYo'q - 1\n\tIltimos tanlovingizni 0 va 1 bilan kiriting: ")
    a = a1.replace(" ","")

    if a == "0":
        game()
    elif a == "1":
        yuq()
    else:
        print("\n\tNoto'g'ri tanlov.")
        again()
def yuq():
    input("\n\tE'tiboringiz uchun raxmat. O'yinni Raxmatjon tuzdi!")
    yuq()



game()