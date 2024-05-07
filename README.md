

# FTP Sender
---

Welcome to FTP Sender, a project designed to ease the sending of files to FTP servers. It enables the sending of files to multiple FTP servers, helping to automate the proccess and also alerting you to successful file transfers and any failed connections. 

FTP Sender also enables you to transfer files to a specific server from your list of servers.

### Why FTP Sender was created
---
If you are in the position (such as a photographer) where you need to regulary send files to multiply servers, it can become very tedious when using a 'normal' client such as FileZilla. FTP Sender automates the process, just pass it a list of servers, a folder, and it will send to each one.

## Hows it was made

##### Language: Python

###### Overview 

- FtplibFTP protocol client handles the sending of files.
 - Pathlib's Path class is used for file handling, enabling a platform-independent way to manipulate file paths and directories and making the code less prone to human error. 
 - Server detils are handled securley via environment varibles   


The core of the project is within the main.py file which is structred in this way.

- Classes are defined for handling FTP connections, error handling, retrieving files, and sending files.
- Contains the main execution logic within the __main__ block.

Server deatils are held in server.py, deatils are passed uing environment varibles handled by the python-environ packaage.

### Dependencies
- Python (version 3.9.5)
- ftplib 
- pathlib
- dotenv

### How to use

###### Installation
First clone the repository
```
git clone https://github.com/robertmelen/FTPsender.git
```


