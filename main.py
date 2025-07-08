import xmltodict
import customtkinter
from pegar_moeda import pegar_moeda

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

with open('moedas.xml', 'rb') as file:
    dict_moeda = xmltodict.parse(file)
    moedas = dict_moeda["xml"]
    currency_codes = list(moedas.keys())
    
app = customtkinter.CTk()
app.geometry("500x700")

titulo = customtkinter.CTkLabel(app, text="Conversor De Moedas", font=("", 32))
titulo.pack(padx="10", pady="10")

def converter_moeda():
    moeda_origem = campo_origem.get().upper()
    moeda_destino = campo_destino.get().upper()
    
    try:
        cotacao = pegar_moeda(moeda_origem, moeda_destino)
        valor = float(campo_valor.get())
        convertido = valor * float(cotacao)
        texto_resultado.configure(text=f"{moeda_origem} {valor} = {moeda_destino} {convertido:.2f}")
    except ValueError:
        texto_resultado.configure(text="Erro: Valor Inválido")
    except Exception as e:
        texto_resultado.configure(text=f"Erro: Essa moeda não existe,\nou essa conversão\nnão é possível!")

texto_moeda_origem = customtkinter.CTkLabel(app, text="Digite a Moeda de Origem")
texto_moeda_origem.pack(pady="30")
campo_origem = customtkinter.CTkEntry(app, placeholder_text="e.g. BRL, USD, EUR...", width=200)
campo_origem.pack()

texto_moeda_destino = customtkinter.CTkLabel(app, text="Digite a Moeda de Destino")
texto_moeda_destino.pack(pady="30")
campo_destino = customtkinter.CTkEntry(app, placeholder_text="e.g. BRL, USD, EUR...", width=200)
campo_destino.pack()

texto_valor = customtkinter.CTkLabel(app, text="Digite o valor a converter")
texto_valor.pack(padx="50", pady="50")
campo_valor = customtkinter.CTkEntry(app, placeholder_text="e.g. 10, 25, 50...", width=200)
campo_valor.pack()

botao_convert = customtkinter.CTkButton(app, text="Converter", command=converter_moeda, corner_radius=5)
botao_convert.pack(padx="10", pady="10")

texto_resultado = customtkinter.CTkLabel(app, text="", font=("", 26))
texto_resultado.pack(padx="40", pady="40")

app.mainloop()