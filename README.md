# PainterLite
An implemintation of DDA algorithm and a polygon drawing algorithm in a small project for Computer Graphics course
# The canvas
The place where we draw is just an image and we just change pixels(a way for us to implement the algorithms with no complicated stuff
the dda algorithm uses the built in rectangle drawing function of the tkinter lib to draw on pixels so we don't have to code a way to handle out of canvas pixels (tight deadline)
#every pixel is mapped and get's a shape id
shapes_cords has the pixels written in it with shape ids as a 2D dictionary
shape_ids is a list that has all shapes drawn in a list so you don't have to iterate on every drawn pixel to get the shapes that are drawn
shape_counter is incremented everytime you draw a circle(or polygon if you change code) or you connect the drawn lines with connect polygon
SIDES variable is for how many sides the polygon algorithm draws for the polygon
I didn't have time to add it's functionality to the UI so i just gave it a big value like 100
and used it to draw a circle in a cheaty way

#Color different shapes Function
It colors the first shape(or chosen shape) with a color and all other shapes with another color.

#This code has no restrictions of using it in any way possible, Totally opensource
