import tkinter as tk, json, os, sys

filename="linerect.linerect"

def main():
    # if len(sys.argv)<=1:
    #     print("[USAGE] python3 draw_linerect.py(file)")
    # filename = sys.argv[1]
    global canvas
    app=tk.Tk()
    canvas=tk.Canvas(app, bg="white")
    app.geometry("800x600")
    canvas.pack(fill=tk.BOTH, expand=True)
    with open(filename,"r",encoding="utf-8") as f:
        data = json.load(f)
    draw_screen(data)
    app.mainloop()

def draw_screen(data):
    for v in data:
        if v["type"]=="line":
            xy=v["xy"]
            canvas.create_line(xy[0], xy[1], xy[2], xy[3],fill=v["color"], width=v["width"], capstyle="round")
        if v["type"]=="rect":
            xy = v["xy"]
            canvas.create_rectangle(xy[0], xy[1], xy[2], xy[3],fill=v["fill"], width=v["width"], outline=v["border"])

if __name__ == "__main__":
    main()