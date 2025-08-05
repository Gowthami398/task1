import tkinter as tk
from tkinter import messagebox, ttk
import json
from datetime import datetime
import os

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        # Data storage
        self.tasks = []
        self.load_tasks()
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="My Daily Work - To-Do List", 
                             font=("Arial", 16, "bold"), bg='#f0f0f0', fg='#333')
        title_label.pack(pady=10)
        
        # Input frame
        input_frame = tk.Frame(self.root, bg='#f0f0f0')
        input_frame.pack(pady=10, padx=20, fill='x')
        
        # Task entry
        tk.Label(input_frame, text="Task:", bg='#f0f0f0', font=("Arial", 10)).pack(anchor='w')
        self.task_entry = tk.Entry(input_frame, font=("Arial", 12), width=40)
        self.task_entry.pack(pady=5, fill='x')
        
        # Priority selection
        tk.Label(input_frame, text="Priority:", bg='#f0f0f0', font=("Arial", 10)).pack(anchor='w', pady=(10,0))
        self.priority_var = tk.StringVar(value="Medium")
        priority_frame = tk.Frame(input_frame, bg='#f0f0f0')
        priority_frame.pack(pady=5)
        
        priorities = [("High", "High"), ("Medium", "Medium"), ("Low", "Low")]
        for text, value in priorities:
            tk.Radiobutton(priority_frame, text=text, variable=self.priority_var, 
                          value=value, bg='#f0f0f0', font=("Arial", 10)).pack(side='left', padx=10)
        
        # Buttons frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Add Task", command=self.add_task, 
                 bg='#4CAF50', fg='white', font=("Arial", 10, "bold"), 
                 padx=20, pady=5).pack(side='left', padx=5)
        
        tk.Button(button_frame, text="Delete Selected", command=self.delete_task, 
                 bg='#f44336', fg='white', font=("Arial", 10, "bold"), 
                 padx=20, pady=5).pack(side='left', padx=5)
        
        tk.Button(button_frame, text="Mark Complete", command=self.toggle_complete, 
                 bg='#2196F3', fg='white', font=("Arial", 10, "bold"), 
                 padx=20, pady=5).pack(side='left', padx=5)
        
        # Tasks display
        tk.Label(self.root, text="Your Tasks:", bg='#f0f0f0', font=("Arial", 12, "bold")).pack(pady=(20,5))
        
        # Treeview for tasks
        self.tree = ttk.Treeview(self.root, columns=("Priority", "Status", "Date"), show="tree headings", height=15)
        self.tree.heading("#0", text="Task")
        self.tree.heading("Priority", text="Priority")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Date", text="Date Added")
        
        self.tree.column("#0", width=300)
        self.tree.column("Priority", width=80)
        self.tree.column("Status", width=80)
        self.tree.column("Date", width=120)
        
        self.tree.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Bind double-click to edit
        self.tree.bind("<Double-1>", self.edit_task)
        
        # Load existing tasks
        self.refresh_tasks()
        
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Warning", "Please enter a task!")
            return
            
        priority = self.priority_var.get()
        date_added = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        task = {
            "text": task_text,
            "priority": priority,
            "completed": False,
            "date_added": date_added
        }
        
        self.tasks.append(task)
        self.save_tasks()
        self.refresh_tasks()
        self.task_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Task added successfully!")
        
    def delete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            return
            
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this task?"):
            try:
                index = int(selected_item[0])
                if 0 <= index < len(self.tasks):
                    del self.tasks[index]
                    self.save_tasks()
                    self.refresh_tasks()
                    messagebox.showinfo("Success", "Task deleted successfully!")
            except ValueError:
                messagebox.showerror("Error", "Invalid task selection!")
                
    def toggle_complete(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task!")
            return
            
        try:
            index = int(selected_item[0])
            if 0 <= index < len(self.tasks):
                self.tasks[index]["completed"] = not self.tasks[index]["completed"]
                self.save_tasks()
                self.refresh_tasks()
        except ValueError:
            messagebox.showerror("Error", "Invalid task selection!")
            
    def edit_task(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return
            
        try:
            index = int(selected_item[0])
            if 0 <= index < len(self.tasks):
                # Create edit dialog
                edit_window = tk.Toplevel(self.root)
                edit_window.title("Edit Task")
                edit_window.geometry("400x200")
                edit_window.configure(bg='#f0f0f0')
                
                tk.Label(edit_window, text="Edit Task:", bg='#f0f0f0', font=("Arial", 12, "bold")).pack(pady=10)
                
                edit_entry = tk.Entry(edit_window, font=("Arial", 12), width=40)
                edit_entry.insert(0, self.tasks[index]["text"])
                edit_entry.pack(pady=10)
                
                def save_edit():
                    new_text = edit_entry.get().strip()
                    if new_text:
                        self.tasks[index]["text"] = new_text
                        self.save_tasks()
                        self.refresh_tasks()
                        edit_window.destroy()
                        messagebox.showinfo("Success", "Task updated successfully!")
                    else:
                        messagebox.showwarning("Warning", "Task cannot be empty!")
                
                tk.Button(edit_window, text="Save", command=save_edit, 
                         bg='#4CAF50', fg='white', font=("Arial", 10, "bold")).pack(pady=10)
        except ValueError:
            messagebox.showerror("Error", "Invalid task selection!")
            
    def refresh_tasks(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Add tasks to treeview
        for i, task in enumerate(self.tasks):
            status = "✓ Completed" if task["completed"] else "⏳ Pending"
            priority_color = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
            
            item = self.tree.insert("", "end", iid=str(i), text=task["text"], 
                                  values=(f"{priority_color[task['priority']]} {task['priority']}", 
                                         status, task["date_added"]))
            
            # Color completed tasks
            if task["completed"]:
                self.tree.item(item, tags=("completed",))
                
        # Configure tag for completed tasks
        self.tree.tag_configure("completed", foreground="gray")
        
    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f, indent=2)
            
    def load_tasks(self):
        if os.path.exists("tasks.json"):
            try:
                with open("tasks.json", "r") as f:
                    self.tasks = json.load(f)
            except:
                self.tasks = []
        else:
            self.tasks = []

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
