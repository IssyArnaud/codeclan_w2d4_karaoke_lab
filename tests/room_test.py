import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Cat", 25, "Wonderwall")
        self.guest_2 = Guest("Ellie", 30, "Wonderwall")
        self.guest_3 = Guest("Amy", 20, "Wonderwall")
        self.guest_4 = Guest("Rowan", 20, "Wonderwall")
        self.guest_5 = Guest("Alice", 25, "Wonderwall")
        self.song_1 = Song("Wonderwall", "Oasis")
        self.song_2 = Song("Bohemian Rhapsody", "Queen")
        self.song_3 = Song("Dancing Queen", "Abba")
        self.song_4 = Song("Livin' on a Prayer", "Bon Jovi")
        self.song_5 = Song("I Want it That Way", "Backstreet Boys")
        self.room = Room("Tunez", 100, 7,
                         [self.guest_1, self.guest_2, self.guest_3], 
                         [self.song_1, self.song_2, self.song_3, self.song_4])
        
    def test_room_has_properties(self):
        self.assertEqual("Tunez", self.room.name)
        self.assertEqual([self.guest_1, self.guest_2, self.guest_3], self.room.guests_list)
        self.assertEqual([self.song_1, self.song_2, self.song_3, self.song_4], self.room.songs_list)
    
    def test_interaction_of_classes(self):
        self.assertEqual("Cat", self.guest_1.name)
        self.assertEqual("Queen", self.song_2.artist)
    
    def test_check_in_guest(self):
        self.room.check_in_guest(self.guest_4)
        self.assertEqual([self.guest_1, self.guest_2, self.guest_3, self.guest_4], self.room.guests_list)
        self.assertEqual(4, len(self.room.guests_list))
    
    def test_check_out_guest(self):
        self.room.check_out_guest(self.guest_3)
        self.assertEqual([self.guest_1, self.guest_2], self.room.guests_list)
        self.assertEqual(2, len(self.room.guests_list))
    
    def test_add_song(self):
        self.room.add_song(self.song_5)
        self.assertEqual([self.song_1, self.song_2, self.song_3, self.song_4, self.song_5], self.room.songs_list)
    
    def test_guest_maximum(self):
        self.room.check_in_guest(self.guest_4)
        self.room.check_in_guest(self.guest_5)
        self.assertEqual([self.guest_1, self.guest_2, self.guest_3, self.guest_4], self.room.guests_list)
    
    def test_charging_check_in_fee(self):
        self.room.check_in_guest(self.guest_4)
        self.assertEqual(13, self.guest_4.wallet)
        self.assertEqual(107, self.room.till)