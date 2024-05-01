import unittest
from FTP_Sender import main
from FTP_Sender.main import FTPconnect

class TestFTPconnect(unittest.TestCase):

    """Tests FTPConnect which handles connection to FTP servers. 
    Test uses a public FTP server. FTPConnect will return None if connection fails"""

    def test_connect(self):

        server_details = {'host':'ftp.dlptest.com', 'user': 'dlpuser', 'password': 'rNrKYTX9g7z3RgJRmxWuGHbeu'}
        ftp_connect = FTPconnect(server_details)
        test_connect = ftp_connect.connect('ftp.dlptest.com', 'dlpuser', 'rNrKYTX9g7z3RgJRmxWuGHbeu')
        self.assertIsNotNone(test_connect)
        test_connect.quit()


    def test_errors(self):
        #connect to a ftp server that is invalid
        server_details = {'host': 'foo', 'user': 'bar'}
        ftp_server = FTPconnect(server_details)
        ftp_server.connect()

#class TestErrorHandling(unittest.TestCase):


    


if __name__ == '__main__': 
    unittest.main()