import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def open_website():
    url = url_entry.get()
    driver = webdriver.Chrome(executable_path=r"C:\Users\202103049648\Desktop\Sistema-Edital\chromedriver")
    #driver.get("https://"+url)
    driver.get("https://www.gov.br/compras/pt-br")
    sleep(10)
    #passo2
    navegador.maximize_window()
    navegador.find_element('xpath', '//*[@id="searchtext-input"]').send_keys("24062003")
    sleep(1)
    navegador.find_element('xpath', '//*[@id="searchtext-label"]/button').click()
    sleep(10)
root = tk.Tk()
root.title("Acessar Página")

url_label = tk.Label(root, text="Insira a URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

access_button = tk.Button(root, text="Acessar Página", command=open_website)
access_button.pack()

root.mainloop()
