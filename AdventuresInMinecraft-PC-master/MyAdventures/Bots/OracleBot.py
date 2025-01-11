import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
 # Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import random

mode = 1
preestablertes = {"Com es fa una taula de crafteig?", "Com domesticar un llop?",
        "Com es fabrica una espasa?",
        "Què és el Nether?",
        "Com trobo diamants?",
        "Com es fa un portal al Nether?", "Com es crafteja un llit?",
        "Com es fa un encenedor?"}

def existent(input):
    if input in preestablertes:
        return True
    else:
        return False

def run(m, input):
    # Connect to the Minecraft game
    mc = m
    #pos = mc.player.getTilePos()
    #mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)

    # Preguntes i respostes predefinides
    faq1 = {
        "Com es fa una taula de crafteig?": "Necessites 4 blocs de fusta processada. Col·loca'ls en un quadrat 2x2 al teu inventari.",
        "Com domesticar un llop?": "Dóna-li ossos fins que apareguin cors. Ara serà el teu aliat!",
        "Com es fabrica una espasa?": "Necessites 1 pal i 2 materials (fusta, pedra, ferro, or o diamant). Col·loca'ls en forma vertical a la taula de crafteig.",
        "Què és el Nether?": "El Nether és una dimensió infernal plena de monstres i recursos únics. Pots accedir-hi mitjançant un portal fet d'obsidiana.",
        "Com trobo diamants?": "Els diamants es troben a les capes baixes del món, normalment entre la 5 i la 12. Utilitza un pic de ferro o millor per extreure'ls.",
        "Com es fa un portal al Nether?": "Necessites 10 blocs d'obsidiana i un encenedor. Fes un marc rectangular (4 d'alt, 5 d'ample) i encén-lo.",
        "Com es crafteja un llit?": "Necessites 3 blocs de llana i 3 blocs de fusta. Col·loca'ls en una fila a la taula de crafteig.",
        "Com es fa un encenedor?": "Necessites 1 barra de ferro i 1 fragment de sílex. Col·loca'ls diagonalment a la taula de crafteig."
    }
    
    faq2 = {
        "Com es fa una taula de crafteig?": "De debò no saps això? Només agafa 4 blocs de fusta processada i posa'ls en un quadrat 2x2. Ni que fos física quàntica!",
        "Com domesticar un llop?": "Ah, vols un gosset virtual? Dóna-li ossos fins que surtin cors. Però no esperis que et porti el diari, eh!",
        "Com es fabrica una espasa?": "Oh, el gran guerrer vol una espasa! Necessites 1 pal i 2 materials. Col·loca'ls en vertical, com si fos un Lego per a adults.",
        "Què és el Nether?": "El Nether és bàsicament l'infern. Si no et perds o et maten, serà tot un miracle.",
        "Com trobo diamants?": "Ah, el somni de tothom. Baixa fins a les capes 5-12 i excava. Bona sort, perquè segur que et sortirà lava abans de trobar-ne.",
        "Com es fa un portal al Nether?": "Necessites 10 blocs d'obsidiana. Però primer aconsegueix diamant per fer un pic. Ah, espera... no tens diamants? Això serà llarg.",
        "Com es crafteja un llit?": "Per descansar d'excavar com un boig, necessites 3 blocs de llana i 3 de fusta. Fes una fila i voilà! Però ves amb compte on dorms al Nether, que explota.",
        "Com es fa un encenedor?": "Encara no has trobat sílex? Només necessites un fragment de sílex i una barra de ferro. Col·loca'ls diagonalment, i ja pots cremar coses. Molt madur."
    }   

    
    if mode == 1: faq = faq1
    elif mode == 2: faq = faq2
    else: mc.postToChat(f"OracleBot: no conec aquest mode de xat :(")
    # Bucle principal
    #while True:
        # Recuperar missatges nous del xat
        #chat_messages = mc.events.pollChatPosts()

        #for message in chat_messages:
        #    preguntes = message.message  

        # Respondre si la pregunta està a la llista
        #if input in faq:
    response = faq[input]  # Obtenir la resposta adient
    mc.postToChat(f"OracleBot: {response}")
        
