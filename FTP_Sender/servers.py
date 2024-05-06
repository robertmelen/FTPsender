import os
from dotenv import dotenv_values

secrets = dotenv_values()
local_secrets = dotenv_values()



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
     
     },
     

)