#Turtle will be used to draw the maze.
import turtle
import time
#Pygame is imported for audio
import pygame
from pygame import mixer
#Mixer is initialized for audio
mixer.init()

mixer.music.load('backgroundmusic.wav')

mixer.music.play()

#Initial variable for page number and amount of starfish collected
page = 0
starfish_counter = 0

#list to hold position of starfish
starfishlist = []

#Dimensions for the maze
screenheight = 800
screenwidth = 800

#Amount of blocks for the maze
numofblocksx = 25
numofblocksy = 25

#graphics
blocktexture = "mazeblockblue.gif"

playersprite = "player.gif"

#Player movement delay to get rid of lagging
moveDelay = 2

#Initial window
playerscreen = turtle.Screen()

#Load all images
playerscreen.addshape("mazeblockblue.gif")
playerscreen.addshape("mazeblocktwilight.gif")
playerscreen.addshape("mazeblockgreen.gif")
playerscreen.addshape("mazeblockindigo.gif")
playerscreen.addshape("star.gif")
playerscreen.addshape("startscreen.gif")
playerscreen.addshape("loreslide.gif")
playerscreen.addshape("endscreen.gif")
playerscreen.addshape("player1.gif")
playerscreen.addshape("player2.gif")
playerscreen.addshape("player3.gif")
playerscreen.addshape("player4.gif")
playerscreen.addshape("player5.gif")

#Dimensions for the screen
playerscreen.setup(screenwidth,screenheight)

#Function to get a page's desired attributes
def getObjects():
  global playersprite
  global blocktexture
  global playerscreen
    #If statements to load each page's graphics
  if page == 0:
    playerscreen.bgpic("startscreen.gif")
    blocktexture = "mazeblockindigo.gif"
    playersprite = "player4.gif"
  elif page == 1:
    playerscreen.bgpic("loreslide.gif")
    blocktexture = "mazeblockblue.gif"
    playersprite = "player1.gif"
  elif page == 2:
    playerscreen.bgpic("abyssalzone.gif")
    blocktexture = "mazeblockindigo.gif"
    playersprite = "player1.gif"
  elif page == 3:
    playerscreen.bgpic("abyssalzone.gif")
    blocktexture = "mazeblockindigo.gif"
    playersprite = "player2.gif"
  elif page == 4:
    playerscreen.bgpic("twilightzone.gif")
    blocktexture = "mazeblocktwilight.gif"
    playersprite = "player3.gif"
  elif page == 5:
    playerscreen.bgpic("background1.gif")
    blocktexture = "mazeblockgreen.gif"
    playersprite = "player4.gif"
  elif page == 6:
    playerscreen.bgpic("shore.gif")
    blocktexture = "mazeblockblue.gif"
    playersprite = "player5.gif"
  elif page == 7:
    playerscreen.bgpic("endscreen.gif")
    blocktexture = "mazeblockindigo.gif"
    playersprite ="player5.gif"

