import tkinter as tk
from tkinter import messagebox
import subprocess

def run_ansible_task(task_name):
    ansible_command = f"ansible-playbook {task_name}.yml"
    subprocess.run(ansible_command, shell=True)

def execute_selected_tasks(root, choices):
    for choice in choices:
        if choice == "1":
            run_ansible_task("message")
        elif choice == "2":
            run_ansible_task("install_tree")
        elif choice == "3":
            run_ansible_task("new")
        elif choice.lower() == "q":
            messagebox.showinfo("Information", "Merci d'avoir utilisé le menu Ansible.")
            root.destroy()  # Fermer la fenêtre si l'utilisateur choisit de quitter
        else:
            messagebox.showerror("Erreur", f"Option invalide : {choice}")

def main():
    root = tk.Tk()
    root.title("Menu de sélection Ansible")

    label = tk.Label(root, text="Veuillez sélectionner une ou plusieurs options :")
    label.pack()

    options = [("Installer l'application", "1"),
               ("Mettre à jour l'application", "2"),
               ("new", "3"),
               ("Quitter", "q")]

    choices = []

    for text, value in options:
        var = tk.IntVar()
        cb = tk.Checkbutton(root, text=text, variable=var, onvalue=1, offvalue=0)
        cb.pack()
        choices.append((value, var))

    button = tk.Button(root, text="Exécuter", command=lambda: execute_selected_tasks(root, [choice for choice, var in choices if var.get()]))
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
