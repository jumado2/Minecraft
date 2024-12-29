import mcpi.minecraft as minecraft
import mcpi.block as block

# Classe per encapsular l'observador del bot
class AchievementBot:
    def __init__(self):
        self.mc = minecraft.Minecraft.create()
        self.block_count = {}
        self.logro_threshold = 100  # Nombre de blocs necessaris per a logro

    def on_block_placed(self, event):
        # Funció que es crida quan es col·loca un bloc.
        pos = event.pos
        block_type = event.block  # Assumeix que l'esdeveniment conté block.type

        # Actualitzar el recompte del bloc
        if block_type not in self.block_count:
            self.block_count[block_type] = 0
        self.block_count[block_type] += 1

        # Comprovar si s'ha arribat al minim
        if self.block_count[block_type] == self.logro_threshold:
            self.mc.postToChat(f"Felicitats! Has col·locat {self.logro_threshold} blocs del tipus {block_type}. 🎉")
            # Reiniciar el recompte del bloc
            self.block_count[block_type] = 0

    def run(self):
        # Iniciar el bot i registrar l'observador.
        self.mc.postToChat("AchievementBot està actiu! Aconsegueix 100 blocs per un logro!")

        # Registrar l'observador
        # Això depèn del suport de l'API o de la capa d'esdeveniments.
        self.mc.registerEventHandler("blockPlaced", self.on_block_placed)

        # Mantenir el bot actiu (si cal)
        try:
            while True:
                pass  # No cal fer res més, l'observer s'encarrega de tot
        except KeyboardInterrupt:
            print("AchievementBot s'ha aturat.")