#Create player using object-oriented programming

    
class Character(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    # self.shape(playersprite)
    self.color("red")
    #Pen is lifted up because we don't want the player to leave a trail.
    self.penup()
    #Player speed
    self.speed(0)
    self.x = 0
    self.y = 0
    self.canMove = False

  #dX and dY represent the future coordinates upon a player's keypress
  def player_move(self, dX, dY):
    global page
    person.futureX = self.x + screenwidth/numofblocksx * dX
    person.futureY = self.y + screenheight/numofblocksy * dY
    gridX = int((self.futureX + 384) / screenwidth * numofblocksx)
    gridY = int((self.futureY - 384) / -screenheight * numofblocksy)
    
    #if the player can move and their coordinate upon movement is not that of a wall, they are able to move. Note that we subtract 1 from page because the value is stored in a list, and lists start at 0
    if self.canMove == True and levellist[page][gridY][gridX] != "x":
      self.canMove = False
      #person's x position gets increased by one block, and is then multiplied by the change in x. we need this so we know the character's future position. same is applied for y
      self.x = self.futureX
      self.y = self.futureY
      
      self.goto(self.x, self.y)

      #when you're on an s tile,
      if levellist[page][gridY][gridX] == "s":
        #loop backwards because youre removing something
        for i in range(len(starfishlist) - 1, -1, -1):
          #if the player runs into a starfish
          if gridX == starfishlist[i].gridX and gridY == starfishlist[i].gridY:
            #removes starfish from list
            starfishlist[i].goto(1000,1000)
            starfishlist.pop(i)
            if len(starfishlist) == 0:
              print("yes")
              coinnoise()
              #once all the starfish are collected, the page is turned and the screen is reset.
              page = page + 1
              levelsetup(levellist[page])

  #Create the maze using goto, turtle's own command
  def player_up(self):
    #player moves 1 block up, process is repeated
    self.player_move(0, 1)
    
  def player_down(self):
    self.player_move(0, -1)
    
  def player_left(self):
    self.player_move(-1, 0)
  
  def player_right(self):
    self.player_move(1, 0)
  
class Draw(turtle.Turtle):
  def __init__(self, x, y):
    turtle.Turtle.__init__(self)
    self.penup()
    self.speed(0)
    self.goto(x, y)
    #Details for the walls
    self.shape(blocktexture)

class Star(turtle.Turtle):
  def __init__(self, x, y):
    turtle.Turtle.__init__(self)
    self.shape("star.gif")
    self.penup()
    self.speed(0)
    self.x = 0
    self.y = 0
    self.gridX = int((x + 384) / screenwidth * numofblocksx)
    self.gridY = int((y - 384) / -screenheight * numofblocksy)

#first level map
level1 = [
   "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "     xxxxxxxxxxx        ",
  "     x x    x sx        ",
  "     x    p    x        ",
  "     xxx xx   xx        ",
  "     xs   x    x        ",
  "     xx   x  s x       ",
  "     xxxxxxxxxxx       ",
  "                        "
]    
level2 = [
     "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "          xsx           ",
  "          sxs           ",
  "          xsx           ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "           p            ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        "
]
level3 = [
  "xxxxxxxxxxxxxxxxxxxxxxxx",
  "x                      x",
  "x         x           xx",
  "xxxxxxxxxxx      xxxxxxx",
  "xs               x     x",
  "x       x        x     x",
  "x       xxxxxxxxxx     x",
  "x                      x",
  "xxxxxxxx               x",
  "x       s              x",
  "x                      x",
  "x   xxx    x       xxxxx",
  "x    x     x          sx",
  "x    x     x   xxxxx   x",
  "x    xx    x   x   x   x",
  "x     x    x   x       x",
  "x     x    xxxxxxxxxxxxx",
  "x     x                x",
  "x     x         x      x",
  "xxxxxxx         x      x",
  "x          xxxxxxxx    x",
  "x      x   x      x    x",
  "x      xxxxx      x    x",
  "xp                x    x",
  "xxxxxxxxxxxxxxxxxxxxxxxx"
]
level4 = [
   "xxxxxxxxxxxxxxxxxxxxxxxx",
  "xs  x        x      x px",
  "x   x        x      x  x",
  "x  xxxxxxx       x     x",
  "x                x     x",
  "x     xxxxxxxxxxxxx    x",
  "x     x     x          x",
  "x     x                x",
  "x    xxxxxxxxxxxxxxxxxxx",
  "x                 x    x",
  "xxxxxxxxxxxxx     x    x",
  "x     x   x       x    x",
  "xxxxx x   x     xxxxx  x",
  "x     x   x            x",
  "x  x s        xxxxxxxxxx",
  "xxxxxxxx       x   x   x",
  "x s x   x      x   x   x",
  "x   x   xxx            x",
  "x                 xxxxxx",
  "x   xxx             x  x",
  "x     x    xxxxxxxxx   x",
  "x x  xx      x    xs   x",
  "x x   x      x         x",
  "xsx   x                x",
  "xxxxxxxxxxxxxxxxxxxxxxxx"
]
level5 = [
   "xxxxxxxxxxxxxxxxxxxxxxxx",
  "x s   xxxxxx    x  x   x",
  "x                     xx",
  "xxxxxxxxxxx      xxxxxxx",
  "x   xx   xs            x",
  "x   xx       xxxxxxxxxxx",
  "x            xs        x",
  "x x          x xxx xs  x",
  "xxxxxxxxx      xx  xxxxx",
  "x  xxxxxxx xx xxx      x",
  "x      x   xx   xxx    x",
  "xxxxxx   xxxx      xxxxx",
  "x          xx       x  x",
  "xxx   xx   xx   xxxxx  x",
  "x     x    xxx  x   x  x",
  "x  x  x    xx          x",
  "x  x  x    xxxxxxxxxxxxx",
  "x xx  x     x       x  x",
  "x x  sx             x  x",
  "xxxxxxx      xxxxxx    x",
  "x                 xxxx x",
  "xs       x  xxx   x x  x",
  "xxxxxxxxxx  x     x x  x",
  "xp          x     x    x",
  "xxxxxxxxxxxxxxxxxxxxxxxx"
]
level6 = [
   "xxxxxxxxxxxxxxxxxxxxxxxx",
  "xsxx  xxxxxxx   x  x   x",
  "x  x        x         xx",
  "x xxx xxxx  x  xxxxxxxxx",
  "x   xx   x             x",
  "xx  xxx      xxxxxxxxxxx",
  "x         x  x       x x",
  "x x  x   xx  x xxx x   x",
  "xxxxxxxxx      xx  xxxxx",
  "x  xxxxxxx xx xxx   x sx",
  "x      x   xx   xxx    x",
  "xxxxxx   xxxxx     xxxxx",
  "x          xxxx     x  x",
  "xxx   xx   xx   xxxxx  x",
  "x     x    xxx  x   x  x",
  "x  x  x    xx          x",
  "x  x  x    xxxxxxxxxxxxx",
  "x xx  x    x   x    x  x",
  "x x   x  x   x      x  x",
  "xxxxxxxxxx   xxxxxx    x",
  "x      x          xxxx x",
  "x  xx    x  xxx   x x  x",
  "x  x x  xx  x     x x  x",
  "x  xs       x     x   px",
  "xxxxxxxxxxxxxxxxxxxxxxxx"
]
level7 = [
   "xxxxxxxxxxxxxxxxxxxxxxxx",
  "xp   x   x    x     x  x",
  "x xxxx   x  xxx   xxx  x",
  "x  x   x x             x",
  "x  x   x     x  x   x  x",
  "xx    xx xx  xxxxxxxxxxx",
  "x         x  x   x  x  x",
  "x x  x   xx  xx  x     x",
  "xxx  x   x          xxxx",
  "x  xxx     xx xxx   x sx",
  "x      xx  x    xxx    x",
  "xxxxxx  xxxx   x    xxxx",
  "x   xx     x   x    xxsx",
  "xxx   xxs  xx      x   x",
  "x     xxx    x   xxxx  x",
  "x  x  xx   xx          x",
  "x  x  xx   xxxxxxxxxxxxx",
  "xs x   x   x   x    x  x",
  "x     xx x   x      x  x",
  "x x  xxxxx   xxxxxx    x",
  "x x    x      x   xxxxsx",
  "xxx      x  xxx   x x  x",
  "x     xx            x  x",
  "xs x   x    x xxx      x",
  "xxxxxxxxxxxxxxxxxxxxxxxx"
]
level8 = [
   "                        ",
  "   s                    ",
  "                        ",
  "                        ",
  "                        ",
  "                     s  ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "  s                     ",
  "                        ",
  "                        ",
  "                        ",
  "            p           ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  " s                      ",
  "                   s    ",
  "                        ",
  "                        "
]
#add levels to level list
levellist = []
levellist.append(level1)
levellist.append(level2)
levellist.append(level3)
levellist.append(level4)
levellist.append(level5)
levellist.append(level6)
levellist.append(level7)
levellist.append(level8)

#Find walls for collisions
walls = []

#set up the level

def levelsetup(lvl):
  global starfishlist
  global walls
  starfishlist = []
  for i in walls:
    #sends walls outside of the screen to remove them
    i.goto(1000,1000)
  #empties the wall list
  walls = []
  getObjects()
  for y in range(len(lvl)):
    for x in range(len(lvl[y])):
      
      #find xy coordinates of the screen
      screen_x = -384 + (x*(screenwidth/numofblocksx))
      screen_y = 384 - (y*(screenwidth/numofblocksy))
      
      #coordinates of player
      character = lvl[y][x]

      #player spawns where p is
      if character == "p":
        person.goto(screen_x,screen_y)
        person.x = screen_x
        person.y = screen_y
        person.shape(playersprite)
        
      #place a block where an x is
      elif character == "x":
        #add coordinate pairs of every block in the walls
        walls.append(Draw(screen_x, screen_y))
        
      elif character == "s":
        starfishlist.append(Star(screen_x, screen_y))
        starfishlist[len(starfishlist)-1].goto(screen_x, screen_y)

#Class commands
person = Character()


#Set Keybinds 
playerscreen.onkey(person.player_down, "s")
playerscreen.onkey(person.player_up, "w")
playerscreen.onkey(person.player_left, "a")
playerscreen.onkey(person.player_right, "d")

#onkey means that the command is run when a key is pressed. w,s,a, and d refer to WASD
playerscreen.listen()

levelsetup(levellist[page])
moveTimer = 0


#Game Loop
while 1:
  
  moveTimer += 1
  if moveTimer > moveDelay:
    person.canMove = True
  # person.forward(0.5)
  playerscreen.update()
