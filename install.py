import os, time

print("\n\033[92m[\033[37m*\033[92m] \033[37mProcessando....\n")
print("\033[92m[\033[37m*\033[92m] \033[37mLendo Arquivo: ", end="", flush=1)
try:
    fileData = open("d-pro.py", "r").read()
except:
    print("Error")
    print("\033[92m[\033[91m!\033[92m] \033[37mArquivo Não Encontrado")
    exit()

scriptData = fileData.replace("logo() # Removable", "")
time.sleep(1)
print("Done")

print("\033[92m[\033[37m*\033[92m] \033[37mInstalling Script: ", end="", flush=1)

if (os.path.exists("/data/data/com.termux/files/home/bin/termux-url-opener")):
    os.system("mv '/data/data/com.termux/files/home/bin/termux-url-opener' '/data/data/com.termux/files/home/bin/termux-url-opener.old'")

file = open("/data/data/com.termux/files/home/bin/termux-url-opener", "w")
file.write(scriptData)
file.close()

file = open("/data/data/com.termux/files/usr/bin/d-pro", "w")
file.write(scriptData)
file.close()

time.sleep(1)
print("Done")

print("\033[92m[\033[37m*\033[92m] \033[37mChanging Execute Mode: ", end="", flush=1)
os.system("chmod +x /data/data/com.termux/files/home/bin/termux-url-opener")
os.system("chmod +x /data/data/com.termux/files/usr/bin/d-pro")
time.sleep(1)
print("Done")

time.sleep(1)
print("\n\033[92m[\033[37m#\033[92m] \033[37mUses :")
print("\n[*] For command line use, type: d-pro \033[3mvideo url\033[0m")
print("  Exemplo: d-pro https://youtu.be/dQw4w9WXXcQ")
print("\n[*] Compartilhe vídeos com o Termux para processar vídeos automaticamente")

print("\n\033[92m[\033[37m#\033[92m] \033[37mNote: ")
print("\n[*] Use \" Ou ' para evitar erro de url inválido")
print("\033[37m  Exemplo: d-pro \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"")
print("\n")