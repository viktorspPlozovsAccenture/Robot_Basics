
import sys
import win32com.client
import base64
import zlib
import gzip
import shutil



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

def convert_to_unix_lf(input_file, output_file):
    try:
        # Apriamo il file di input in modalità lettura
        with open(input_file, 'r', newline='') as f_in:
            # Leggiamo tutto il contenuto del file
            content = f_in.read()
        
        # Sostituiamo tutti i ritorni a capo con LF (\n)
        content = content.replace('\r\n', '\n')  # Windows CRLF to Unix LF
        content = content.replace('\r', '\n')    # Mac OS Classic CR to Unix LF
        
        # Apriamo il file di output in modalità scrittura
        with open(output_file, 'w', newline='\n') as f_out:
            # Scriviamo il contenuto modificato nel nuovo file
            f_out.write(content)
        
        print(f"Conversione completata. File convertito: {output_file}")

    except FileNotFoundError:
        print("File non trovato. Assicurati che il percorso del file di input sia corretto.")

def compress_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'rb') as f_in:
            with gzip.open(output_file_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"File compresso con successo: {output_file_path}")
    except FileNotFoundError:
        print("Errore: File non trovato.")
    except Exception as e:
        print(f"Si è verificato un errore durante la compressione: {e}")




