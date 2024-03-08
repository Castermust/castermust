import tkinter as tk
import pyperclip

# Funzione per sostituire il numero nelle stringhe
def replace_number_in_string(text, old_number, new_number):
    return text.replace(str(old_number), str(new_number))

# Funzione per chiedere all'utente di inserire un nuovo titolo e sostituire nelle stringhe
def replace_game_title(text, old_title, new_title):
    return text.replace(old_title, new_title)

# Funzione per generare il testo con le sostituzioni e copiarlo negli appunti
def generate_and_copy_html():
    old_number = 8
    old_link = "https://t.ly/PhUCc"
    image_link = f"<a href=\"{old_link}\" onclick=\"openPopup('../image{old_number}.jpg', 'Banishers Ghost of new Eden', 'description{old_number}.txt')\"><img src=\"../image{old_number}.jpg\" alt=\"Banishers - Ghost of New Eden\" class=\"zoom-effect\"></a>"

    new_number = new_number_entry.get()
    new_title = new_title_entry.get()
    new_link = new_link_entry.get()

    new_image_link = replace_number_in_string(image_link, old_number, new_number)
    new_image_link = replace_game_title(new_image_link, "Banishers Ghost of new Eden", new_title)
    new_image_link = new_image_link.replace(old_link, new_link)
    new_image_link = new_image_link.replace("Banishers - Ghost of New Eden", new_title)

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, new_image_link)
    pyperclip.copy(new_image_link)

# Creazione dell'interfaccia grafica
root = tk.Tk()
root.title("Generatore di Codice HTML")

tk.Label(root, text="Nuovo Numero:").pack()
new_number_entry = tk.Entry(root)
new_number_entry.pack()

tk.Label(root, text="Nuovo Titolo del Gioco:").pack()
new_title_entry = tk.Entry(root)
new_title_entry.pack()

tk.Label(root, text="Nuovo Link:").pack()
new_link_entry = tk.Entry(root)
new_link_entry.pack()

generate_button = tk.Button(root, text="Genera e Copia HTML", command=generate_and_copy_html)
generate_button.pack()

output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()
