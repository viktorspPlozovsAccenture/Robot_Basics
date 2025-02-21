import os

# Imports IBM DB2 dll
def load_dll():
    current_directory = os.getcwd()
    os.add_dll_directory(f"{current_directory}\\.venv\\Lib\\site-packages\\clidriver\\bin")
    import ibm_db