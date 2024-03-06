import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox
import pyperclip  # Libreria per copiare negli appunti

# Funzione per sostituire i parametri nel testo originale
def sostituisci_parametri(percorso_immagine, nome_gioco, nome_abbreviato, descrizione, link):
    testo_originale = '''
    <figure class="swiper-slide">
          
                    <div class="cardPopout" data-swiper-parallax="30" data-swiper-parallax-scale="0.9" data-swiper-parallax-opacity="0.8" data-swiper-parallax-duration="1000">
          
                      <img src="image6.jpg" alt="Naruto ultimate storm connection" width="800" height="400" data-swiper-parallax="80" data-swiper-parallax-duration="2000">
          
                      <h2 class="title" data-swiper-parallax="80" data-swiper-parallax-duration="1000">
                        USC
                      </h2>
          
                      <h4 class="subtitle" data-swiper-parallax="80" data-swiper-parallax-duration="1500">
                        ULTIMATE STORM CONNECTION
                      </h4>
          
                      <figcaption data-swiper-parallax="80" data-swiper-parallax-duration="1250">
          
                        <p>
                            Con una grafica eccezionale e sequenze d'intermezzo spettacolari, il gioco offre una modalità storia che riprende gli eventi classici della serie Naruto, insieme a una storia inedita scritta appositamente per il gioco.
                        </p>
          
                      </figcaption>
          
                      <a href="javascript:void(0);" title="Scarica ora" data-swiper-parallax="80" data-swiper-parallax-opacity="0.2" data-swiper-parallax-duration="1750">
                        Scarica ora!
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-short" viewBox="0 0 16 16">
                          <path fill-rule="evenodd" d="M4 8a.5.5 0 0 1 .5-.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5A.5.5 0 0 1 4 8" />
                        </svg>
                      </a>
          
                    </div>
          
                </figure>
    '''
    
    testo_modificato = testo_originale.replace("image6.jpg", percorso_immagine)
    testo_modificato = testo_modificato.replace("Naruto ultimate storm connection", nome_gioco)
    testo_modificato = testo_modificato.replace("ULTIMATE STORM CONNECTION", nome_gioco)
    testo_modificato = testo_modificato.replace("USC", nome_abbreviato)
    testo_modificato = testo_modificato.replace("Con una grafica eccezionale e sequenze d'intermezzo spettacolari, il gioco offre una modalità storia che riprende gli eventi classici della serie Naruto, insieme a una storia inedita scritta appositamente per il gioco.", descrizione)
    testo_modificato = testo_modificato.replace('javascript:void(0);', link)
    
    return testo_modificato

# Funzione per copiare il testo negli appunti
def copy_to_clipboard(text):
    pyperclip.copy(text)
    tkinter.messagebox.showinfo("Copiato negli Appunti", "L'output è stato copiato negli appunti!")

# Creazione dell'interfaccia grafica
root = tk.Tk()
root.withdraw() # Nasconde la finestra principale

# Richiesta dei dati all'utente
percorso_immagine = simpledialog.askstring("Inserisci il percorso dell'immagine", "Percorso immagine:")
nome_gioco = simpledialog.askstring("Inserisci il nome del gioco", "Nome del gioco:")
nome_abbreviato = simpledialog.askstring("Inserisci il nome abbreviato", "Nome abbreviato:")
descrizione = simpledialog.askstring("Inserisci la descrizione del gioco", "Descrizione:")
link = simpledialog.askstring("Inserisci il link", "Link:")

# Generazione del testo modificato
testo_finale = sostituisci_parametri(percorso_immagine, nome_gioco, nome_abbreviato, descrizione, link)

# Visualizzazione dell'output in una finestra grafica
output_window = tk.Tk()
output_window.title("Output Modificato")
output_label = tk.Label(output_window, text=testo_finale)
output_label.pack()

# Bottone per copiare l'output negli appunti
copy_button = tk.Button(output_window, text="Copia Output", command=lambda: copy_to_clipboard(testo_finale))
copy_button.pack()

# Loop principale per mantenere aperta la finestra grafica
output_window.mainloop()