# pgplot
 A simple library adding graph drawing functionality to Pygame</br>
 Just download pgplot file - that contains everything needed for full functionality. Then drag the pgplot.py file into the same folder as any program you need it for</br>
 Alternatively, run the command 'pip install pgplot' on command prompt/powershell</br>
 Then, to use it in your program, add 'import pgplot' at the start.

### Don't use negative numbers, they will be drawn off of the graph. Or do, I can't stop you

# Usage
Need Pygame. Put pygame.init() and pygame.font.init at the start of your program<br/>
Place pgplot.py in your working directory and call import pgplot at the start of your program

## Graphing object: graphObj = Pgp(surface, width, height, topleft=None, topright=None, bottomleft=None, bottomright=None, centre=None, drawLine=None)
surface is a Pygame surface object (for example, pg.display.set_mode((width, height)))<br/>
MUST specify coordinates for one of: topleft, topright, bottomleft, bottomright, centre. These are used for placing your graph on the screen.<br/>
drawLine determines whether the line connecting points will be drawn - can have scatter graphs or line graphs.</br>
Minimum size for graph: 300x300 (anything smaller will be set to this)</br>
Usage example: pgp = Pgp(screen, 450, 450, centre=(500, 500), drawLine=True) - will create a line graph of size 450x450 with centre 500, 500

### Usage - after creation
To add a plot: graphObj.addPlot(plotCoords, position=None, line=None)<br/>
plotCoords - tuple containing coordinates on the graph, e.g. (2,5)<br/>
position can be specified in case you need to add a plot to the middle of the graph. Works like list indices - 0 indexed<br/>
line is optional, specify line=2 to add plots to a second line. Only two lines are supported at the moment<br/>

Draw graph: graphObj.draw() - call every frame
