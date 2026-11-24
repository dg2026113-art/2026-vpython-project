Web VPython 3.2
box(size=vec(0.5,1.5,0.5),pos = vec(-2,0,0),texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRfz0Watnweawnub_IUFVGaF-UpYD_LqEP14dcbojM9MCP6GOZxmb8dQw&s=10")
rim = ring(pos=vec(3, 1.5, 0), axis=vec(0, 50, 0), radius = 0.32,color=color.red)
pillar = box(size=vec(0.1,2.5,0.2),pos=vec(3.35,0.3,0),color = vec(0,51/255,25/255))
backboard = box(size = vec(0.1,0.8,1.2), pos = vec(3.35,1.8,0),color = color.blue)
hoop = compound([rim,pillar,backboard])
shotclock = box(size = vec(1,2/3,-0.5),pos = vec(0.3,3.5,0))
s = sphere(size=vec(0.25,0.25,0.25),pos=vec(-1.7,1,0),make_trail=True)
zero1 = sphere(radius = 0.3,pos = vec(0.5,3.5,-0.02))
zero1.color = color.black
zero2 = sphere(radius = 0.3,pos = vec(0.1,3.5,-0.02))
zero2.color = color.black
white1 = sphere(radius = 0.1,pos = vec(0.5,3.5,0.1955))
white2 = sphere(radius = 0.1,pos = vec(0.1,3.5,0.1955))
g = vec(0,-9.8,0)
s.v= vec(5,5,0)
dt = 0.0175
while True:
    rate(30)
    k = keysdown()
                
    if ' ' in k :
        while s.pos.y>=-0.6:
            rate (80)
            s.pos = s.pos+s.v*dt
            s.v = s.v+g*dt
    for i in [color.red,color.blue,color.cyan,color.magenta,color.green,color.white]:
        k = keysdown()
        rate(10)
        if 'c' in k:
            s.color = i
