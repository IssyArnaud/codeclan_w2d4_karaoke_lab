class Guest:
    def __init__(self, input_name, input_wallet, input_fav_song):
        self.name = input_name
        self.wallet = input_wallet
        self.fav_song = input_fav_song
    
    def can_pay(self, input_amount):
        if self.wallet >= input_amount:
            return True
    
    def make_payment(self, input_amount):
        result = self.can_pay(input_amount)
        if result == True:
            self.wallet -= input_amount
    
    def cheer_fav_song(self, input_room):
        for song in input_room.songs_list:
            if song == self.fav_song:
                return "Whoo!"

    def pay_room_fee(self, input_room):
            self.make_payment(input_room.fee)