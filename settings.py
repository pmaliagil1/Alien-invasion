class Settings:
    """Una clase para guardar toda la configuración de Alien Invasion"""

    def __init__(self):
        """Inicialzia la configuración del juego"""
        #Configuración de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Configuracion de la nave
        self.ship_speed = 5.0

        #Configuración de las balas
        self.bullet_speed = 8.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3