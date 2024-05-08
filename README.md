

# FTPSender
---

*Welcome to FTPSender, a small project designed to ease the sending of files to FTP servers*. It enables the sending of files to multiple FTP servers, helping to automate the proccess and also alerting you to successful file transfers and any failed connections. 

FTP Sender also lets you to transfer files to a specific server, from your list of servers.

### Why FTP Sender was created
---
If you are in the position (such as a photographer) where you need to regulary send files to multiply servers, it can become very tedious when using a 'normal' client such as FileZilla. FTP Sender automates the process, just pass it a list of servers, a folder, and it will send to each one.

---
## Hows it was made

##### Language: Python

###### Overview 

- **FtplibFTP** protocol client handles the sending of files.
 - **Pathlib** Path class is used for file handling, enabling a platform-independent way to manipulate file paths and directories and making the code less prone to human error. 
 - Server details are handled securely via environment variables  


The core of the project is within the `main.py` file which is structured in this way.

- Classes are defined for handling FTP connections, error handling, retrieving files, and sending files.
- Contains the main execution logic within the `__main__` block.

Server details are held in `server.py`, these are passed using environment variables handled by the **python-environ** package.

### Dependencies
- Python 3+
- python-environ

### How to use

###### Installation
Fork the repository
```
git clone https://github.com/robertmelen/FTPsender.git
```

Install requirements
``` 
pip install -r requirements.txt
 ```
Once cloned and `python-environ` is successfully installed, create a `.env` file in the root directory. 


###### How to use the server details within the '.env' file and `main.py`.
Your file should look like this, just amend with your own credentials and increase variable number with each server you add.
```
HOST1_NAME1=Personal
HOST1=ftp.example.com
HOST1_USER=foobar
HOST1_PASSWORD=password

HOST2_NAME2=work
HOST2=ftp.work.com
HOST2_USER=foobar
HOST2_PASSWORD=password

```
Use the `env` variables by adding them as a `dictionary` within the `ftp_server_details` `tuple`. Refer to the dotenv documentation [here](https://pypi.org/project/python-dotenv/) for more information on environment variables, if needed.

```
ftp_server_details = (

    {'name':os.environ.get('HOST1_NAME1'),
     'details': {
     'host':os.environ.get('HOST1'), 
     'user':os.environ.get('HOST1_USER'), 
     'password':os.environ.get('HOST1_PASSWORD')
                }
     
     },

     {'name':os.environ.get('HOST2_NAME2'),
     'details': {
     'host':os.environ.get('HOST2'), 
     'user':os.environ.get('HOST2_USER'), 
     'password':os.environ.get('HOST2_PASSWORD')
                }
     
     },)
```

Once setup, run `main.py` and you will see a menu within your terminal with your servers listed. Just press the corresponding number, which will send files to that server.
To send files to all servers, press `0`. Press any other key to exit the program.


### Roadmap

FTPSender works well, but will be improved! **Coming soon....**
- Ability to add new servers from the menu
- Cancellation during sending
- Improved customisation of server settings (adding port and mode options)
- Improved user feedback once files are sent
- File sending progress
- Additional unit testing will be added asap

### Tests

The file `test_ftp_sender.py` includes three unit tests, each testing that core functionality is working. Feel free to run these test before using FTPSender.

- **TestSendFile** checks that the `send()` function within the `SendFiles` class is correctly sending an image to a mock server.
- **TestGetFiles** tests that the `GetFiles` class is only using a single folder as source
- **TestFTPconnect** checks that `ftplib` is called with `host`, and the `connect()` method is called once

### License

Distributed under the MIT License. See LICENSE.txt for more information.


### Acknowledgments


Many thanks to all the contributors of ftplib which does all the heavy lifting for this project. Source code can be found [here](https://github.com/python/cpython/blob/3.12/Lib/ftplib.py)

Also thanks to **u/Diapolo10** on Reddit, who gave me advice on much-needed improvements to the code and this repository, I've learned a lot! Much appreciated.

