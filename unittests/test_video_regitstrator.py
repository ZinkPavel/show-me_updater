import unittest
import tempfile
import shutil
import sys
import os
from urllib import request

sys.path.append(os.path.join("src"))

from Updater import update
from VideoRegitstrator import VideoRegistrator


class TestVideoRegitstrator(unittest.TestCase):
    def test_available_all_update_links(self):
        for update_link in VideoRegistrator.AVAILABLE_MODELS.values():
            self.assertEqual(request.urlopen(update_link).getcode(), 200)


if __name__ == "__main__":
    unittest.main()
