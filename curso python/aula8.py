import os
import datetime
import pyautogui


pyautogui.press("win")
pyautogui.write("chrome")

print(os.listdir("arquivos"))
print(datetime.date.today())

lista_aquivos = os.listdir("arquivos")

for arquivo in lista_aquivos:
    if ".txt" in arquivo:
     if "22" in arquivo:
            os.rename(f"arquivos/{arquivo}",f"arquivos/22/{arquivo}")
    elif "23" in arquivo:
        os.rename(f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")

