import os
import unittest
import tempfile
import shutil

from src import utils


class DownlaodFileWithMessageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self) -> None:
        shutil.rmtree(self.tmpdir)

    def test_base(self):
        python_logo_url = r"https://www.python.org/static/img/python-logo.png"

        result = utils.download_file_with_message(
            url=python_logo_url,
            out=self.tmpdir,
            msg="test message",
        )

        self.assertEqual(
            os.path.normpath(
                os.path.join(self.tmpdir, os.path.basename(python_logo_url))
            ),
            os.path.normpath(result),
        )

    def test_without_msg(self):
        python_logo_url = r"https://www.python.org/static/img/python-logo.png"

        result = utils.download_file_with_message(
            url=python_logo_url,
            out=self.tmpdir,
            msg=None,
        )

        self.assertEqual(
            os.path.normpath(
                os.path.join(self.tmpdir, os.path.basename(python_logo_url))
            ),
            os.path.normpath(result),
        )


if __name__ == "__main__":
    unittest.main()
