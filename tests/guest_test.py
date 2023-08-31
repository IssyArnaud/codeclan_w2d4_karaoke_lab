import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Wonderwall", "Oasis")
        self.song_2 = Song("Bohemian Rhapsody", "Queen")
        self.song_3 = Song("Dancing Queen", "Abba")
        self.song_4 = Song("Livin' on a Prayer", "Bon Jovi")
        self.song_5 = Song("I Want it That Way", "Backstreet Boys")
        self.guest = Guest("Cat", 25, self.song_1)
        self.room_1 = Room("Tunez", 100, 7,
                         [self.guest], 
                         [self.song_1, self.song_2, self.song_3, self.song_4])
    
    def test_guest_has_name(self):
        self.assertEqual("Cat", self.guest.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(25, self.guest.wallet)
    
    def test_reduce_wallet(self):
        self.guest.reduce_wallet(5)
        self.assertEqual(20, self.guest.wallet)
    
    def test_cheer_fav_song(self):
        result = self.guest.cheer_fav_song(self.room_1)
        self.assertEqual("Whoo!", result)