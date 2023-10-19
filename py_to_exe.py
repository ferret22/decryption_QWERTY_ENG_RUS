import PyInstaller.__main__ as pyinstl


pyinstl.run([
    'qwerty_decryption.py',
    '--onefile',
    '--noconsole',
    '--icon=icon/qwerty.ico',
    '--name=qwerty_decryption'
])
