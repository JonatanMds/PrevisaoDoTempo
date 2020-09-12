import requests
import json


cidade = input('Digite o nome da sua cidade cidade: ')

#URL da api utilizada e sua chave de acesso.
req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=75cd523398152201e9e42dd3a0711bb5')

#tranformando json em um objeto to python(transformando em um dicionario)
temp = json.loads(req.text)
#print(req.text)

#Previsao do tempo separadas por temperatura
if temp['main']['temp']-273.15 < 15:#passagem de kelvin para celsius
    print(temp['weather'][0]['description'],'\033[1;104m   \033[m')#pegando o intem '0' da lista weather
    print(round((temp['main']['temp'])-273.15),'°C')#passagem de kelvin para celsius
    print('Vento: ',temp['wind']['speed'],'km/h')
    print(temp['weather'][0]['main'])
    print('Humidade: ',temp['main']['humidity'],'%')
    print('Pressão: ',temp['main']['pressure'],'hPA')

elif temp['main']['temp']-273.15 >= 35:
    print(temp['weather'][0]['description'],'\033[1;41m   \033[m')
    print(round((temp['main']['temp']) - 273.15), '°C')
    print('Vento: ', temp['wind']['speed'], 'km/h')
    print(temp['weather'][0]['main'])
    print('Humidade: ', temp['main']['humidity'], '%')
    print('Pressão: ', temp['main']['pressure'], 'hPA')


else:
    print(temp['weather'][0]['description'],'\033[1;43m   \033[m')
    print(round((temp['main']['temp']) - 273.15), '°C')
    print('Vento: ', temp['wind']['speed'], 'km/h')
    print('Humidade: ', temp['main']['humidity'], '%')
    print('Pressão: ', temp['main']['pressure'], 'hPA')

