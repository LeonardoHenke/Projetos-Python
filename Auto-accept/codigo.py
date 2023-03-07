from time import sleep
import pyautogui


# dando entrada na imagem
recusar = r"E:\Programas\Projetos-Python\Auto-accept\recusar.png"

# procurando a img
contagem = 0
while not pyautogui.locateCenterOnScreen(recusar):
    sleep(4)
    contagem += 1
    print(f'Procurando partida {contagem}')

# clicar em aceitar partida
pyautogui.click(1027, 717, duration=0.5)

# printar que aceitou partida
print('Partida aceita')
