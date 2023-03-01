import pyautogui
import pygetwindow as gw
from time import sleep
import mods

# a cor que iremos procurar na comparação
pixel_amarelo = (250, 190, 10)

# coordenadas que iremos usar para buscar a cor
coordenadas_pixel = [[373, 328], [373, 374], [373, 416], [373, 458], [373, 499]]

# coordenadas do botão de denunciar
cordenadas_botaoDenunc = [[600, 336], [601, 373], [601, 414], [601, 459], [602, 496]]

# abrir a janela do lol
lol_window = gw.getWindowsWithTitle('League of Legends')[0]
lol_window.activate()

# esperando carregar a página
while not pyautogui.locateCenterOnScreen('honra.png'):
    sleep(1.5)

# pular honras:
mods.botao_pular_honras()

# esperando carregar a página
while not pyautogui.locateCenterOnScreen('continuar1.png'):
    sleep(1.5)

# - clicar em continuar:
mods.botao_continuar()

# esperando carregar a página
while not pyautogui.locateCenterOnScreen('continuar2.png'):
    sleep(1.5)

# verificar se a cor do pixel é amarela
for i, regiao in enumerate(coordenadas_pixel):
    x,y = regiao
    cor_pixel = pyautogui.pixel(x, y)
    if cor_pixel != pixel_amarelo:
        pyautogui.click(cordenadas_botaoDenunc[i], duration=0.2)
        mods.denuncias_do_jogador()
        print(f'Player{i+1} - reportado')
    else:
        print(f'Player{i+1} - é nóis')

# - clicar em continuar:
pyautogui.click(825, 834, duration=0.2)
