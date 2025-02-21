
import pyautogui
import sys
import win32com.client
import base64
import zlib



def createFile(filename, testo):
    try:
        with open(filename, 'w') as file:
            file.write(testo)
        print(f"Testo scritto con successo nel file '{filename}'.")
    except Exception as e:
        print(f"Si è verificato un errore durante la scrittura nel file '{filename}': {e}")
        BlockingIOError

def compress_text(text):
    compressed = zlib.compress(text.encode('UTF-8'), 9)
    return base64.b64encode(compressed).decode('ASCII')


