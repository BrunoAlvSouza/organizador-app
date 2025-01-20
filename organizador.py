import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def salvar_pasta_destino(pasta_destino):
    """
    Salva a pasta de destino em um arquivo para ser carregada posteriormente.
    """
    with open("config.txt", "w") as config:
        config.write(pasta_destino)

def carregar_pasta_destino():
    """
    Carrega a pasta de destino do arquivo de configuração, se existir.
    """
    if os.path.exists("config.txt"):
        with open("config.txt", "r") as config:
            return config.read().strip()
    return os.path.expanduser("~/Arquivos_Organizados")

def mover_com_renomeio(caminho_arquivo, pasta_destino):
    nome_arquivo = os.path.basename(caminho_arquivo)
    nome, extensao = os.path.splitext(nome_arquivo)
    destino = os.path.join(pasta_destino, nome_arquivo)

    contador = 1
    while os.path.exists(destino):
        novo_nome = f"{nome}_{contador}{extensao}"
        destino = os.path.join(pasta_destino, novo_nome)
        contador += 1

    shutil.move(caminho_arquivo, destino)
    print(f"Movido: {caminho_arquivo} -> {destino}")

def organizar_arquivos(pasta_origem, pasta_destino_base, extensoes):
    for extensao in extensoes:
        pasta_destino = os.path.join(pasta_destino_base, extensao.lstrip('.'))
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        
        for arquivo in os.listdir(pasta_origem):
            caminho_arquivo = os.path.join(pasta_origem, arquivo)
            if os.path.isfile(caminho_arquivo) and arquivo.endswith(extensao):
                mover_com_renomeio(caminho_arquivo, pasta_destino)

def apagar_pastas_vazias(pasta_origem):
    """
    Apaga todas as pastas vazias diretamente na pasta principal indicada.
    """
    for dir in os.listdir(pasta_origem):
        caminho_dir = os.path.join(pasta_origem, dir)
        if os.path.isdir(caminho_dir) and not os.listdir(caminho_dir):
            os.rmdir(caminho_dir)
            print(f"Removida pasta vazia: {caminho_dir}")
    messagebox.showinfo("Sucesso", "Pastas vazias na pasta principal foram removidas!")

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entry_pasta_origem.delete(0, tk.END)
        entry_pasta_origem.insert(0, pasta)

def selecionar_todas_extensoes():
    """
    Marca todas as extensões disponíveis.
    """
    for var in extensao_vars.values():
        var.set(True)

def executar():
    pasta_origem = entry_pasta_origem.get()
    pasta_destino_base = entry_pasta_destino.get()
    if not pasta_origem or not pasta_destino_base:
        messagebox.showerror("Erro", "Selecione as pastas de origem e destino!")
        return

    extensoes = [ext for ext, var in extensao_vars.items() if var.get()]
    if not extensoes:
        messagebox.showerror("Erro", "Selecione pelo menos uma extensão!")
        return

    try:
        organizar_arquivos(pasta_origem, pasta_destino_base, extensoes)
        salvar_pasta_destino(pasta_destino_base)
        messagebox.showinfo("Sucesso", "Arquivos organizados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao organizar arquivos: {e}")

# Criar a janela principal
root = tk.Tk()
root.title("Organizador de Arquivos")

# Pasta de origem
frame_origem = tk.Frame(root)
frame_origem.pack(pady=10)
tk.Label(frame_origem, text="Pasta de origem:").pack(side=tk.LEFT, padx=5)
entry_pasta_origem = tk.Entry(frame_origem, width=50)
entry_pasta_origem.pack(side=tk.LEFT, padx=5)
tk.Button(frame_origem, text="Selecionar", command=selecionar_pasta).pack(side=tk.LEFT)

# Pasta de destino
frame_destino = tk.Frame(root)
frame_destino.pack(pady=10)
tk.Label(frame_destino, text="Pasta fixa para organização:").pack(side=tk.LEFT, padx=5)
entry_pasta_destino = tk.Entry(frame_destino, width=50)
entry_pasta_destino.insert(0, carregar_pasta_destino())
entry_pasta_destino.pack(side=tk.LEFT, padx=5)

# Opções de extensões
frame_extensoes = tk.LabelFrame(root, text="Selecione as extensões")
frame_extensoes.pack(pady=10, padx=10, fill="both")

extensoes_disponiveis = [".txt", ".pdf", ".jpg", ".png", ".JPG", ".docx", ".log", ".doc", ".webp", ".xlsx", ".csv", ".xls", ".odt", ".ods", ".zip", ".rar", ".mp3", ".mp4", ".m4a", ".pptx", ".tar", ".PDF", ".psd", ".jpeg", ".odp"]
extensao_vars = {}
for ext in extensoes_disponiveis:
    var = tk.BooleanVar()
    tk.Checkbutton(frame_extensoes, text=ext, variable=var).pack(anchor=tk.W)
    extensao_vars[ext] = var

# Botões para executar
tk.Button(root, text="Organizar", command=executar).pack(pady=10)
tk.Button(root, text="Apagar Pastas Vazias", command=lambda: apagar_pastas_vazias(entry_pasta_origem.get())).pack(pady=10)
tk.Button(root, text="Selecionar Todas as Extensões", command=selecionar_todas_extensoes).pack(pady=10)

root.mainloop()
