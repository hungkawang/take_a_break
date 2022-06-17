import tkinter as tk
import time

def button_event():
    if entry.get() != "":
        if entry.get().isnumeric():
            later = entry.get()
            print(later)
        else:
            # TODO
            pass
            print("Invalid input")
            
def destroy():
    if entry.get().isnumeric():
        later = int(entry.get())
        pop.destroy()
        time.sleep(later)
        popup()

def remind_in_30min():
    pop.destroy()
    time.sleep(30*60)
    popup()
        

def popup():
    global pop
    pop = tk.Toplevel()
    pop.title("test")
    pop.geometry("250x150")
    pop.config(bg="#00F000")
    
    p1 = tk.Label(pop, text="Take a break:)", bg="#00F000", font=(20, 20))
    p1.grid()
    
    button2 = tk.Button(pop, text="Remind me again in 30 mins", command=remind_in_30min)
    button2.grid()
    
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Take a break reminder")

    window.geometry("250x150")

    prompt = tk.Label(text="Take a break:)", font=(20, 20))
    prompt.grid()

    button1 = tk.Button(text="Click me to start!", command=popup)
    button1.grid()

    window.mainloop()