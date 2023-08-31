class Guest:
    def __init__(self, input_name, input_wallet, input_fav_song):
        self.name = input_name
        self.wallet = input_wallet
        self.fav_song = input_fav_song
    
    def reduce_wallet(self, input_amount):
        self.wallet -= input_amount
    
    def cheer_fav_song(self, input_room):
        for song in input_room.songs_list:
            if song == self.fav_song:
                return "Whoo!"
    
    # def pay_for_check_in(self, input_room):
    #     self.reduce_wallet(input_room.fee)