# 🚀 Laboratório Raspberry Pi: Sistemas Embarcados e Protocolos

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Raspberry Pi](https://img.shields.io/badge/Hardware-Raspberry%20Pi-C51A4A?style=flat&logo=raspberrypi&logoColor=white)](https://www.raspberrypi.org/)
[![Licença](https://img.shields.io/badge/Licenca-GNU-blue.svg)](LICENSE)

Bem-vindo ao repositório do **Laboratório Raspberry Pi**. Este projeto é um roteiro prático e estruturado para o aprendizado de sistemas embarcados, integração de hardware e protocolos de comunicação de baixo nível utilizando a plataforma Raspberry Pi e Python.

---

## 📌 Visão Geral do Projeto

Este repositório documenta a implementação passo a passo dos principais experimentos de hardware:
1. **Entrada e Saída Digital (GPIO):** Fundamentos da leitura de estados binários e controle de periféricos.
2. **SPI e Leitura Analógica:** Interfaciamento de conversores Analógico-Digitais (ADC) externos para contornar limitações físicas de hardware.
3. **Protocolo I2C e Sensores:** Comunicação a nível de registradores com sensores digitais usando arquitetura de barramento.

---

## 📂 Estrutura do Repositório

```text
raspberry-pi-lab/
├── .gitignore
├── LICENSE
├── README.md
├── docs/
│   ├── conceitos-linux.md
│   ├── gpio-pinout.md
│   └── protocolos-spi-i2c.md
├── exp01-digital-io/
│   ├── circuit-diagram.png
│   ├── main.py
│   └── README.md
├── exp03-spi-analog/
│   ├── circuit-diagram.png
│   ├── main.py
│   └── README.md
└── exp04-i2c-sensor/
    ├── circuit-diagram.png
    ├── main.py
    └── README.md
```
---

## 🧪 Resumo dos Experimentos

**1. Experimento 01: Entrada e Saída Digital**
Foco: Pinagem GPIO, botões (push-buttons), LEDs e resistores de Pull-up/Pull-down.

Objetivo: Ler sinais digitais discretos (HIGH / LOW) e alterar o estado das saídas correspondentes utilizando a biblioteca gpiozero.

**2. Experimento 03: Barramento SPI e Entrada Analógica**
Foco: Interface Periférica Serial (SPI) e conversor ADC MCP3008.

Objetivo: Conectar um ADC externo de 10 bits via linhas SPI (MISO, MOSI, SCLK, CE) para ler tensões analógicas contínuas de sensores ou potenciómetros.

**3. Experimento 04: Sensor de Temperatura I2C**
Foco: Protocolo I2C (Inter-Integrated Circuit), endereçamento de dispositivos e leitura de registradores.

Objetivo: Comunicar através de duas linhas compartilhadas (SDA, SCL), detectar endereços ativos de dispositivos via i2cdetect e processar a telemetria de temperatura.

---

## ⚙️ Configuração de Hardware e Software

**Pré-requisitos**
Hardware: Raspberry Pi (3B/4B/5), Protoboard, Jumpers, LEDs, Botões, ADC MCP3008 e um Sensor de Temperatura I2C.

Sistema Operacional: Raspberry Pi OS (Linux)

Linguagem: Python 3.x

**1. Habilitar Interfaces de Hardware**

Abra o terminal da Raspberry Pi e execute:
```bash
sudo raspi-config
```
Navegue até Interface Options e habilite o SPI e o I2C.

**2. Instalar Dependências**

Instale as bibliotecas Python necessárias para a interatividade com o hardware:
```bash
pip install gpiozero smbus2 spidev
```
## 🚀 Executando os Experimentos
Navegue até a pasta de qualquer experimento e execute o script principal:

```bash
# Exemplo: Executando o Experimento 01
cd exp01-digital-io
```
```bash
python3 main.py
```
Para detectar dispositivos I2C no barramento (usado no Experimento 04):
```bash
i2cdetect -y 1
```

