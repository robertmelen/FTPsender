import unittest
import ftplib
from FTP_Sender import main
from FTP_Sender.main import FTPconnect

runner = unittest.TextTestRunner(verbosity=2)

class TestFTPconnect(unittest.TestCase):

    """Tests FTPConnect which handles connection to FTP servers. 
    Test uses a public FTP server. FTPConnect will return None if connection fails"""

    def test_connect(self):
        ftp_connect = FTPconnect()
        test_connect = ftp_connect.connect('ftp.dlptest.com', 'dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')
        self.assertIsNotNone(test_connect)
        test_connect.quit()

    """Tests if FTPconnect raises an error if it cannot connect to a server
    method is passed false connection details."""

    def test_errors(self):
        ftp_server = FTPconnect()
        test = ftp_server.connect('foo', 'bar', 'foobar')
        self.assertIsNone(test)

        
if __name__ == '__main__': 
     suite = unittest.TestLoader().loadTestsFromTestCase(TestFTPconnect)
     runner = unittest.TextTestRunner(verbosity=2)
     runner.run(suite)