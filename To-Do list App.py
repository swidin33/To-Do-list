import tkinter as tk
from tkinter import ttk, messagebox

class App(tk.Tk):
    def __init__(self, tasks):
        super().__init__()
        self.title("To-Do list App")


        self.tasks = []

        self.label = ttk.Label(self, text="To-Do list", font=("Aerial", 20))
        self.label.grid(row=0, column=0, columnspan=5, pady=15)

        self.combobox = ttk.Combobox(self, values=tasks, state="readonly", font=("Aerial", 20))
        self.combobox.grid(row=1, column=0)
        self.combobox.set("Tasks")

        self.label_add = ttk.Label(self, text="Add Tasks", font=("Aerial", 14),)
        self.label_add.grid(row=1, column=1)

        self.entry_add = ttk.Entry(self, width=25)
        self.entry_add.grid(row=1, column=2, columnspan=2)

        self.btn_add = ttk.Button(self, text="Add", command=self.add_tasks)
        self.btn_add.grid(row=1, column=4, padx=5, pady=5)

        self.label_remove = ttk.Label(self, text="Remove Tasks", font=("Aerial", 14))
        self.label_remove.grid(row=2, column=1)

        self.label_remove2 = ttk.Label(self, text="(Pick task index)", font=("Aerial", 14))
        self.label_remove2.grid(row=2, column=2)

        self.entry_remove = ttk.Entry(self, width=10)
        self.entry_remove.grid(row=2, column=3)

        self.btn_remove = ttk.Button(self, text="Remove", command=self.remove_tasks)
        self.btn_remove.grid(row=2, column=4, padx=5, pady=5)

        self.label_mark = ttk.Label(self, text="Mark Tasks", font=("Aerial", 14))
        self.label_mark.grid(row=3, column=1)

        self.label_mark2 = ttk.Label(self, text="(Pick task index)", font=("Aerial", 14))
        self.label_mark2.grid(row=3, column=2)

        self.entry_mark = ttk.Entry(self, width=10)
        self.entry_mark.grid(row=3, column=3)

        self.btn_mark = ttk.Button(self, text="Mark", command=self.mark_tasks)
        self.btn_mark.grid(row=3, column=4, padx=5, pady=5)

    def refresh_tasks(self):
        numbered_tasks = []
        for i, task in enumerate(self.tasks, start=1):
            numbered_tasks.append(f"{i}. {task}")
        self.combobox["values"] = numbered_tasks
        self.combobox.set("Tasks")


    def add_tasks(self):
        task = self.entry_add.get()
        if task:
            self.tasks.append(task)
            self.refresh_tasks()
            self.entry_add.delete(0, tk.END)

    def remove_tasks(self):

            try:
                task_to_remove = int(self.entry_remove.get()) - 1
                if 0 <= task_to_remove < len(self.tasks):
                    self.tasks.pop(task_to_remove)
                    self.refresh_tasks()
                    self.entry_remove.delete(0, tk.END)
                else:
                    messagebox.showerror("Error!", "Invalid task index")
            except ValueError:
                messagebox.showerror("Error!", "Invalid task index")

    def mark_tasks(self):
        try:
            task_to_mark = int(self.entry_mark.get()) - 1
            if 0 <= task_to_mark < len(self.tasks):
                if not self.tasks[task_to_mark].endswith(" (Completed)"):
                    self.tasks[task_to_mark] += " (Completed)"
                    self.refresh_tasks()
                    self.entry_mark.delete(0, tk.END)
                else:
                    messagebox.showerror("Error!", "The task is already completed")
            else:
                messagebox.showerror("Error!", "Invalid task index")
        except ValueError:
            messagebox.showerror("Error!", "Invalid task index")

app = App(tasks=[])
app.mainloop()