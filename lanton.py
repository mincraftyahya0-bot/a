import turtle

def langton():

    window = turtle.Screen()
    window.bgcolor('white')
    window.screensize(1000,1000)

    maps = {}


    ant = turtle.Turtle()
    
    ant.shape('square')    
    
    ant.shapesize(0.5)
    
    ant.speed(99999999999999999999999999999999999)                                 
                
    pos = coordinate(ant)                             
    
    while True:
        
        step = 10                                     
        if pos not in maps or maps[pos] == "white":
            
            ant.fillcolor("black")        
            
            ant.stamp()                                 
            invert(maps, ant, "black")
            ant.right(90)
            
            ant.forward(step)                         
            pos = coordinate(ant)
            
        elif maps[pos] == "black":
            ant.fillcolor("white")
            invert(maps, ant, "white")
            
            ant.stamp()
            ant.left(90)
            ant.forward(step)
            pos = coordinate(ant)

def invert(graph, ant, color):
    graph[coordinate(ant)] = color

def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))

langton()