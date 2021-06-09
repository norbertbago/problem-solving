def welcome_window():
    print("""

    Vitaj v hre Piskorky"
    -------------------------------------------------------
    Toto je hra s dvoma hracmi, kde vyhra iba ten najlepsi"

    Hracia plocha 3x3
    1. hrac je oznaceny symbolom \t "x"
    2. hrac je oznaceny symobol  \t "o" 
    """)

def start_game():

    user_input = "";
    while "no" or "yes" not in user_input:
        user_input = input("Chete zacat hru? (yes/no) ")
        user_input = user_input.lower()

        if "no" not in user_input and "yes" not in user_input:
            print("Prosim zadaj spravnu klavesnicu(yes/no)")
            
        if "yes" in user_input:
            return True
        if "no" in user_input:
            return False
    


  





