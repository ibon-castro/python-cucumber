import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")
        
        self.count = 0
        self.label = tk.Label(root, text=str(self.count), font=("Arial", 24))
        self.label.pack(pady=20)
        
        self.increment_button = tk.Button(root, text="Increment", command=self.increment)
        self.increment_button.pack()
        
        self.decrement_button = tk.Button(root, text="Decrement", command=self.decrement)
        self.decrement_button.pack()
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack()
    
    def increment(self):
        self.count += 1
        self.update_label()
    
    def decrement(self):
        self.count -= 1
        self.update_label()
    
    def reset(self):
        self.count = 0
        self.update_label()
    
    def update_label(self):
        self.label.config(text=str(self.count))

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
