import itertools
import string
import tkinter as tk
from tkinter import messagebox, ttk
import pyfiglet
from typing import Optional, Tuple

class DictionaryGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Générateur de dictionnaire - Pro")
        self.master.geometry("700x400")
        self.master.resizable(False, False)
        
        # Couleurs
        self.bg_color = "#0F0F1E"
        self.widget_bg = "#1F1F3B"
        self.text_color = "#EAEAEA"
        self.accent_color = "#00D1D1"
        self.error_color = "#FF4C61"
        self.success_color = "#00D1D1"
        self.button_color = self.accent_color
        
        self.master.configure(bg=self.bg_color)
        
        # Style
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabel", background=self.bg_color, foreground=self.text_color, font=("Segoe UI", 10))
        self.style.configure("TEntry", fieldbackground=self.widget_bg, foreground=self.text_color, insertcolor=self.accent_color)
        self.style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
        self.style.map("TButton",
            background=[("active", self.accent_color)],
            foreground=[("active", "black")]
        )

        # Header
        self.header_frame = ttk.Frame(master)
        self.header_frame.pack(pady=10)

        # Header text
        ascii_banner = pyfiglet.figlet_format("DICT-GENERATOR")
        self.header_text = tk.Text(self.header_frame, 
                                height=6, 
                                bg=self.bg_color,
                                fg=self.accent_color, 
                                font=("Courier", 10), 
                                bd=0,
                                relief="flat")
        self.header_text.insert(tk.END, ascii_banner)
        self.header_text.configure(state="disabled")  # Lecture seule
        self.header_text.pack()


        # Ligne séparatrice
        ttk.Separator(master, orient='horizontal').pack(fill='x', padx=20, pady=5)

        # Cadre principal centré
        self.card = ttk.Frame(master, style="TFrame")
        self.card.pack(pady=30)

        # Inputs
        self.length_frame = ttk.Frame(self.card)
        self.length_frame.pack(pady=10)

        self.min_length_label = ttk.Label(self.length_frame, text="Longueur minimale :")
        self.min_length_label.grid(row=0, column=0, padx=10, pady=8, sticky="e")
        self.min_length_entry = ttk.Entry(self.length_frame, width=8)
        self.min_length_entry.grid(row=0, column=1, padx=10, pady=8)

        self.max_length_label = ttk.Label(self.length_frame, text="Longueur maximale :")
        self.max_length_label.grid(row=1, column=0, padx=10, pady=8, sticky="e")
        self.max_length_entry = ttk.Entry(self.length_frame, width=8)
        self.max_length_entry.grid(row=1, column=1, padx=10, pady=8)

        # Bouton
        self.button_frame = ttk.Frame(self.card)
        self.button_frame.pack(pady=20)

        self.generate_button = ttk.Button(
            self.button_frame,
            text="🔄 Générer le dictionnaire",
            command=self.generate_dictionary
        )
        self.generate_button.pack()

        # Barre de statut
        self.status_var = tk.StringVar()
        self.status_bar = tk.Label(
            master,
            textvariable=self.status_var,
            anchor="w",
            bg=self.widget_bg,
            fg=self.success_color,
            font=("Segoe UI", 9),
            relief="sunken",
            bd=1
        )
        self.status_bar.pack(side="bottom", fill="x")
        self.update_status("✅ Prêt")

    def update_status(self, message: str, error: bool = False):
        self.status_var.set(message)
        self.status_bar.config(fg=self.error_color if error else self.success_color)

    def validate_inputs(self) -> Optional[Tuple[int, int]]:
        try:
            min_len = int(self.min_length_entry.get())
            max_len = int(self.max_length_entry.get())

            if min_len <= 0 or max_len <= 0:
                raise ValueError("Les longueurs doivent être positives")

            if min_len > max_len:
                raise ValueError("La longueur minimale doit être inférieure ou égale à la maximale")

            if max_len > 10:
                if not messagebox.askyesno(
                    "Avertissement",
                    f"Un dictionnaire de longueur {max_len} peut être très volumineux.\nVoulez-vous continuer ?"
                ):
                    return None

            return min_len, max_len

        except ValueError as e:
            self.update_status(f"❌ {str(e)}", error=True)
            messagebox.showerror("Erreur de saisie", str(e))
            return None

    def generate_dictionary(self):
        valid_lengths = self.validate_inputs()
        if not valid_lengths:
            return

        min_len, max_len = valid_lengths
        output_file = "dict.txt"

        try:
            self.generate_button.config(state="disabled")
            self.update_status("⏳ Génération en cours...")
            self.master.update()

            with open(output_file, "w", encoding="utf-8") as f:
                for length in range(min_len, max_len + 1):
                    for word in itertools.product(string.ascii_letters + string.digits, repeat=length):
                        f.write("".join(word) + "\n")

            self.update_status("✅ Dictionnaire généré avec succès !")
            messagebox.showinfo("Succès", f"Fichier généré : {output_file}")

        except Exception as e:
            self.update_status(f"❌ Erreur: {str(e)}", error=True)
            messagebox.showerror("Erreur", f"Une erreur est survenue :\n{str(e)}")

        finally:
            self.generate_button.config(state="normal")

def main():
    root = tk.Tk()
    app = DictionaryGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
