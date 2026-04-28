#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank 
from ev3dev2.sensor import INPUT_1, INPUT_4, INPUT_2
from ev3dev2.sensor.lego import ColorSensor, GyroSensor 
from time import sleep

tank = MoveTank(OUTPUT_B, OUTPUT_C)

gyro = GyroSensor(INPUT_2)

cs_dir = ColorSensor(INPUT_1) 
cs_esq = ColorSensor(INPUT_4) 

cs_dir.mode = 'COL-COLOR'
cs_esq.mode = 'COL-COLOR'
  
  
def ler_cor_confirmada(sensor, vezes=5):
    contagem = {}

    for _ in range(vezes):
        c = sensor.value()
        contagem[c] = contagem.get(c, 0) + 1
        sleep(0.01)

    return max(contagem, key=contagem.get)

def curva_direita():
    tank.on_for_seconds(20, 20, 0.15)

    tank.on(-15, 25)

    while True:
        if cs_esq.value() == 1:
            break
            
        sleep(0.01)

    tank.off()
    
    
def curva_esquerda():
    tank.on_for_seconds(20, 20, 0.15)

    tank.on(25, -15)

    while True:
        if cs_dir.value() == 1:
            break

        sleep(0.01)

    tank.off()    
    


while True:
    SEsq = ler_cor_confirmada(cs_esq)
    SDir = ler_cor_confirmada(cs_dir)

    print("ESQ:", SEsq, "DIR:", SDir)

    if cs_esq.value() == 3 and cs_dir.value() == 3:
        tank.on_for_seconds(0, 0, 0.2)
        if SEsq == 3 and SDir == 3:
            tank.on_for_seconds(20, 20, 0.5)

            gyro.reset()
            sleep(0.2)

            tank.on(20, -20)
            while abs(gyro.value()) < 180:
                sleep(0.01)

            tank.off()
            
    elif cs_dir.value() == 3 and cs_esq.value() == 6:
        tank.on_for_seconds(0, 0, 0.2)
        if SDir == 3 and SEsq == 6:
            tank.on_for_seconds(20, 20, 0.8)

            gyro.reset()
            sleep(0.2)

            tank.on(-20, 20)
            while abs(gyro.value()) < 90:
                sleep(0.01)

            tank.off()
            
    elif cs_dir.value() == 6 and cs_esq.value() == 3:
        tank.on_for_seconds(0, 0, 0.2)
        if SDir == 6 and SEsq == 3:
            tank.on_for_seconds(20, 20, 0.8)

            gyro.reset()
            sleep(0.2)

            tank.on(20, -20)
            while abs(gyro.value()) < 90:
                sleep(0.01)

            tank.off()
            
    elif cs_dir.value() == 1 and cs_esq.value() == 1:
        tank.on_for_seconds(0, 0, 0.2)
        tank.on_for_seconds(-5, -5, 0.1)
        if SDir == 1 and SEsq == 1:
            tank.on_for_seconds(20, 20, 0.7)

    elif SDir == 1 and SEsq == 6:
        curva_direita()
        tank.on_for_seconds(20,-20, 0.6)

    elif SDir == 6 and SEsq == 1:
        curva_esquerda()
        tank.on_for_seconds(-20, 20, 0.6)
        
    elif SDir == 5 and SEsq == 5:
        tank.on_for_seconds(0, 0, 1)
        tank.off()
        
    else:
        tank.on(25, 25)