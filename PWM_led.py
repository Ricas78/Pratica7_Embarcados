# Ricardo Dias 12704331
# Gustavo Rinaldi 10845022

import RPi.GPIO as GPIO  # utilizando o apelido "GPIO" para se referir a função RPi.GPIO
from time import sleep  # importando apenas a função sleep da biblioteca time

# definindo que a convenção para o número das portas será o mesmo da GPIO na placa
GPIO.setmode(GPIO, BCM)
GPIO.setup(26, GPIO.OUT)  # definindo que a GPIO 26 será um pino de saída

# teste 1, frequência do sinal em 100Hz e dutycycle em 100%

# definindo que a variável "pwm" recebe o que retorna da função "GPIO.PWM(26,100)", esta função define que a GPIO 26 será o pino com recurso PWM e a frequência do sinal será de 100Hz
pwm = GPIO.PWM(26, 100)
pwm.start(0)  # definindo que a porcentagem do dutycycle inicial será de 0% para a varia´vel acima que representa o sinal PWM gerado

for dc in range(101):  # laço for que vai incrementar a variável "dc" de 0 a 100
    # variação da porcentagem do dutycycle do sinal pwm gerado varia de acordo com o incremento da variável "dc"
    pwm.ChangeDutyCycle(dc)
    sleep(0.2)  # o tempo de um incremento de 0,2 segundos para o outro no laço for

# teste 2, frequência do sinal em 50Hz, dutycycle em 100%
# teste 3, frequência do sinal em 100Hz, dutycycle em 50%
