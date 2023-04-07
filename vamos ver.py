"""
pip install requests #Instalar a biblioteca
"""
from selenium import webdriver
from time import * # Da um tempo p\ carregar


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Essa biblioteca nativamente te opriga a baixar o Webdriver do Navegadir
#Chrome---> chromedriver Firefox--->geckodriver
#Linhas de codigos PAD. para não da erro e atualizar sozinho de cada navegador, sempre igaul p\ usar Selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
navegador = webdriver.Chrome(service=servico)  #Rodando o  WebDriver do codigo, ñ algum que esteja instalado no computador
#Entrar no Navegador
link = 'https://www.gov.br/compras/pt-br'
navegador.get(url=link)
sleep(10)
#passo2
navegador.maximize_window()
sleep(1)
navegador.find_element('xpath', '//*[@id="sso-status-bar"]/section[1]').click()
sleep(100)
#\\\\\\\\\\\\\\\\\\\\\\\\\ Fazer um request da Pagina ////////////////////////////////
"""res = requests.get('https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublicaExibir.asp')
res.enconding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')
dados = soup.find_all('div', attrs={'class": "clConteudoDados'})"""
#PARA SABER SE O SITE PERMITE QUE VOCÊ MEXA COM ROBO COLOQUE
#           AO FINAL DO LIIIIIINK /robots.txt



"""print(soup)"""

pass