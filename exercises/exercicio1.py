temperaturaCelsius = float(input("Informe a temperatura em °C: "))

temperaturaFahrenheit = temperaturaCelsius * 9/5 + 32
print(f"Temperatura em Fahrenheit: {temperaturaFahrenheit:.2f} °F")

if temperaturaCelsius < 0:
    print("Abaixo do ponto de congelamento da água.")