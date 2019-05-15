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

    def calculateBestMove(self,sums):
         pass
            

class Server:

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


    def movement(self,maximumdirection,maximumPos,freeCubes):
        if maximumDirection == 0 : 
            if maximumPos ==0:
                
            if maximumPos ==1:
            if maximumPos ==2:
            if maximumPos ==3:
            if maximumPos ==4:
            pass
        if maximumDirection == 1 : 
            pass
        if maximumDirection == 2 :
            pass




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

        self.cubes = self.createCubes(body['game']) # generate all the cubes
        
        self.players = self.createPlayers(self.cubes,body['players']) # generate the players with their occupied cubes
        
        freecubes = self.getFreeCubes(self.cubes) # get all the free cubes
        
        sums = self.makeTheSums(self.cubes) # generate a dico with the sum of each line and row and diag

        # AI #
        # Je récupère la plus grande valeur et la ligne , colone, ou de cette plus grande valeur
       
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

        if body['players'][1] == body['you']: # in case of second player
            horizontal =[]
            vertical =[]
            diagonal =[]
            for results in sums['horizontal']:
                horizontal.append(results[1])
            maximum1 = max(horizontal)
            maximum1Pos = horizontal.index(maximum1)

            for results in sums['vertical']:
                vertical.append(results[1])
            maximum2 = max(vertical)
            maximum2Pos = vertical.index(maximum2)

            for results in sums['diagonal']:
                diagonal.append(results[1])
            maximum3 = max(diagonal)
            maximum3Pos = diagonal.index(maximum3)

            listMaxima = [maximum1,maximum2,maximum3]
            self.maximumvalue = max(listMaxima)
            self.maximumdirection = listMaxima.index(maximumvalue) # 0-Horizontal , 1-Vertical, 2-Diagonal
            
            # maximumPos gives the index of line , col or diag containing the max
            if maximumdirection == 0 :
                self.maximumPos = maximum1Pos
            if maximumdirection == 1 :
                self.maximumPos = maximum2Pos
            if maximumdirection == 2 :
                self.maximumPos = maximum3Pos
        
        # Si je peux augmenter, je le fais.
        
            



        # Si le joueur adverse peut former un 5. 
        # Si je peux le bloquer , je joue le jeu qui le bloque.
        # Sinon un des trois déplacements possibles augmente la plus grosse somme pour moi , je joue le coup.
        # Sinon je joue le coup qui bloque la plus grosse valeur de l'adversaire.
    

        return {"move": (maximumvalue,maximumdirection,maximumPos)}



    


if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8000

    cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': port})
    cherrypy.quickstart(Server())