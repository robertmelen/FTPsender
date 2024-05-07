
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
from servers import ftp_server_details









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
            send = self.connect(server['details']['host'], 
                                server['details']['user'], 
                                server['details']['password'])
            if send:
                print("Number of files to send", self.file_number())    
                print(send.getwelcome())
                for file_name in self.file_list:
                    file_path = Path(self.folder, file_name) 
                    print(file_path)
                    with file_path.open(mode='rb') as file:
                        response = send.storbinary(f'STOR {file_name}', file)
                        if response.startswith('226'):  
                            print(f"File '{file_name}' sent successfully to {server['details']['host']}")
                        else:
                            print(f"Failed to send file '{file_name}' to {server['details']['host']}: {response}")
                print(self.file_number(), "FILES SENT SUCCESSFULLY")
                send.quit()   
            else:
                print(f"Sorry, unable to connect to {server['details']['host']}")        


if __name__ == "__main__":
    print("....FTP SERVER MENU....")
    number_of_choices = 0
    for menu, server in enumerate(ftp_server_details):
        print(f"{menu + 1}:" + " " + f"{server['name']}")
        number_of_choices += menu 
        
    print(f"You have {number_of_choices} server choices, press Q to")
    while True:
        try:
            choice = int(input("Please choose which server to send to. Press '0' for all or any key to Quit: "))
            if choice == 0:
                sender = SendFiles(ftp_server_details, Path(os.environ.get('FOLDER')))
                sender.send()
            elif 1 <= choice <= len(ftp_server_details):
                sender = SendFiles([ftp_server_details[choice - 1]], Path(os.environ.get('FOLDER')))
                sender.send()
        except ValueError:
            print("Quitting")
            break













   