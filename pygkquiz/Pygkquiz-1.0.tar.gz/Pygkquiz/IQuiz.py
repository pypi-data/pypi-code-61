
# this is a General Knowledge quiz Game...
# Designed and Created By Ash bhatia...

quiz_key = [
  {
    "A": "Fructose",
    "B": "Sulphuric Acid",
    "C": "Platinum",
    "D": "7.5",
    "E": "Nitrogen"
  },
  {
    "A": "Shahjhan",
    "B": "Herodotus",
    "C": "1757",
    "D": "Humayun",
    "E": "323"
  },
  {
    "A": "Asia",
    "B": "Lucknow",
    "C": "Kangchenjunga",
    "D": "8586",
    "E": "Michigan Huron"
  },
  {
    "A": "June 21",
    "B": "United Kingdom",
    "C": "G Washington",
    "D": "Alexander Fleming",
    "E": "Alfred Nobel"
  }
]

def gkquiz():
    options = 0
    positive_marking = 1
    negative_marking = 0.25
    total_marks = 0
    science_marks = 0
    history_marks = 0
    geography_marks = 0
    general_aware_marks = 0
    name = ""
    science_started = False
    history_started = False
    geography_started = False
    General_awareness_started = False

    
    print("\033[38m".center(100, "-"))
    print("\033[38m".center(100, "-"))
    print("Fill your personal details here".center(100).upper())
    name = input("Name :: ".center(10).upper()).upper()
    quiz_option = ["Science", "History",
                   "Geography", "General Awareness", "Exit"]
    try:
        while True:
            print("\033[38m".center(100, "-"))
            print("\033[38m".center(100, "-"))
            print("GENERAL KNOWLEDGE QUIZ".center(100).upper())
            print(f"Welcome : \033[31m {name}\033[37m".rjust(100))
            print("""
Press 1 - Science quiz.
Press 2 - History quiz
Press 3 - Geography quiz
Press 4 - General awareness quiz
Press 5 - Exit\n""".title())
            options = int(input("Enter your option Here : ".upper())).__abs__()
            if options == 1:
                if science_started:
                    print("\033[35m Science Quiz already taken...", "\033[37m")
                else:
                    science_started = True
                    print(
                        f"\nYou have selected \033[34m{quiz_option[0].upper()} QUIZ :", "\033[37m")
                    # Question No. 1
                    science_query_first = input("""
Q1. Which one is the sweetest sugar ?
A - Sucrose
B - Maltose
C - Fructose
D - Lactose\n>> """).title()
                    if science_query_first in quiz_key[0].values():
                        print(
                            f"\033[38m {science_query_first} \033[36m is the Correct Answer", "\033[37m")
                        science_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {science_query_first} \033[36m is the Wrong Answer", "\033[37m")
                        science_marks -= negative_marking

                    # Question No. 2
                    science_query_second = input("""
Q2. Which one is the king of all chemical ?
A - Sulphuric Acid
B - Hydrochloric Acid
C - lactic Acid
D - Nitric Acid\n>> """).title()
                    if science_query_second in quiz_key[0].values():
                        print(
                            f"\033[38m {science_query_second} \033[36m is the Correct Answer", "\033[37m")
                        science_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {science_query_second} \033[36m is the Wrong Answer", "\033[37m")
                        science_marks -= negative_marking
                    # Question No. 3
                    science_query_third = input("""
Q3. Which one is known as 'White Gold' ?
A - Gold
B - Platinum
C - Silver
D - Bronze\n>> """).title()
                    if science_query_third in quiz_key[0].values():
                        print(
                            f"\033[38m {science_query_third} \033[36m is the Correct Answer", "\033[37m")
                        science_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {science_query_third} \033[36m is the Wrong Answer", "\033[37m")
                        science_marks -= negative_marking
                    # Question No. 4
                    science_query_fourth = input("""
Q4. PH Value of the Blood is ?
A - 6.0
B - 7.0
C - 7.5
D - 5.5\n>> """).title()
                    if science_query_fourth in quiz_key[0].values():
                        print(
                            f"\033[38m {science_query_fourth} \033[36m is the Correct Answer", "\033[37m")
                        science_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {science_query_fourth} \033[36m is the Wrong Answer", "\033[37m")
                        science_marks -= negative_marking

                    # Question No. 5
                    science_query_fifth = input("""
Q5. Which gas is use as Preservative ?
A - Methane
B - Butane
C - Oxygen
D - Nitrogen\n>> """).title()
                    if science_query_fifth in quiz_key[0].values():
                        print(
                            f"\033[38m {science_query_fifth} \033[36m is the Correct Answer", "\033[37m")
                        science_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {science_query_fifth} \033[36m is the Wrong Answer", "\033[37m")
                        science_marks -= negative_marking
                print("\nDo you want to continue or not!")

                main_quiz_continue = input(
                    "Press (Y) - Yes or (N) - No : ").upper()

                if main_quiz_continue == 'Y':
                    continue
                elif main_quiz_continue == 'N':
                    print(
                        f"\nTotal Marks in Science is :\033[33m {science_marks} Marks", "\033[37m")
                    break
                else:
                    print("\033[31mYou have entered wrong input", "\033[37m")
            elif options == 2:
                if history_started:
                    print("\033[35m History Quiz already taken...", "\033[37m")
                else:
                    history_started = True
                    print(
                        f"\nYou have selected \033[34m{quiz_option[1].upper()} QUIZ :", "\033[37m")

                    # Question No. 1
                    history_query_first = input("""
Q1. Who built the Taj Mahal?
A - Noorjhan
B - Shahjhan
C - Akbar
D - Bhadhur Shah Jaffar\n>> """).title()
                    if history_query_first in quiz_key[1].values():
                        print(
                            f"\033[38m {history_query_first} \033[36m is the Correct Answer", "\033[37m")
                        history_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {history_query_first} \033[36m is the Wrong Answer", "\033[37m")
                        history_marks -= negative_marking

                    # Question No. 2
                    history_query_second = input("""
Q2. Who was the founder of History ?
A - Aristotle
B - Herodotus
C - Newton
D - Coloumbs \n>> """).title()
                    if history_query_second in quiz_key[1].values():
                        print(
                            f"\033[38m {history_query_second} \033[36m is the Correct Answer", "\033[37m")
                        history_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {history_query_second} \033[36m is the Wrong Answer", "\033[37m")
                        history_marks -= negative_marking
                    # Question No. 3
                    history_query_third = input("""
Q3. Battle of Plassey was fought in which year?
A - 1684
B - 1498
C - 1757
D - 1857\n>> """).title()
                    if history_query_third in quiz_key[1].values():
                        print(
                            f"\033[38m {history_query_third} \033[36m is the Correct Answer", "\033[37m")
                        history_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {history_query_third} \033[36m is the Wrong Answer", "\033[37m")
                        history_marks -= negative_marking
                    # Question No. 4
                    history_query_fourth = input("""
Q4. Which mughal king died in his library due to skipped from ladder ?
A - Jahangir
B - Babar
C - Humayun
D - Akbar\n>> """).title()
                    if history_query_fourth in quiz_key[1].values():
                        print(
                            f"\033[38m {history_query_fourth} \033[36m is the Correct Answer", "\033[37m")
                        history_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {history_query_fourth} \033[36m is the Wrong Answer", "\033[37m")
                        history_marks -= negative_marking
                    # Question No. 5
                    history_query_fifth = input("""
Q5. When was The Great Alexander came in India (B.C) ?
A - 236
B - 323
C - 326
D - 330\n>> """).title()
                    if history_query_fifth in quiz_key[1].values():
                        print(
                            f"\033[38m {history_query_fifth} \033[36m is the Correct Answer", "\033[37m")
                        history_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {history_query_fifth} \033[36m is the Wrong Answer", "\033[37m")
                        history_marks -= negative_marking
                print("\nDo you want to continue or not!")
                main_quiz_continue = input(
                    "Press (Y) - Yes or (N) - No : ").upper()
                if main_quiz_continue == 'Y':
                    continue
                elif main_quiz_continue == 'N':
                    print(
                        f"Total Marks in history is : \033[33m{history_marks} Marks", "\033[37m")
                    break
                else:
                    print("\033[31m You have entered wrong input", "\033[31m")
            elif options == 3:
                if geography_started:
                    print(
                        "\033[35m Geography Quiz already taken...", "\033[37m")
                else:
                    geography_started = True
                    print(
                        f"\nYou have selected \033[34m {quiz_option[2]} QUIZ :", "\033[37m")

                    # Question No. 1
                    geography_query_first = input("""
Q1. Which one is the largest continent in the world ?
A - Australia
B - Zealandia
C - Asia
D - Africa\n>> """).title()
                    if geography_query_first in quiz_key[2].values():
                        print(
                            f"{geography_query_first} \033[36m is the Correct Answer", "\033[37m")
                        geography_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {geography_query_first} \033[36m is the Wrong Answer", "\033[37m")
                        geography_marks -= negative_marking

                    # Question No. 2
                    geography_query_second = input("""
Q2. Which City is located on the Bank of 'Gomati River' ?
A - Delhi
B - Patna
C - Kanpur
D - Lucknow\n>> """).title()
                    if geography_query_second in quiz_key[2].values():
                        print(
                            f"{geography_query_second} \033[36m is the Correct Answer", "\033[37m")
                        geography_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {geography_query_second} \033[36m is the Wrong Answer", "\033[37m")
                        geography_marks -= negative_marking

                    # Question No. 3
                    geography_query_third = input("""
Q3. Which one is the India's highest mountain peak ?
A - Nanda
B - Kangchenjunga
C - Nanga
D - Shilla\n>> """).title()

                    if geography_query_third in quiz_key[2].values():
                        print(
                            f"\033[38m {geography_query_third} \033[36m is the Correct Answer", "\033[37m")
                        geography_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {geography_query_third} \033[36m is the Wrong Answer", "\033[37m")
                    geography_marks -= negative_marking

                # Question No. 4

                    geography_query_fourth = input("""
Q4. Height of 'Kangchenjunga Peak' in m(meter) is ?
A - 7026
B - 6638
C - 8848
D - 8586\n>> """).title()
                    if geography_query_fourth in quiz_key[2].values():
                        print(
                            f"\033[38m {geography_query_fourth} \033[36m is the Correct Answer", "\033[37m")
                        geography_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {geography_query_fourth} \033[36m is the Wrong Answer", "\033[37m")
                        geography_marks -= negative_marking
                    # Question No. 5
                    geography_query_fifth = input("""
Q5. Which is the largest fresh water lake in the world ?
A - Michigan Huron
B - Superior
C - Baikal
D - Poyang\n>> """).title()
                    if geography_query_fifth in quiz_key[2].values():
                        print(
                            f"\033[38m {geography_query_fifth} \033[36m is the Correct Answer", "\033[37m")
                        geography_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {geography_query_fifth} \033[36m is the Wrong Answer", "\033[37m")
                        geography_marks -= negative_marking

                print("\nDo you want to continue or not!")

                main_quiz_continue = input(
                    "Press (Y) - Yes or (N) - No : ").upper()
                if main_quiz_continue == 'Y':
                    continue
                elif main_quiz_continue == 'N':
                    print(
                        f"\nTotal Marks in geography is : \033[33m{geography_marks} Marks", "\033[37m")
                    break
                else:
                    print("\033[31mYou have entered wrong input", "\033[37m")

            # General Awareness Quiz
            elif options == 4:
                if General_awareness_started:
                    print("\033[35m General Quiz already taken...", "\033[37m")
                else:
                    General_awareness_started = True
                    print(
                        f"\nYou have selected \033[34m{quiz_option[3].upper()} QUIZ:", "\033[37m")

                    # Question No. 1
                    general_awareness_query_first = input("""
Q1. When is the International Yoga Day celebrated ?
A June 21
B March 21
C April 22
D May 31\n>> """).title()
                    if general_awareness_query_first in quiz_key[3].values():
                        print(
                            f"\033[38m {general_awareness_query_first} \033[36m is the Correct Answer", "\033[37m")
                        general_aware_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {general_awareness_query_first} \033[36m is the Wrong Answer", "\033[37m")
                        general_aware_marks -= negative_marking

                    # Question No. 2
                    general_awareness_query_second = input("""
Q2. River Thames is flows in which country ?
A - USA
B - United Kingdom
C - India
D - Africa \n>> """).title()
                    if general_awareness_query_second in quiz_key[3].values():
                        print(
                            f"\033[38m {general_awareness_query_second} \033[36m is the Correct Answer", "\033[37m")
                        general_aware_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {general_awareness_query_second} \033[36m is the Wrong Answer", "\033[37m")
                        general_aware_marks -= negative_marking
                    # Question No. 3
                    general_awareness_query_third = input("""
Q3. Who was the first President of USA ?
A - G Washington
B - F Roosevelt
C - Abraham Linclon
D - Jf Kennedy\n>> """).title()
                    if general_awareness_query_third in quiz_key[3].values():
                        print(
                            f"\033[38m {general_awareness_query_third} \033[36m is the Correct Answer", "\033[37m")
                        general_aware_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {general_awareness_query_third} \033[36m is the Wrong Answer", "\033[37m")
                        general_aware_marks -= negative_marking
                    # Question No. 4
                    general_awareness_query_fourth = input("""
Q4. Who invented penicillin ?
A - JJ.Thomson
B - Pablo DT Valenzuela
C - Alexander Fleming
D - Edward Jenner\n>> """).title()
                    if general_awareness_query_fourth in quiz_key[3].values():
                        print(
                            f"\033[38m {general_awareness_query_fourth} \033[36m is the Correct Answer", "\033[37m")
                        general_aware_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {general_awareness_query_fourth} \033[36m is the Wrong Answer", "\033[37m")
                        general_aware_marks -= negative_marking
                    # Question No. 5
                    general_awareness_query_fifth = input("""
Q5. Who started Noble prize Award ?
A - Ernest Rutherford
B - W.Conrad Rontgen
C - Henry Dunant
D - Alfred Nobel\n>> """).title()
                    if general_awareness_query_fifth in quiz_key[3].values():
                        print(
                            f"\033[38m {general_awareness_query_fifth} \033[36m is the Correct Answer", "\033[37m")
                        general_aware_marks += positive_marking
                    else:
                        print(
                            f"\033[31m {general_awareness_query_fifth} \033[36m is the Wrong Answer", "\033[37m")
                        general_aware_marks -= negative_marking

                print("\nDo you want to continue or not!")

                main_quiz_continue = input(
                    "Press (Y) - Yes or (N) - No : ").upper()
                if main_quiz_continue == 'Y':
                    continue
                elif main_quiz_continue == 'N':
                    print(
                        f"\033[33mTotal Marks in General_awareness is : {general_aware_marks} Marks")
                    break
                else:
                    print("\033[31mYou have entered wrong input", "\033[37m")

            elif options == 5:
                print(
                    f"\n\033[35mYou've pressed option \033[33m{options}", "\033[35m")
                print("You are now Exit...", "\033[37m")
                break
            else:
                print(
                    "\n\033[31mYou have entered wrong input try again..\n", "\033[37m")
        print("".center(50, "^"))
        print("FINAL REPORT CARD".center(50))

        print("\033[37m", f"""
Marks in Science           :  {science_marks} points
Marks in History           :  {history_marks} points
Marks in Geography         :  {geography_marks} points
Marks in General Awareness :  {general_aware_marks} points""")
        total_marks = science_marks + history_marks + \
            geography_marks + general_aware_marks
        print(f"""\033[35m---------------------------------------------
Total Marks                :  {total_marks}/20 points
---------------------------------------------\033[37m""")
        if total_marks >= 17:
            print(
                f"\033[33m{name.upper()} \033[37mYOUR GRADE IS \033[33m'A'", "\033[37m")
        elif total_marks >= 13 and total_marks < 17:
            print(
                f"\033[33m{name.upper()} \033[37mYOUR GRADE IS \033[33m'B'", "\033[37m")
        elif total_marks >= 9 and total_marks < 13:
            print(
                f"\033[33m{name.upper()} \033[37mYOUR GRADE IS \033[33m'C'", "\033[37m")
        elif total_marks >= 5 and total_marks < 9:
            print(
                f"\033[33m{name.upper()} \033[37mYOUR GRADE IS \033[33m'D'", "\033[37m")
        elif total_marks >= 1 and total_marks < 5:
            print(
                f"\033[33m{name.upper()} \033[37mYOUR GRADE IS \033[33m'E'", "\033[37m")
        else:
            print(
                f"\033[31m{name.upper()} \033[37mYOUR ARE \033[31m'FAIL'", "\033[37m")

    except Exception:
        print("\033[31mYou have entered wrong option")
        print('\033[37mEnter digits between (1 to 5) only')
        gkquiz()


gkquiz()
