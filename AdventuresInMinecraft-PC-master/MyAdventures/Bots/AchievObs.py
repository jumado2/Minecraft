import mcpi.minecraft as minecraft
import mcpi.block as block

hit_count = {}
logro_threshold = 5  # Nombre de blocs necessaris per a logro
    
# Classe per encapsular l'observador del bot
def run(m, event):
    mc = m
    # Funció que es crida quan es col·loca un bloc.
    pos = event.pos
    block_type = event.block

    # Actualitzar el recompte del bloc
    if block_type not in hit_count:
        hit_count[block_type] = 0
    hit_count[block_type] += 1

    # Comprovar si s'ha arribat al minim
    if hit_count[block_type] == logro_threshold:
        mc.postToChat(f"Felicitats! Has colpejat {logro_threshold} blocs del tipus {block_type}. 🎉")
        # Reiniciar el recompte del bloc
        hit_count[block_type] = 0

    '''def run(self, tipus):
        # Iniciar el bot i registrar l'observador.
        self.mc.postToChat("AchievementBot està actiu! Aconsegueix 100 blocs per un logro!")

        # Registrar l'observador
        # Això depèn del suport de l'API o de la capa d'esdeveniments.
        #self.mc.registerEventHandler("blockHit", self.on_block_hit)
        self.on_block_hit(tipus)'''