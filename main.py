mport RPi.GPIO as GPIO
from rdm6300 import BaseReader
import I2C_LCD_driver
import time
import servomoteur

# Initialisation des composants
reader = BaseReader('/dev/ttyS0') 
lcd = I2C_LCD_driver.lcd()  
authorized_badges = ["348906", "11884836"]  
secret_code = "*122#"  # Code secret pour l'ouverture par clavier

# Fonction d'ouverture de la barrière
def open_barrier():
    print("Ouverture de la barrière...")
    servomoteur.angle_to_percent(90)  
    time.sleep(2)
    servomoteur.angle_to_percent(0)  
    print("Barrière ouverte !")

# Fonction d'affichage sur l'écran LCD
def display_message(message):
    lcd.lcd_clear()  # Effacer l'écran
    lcd.lcd_display_string(message, 1)  

# Démarrage du lecteur de badge
reader.start()

while True:
    card = reader.read_card()
    # Badge présent
    if card:
        # Vérification de l'autorisation
        if str(card.value) in authorized_badges:
            open_barrier()
            display_message("Bonjour !")
        else:
            display_message("Badge non autorisé. Veuillez réessayer.")

    # Badge absent, on passe au clavier
    else:
        # Lecture du code clavier
        keypad_input = keypadTask()
        # Code correct
        if keypad_input == secret_code:
            open_barrier()
            display_message("Bonjour !")
        # Code incorrect
        else:
            display_message("Mot de passe incorrect. Veuillez réessayer.")

reader.stop()
GPIO.cleanup()

print("Fin du programme.")