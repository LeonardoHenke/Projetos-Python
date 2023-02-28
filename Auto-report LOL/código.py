import pyautogui
import pygetwindow as gw
from time import sleep
import mods

cordenadas_botaoDenunc = [[600, 336], [601, 373], [601, 414], [601, 459], [602, 496]]
cordenadas_regiao = [[511, 318, 80, 23], [511, 358, 80, 23], [511, 399, 80, 23], [511, 441, 80, 23], [511, 482, 80, 23]]


# abrir a janela do lol
lol_window = gw.getWindowsWithTitle('League of Legends')[0]
lol_window.activate()

# pular honras:
mods.botao_pular_honras()

# esperando carregar a página
sleep(4)

# - clicar em continuar:
mods.botao_continuar()

# esperando carregar a página
sleep(2)

for i, regiao in enumerate(cordenadas_regiao):
    if not pyautogui.locateOnScreen('nickname.png', region=(regiao), grayscale=True, confidence=0.4):
        pyautogui.click(cordenadas_botaoDenunc[i], duration=0.2)
        mods.denuncias_do_jogador()

# - clicar em continuar:
#pyautogui.click(825, 834, duration=0.2)

# while not locateonscreen
# print(pyautogui.position())