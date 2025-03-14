import pytest
from datetime import datetime
from main import Note, Notebook

def test_note_creation():
    note = Note("Jan Kowalski", "Testowa notatka")
    assert note.author == "Jan Kowalski"
    assert note.content == "Testowa notatka"
    assert isinstance(note.creation_time, datetime)

def test_notebook_creation():
    notebook = Notebook()
    assert isinstance(notebook, Notebook)
    assert notebook.notes == []

def test_add_new_note_to_notebook():
    notebook = Notebook()
    notebook.dodaj_nowa("Jan Kowalski", "Nowa notatka")
    assert len(notebook.notes) == 1

def test_add_existing_note_to_notebook():
    notebook = Notebook()
    note = Note("Jan Kowalski", "Istniejąca notatka")
    notebook.dodaj(note)
    assert len(notebook.notes) == 1

def test_add_invalid_object_to_notebook():
    notebook = Notebook()
    with pytest.raises(ValueError):
        notebook.dodaj("Nieprawidłowy obiekt")

def test_count_notes_in_notebook():
    notebook = Notebook()
    notebook.dodaj_nowa("Jan Kowalski", "Pierwsza notatka")
    notebook.dodaj_nowa("Jan Kowalski", "Druga notatka")
    assert notebook.ile_notatek() == 2

def test_display_all_notes():
    notebook = Notebook()
    notebook.dodaj_nowa("Jan Kowalski", "Pierwsza notatka")
    notebook.dodaj_nowa("Jan Kowalski", "Druga notatka")
    result = notebook.wyswietl_wszystko()
    assert "Pierwsza notatka" in result
    assert "Druga notatka" in result

def test_display_empty_notebook():
    notebook = Notebook()
    assert notebook.wyswietl_wszystko() == "Notatnik jest pusty."
