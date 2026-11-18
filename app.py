import tkinter as tk

window = tk.Tk()
window.title("Планировщик задач")
window.geometry("460x520")

img = tk.PhotoImage(file="Photo.png")
tk.Label(window, image=img).pack(pady=10)

tk.Label(window, text="Название задачи").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Длительность (дней)").pack()
duration_entry = tk.Entry(window)
duration_entry.pack()

count = 0

def add_task():
    global count
    count += 1
    counter.config(text=f"Задач добавлено: {count}")
    print(name_entry.get(), duration_entry.get())

def clear_fields():
    name_entry.delete(0, tk.END)
    duration_entry.delete(0, tk.END)

tk.Button(window, text="Добавить задачу", command=add_task).pack(pady=5)
tk.Button(window, text="Очистить поля", command=clear_fields).pack()

counter = tk.Label(window, text="Задач добавлено: 0")
counter.pack(pady=10)

window.mainloop()