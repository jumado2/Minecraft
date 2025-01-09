import threading
import time
import OracleBot
import InsultBot
import TNTBot
import AchievObs
import mcpi.minecraft as minecraft

'''
    # Crear un fil per a cada bot
oracle_thread = threading.Thread(target=OracleBot.run, name="OracleBot")
insult_thread = threading.Thread(target=InsultBot.run, name="InsultBot")
tnt_thread = threading.Thread(target=TNTBot.run, name="TNTBot")
achiev_thread = threading.Thread(target=AchievObs.run, name="AchievObs")
    
    #setattr(OracleBot, "mode", 1)       #Reflectiu
    #setattr(OracleBot, "mode", 2)       #Es pot fer d'aquesta manera, de moment esta fet que ho canvii el InsultBot, ja que tambe son "insults"
    # Arrencar el fil
oracle_thread.start()
insult_thread.start()
tnt_thread.start()
achiev_thread.start()
'''

# Connect to the Minecraft game
mc = minecraft.Minecraft.create()
sem = threading.Lock()


# Comú per a OracleBot i InsultBot i Tnt (Fan servir el xat)
def llegirXat():
    while True:
        with sem:
            input = mc.events.pollChatPosts()
        for i in input:
            if (input.casefold() == "tnt"):
                TNTBot.run(mc)
            elif (OracleBot.existent(i)):
                OracleBot.run(mc)
            else:
                InsultBot.run(mc)
        
    
def achiev():
    achievBot = AchievObs.AchievementBot(mc)
   # achievBot.__init__ (achievBot, mc)
    while True:
        with sem:
            achievBot.run()

xat_thread = threading.Thread(target=llegirXat)
achiev_thread = threading.Thread(target=achiev)

xat_thread.start()
achiev_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    with sem:
        mc.postToChat("Aturant programa...")
