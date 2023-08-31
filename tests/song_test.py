import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Wonderwall", "Oasis")
    
    def test_song_has_properties(self):
        self.assertEqual("Wonderwall", self.song.name)
        self.assertEqual("Oasis", self.song.artist)