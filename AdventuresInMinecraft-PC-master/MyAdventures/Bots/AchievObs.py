import mcpi.minecraft as minecraft
import mcpi.block as block

# Classe per encapsular l'observador del bot
class AchievementBot:
    def __init__(self, m):
        self.mc = m
        self.hit_count = {}
        self.logro_threshold = 100  # Nombre de blocs necessaris per a logro

    def on_block_hit(self, event):
        # Funció que es crida quan es col·loca un bloc.
        pos = event.pos
        block_type = event.block

        # Actualitzar el recompte del bloc
        if block_type not in self.hit_count:
            self.hit_count[block_type] = 0
        self.hit_count[block_type] += 1

        # Comprovar si s'ha arribat al minim
        if self.hit_count[block_type] == self.logro_threshold:
            self.mc.postToChat(f"Felicitats! Has colpejat {self.logro_threshold} blocs del tipus {block_type}. 🎉")
            # Reiniciar el recompte del bloc
            self.hit_count[block_type] = 0

    def run(self):
        # Iniciar el bot i registrar l'observador.
        self.mc.postToChat("AchievementBot està actiu! Aconsegueix 100 blocs per un logro!")

        # Registrar l'observador
        # Això depèn del suport de l'API o de la capa d'esdeveniments.
        self.mc.registerEventHandler("blockHit", self.on_block_hit)

        # Mantenir el bot actiu (si cal)
        try:
            while True:
                pass  # No cal fer res més, l'observer s'encarrega de tot
        except KeyboardInterrupt:
            print("AchievementBot s'ha aturat.")