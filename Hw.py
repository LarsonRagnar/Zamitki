import tkinter as tk
from tkinter import messagebox, simpledialog


class NotesApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Заметки")

        self.notes_listbox = tk.Listbox(self.root, width=50)
        self.notes_listbox.pack(pady=10)

        self.new_note_button = tk.Button(self.root, text="Новая заметка", command=self.create_note)
        self.new_note_button.pack()

        self.edit_note_button = tk.Button(self.root, text="Редактировать заметку", command=self.edit_note)
        self.edit_note_button.pack()

        self.delete_note_button = tk.Button(self.root, text="Удалить заметку", command=self.delete_note)
        self.delete_note_button.pack()

        # загрузка списка заметок из файла
        self.load_notes()

    def run(self):
        self.root.mainloop()

    def load_notes(self):
        try:
            with open("notes.txt", "r") as file:
                notes = file.readlines()
                for note in notes:
                    self.notes_listbox.insert(tk.END, note.strip())
        except FileNotFoundError:
            pass

    def save_notes(self):
        with open("notes.txt", "w") as file:
            for i in range(self.notes_listbox.size()):
                file.write(self.notes_listbox.get(i) + "\n")

    def create_note(self):
        note = simpledialog.askstring("Новая заметка", "Введите текст заметки:")
        if note:
            self.notes_listbox.insert(tk.END, note)
            self.save_notes()

    def edit_note(self):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            note = simpledialog.askstring("Редактировать заметку", "Измените текст заметки:",
                                          initialvalue=self.notes_listbox.get(selected_index))
            if note:
                self.notes_listbox.delete(selected_index)
                self.notes_listbox.insert(selected_index, note)
                self.save_notes()

    def delete_note(self):
        selected_index = self.notes_listbox.curselection()
        if selected_index:
            self.notes_listbox.delete(selected_index)
            self.save_notes()


if __name__ == "__main__":
    app = NotesApp()
    app.run()