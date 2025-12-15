import requests

identifier = 'BR'
indicator = '77822'
url = f'https://servicodados.ibge.gov.br/api/v1/paises/{identifier}/indicadores/{indicator}'

response = requests.get(url)
response.encoding = 'utf-8'
if response.status_code == 200:
  data = response.json()
  indicator_list = data[0]["indicador"].split("-")
  print(f'Área de estudo: {indicator_list[0]}')
  print(f'País estudado: {data[0]["series"][0]["pais"]["nome"]}')
  print(f'Indicador de interesse: {indicator_list[1]}')
  print('Série histórica:')
  serie = data[0]["series"][0]["serie"]
  for item in serie:
    for chave in item:
      ano = chave
      valor = item[ano]
      if valor is None:
        continue
      else:
        print(f'Ano: {ano} | %{valor}')      
else:
  print('failure')