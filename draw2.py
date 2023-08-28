from Focus_Roots import *

def change():
    set_background(color_aqua)
    draw_circle(250,250,180,0,color=color_light_salmon)
    draw_rect(70,40,400,250,0,color=color_aqua)
    draw_rect(130,20,30,340,0,color=color_chocolate)
    draw_polygon([[150,40],[10,170],[150,250]],0,color=color_orchid)
    draw_circle(200,350,40,0,color=color_blue)
    draw_circle(300,350,30,0,color=color_blue)
    write_text("Boat",260,40,50,color=color_white)



draw(change)
