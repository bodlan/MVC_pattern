import tkinter as tk
import view_gui
import model
def create(event):
    global app1
    CreateWindow=tk.Toplevel()
    app1=view_gui.Create(CreateWindow)
def read(event):
    global app2
    ReadWindow=tk.Toplevel()
    app2=view_gui.Read(ReadWindow)
def update(event):
    global app3
    UpdateWindow=tk.Toplevel()
    app3=view_gui.Update(UpdateWindow)
def delete(event):
    global app4
    DeleteWindow=tk.Toplevel()
    app4=view_gui.Delete(DeleteWindow)
def exit(event):
    quit()

def handler_click(event):
    info=[app1.name.get(),app1.surname.get(),app1.year.get(),app1.course.get(),app1.email.get()]
    model.create(info)
def close_window():
    app1.master.destroy()

def update_info():
    model.update(app3.old.get(),app3.new.get())

def delete_student():
    model.delete([app4.name.get(),app4.surname.get()])


def main():
    root=tk.Tk()
    app=view_gui.Main(root)
    root.mainloop()
if __name__ == '__main__':
    main()