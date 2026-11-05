Web VPython 3.2
box(size=vec(0.5,1.5,0.5),pos = vec(-1.5,0,0),texture = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRfz0Watnweawnub_IUFVGaF-UpYD_LqEP14dcbojM9MCP6GOZxmb8dQw&s=10")
rim = ring(pos=vec(3, 1.5, 0), axis=vec(0, 50, 0), radius = 0.32,color=color.red)
pillar = box(size=vec(0.1,2.5,0.2),pos=vec(3.35,0.3,0),color = vec(0,51/255,25/255))
backboard = box(size = vec(0.1,0.8,1.2), pos = vec(3.35,1.8,0),color = color.blue)
hoop = compound([rim,pillar,backboard])
s = sphere(size=vec(0.25,0.25,0.25),pos=vec(-1.2,1,0))
while True:
    rate(30)
    k = keysdown()
    if 'd' in k:
        s.pos.x = s.pos.x+0.1
    if 'w' in k:
        s.pos.y = s.pos.y+0.1
