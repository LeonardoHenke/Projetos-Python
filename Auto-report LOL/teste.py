import pyautogui
import pygetwindow as gw
from time import sleep
import mods

#pegar a cor do amarelo
pixel_amarelo = (250, 190, 10)

# pegar todas a locs
coordenadas_pixel = [[373, 328], [373, 374], [373, 416], [373, 458], [373, 499]]
cordenadas_botaoDenunc = [[600, 336], [601, 373], [601, 414], [601, 459], [602, 496]]

#sleep(3)
# verificar se a cor do pixel é amarela
for i, regiao in enumerate(coordenadas_pixel):
    x,y = regiao
    cor_pixel = pyautogui.pixel(x, y)
    if cor_pixel != pixel_amarelo:
        pyautogui.click(cordenadas_botaoDenunc[i], duration=0.2)
        mods.denuncias_do_jogador()
    else:
        print(f'O player{i+1} é nóis')

