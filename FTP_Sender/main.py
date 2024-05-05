
"""
FTP File Sender

This script connects to FTP servers and sends files from a specified folder to each server.
It retrieves server details and folder location from environment variables and sends the
files using FTP protocol.

Usage:
- Ensure environment variables are set for FTP server details and folder location.
- Run the script to initiate the file sending process.

Author: Robert Melen
Date: 29/4/2024
"""

import ftplib
import os
from pathlib import Path
from dotenv import dotenv_values

secrets = dotenv_values()
local_secrets = dotenv_values()



ftp_server_details = (

    {'host':os.environ.get('HOST1'), 
     'user':os.environ.get('HOST1_USER'), 
     'password':os.environ.get('HOST1_PASSWORD')},

    {'host':os.environ.get('HOST2'), 
     'user':os.environ.get('HOST2_USER'), 
     'password':os.environ.get('HOST2_PASSWORD')},
     

)

#ftp_server_details = {'host': 'ftp.example.com', 'user': 'username', 'password': 'password'}



class ErrorHandling:

    '''

    Error handling class

    '''
    def __init__(self, error):
        self.error = error
    def error_message(self):
        print(f"Failed to connect. Error: {self.error}")
    



class FTPconnect():

    '''

    Class to handle connection to a FTP server
    
    '''
   
    def connect(self, host, user, password):
        try:
            ftp = ftplib.FTP(host)
            ftp.login(user, password)
            return ftp
        except ftplib.all_errors as error:
            print(error)
            handle_error = ErrorHandling(error)
            handle_error.error_message()
            return None

        

class GetFiles:

    '''

    Class that handles folder location

    '''
    def __init__(self, folder):
        self.folder = folder
        self.file_list = os.listdir(self.folder)

    def file_number(self):
        return len(self.file_list)


class SendFiles(FTPconnect, GetFiles):

    '''

    Class to handle sending files. Inherits from FTPconnect and Getfiles

    '''
    def __init__(self, server_details, folder):
        GetFiles.__init__(self, folder)    
        self.server_details = server_details
        self.folder = folder               

    def send(self):
        for server in self.server_details:
            send = self.connect(server['host'], server['user'], server['password'])
            if send:
                print("Number of files to send", self.file_number())
                print(send.getwelcome())
                for file_name in self.file_list:
                    file_path = Path(self.folder, file_name) 
                    print(file_path)
                    with file_path.open(mode='rb') as file:
                        response = send.storbinary(f'STOR {file_name}', file)
                        if response.startswith('226'):  
                            print(f"File '{file_name}' sent successfully to {server['host']}")
                        else:
                            print(f"Failed to send file '{file_name}' to {server['host']}: {response}")
                print(self.file_number(), "FILES SENT SUCCESSFULLY")
                send.quit()   
            else:
                print(f"Sorry, unable to connect to {server['host']}")        


if __name__ == "__main__":
    sender = SendFiles(ftp_server_details, Path("D:\Images\FTP folder"))
    sender.send()
    

    












   