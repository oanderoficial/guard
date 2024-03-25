import tkinter as tk
import tkinter.messagebox as messagebox
import os
from tkinter import filedialog

def decompile_manifest():
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal

    file_path = filedialog.askopenfilename(title="Selecionar arquivo APK", filetypes=[("APK files", "*.apk")])

    if file_path:
        try:
            os.system(f'androaxml {file_path}')
            messagebox.showinfo("Sucesso", "AndroidManifest.xml foi descompilado com sucesso!")
            os.system('clear')
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao descompilar: {str(e)}")

def decompile_resources():
    root = tk.Tk()
    root.withdraw()  # Esconder a janela principal

    file_path = filedialog.askopenfilename(title="Selecionar arquivo APK", filetypes=[("APK files", "*.apk")])

    if file_path:
        try:
            os.system(f'androarsc {file_path} ')
            messagebox.showinfo("Sucesso", "resources.arsc foi descompilado com sucesso!")
            os.system('clear')
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao descompilar: {str(e)}")

def sign_apk():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Selecionar arquivo APK", filetypes=[("APK files", "*.apk")])

    if file_path:
        try:
            os.system(f'androsign {file_path}')
            messagebox.showinfo("Sucesso", "O APK foi assinado digitalmente com sucesso!")
            os.system('clear')
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao assinar o APK: {str(e)}")

while True:
    print("""
     ______        __  __        ______        ______        _____    
    /\  ___\      /\ \/\ \      /\  __ \      /\  == \      /\  __-.  
    \ \ \__ \     \ \ \_\ \     \ \  __ \     \ \  __<      \ \ \/\ \ 
     \ \_____\     \ \_____\     \ \_\ \_\     \ \_\ \_\     \ \____- 
      \/_____/      \/_____/      \/_/\/_/      \/_/ /_/      \/____/

      by: Anderson B silva (@oanderoficial) - V 1.0 
    """)

    print("1 - Descompilar o arquivo AndroidManifest.xml do APK.")
    print("2 - Descompilar o arquivo resources.arsc do APK.")
    print("3 - Assinar digitalmente um arquivo APK.")
    print("5 - Sair ")

    menu = input("Digite uma opção:")

    if menu == "1":
        decompile_manifest()

    elif menu == "2":
        decompile_resources()

    elif menu =="3": 
        sign_apk()

    elif menu == "5":
        print("Saindo...")
        break
