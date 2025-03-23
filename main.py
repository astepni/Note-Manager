import datetime

class Note:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.creation_time = datetime.datetime.now()

    def __str__(self):
        return f"{self.author}: \"{self.content}\" o godzinie {self.creation_time.hour:02}:{self.creation_time.minute:02}"

class Notebook:
    def __init__(self):
        self.notes = []

    def dodaj_nowa(self, author, content):
        new_note = Note(author, content)
        self.notes.append(new_note)

    def dodaj(self, note):
        if isinstance(note, Note):
            self.notes.append(note)
        else:
            raise ValueError("Obiekt nie jest instancją klasy Note")

    def ile_notatek(self):
        return len(self.notes)

    def wyswietl_wszystko(self):
        if not self.notes:
            return "Notatnik jest pusty."
        return "Masz takie notatki:\n" + '\n'.join([f'{i + 1}. {note}' for i, note in enumerate(self.notes)])

# Przykład użycia
if __name__ == "__main__":
    # Tworzenie nowego notatnika
    nb = Notebook()

    # Dodanie nowej notatki
    nb.dodaj_nowa("Bartek", "Dokonczyc instrukcje")

    # Wyświetlenie notatek
    print(nb.wyswietl_wszystko())

    # Tworzenie nowej notatki
    n1 = Note("Andrii", "Sprawdzic instrukcje ")

    # Dodanie istniejącej notatki
    nb.dodaj(n1)

    # Wyświetlenie wszystkich notatek
    print(nb.wyswietl_wszystko())
