import random

print("\n\tTanlovingiz orqali 1 dan 10 gacah bo'lgan tasodifiy raqamni toping!")

def menu():
    m1 = input("\n\tQaysi birini o'ynaysiz:\n\n\t Haqqoniy - 0\n\t (Hint) - 1\n\n\tIltimos 0 va 1 orqali javob bering: ")
    m = m1.replace(" ","")
    if m == "0":
        def game():
            a = ""
            r = random.randrange(1, 11, 1)
            imk = 0
            limit = 5
            ok = False
            while a != str(r) and not (ok):
                if imk == 0:
                    a1 = input("\n\tSizning " + str(imk + 1) + "-imkoniyatingiz" + "\n\tTanlovingizni kiriting: ")
                    a = a1.replace(" ", "")
                    imk += 1
                    if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6" or a == "7" or a == "8" or a == "9" or a == "10":
                        imk = imk + 1
                    else:
                        def xk():
                            print("\n\tNoto'g'ri tanlov!")

                            def again():
                                ag1 = input(
                                    "\n\tYana o'ynaysizmi:\n\t Ha - 0\n\t Yo'q - 1\n\t Menu - 2\n\tIltimos 0, 1 va 2 orqali javob bering: ")
                                agg1 = ag1.replace(" ", "")
                                if agg1 == "0":
                                    game()
                                elif agg1 == "1":
                                    def yuq():
                                        input("E'tiboringiz uchun raxmat. O'yinni Raxmatjon tuzdi!")

                                    yuq()
                                elif agg1 == "2":
                                    menu()
                                else:
                                    print("\n\tNoto'g'ri tanlov!")
                                    again()

                            again()

                        xk()
                elif imk <= limit:
                    a1 = input("\n\tTopa olmadingiz\n\n\tSizning " + str(
                        imk) + "-imkoniyatingiz" + "\n\tTanlovingizni kiriting: ")
                    a = a1.replace(" ", "")
                    if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6" or a == "7" or a == "8" or a == "9" or a == "10":
                        imk += 1
                    else:
                        def xk1():
                            print("\n\tNoto'g'ri tanlov!")

                            def again():
                                ag1 = input(
                                    "\n\tYana o'ynaysizmi:\n\t Ha - 0\n\t Yo'q - 1\n\t Menu - 2\n\tIltimos 0, 1 va 2 orqali javob bering: ")
                                agg1 = ag1.replace(" ", "")
                                if agg1 == "0":
                                    game()
                                elif agg1 == "1":
                                    def yuq():
                                        input("E'tiboringiz uchun raxmat. O'yinni Raxmatjon tuzdi!")

                                    yuq()
                                elif agg1 == "2":
                                    menu()
                                else:
                                    print("\n\tNoto'g'ri tanlov!")
                                    again()

                            again()

                        xk1()
                else:
                    ok = True
            if ok:
                print("\n\tImkoniyatingiz tugadi! Siz Yutqazdingiz!")

                def again():
                    ag1 = input("\n\tYana o'ynaysizmi:\n\t Ha - 0\n\t Yo'q - 1\n\t Menu - 2\n\tIltimos 0, 1 va 2 orqali javob bering: ")
                    agg1 = ag1.replace(" ", "")
                    if agg1 == "0":
                        game()
                    elif agg1 == "1":
                        def yuq():
                            input("E'tiboringiz uchun raxmat. O'yinni Raxmatjon tuzdi!")
                        yuq()
                    elif agg1 == "2":
                        menu()
                    else:
                        print("\n\tNoto'g'ri tanlov!")
                        again()

                again()

            else:
                print("\n\tSiz yutdingiz!")

                def again():
                    ag1 = input("\n\tYana o'ynaysizmi:\n\t Ha - 0\n\t Yo'q - 1\n\t Menu - 2\n\tIltimos 0, 1 va 2 orqali javob bering: ")
                    agg1 = ag1.replace(" ", "")
                    if agg1 == "0":
                        game()
                    elif agg1 == "1":
                        def yuq():
                            input("E'tiboringiz uchun raxmat. O'yinni Raxmatjon tuzdi!")
                            yuq()
                        yuq()
                    elif agg1 == "2":
                        menu()
                    else:
                        print("\n\tNoto'g'ri tanlov!")
                        again()

                again()

        game()
    elif m == "1":
        def game1():
            a = ""
            r = random.randrange(1, 11, 1)
            imk = 0
            limit = 5
            ok = False
            while a != str(r) and not (ok):
                if imk == 0:
                    a1 = input("\n\tSizning " + str(imk + 1) + "-imkoniyatingiz" + "\n\tTanlovingizni kiriting(Hint" + str(
                        r) + "): ")
                    a = a1.replace(" ", "")
                    imk += 1
                    if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6" or a == "7" or a == "8" or a == "9" or a == "10":
                        imk = imk + 1
                    else:
                        def xk():
                            print("\n\tNoto'g'ri tanlov!")

                            def again():
                                ag1 = input(
                                    "\n\tYana o'ynaysizmi:\n\t Ha - 0\n\t Yo'q - 1\n\t Menu - 2\n\tIltimos 0, 1 va 2 orqali javob bering: ")
                                agg1 = ag1.replace(" ", "")
                                if agg1 == "0":
                                    game1()
                                elif agg1 == "1":
                                    def yuq():
                                        input("E'tiboringiz uchun raxmat. O'yinni Raxmatjon tuzdi!")

                                    yuq()
                                elif agg1 == "2":
                                    menu()
                                else:
                                    print("\n\tNoto'g'ri tanlov!")
                                    again()

                            again()

                        xk()
                elif imk <= limit:
                    a1 = input("\n\tTopa olmadingiz\n\n\tSizning " + str(
                        imk) + "-imkoniyatingiz" + "\n\tTanlovingizni kiriting(Hint" + str(r) + "): ")
                    a = a1.replace(" ", "")
                    if a == "1" or a == "2" or a == "3" or a == "4" or a == "5" or a == "6" or a == "7" or a == "8" or a == "9" or a == "10":
                        imk += 1
                    else:
                        def xk1():
                            print("\n\tNoto'g'ri tanlov!")

                            def again():
                                ag1 = input(
                                    "\n\tYana o'ynaysizmi:\n\t Ha - 0\n\t Yo'q - 1\n\t Menu - 2\n\tIltimos 0, 1 va 2 orqali javob bering: ")
                                agg1 = ag1.replace(" ", "")
                                if agg1 == "0":
                                    game1()
                                elif agg1 == "1":
                                    def yuq():
                                        input("E'tiboringiz uchun raxmat. O'yinni Raxmatjon tuzdi!")

                                    yuq()
                                elif agg1 == "2":
                                    menu()
                                else:
                                    print("\n\tNoto'g'ri tanlov!")
                                    again()

                            again()

                        xk1()
                else:
                    ok = True
            if ok:
                print("\n\tImkoniyatingiz tugadi! Siz Yutqazdingiz!")

                def again():
                    ag1 = input("\n\tYana o'ynaysizmi:\n\t Ha - 0\n\t Yo'q - 1\n\t Menu - 2\n\tIltimos 0, 1 va 2 orqali javob bering: ")
                    agg1 = ag1.replace(" ", "")
                    if agg1 == "0":
                        game1()
                    elif agg1 == "1":
                        def yuq():
                            input("E'tiboringiz uchun raxmat. O'yinni Raxmatjon tuzdi!")

                        yuq()
                    elif agg1 == "2":
                        menu()
                    else:
                        print("\n\tNoto'g'ri tanlov!")
                        again()

                again()

            else:
                print("\n\tSiz yutdingiz!")

                def again():
                    ag1 = input("\n\tYana o'ynaysizmi:\n\t Ha - 0\n\t Yo'q - 1\n\t Menu - 2\n\tIltimos 0, 1 va 2 orqali javob bering: ")
                    agg1 = ag1.replace(" ", "")
                    if agg1 == "0":
                        game1()
                    elif agg1 == "1":
                        def yuq():
                            input("E'tiboringiz uchun raxmat. O'yinni Raxmatjon tuzdi!")
                            yuq()

                        yuq()
                    elif agg1 == "2":
                        menu()
                    else:
                        print("\n\tNoto'g'ri tanlov!")
                        again()

                again()

        game1()
    else:
        print("\n\tNoto'g'ri tanlov!")
        menu()
menu()








