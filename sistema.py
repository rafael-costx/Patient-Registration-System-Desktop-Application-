import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# ---------------------------
# Configuração do banco de dados
# ---------------------------
conn = sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    telefone TEXT,
    caso TEXT
)
""")
conn.commit()

# ---------------------------
# Funções do sistema
# ---------------------------
def adicionar_paciente():
    nome = entry_nome.get().strip()
    idade = entry_idade.get().strip()
    telefone = entry_telefone.get().strip()
    caso = entry_caso.get().strip()

    if nome == "":
        messagebox.showwarning("Erro", "O nome é obrigatório!")
        return

    if idade and not idade.isdigit():
        messagebox.showwarning("Erro", "Idade deve ser um número.")
        return

    idade = int(idade) if idade else None

    cursor.execute("INSERT INTO pacientes (nome, idade, telefone, caso) VALUES (?, ?, ?, ?)",
                   (nome, idade, telefone, caso))
    conn.commit()
    messagebox.showinfo("Sucesso", f"Paciente {nome} cadastrado com sucesso!")
    limpar_campos()
    listar_pacientes()

def listar_pacientes():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM pacientes")
    for paciente in cursor.fetchall():
        tree.insert("", "end", values=paciente)

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    entry_caso.delete(0, tk.END)

def deletar_paciente():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Erro", "Selecione um paciente para deletar.")
        return
    paciente_id = tree.item(selected_item)['values'][0]
    cursor.execute("DELETE FROM pacientes WHERE id=?", (paciente_id,))
    conn.commit()
    messagebox.showinfo("Sucesso", "Paciente deletado!")
    listar_pacientes()

# ---------------------------
# Interface gráfica
# ---------------------------
root = tk.Tk()
root.title("Sistema de Cadastro de Pacientes")
root.geometry("750x450")
root.resizable(False, False)

# Frame principal
frame_main = tk.Frame(root, padx=10, pady=10)
frame_main.pack(fill=tk.BOTH, expand=True)

# Frame do formulário (à esquerda)
frame_form = tk.Frame(frame_main)
frame_form.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))

tk.Label(frame_form, text="Nome").grid(row=0, column=0, sticky="w", pady=5)
entry_nome = tk.Entry(frame_form, width=40)
entry_nome.grid(row=0, column=1, pady=5)

tk.Label(frame_form, text="Idade").grid(row=1, column=0, sticky="w", pady=5)
entry_idade = tk.Entry(frame_form, width=40)
entry_idade.grid(row=1, column=1, pady=5)

tk.Label(frame_form, text="Telefone").grid(row=2, column=0, sticky="w", pady=5)
entry_telefone = tk.Entry(frame_form, width=40)
entry_telefone.grid(row=2, column=1, pady=5)

tk.Label(frame_form, text="Caso").grid(row=3, column=0, sticky="w", pady=5)
entry_caso = tk.Entry(frame_form, width=40)
entry_caso.grid(row=3, column=1, pady=5)

# Frame dos botões (à direita do formulário)
frame_botoes = tk.Frame(frame_main)
frame_botoes.pack(side=tk.LEFT, fill=tk.Y)

tk.Button(frame_botoes, text="Adicionar Paciente", width=20, command=adicionar_paciente).pack(pady=10)
tk.Button(frame_botoes, text="Deletar Paciente", width=20, command=deletar_paciente).pack(pady=10)

# Frame da lista de pacientes (embaixo)
frame_list = tk.Frame(root, padx=10, pady=10)
frame_list.pack(fill=tk.BOTH, expand=True)

cols = ("ID", "Nome", "Idade", "Telefone", "Caso")
tree = ttk.Treeview(frame_list, columns=cols, show="headings", height=10)
for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")
tree.pack(fill=tk.BOTH, expand=True)

listar_pacientes()
root.mainloop()