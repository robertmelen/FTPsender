import unittest
from FTP_Sender import main
from FTP_Sender.main import FTPconnect

class TestFTPconnect(unittest.TestCase):

    """Tests FTPConnect which handles connection to FTP servers. 
    Test uses a public FTP server."""

    def test_connect(self):

        server_details = {'host':'ftp.dlptest.com', 'user': 'dlpuser', 'password': 'rNrKYTX9g7z3RgJRmxWuGHbeu'}
        ftp_connect = FTPconnect(server_details)
        test_connect = ftp_connect.connect('ftp.dlptest.com', 'dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')
        self.assertIsNotNone(test_connect)
        test_connect.quit()


if __name__ == '__main__': 
    unittest.main()