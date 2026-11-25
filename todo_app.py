import tkinter as tk
from tkinter import messagebox, filedialog
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="To-Do List", font=("Helvetica", 18, "bold"))
        title.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10, padx=10, fill=tk.X)
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Buttons Frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        add_btn = tk.Button(btn_frame, text="Add Task", command=self.add_task, width=12)
        del_btn = tk.Button(btn_frame, text="Delete Task", command=self.delete_task, width=12)
        save_btn = tk.Button(btn_frame, text="Save Tasks", command=self.save_tasks, width=12)
        load_btn = tk.Button(btn_frame, text="Load Tasks", command=self.load_tasks, width=12)

        add_btn.grid(row=0, column=0, padx=5)
        del_btn.grid(row=0, column=1, padx=5)
        save_btn.grid(row=1, column=0, padx=5, pady=5)
        load_btn.grid(row=1, column=1, padx=5, pady=5)

        # Task List
        self.task_listbox = tk.Listbox(self.root, font=("Helvetica", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(self.task_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        if tasks:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, "w") as file:
                    for task in tasks:
                        file.write(task + "\n")
                messagebox.showinfo("Saved", "Tasks saved successfully.")
        else:
            messagebox.showinfo("Nothing to Save", "There are no tasks to save.")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path and os.path.exists(file_path):
            with open(file_path, "r") as file:
                tasks = file.readlines()
            self.task_listbox.delete(0, tk.END)
            for task in tasks:
                self.task_listbox.insert(tk.END, task.strip())

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
