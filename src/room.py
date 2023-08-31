class Room:
    def __init__(self, input_name, input_till, input_fee, input_guests_list, input_songs_list):
        self.name = input_name
        self.till = input_till
        self.fee = input_fee
        self.guests_list = input_guests_list
        self.songs_list = input_songs_list
    
    def check_in_guest(self, input_guest):
        maximum_guests = 4
        if len(self.guests_list) < maximum_guests:
            self.guests_list.append(input_guest)
            input_guest.reduce_wallet(self.fee)
            self.till += self.fee
    
    def check_out_guest(self, input_guest):
        self.guests_list.remove(input_guest)
    
    def add_song(self, input_song):
        self.songs_list.append(input_song)