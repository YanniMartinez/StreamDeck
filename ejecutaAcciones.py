import subprocess
import webbrowser
import time

# URL que se abrirá en el navegador predeterminado
url = "https://www.google.com"

# Abrir la URL en el navegador predeterminado
webbrowser.open(url)


# Comando para abrir Visual Studio Code
comando = "code"

# Ejecuta el comando
subprocess.run(comando, shell=True)



# Comando para abrir el Bloc de notas con el archivo de script
comando = "notepad.exe"

# Ejecuta el comando
subprocess.run(comando, shell=True)


# Comando para abrir Microsoft Word
comando = "start winword"

# Ejecuta el comando
subprocess.run(comando, shell=True)

# Comando para abrir Microsoft PowerPoint
comando = "start powerpnt"

# Ejecuta el comando
subprocess.run(comando, shell=True)


# Comando para abrir Microsoft Excel
comando = "start excel"

# Ejecuta el comando
subprocess.run(comando, shell=True)

# Ruta al ejecutable de Epic Games Launcher
ruta_epicgames = "C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"

# Comando para abrir Epic Games Launcher
comando = f'"{ruta_epicgames}"'

# Ejecuta el comando
subprocess.run(comando, shell=True)



# Ruta al ejecutable de Steam
ruta_steam = "C:\Program Files (x86)\Steam\steam.exe"

# Comando para abrir Steam Launcher
comando = f'"{ruta_steam}"'

# Ejecuta el comando
subprocess.run(comando, shell=True)


time.sleep(5)

# Comando para suspender el equipo
#comando = "shutdown /h"

# Ejecuta el comando
#subprocess.run(comando, shell=True)