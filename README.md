# pgplot
 A simple library adding graph drawing functionality to Pygame

# Don't use negative numbers, they will be drawn off of the graph. Or do, I can't stop you

## Usage
Need Pygame
Put pygame.init() and pygame.font.init at the start of your program

# Graphing object: Pgp(surface, width, height, topleft=None, topright=None, bottomleft=None, bottomright=None, centre=None, labelColour=None)
surface is a Pygame surface object (for example, pg.display.set_mode((width, height)))
MUST specify coordinates for one of: topleft, topright, bottomleft, bottomright, centre. These are used for placing your graph on the screen
labelColour is optional, but will need to be a tuple containing an rgb code - for the axis labels.
