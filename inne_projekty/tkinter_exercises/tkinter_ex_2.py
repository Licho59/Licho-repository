# not recommended to develop GUI programs - by using global variables

import tkinter as tk

global my_counter


def create_user_interface(application_window):
    global my_counter

    my_counter = tk.Label(application_window, text="0")
    my_counter['fg'] = 'green'
    my_counter.grid(row=0, column=0)

    increment_button = tk.Button(application_window, text="Add 1 to counter")
    increment_button.grid(row=1, column=0)
    increment_button['bg'] = 'yellow'
    increment_button['command'] = increment_counter

    quit_button = tk.Button(application_window, text="Quit")
    quit_button.grid(row=2, column=0)
    quit_button['fg'] = 'red'
    quit_button['command'] = window.destroy


def increment_counter():
    global my_counter
    my_counter['text'] = str(int(my_counter['text']) + 1)


# Create the application window
window = tk.Tk()

create_user_interface(window)

# Start the GUI event loop
window.mainloop()
