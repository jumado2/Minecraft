import threading
import time
import OracleBot
import InsultBot
import TNTBot

def main():
    # Crear un fil per a cada bot
    oracle_thread = threading.Thread(target=OracleBot.run, name="OracleBot")
    insult_thread = threading.Thread(target=InsultBot.run, name="InsultBot")
    tnt_thread = threading.Thread(target=TNTBot.run, name="TNTBot")
    
    #setattr(OracleBot, "mode", 1)       #Reflectiu
    #setattr(OracleBot, "mode", 2)       #Es pot fer d'aquesta manera, de moment esta fet que ho canvii el InsultBot, ja que tambe son "insults"
    
    
    # Arrencar el fil
    oracle_thread.start()
    insult_thread.start()
    tnt_thread.start()

    # Mantenir el programa viu
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Aturant el programa...")

if __name__ == "__main__":
    main()
