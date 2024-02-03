from rdm6300 import BaseReader
class Reader(BaseReader):
    
    def card_inserted(self,card):
        
        print("card inserted "+str(card.value))
        authorized_badges = ["348906", "11884836"]
        if str(card.value) in authorized_badges:
            print("badge autorisé")
        else:
            print("badge non autorisé")
    def card_removed(self,card):
        print("Removed card " + str(card.value))
    def invalid_card(self,card):
        print("invalid card " +str(card.value))

r=Reader('/dev/ttyS0')
r.start()



    
