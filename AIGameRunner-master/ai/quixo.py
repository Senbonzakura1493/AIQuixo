import cherrypy
import sys


class Cube : 
    def __init__(self,value,position):
        self.value = value
        self.position = position

class Player : 
    def __init__(self,name,cubes):
        self.name = name
        self.cubes = cubes


            
class Server:

    message =''
    #create cubes and their position according to the game
    def createCubes(self,game):
        cubes = []
        i=0
        if i <= len(game) :
            for j in game :
                cube = Cube(j,i) #create cube
                cubes.append(cube)
                i+=1      
        return cubes

    #create players with their associated cubes
    def createPlayers(self,cubes,players):
        createdPlayers =[]
        cubes0 = []
        cubes1 = []
        for cube in cubes: 
            if cube.value == 0:
                cubes0.append(cube)
            if cube.value == 1: 
                cubes1.append(cube)
        
        player0 = Player(players[0],cubes0)
        player1 = Player(players[1],cubes1)

        createdPlayers.append(player0)
        createdPlayers.append(player1)

        return createdPlayers 
    
    def makeTheSums(self,cubes):
        
        def makeSumm(t):
            total0 = 0
            total1 = 0
            for x in t:
                if x == "None":
                    pass
                if  x == 0 : 
                    total0 += 1
                if x == 1 :
                    total1 += x
                    #print(total)
            return (total0,total1) #ok!

        hToSum = []
        hToSum2 = []
        hToSum3 = []
        hToSum4 = []
        hToSum5 = []
        #horizontal sum 
        for cube in cubes:
            if cube.position in [0,1,2,3,4]:#ligne1
                hToSum.append(cube.value)
            if cube.position in [5,6,7,8,9]:#ligne2
                hToSum2.append(cube.value)
            if cube.position in [10,11,12,13,14]:#ligne3
                hToSum3.append(cube.value)
            if cube.position in [15,16,17,18,19]:#ligne4
                hToSum4.append(cube.value)
            if cube.position in [20,21,22,23,24]:#ligne5
                hToSum5.append(cube.value)
        hSum = [makeSumm(hToSum),makeSumm(hToSum2),makeSumm(hToSum3),makeSumm(hToSum4),makeSumm(hToSum5)]
        #vertical sum
        vToSum = []
        vToSum2 = []
        vToSum3 = []
        vToSum4 = []
        vToSum5 = []
        for cube in cubes:
            if cube.position in [0,5,10,15,20]:#col1
                vToSum.append(cube.value)
            if cube.position in [1,6,11,16,21]:#col2
                vToSum2.append(cube.value)
            if cube.position in [2,7,12,17,22]:#col3
                vToSum3.append(cube.value)
            if cube.position in [3,8,13,18,23]:#col4
                vToSum4.append(cube.value)
            if cube.position in [4,9,14,19,24]:#col5
                vToSum5.append(cube.value)
        vSum = [makeSumm(vToSum),makeSumm(vToSum2),makeSumm(vToSum3),makeSumm(vToSum4),makeSumm(vToSum5)]
        #diagonal sum
        dToSum = []
        dToSum2 = []
        for cube in cubes:
            
            if cube.position in [0,6,12,18,24]:#diag1
                dToSum.append(cube.value)
            if cube.position in [4,8,12,16,20]:#diag2
                dToSum2.append(cube.value)

        dSum = [makeSumm(dToSum),makeSumm(dToSum2)]

        return {"horizontal" : hSum,"vertical" : vSum,"diagonal" : dSum}

    def getFreeCubes(self,cubes):
        freecubes = []
        for cube in cubes: 
            if cube.value == "None": # si le cube est libre
                if cube.position in [0,1,2,3,4,5,9,10,14,15,19,20,21,22,23,24] :
                    freecubes.append(cube)
        return freecubes


    def movement(self,maximumdirection,maximumPos,freecubes,value):
        if maximumdirection == 0 : 
            if maximumPos ==0:
                #first line
                for cube in freecubes:
                    if cube.position in [0,4]:
                        if cube.position == 0 :
                            direction = 'E'
                        if cube.position == 4 :
                            direction ='W'
                        cube.value = value
                        
                        return {'cube' : cube.position,
                                'direction' : direction} 
            if maximumPos == 1:
                for cube in freecubes:
                    if cube.position in [5,9]:
                        if cube.position == 5 :
                            direction = 'E'
                        if cube.position == 9 :
                            direction ='W'
                        cube.value = value
                        
                        return {'cube' : cube.position,
                                'direction' : direction} 
            if maximumPos == 2:
                for cube in freecubes:
                    if cube.position in [10,14]:
                        if cube.position == 10 :
                            direction = 'E'
                        if cube.position == 14 :
                            direction ='W'
                        cube.value = value
                        
                        return {'cube' : cube.position,
                                'direction' : direction} 
            if maximumPos == 3:
                for cube in freecubes:
                    if cube.position in [15,19]:
                        if cube.position == 15 :
                            direction = 'E'
                        if cube.position == 19 :
                            direction ='W'
                        cube.value = value
                        
                        return {'cube' : cube.position,
                                'direction' : direction} 
            if maximumPos == 4:
                for cube in freecubes:
                    if cube.position in [20,24]:
                        if cube.position == 20 :
                            direction = 'E'
                        if cube.position == 24 :
                            direction ='W'
                        cube.value = value
             
                        return {'cube' : cube.position,
                                'direction' : direction} 
        if maximumDirection == 1 : # vertical
            if maximumPos ==0:
                #first column 
                for cube in freecubes:
                    if cube.position in [0,10]:
                        if cube.position == 0 :
                            direction = 'S'
                        if cube.position == 4 :
                            direction ='N'
                        cube.value = value
                        
                        return {'cube' : cube.position,
                                'direction' : direction} 
            if maximumPos == 1:
                for cube in freecubes:
                    if cube.position in [1,21]:
                        if cube.position == 1 :
                            direction = 'S'
                        if cube.position == 21 :
                            direction ='N'
                        cube.value = value
                        
                        return {'cube' : cube.position,
                                'direction' : direction} 
            if maximumPos == 2:
                for cube in freecubes:
                    if cube.position in [2,22]:
                        if cube.position == 2 :
                            direction = 'S'
                        if cube.position == 22 :
                            direction ='N'
                        cube.value = value
                        
                        return {'cube' : cube.position,
                                'direction' : direction} 
            if maximumPos == 3:
                for cube in freecubes:
                    if cube.position in [3,23]:
                        if cube.position == 3 :
                            direction = 'S'
                        if cube.position == 23 :
                            direction ='N'
                        cube.value = value
                        
                        return {'cube' : cube.position,
                                'direction' : direction} 
            if maximumPos == 4:
                for cube in freecubes:
                    if cube.position in [4,24]:
                        if cube.position == 4 :
                            direction = 'S'
                        if cube.position == 24 :
                            direction ='N'
                        cube.value = value
                        
                        return {'cube' : cube.position,
                                'direction' : direction} 
        if maximumDirection == 2 : # diagonal
            if maximumPos ==0:# premiere diag
                for cube in freecubes:
                    if cube.position in [10,4]:
                        if cube.position == 10 :
                            direction = 'N'
                        if cube.position == 4 :
                            direction ='S'
                        cube.value = value
                        
                        return {'cube' : cube.position,
                                'direction' : direction} 
            if maximumPos == 1:#deuxieme diag
                for cube in freecubes:
                    if cube.position in [0,24]:
                        if cube.position == 0 :
                            direction = 'S'
                        if cube.position == 24 :
                            direction ='N'
                        cube.value = value
                        return {'cube' : cube.position,
                                'direction' : direction} 

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()

    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        
        if cherrypy.request.method == "OPTIONS":
            return ''
        body = cherrypy.request.json
        print(body)

        self.game = body['game']
        self.cubes = self.createCubes(self.game) # generate all the cubes
        self.players = self.createPlayers(self.cubes,body['players']) # generate the players with their occupied cubes
        self.freecubes = self.getFreeCubes(self.cubes) # get all the free cubes 
        self.moves = (body['moves'])
        sums = self.makeTheSums(self.cubes) # generate a dico with the sum of each line and row and diag
 
        ############################## IA ###########################################
        if body['players'][0] == body['you']: # in case of you 
            horizontal =[]
            vertical =[]
            diagonal =[]
            for results in sums['horizontal']:
                horizontal.append(results[0])
            maximum1 = max(horizontal)
            maximum1Pos = horizontal.index(maximum1)

            for results in sums['vertical']:
                vertical.append(results[0])
            maximum2 = max(vertical)
            maximum2Pos = vertical.index(maximum2)

            for results in sums['diagonal']:
                diagonal.append(results[0])
            maximum3 = max(diagonal)
            maximum3Pos = diagonal.index(maximum3)

            listMaxima = [maximum1,maximum2,maximum3]

            maximumvalue = max(listMaxima)
            maximumdirection = listMaxima.index(maximumvalue) # 0-Horizontal , 1-Vertical, 2-Diagonal
            
            # maximumPos gives the index of line , col or diag containing the max
            if maximumdirection == 0 :
                maximumPos = maximum1Pos
            if maximumdirection == 1 :
                maximumPos = maximum2Pos
            if maximumdirection == 2 :
                maximumPos = maximum3Pos

            horizontal2 =[]
            vertical2 =[]
            diagonal2 =[]
            for results in sums['horizontal']:
                horizontal2.append(results[1])
            maximum4 = max(horizontal2)
            maximum4Pos = horizontal2.index(maximum4)

            for results in sums['vertical']:
                vertical2.append(results[1])
            maximum5 = max(vertical2)
            maximum5Pos = vertical2.index(maximum5)

            for results in sums['diagonal']:
                diagonal2.append(results[1])
            maximum6 = max(diagonal2)
            maximum6Pos = diagonal2.index(maximum6)

            listMaxima2 = [maximum4,maximum5,maximum6]

            maximumvalue2 = max(listMaxima2)
            maximumdirection2 = listMaxima2.index(maximumvalue2) # 0-Horizontal , 1-Vertical, 2-Diagonal
            
            # maximumPos gives the index of line , col or diag containing the max
            if maximumdirection2 == 0 :
                maximumPos2 = maximum4Pos
            if maximumdirection2 == 1 :
                maximumPos2 = maximum5Pos
            if maximumdirection == 2 :
                maximumPos2 = maximum6Pos

        if maximumvalue > maximumvalue2 :
            message = 'maximizing my chance to win'
            if maximumvalue == 4 :
                message = 'movement makes you win!'

            #Movement to maximise my sum on the wanted direction
            movement = self.movement(maximumdirection,maximumPos,self.freecubes,0)
            #update game state
            if movement['direction']=='W':
                newPos = movement['cube']- 4 
                self.game[newPos] = 0
            if movement['direction']=='E':
                newPos = movement['cube']+ 4 
                self.game[newPos] = 0
            if movement['direction']=='S':
                newPos = movement['cube']+ 20 
                self.game[newPos] = 0
            if movement['direction']=='N':
                newPos = movement['cube']- 20 
                self.game[newPos] = 0
        else :
            message = 'blocking enemy progression'
            if maximumvalue2 == 4 :
                message = 'the enemy has a 4 , blocked him !'
            #Movement to stop the progression of my enemy
            movement = self.movement(maximumdirection2,maximumPos2,self.freecubes,0)

            #Update game state
            if movement['direction']=='W':
                newPos = movement['cube']- 4 
                self.game[newPos] = 0
            if movement['direction']=='E':
                newPos = movement['cube']+ 4 
                self.game[newPos] = 0
            if movement['direction']=='S':
                newPos = movement['cube']+ 20 
                self.game[newPos] = 0
            if movement['direction']=='N':
                newPos = movement['cube']- 20 
                self.game[newPos] = 0

        self.moves.append(movement) # add movement to moves
        #make recursively moves according to new state
        #self.move() not working yet need the basic case
        
        return {"move": self.moves.pop(),"message" : message} # return the last moves json response 


if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8000

    cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': port})
    cherrypy.quickstart(Server())