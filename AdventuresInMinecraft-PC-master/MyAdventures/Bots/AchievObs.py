import mcpi.minecraft as minecraft
import mcpi.block as block

# Variables globals per mantenir l'estat del bot
mc = minecraft.Minecraft.create()
block_count = {}
logro_threshold = 100  # Nombre de blocs necessaris per a logro

def on_block_placed(event):
    """
    Funció que es crida quan es col·loca un bloc.
    """
    global block_count

    pos = event.pos
    block_type = event.block  # Assumeix que l'esdeveniment conté block.type

    # Actualitzar el recompte del bloc
    if block_type not in block_count:
        block_count[block_type] = 0
    block_count[block_type] += 1

    # Comprovar si s'ha arribat al minim
    if block_count[block_type] == logro_threshold:
        mc.postToChat(f"Felicitats! Has col·locat {logro_threshold} blocs del tipus {block_type}. 🎉")
        # Reiniciar el recompte del bloc
        block_count[block_type] = 0

def run():
    """
    Iniciar el bot i registrar l'observador.
    """
    mc.postToChat("AchievementBot està actiu! Aconsegueix 100 blocs per un logro!")

    # Registrar l'observador
    # Això depèn del suport de l'API o de la capa d'esdeveniments.
    #mc.registerEventHandler("blockPlaced", on_block_placed)

    # Mantenir el bot actiu (si cal)
    try:
        while True:
            pass  # No cal fer res més, l'observer s'encarrega de tot
    except KeyboardInterrupt:
        print("AchievementBot s'ha aturat.")
