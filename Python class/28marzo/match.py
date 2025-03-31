comando = input("inserisci il comando: ")
match comando:
    case "start":
        print("Avvia la programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pasua":
        print("Programma in pausa.")
    case _:
        print("Comando non riconosciuto.")