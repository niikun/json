import tkinter as tk, json, os

savefile="drawtool.json"
is_mouse_down = False
pos = [0,0]
lines = []

def main():
    global canvas
    app=tk.Tk()
    canvas = tk.Canvas(app,bg="white")
    app.geometry("800x600")
    canvas.pack(fill=tk.BOTH,expand=True)
    button1=tk.Button(app,text="初期化",command=clear_draw)
    button2=tk.Button(app,text="Load",command=reload)
    button1.pack()
    button2.pack()
    canvas.bind("<Button-1>",mouse_down)
    canvas.bind("<ButtonRelease-1>",mouse_up)
    canvas.bind("<Motion>",mouse_move)
    load_file()
    draw_screen()
    app.mainloop()

def reload():
    load_file()
    draw_screen()

def load_file():
    global lines
    if not os.path.exists(savefile):return
    with open(savefile, "r", encoding="utf-8") as f:
        lines = json.load(f)
        print(lines)

def save_file():
    with open(savefile, "w", encoding="utf-8") as f:
        json.dump(lines, f)

def draw_screen():
    canvas.delete("all")
    for v in lines:
        canvas.create_line(v[0],v[1],v[2],v[3], fill="black",width=10,capstyle="round")

def mouse_down(e):
    global pos, is_mouse_down
    pos = [e.x,e.y]
    is_mouse_down = True

def mouse_up(e):
    global is_mouse_down
    mouse_move(e)
    save_file()
    is_mouse_down = False

def mouse_move(e):
    global pos
    if not is_mouse_down: return
    lines.append([pos[0], pos[1], e.x, e.y])
    print(lines)
    pos = [e.x,e.y]
    draw_screen()

def clear_draw():
    lines.clear()
    draw_screen()

if __name__ == "__main__":
    main()
    

