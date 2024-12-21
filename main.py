import os

# Datei zum Speichern der Aufgaben
TASKS_FILE = "tasks.txt"

# Funktion zum Laden der Aufgaben aus einer Datei
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = file.readlines()
            tasks = [task.strip() for task in tasks]  # Aufgaben bereinigen
            return tasks
    return []

# Funktion zum Speichern der Aufgaben in einer Datei
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Funktion zum Anzeigen des Menüs
def display_menu():
    print("\n==== To-Do Liste ====")
    print("1. Aufgaben anzeigen")
    print("2. Aufgabe hinzufügen")
    print("3. Aufgabe als erledigt markieren")
    print("4. Aufgabe löschen")
    print("5. Beenden")
    print("=====================")

# Funktion zum Anzeigen aller Aufgaben
def view_tasks(tasks):
    if not tasks:
        print("\nIhre To-Do Liste ist leer!")
    else:
        print("\nIhre To-Do Liste:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Funktion zum Hinzufügen einer neuen Aufgabe
def add_task(tasks):
    task = input("\nGeben Sie die Aufgabe ein, die Sie hinzufügen möchten: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Aufgabe '{task}' wurde zur Liste hinzugefügt!")

# Funktion zum Markieren einer Aufgabe als erledigt
def mark_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nGeben Sie die Aufgabennummer ein, die Sie als erledigt markieren möchten: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] += " [Erledigt]"
            save_tasks(tasks)
            print(f"Aufgabe '{tasks[task_num - 1]}' wurde als erledigt markiert!")
        else:
            print("Ungültige Aufgabennummer!")
    except ValueError:
        print("Bitte geben Sie eine gültige Aufgabennummer ein!")

# Funktion zum Löschen einer Aufgabe
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("\nGeben Sie die Aufgabennummer ein, die Sie löschen möchten: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Aufgabe '{removed_task}' wurde gelöscht!")
        else:
            print("Ungültige Aufgabennummer!")
    except ValueError:
        print("Bitte geben Sie eine gültige Aufgabennummer ein!")

# Hauptfunktion, um die To-Do List Anwendung auszuführen
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        try:
            choice = int(input("\nGeben Sie Ihre Wahl (1-5) ein: "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                mark_done(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Auf Wiedersehen!")
                break
            else:
                print("Ungültige Wahl! Bitte wählen Sie eine Zahl zwischen 1 und 5.")
        except ValueError:
            print("Bitte geben Sie eine gültige Wahl ein.")

if __name__ == "__main__":
    main()
