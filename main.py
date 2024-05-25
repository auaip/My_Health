import tkinter as tk
from Login_portal import LoginPortal

def main():
    root = tk.Tk()
    root.geometry("500x300")
    app = LoginPortal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
