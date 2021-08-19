import random

def game():
    ig1 = input("\nIltimos tanlang:\n\n   Tosh - 0\n   Qaychi - 1\n   Qog'oz - 2\n\nTanlovni 0, 1, 2 yordamida kiriting:  ")
    ig = ig1.replace(" ","")
    comp = random.randrange(3)
    if ig == "0" or ig == "1" or ig == "2":
        def dd():
            if ig == "0" and comp == 0:
                print("\nDurrang!\nSiz Toshni tanladingiz, Raxmatjon Toshni tanladi!")
                again()
            elif ig == "0" and comp == 1:
                print("\nSiz yutdingiz!\nSiz Toshni tanladingiz, Raxmatjon Qaychini tanladi!")
                again()
            elif ig == "0" and comp == 2:
                print("\nSiz yutqazdingiz!\nSiz Toshni tanladingiz, Raxmatjon Qog'ozni tanladi!")
                again()
            elif ig == "1" and comp == 0:
                print("\nSiz yutqazdingiz!\nSiz Qaychini tanladingiz, Raxmatjon Toshni tanladi!")
                again()
            elif ig == "1" and comp == 1:
                print("\nDurrang!\nSiz Qaychini tanladingiz, Raxmatjon Qaychini tanladi!")
                again()
            elif ig == "1" and comp == 2:
                print("\nSiz yutdingiz!\nSiz Qaychini tanladingiz, Raxmatjon Qog'ozni tanladi!")
                again()
            elif ig == "2" and comp == 0:
                print("\nSiz yutdingiz!\nSiz Qog'ozni tanladingiz, Raxmatjon Toshni tanladi!")
                again()
            elif ig == "2" and comp == 1:
                print("\nSiz yutqazdingiz!\nSiz Qog'ozni tanladingiz, Raxmatjon Qaychini tanladi!")
                again()
            elif ig == "2" and comp == 2:
                print("\nDurrang!\nSiz Qog'ozni tanladingiz, Rahmatjon Qog'ozni tanladi!")
                again()
        dd()
    else:
        xato()

def xato():
    print("\nNoto'g'ri tanlov!")
    game()

def again():
    ag1 = input("\nYana o'ynaysizmi!\n Ha - 0\n Yo'q - 1\nIltimos 0 va 1 orqali javob bering:  ")
    ag = ag1.replace(" ","")
    if ag == "0":
        game()
    elif ag == "1":
        yuq()
    else:
        print("\nNoto'g'ri tanlov!")
        again()


def yuq():
    input("\nE'tiboringiz uchun raxmat! O'yinni Raxmatjon tuzdi!")
    yuq()

game()



