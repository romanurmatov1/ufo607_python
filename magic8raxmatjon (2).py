import random
import string

solutions = {
    1 : "It is Certain.",
    2 : "It is decidedly so.",
    3 : "Without a doubt.",
    4 : "Yes definitely.",
    5 : "As I see it, yes.",
    6 : "Most likely.",
    7 : "Outlook good.",
    8 : "Yes.",
    9 : "Signs point to yes.",
    10 : "Reply hazy, try again.",
    11 : "Ask again later.",
    12 : "Better not tell you now.",
    13 : "Cannot predict now.",
    14 : "Concentrate and ask again.",
    15 : "Don't count on it.",
    16 : "My replys is no",
    17 : "My sources say no",
    18 : "You may rely on it.",
    19 : "Outlook not so good.",
    20 : "Very doubtfull."
}

err = {
    1 : "\t---You must use a question mark(?).---",
    2 : "\t---Incorred character entered.---",
    3 : "\t---The first letter must be an uppercase letter.---",
    4 : "\t---You can't use numbers and you must use a question mark(?)---",
    5 : "\t---All letters must be lowercase(except the first letter).---",
    6 : "\t---The count of words must be more than 3.---"
}
othch = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", ":", '"', "<", ">", "|", "-", "=", "[", "]", ";", "'", ",", ".", "/", "`", "~"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
upl = ["A", "B", "C", "Q", "W", "R", "T", "Y", "U", "I", "O", "P", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "V", "N", "M"]
upl1 = ["A", "B", "C", "Q", "W", "R", "T", "Y", "U", "I", "O", "P", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "V", "N", "M", "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]





r = random.randrange(1, 21, 1)

def game():
    question = input("\n\tEnter your question: ")
    qlen = sum([i.strip(string.punctuation).isalpha() for i in question.split()])
    numm1 = question[0:-1]
    numm2 = numm1.replace(" ","")



    if qlen < 3:
        print(err[6])
        game()
    elif str(question[-1:]) != "?":
        print(err[1])
        game()
    elif str(othch) in question:
        print(err[2])
        game()
    elif question[0:1].islower():
        print(err[3])
        game()

    def lcl():
        for roma1 in question[1:-1]:
            if roma1 in upl:
                print(err[5])
                game()

    def num():
        if numm2.isalpha() == False:
            print(err[4])
            game()
    num()
    lcl()

    def solut():
        print("\n\t  Answer: "+solutions[r])
    solut()

    def again():
        ag1 = input("\n\tWill you play again?\n\n\t    Yes - 0\n\t    No - 1\n\n\tYou can select 0 or 1: ")
        ag = ag1.replace(" ", "")

        def yuq():
            input("\n\tThank you for your attention! The game was created by Rakhmatjon:)")
            yuq()

        if str(ag) == "0":
            game()
        elif str(ag) == "1":
            yuq()
        else:
            print("\n\tYou can just select 0 or 1")
            again()
    again()
game()