import unittest
from unittest.mock import patch, Mock
from unittest import mock
from FTP_Sender import main
from FTP_Sender.main import FTPconnect, GetFiles, ErrorHandling, SendFiles
import tempfile
from pathlib import Path


class TestFTPconnect(unittest.TestCase):

    """Test includes mocking FTP server, testing that 
    Ftplib is called with host, and connect method is called once"""

    @patch('ftplib.FTP')
    #mock object get's passed as and additional argument automatically as whataver it's named
    def test_connection(self, mock_FTP):
        instacnce = mock_FTP.return_value
        host = "testftp"
        user = "test_user"
        password = "test_pass"
        test_connect = FTPconnect()
        connection = test_connect.connect(host, user, password)
        mock_FTP.assert_called_once_with(host)
        instacnce.login.assert_called_once_with(user, password)


class TestGetFiles(unittest.TestCase):

    '''Tests that GetFile is being called with a single folder
    and that os.listdir is called once with a folder'''

    @patch('os.listdir')
    def test_folder(self, mock_listdir):
        folder = '/path/to/test/folder'
        files = GetFiles(folder)
        self.assertEqual(files.folder, folder)
        mock_listdir.assert_called_once_with(folder)
        file_num = files.file_number()
        
        self.assertEqual(type(file_num), int)


#test send file class

class TestSendFile(unittest.TestCase):

    '''A test to check if image files are successfully send to a mock FTP server'''

    @patch('ftplib.FTP')
    def test_sending(self, mock_ftp):
        instance = mock_ftp.return_value
        #NOTE -- SendFiles iterates through a Tuple of dictionaries. ftp_server_details is using a single
        #dictionary within a tuple. Using a singleton tuple, you must include a comma when assigning 
        #the value to a variable. If you don’t include the comma, Python does not store the 
        #value as a tuple and it will raise a TypeError: string indices must be integers
        ftp_server_details = ({'host':'test.ftp', 'user':'test', 'password':'test'},)
        temp_dir = tempfile.mkdtemp()
        files = [Path(temp_dir).joinpath('image1.jpg')]
        for file_path in files:
            with tempfile.NamedTemporaryFile(mode='wb') as jpg:
                with open(file_path, 'w'):
                    jpg.write(b"temp jpg")
            sender = SendFiles(ftp_server_details, Path(temp_dir))
            sender.send()
            instance.storbinary.assert_called_once_with('STOR image1.jpg', mock.ANY)
           

          
if __name__ == '__main__':
    unittest.main()