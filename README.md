# pgplot
 A simple library adding graph drawing functionality to Pygame

### Don't use negative numbers, they will be drawn off of the graph. Or do, I can't stop you

# Usage
Need Pygame \n
Put pygame.init() and pygame.font.init at the start of your program

## Graphing object: Pgp(surface, width, height, topleft=None, topright=None, bottomleft=None, bottomright=None, centre=None, labelColour=None)
surface is a Pygame surface object (for example, pg.display.set_mode((width, height)))
MUST specify coordinates for one of: topleft, topright, bottomleft, bottomright, centre. These are used for placing your graph on the screen
labelColour is optional, but will need to be a tuple containing an rgb code - for the axis labels.
Minimum size for graph: 300x300

### Usage - after creation
To add a plot: graphObj.addPlot(plotCoords, position=None, line=None)
plotCoords - tuple containing coordinates on the graph, e.g. (2,5)
position can be specified in case you need to add a plot to the middle of the graph. Works like list indices - 0 indexed
line is optional, specify line=2 to add plots to a second line. Only two lines are supported at the moment

Draw graph: graphObj.draw() - call every frame
