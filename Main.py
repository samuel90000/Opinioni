def questionario():
    print("Benvenuto al questionario!")
    risposta = input("Preferisci pizza o pasta? ").lower()

    if risposta == "pizza":
        print("Ottima scelta!")
    elif risposta == "pasta":
        print("Anche la pasta Ã¨ una scelta deliziosa!")
    else:
        print("Scelta non valida. Per favore rispondi con 'pizza' o 'pasta'.")
        questionario()


questionario()
 
 