## Creating and managing user accounts
#importing libraries
import os
import subprocess
import sys
import getpass

#add user function
def create_user():
   #Ask for the user input
    username = input ("Enter New Username ")
    
    #Asking for users password
    password = getpass.getpass()
    
    try:
        #executing useradd command using subprocess module
        subprocess.run(['useradd', '-p', password, username])
    except:
         print(f"Failed to add user.")
         sys.exit(1)
create_user()
