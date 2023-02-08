rom tkinter import *
import settings
import utils
root = Tk()
#alters the settings fo the window
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper game")
#root.resizable(False, False)
top_frame = Frame(
    root,
    bg="grey", #change later to black
    width=settings.WIDTH,
    height = utils.width_prct(25)
)
top_frame.place(x=0, y=0) #increase either one to move closer to centre
left_frame = Frame(
    root,
    bg="blue",
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))
root.mainloop()
