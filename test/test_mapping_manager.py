import unittest
from mapper.mapping_manager import ListMusicSoundcloud


class TestSoundcloud(unittest.TestCase):
    def test_urlstatus(self):
        self.assertEqual(ListMusicSoundcloud("https://kymuvqgv84.execute-api.eu-west-3.amazonaws.com/api/").getstatus(), 200)

    def test_urlmetadata(self):
        list_metadata = ListMusicSoundcloud("https://kymuvqgv84.execute-api.eu-west-3.amazonaws.com/api/").getlistmetadatasongdict()
        for elt in list_metadata:
            self.assertTrue("name" in dict(elt).keys(), "metadata name is not in body of content response")
            self.assertTrue("file" in dict(elt).keys(), "metadata file is not in body of content response")
            self.assertTrue("artist" in dict(elt).keys(), "metadata artist is not in body of content response")

    def test_listsongmetadatakeys(self):
        list_metadata = ListMusicSoundcloud("https://kymuvqgv84.execute-api.eu-west-3.amazonaws.com/api/").getlistmetadatasongdict()
        for elt in list_metadata:
            self.assertTrue(dict(elt)["file"].startswith("https") and dict(elt)["file"].endswith(".wav"), "url of song does not have correct format")


if __name__ == '__main__':
    unittest.main()