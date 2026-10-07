import time
import spidev
import RPi.GPIO as GPIO

spi_ch = 0

# Sincroniza o circuito integrado com o raspberry em relação a frequência MHz
spi = spidev.SpiDev(0, spi_ch)
spi.max_speed_hz = 1200000

def read_adc(adc_ch, vref = 3.3):

    # Monta uma estrutura de 2 bytes para trocar infromações com o circuito integrado
    if adc_ch != 0:
        adc_ch = 1

   
    msg = 0b11
    msg = ((msg << 1) + adc_ch) << 5
    msg = [msg, 0b00000000]
    reply = spi.xfer2(msg)

    #   Combina dois bytes e descarta o desnecessário
    adc = 0
    for n in reply:
        adc = (adc << 8) + n

    # Last bit (0) is not part of ADC value, shift to remove it
    adc = adc >> 1

    # Calculate voltage form ADC value
    voltage = (vref * adc) / 1024

    return voltage

# Report the channel 0 and channel 1 voltages to the terminal
try:
    while True:
        adc_0 = read_adc(0)
        adc_1 = read_adc(1)
        print("Ch 0:", round(adc_0, 2), "V Ch 1:", round(adc_1, 2), "V")
        time.sleep(0.2)

finally:
    spi.close()
    GPIO.cleanup()
