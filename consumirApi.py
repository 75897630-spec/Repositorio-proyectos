import requests

URL = "http://10.121.16.118:7010/api/enviar"

# Estructura de datos a enviar
datos = { "imagen": [153,90,60,36,36,60,90,153] }  
  

# Usamos POST y pasamos json=datos (verify=False ignora errores de certificado SSL si la IP es local/HTTPS de prueba)
response = requests.post(URL, json=datos, verify=False)

if response.status_code == 200:
    print('Solicitud exitosa')
    print('Data:', response.json())
else:
    print('Error en la solicitud, detalles:', response.text)