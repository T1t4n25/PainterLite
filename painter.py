from tkinter import *
from tkinter import colorchooser
import math

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1280
MIN_PIXEL_SIZE = 1
MAX_PIXEL_SIZE = 5
NO_POINT = (-1,-1)
SIDES = 100  # used in the polygon drawing algorithm, that can create regular polygons

shape_counter = 1 # start
pixel_size = 2 # Defualt size
pixel_color = "black"  # Default color
start_point = NO_POINT
prev_point = NO_POINT
shapes_cords = {} # 2D Dictionary of shapes
shape_ids = [] # List of shapes ids

def draw_line(event):
    global start_point
    global prev_point
    global shape_counter

    if start_point == NO_POINT:
        start_point = (event.x,event.y)
        prev_point = start_point
        return
    dda_line(event.x, event.y, prev_point[0], prev_point[1], pixel_size)
    prev_point = (event.x,event.y)

def clear_all():
    global start_point
    global shape_counter
    shape_counter = 1
    shapes_cords.clear()
    shape_ids.clear()

    canvas.delete("all")
    start_point = NO_POINT

    image = PhotoImage(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.image = image
    canvas.create_image((WINDOW_WIDTH/2, WINDOW_HEIGHT/2), image=image, state="normal")

def switch_circle():
    connect_polygon()
    global start_point
    start_point = NO_POINT
    canvas.bind('<Button-1>', get_circle)

def switch_polygon():
    global start_point
    start_point = NO_POINT
    canvas.bind('<Button-1>', draw_line)

def get_circle(event):
    global start_point
    if start_point == NO_POINT: # no center yet
        start_point = (event.x,event.y)
    else:
        radius = math.sqrt((event.x - start_point[0])**2 + (event.y - start_point[1])**2)
        draw_circle(start_point[0], start_point[1], radius, SIDES)
        start_point = NO_POINT

def draw_circle(center_x, center_y, radius, sides):
    angle_increment = 360 / sides  # Angle increment in degrees
    current_angle = 0
    global shape_counter
    x1, y1 = center_x + radius * math.cos(math.radians(current_angle)), center_y - radius * math.sin(math.radians(current_angle))

    for _ in range(sides):
        current_angle += angle_increment
        x2 = center_x + radius * math.cos(math.radians(current_angle))
        y2 = center_y - radius * math.sin(math.radians(current_angle))
        dda_line(x1, y1, x2, y2, pixel_size)
        x1, y1 = x2, y2
    shape_counter += 1

def connect_polygon():
    global start_point
    global shape_counter
    if start_point == NO_POINT:
        return
    dda_line(start_point[0],start_point[1],prev_point[0],prev_point[1],pixel_size)
    shape_counter += 1
    start_point = NO_POINT

def dda_line(x1, y1, x2, y2, pixel_size):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    steps = steps if steps > 0 else 1
    xinc = dx / float(steps)
    yinc = dy / float(steps)
    for i in range(round(steps)):
        x1 += xinc
        y1 += yinc
        canvas.create_rectangle(round(x1)-pixel_size, round(y1)-pixel_size, round(x1)+pixel_size, round(y1)+pixel_size, fill=pixel_color, outline='')
        key = (round(y1), round(x1))
        shapes_cords[key] = 'shape' + str(shape_counter)
        

def change_size(new_size):
    global pixel_size
    pixel_size = int(new_size)
    size_label.config(text=f"Pixel Size: {pixel_size}")

def change_color():
    global pixel_color
    color = colorchooser.askcolor(title="Choose color")
    if color[1]:  # Check if a color is chosen (not canceled)
        pixel_color = color[1]

def color_diff(main_shape = 'shape1'):
    main_shape = 'shape1'
    color = ['red', 'green']

    sorted_keys = sorted(shapes_cords.keys(), key=lambda k: (k[0], k[1]))

    for (y, x), current_shape in shapes_cords.items():
        if current_shape != main_shape:
            canvas.create_rectangle(x-pixel_size, y-pixel_size, x+pixel_size, y+pixel_size, fill=color[1], outline='')
        else:
            canvas.create_rectangle(x-pixel_size, y-pixel_size, x+pixel_size, y+pixel_size, fill=color[0], outline='')
        
        


                
window = Tk()
window.title("Painter")
window.resizable(False, False)
window.configure(bg='lightblue')

canvas = Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, background='white')
image = PhotoImage(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.image = image
canvas.create_image((WINDOW_WIDTH/2, WINDOW_HEIGHT/2), image=image, state="normal")
canvas.bind('<Button-1>', draw_line)
canvas.pack()

connect_button = Button(window, text="Draw Polygon", command=switch_polygon)
connect_button.pack(side=LEFT, padx=10, pady=10)

connect_button = Button(window, text="Connect Polygon", command=connect_polygon)
connect_button.pack(side=LEFT, padx=10, pady=10)

size_button = Button(window, text="Draw Circle", command=switch_circle)
size_button.pack(side=LEFT, padx=10, pady=10)

color_button = Button(window, text="Select color", command=change_color)
color_button.pack(side=LEFT, padx=10, pady=10)

clear_button = Button(window, text="Clear All", command=clear_all)
clear_button.pack(side=LEFT, padx=10, pady=10)

clip_button = Button(window, text="Color different shapes", command=color_diff)
clip_button.pack(side=LEFT, padx=10, pady=10)

size_slider = Scale(window, from_=MIN_PIXEL_SIZE, to=MAX_PIXEL_SIZE, orient=HORIZONTAL, command=change_size)
size_slider.set(pixel_size)
size_slider.pack(side=RIGHT, padx=10, pady=10)

size_label = Label(window, text=f"Pixel Size: {pixel_size}")
size_label.pack(side=RIGHT, padx=10, pady=10)



window.mainloop()
