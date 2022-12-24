from Bot import *
class Bot936910(Bot):
	def __init__(self, settings):
		super().__init__(settings)
		self.setName('Bot936910')
		self.count =-1
		mymap = [['$' for i in range(self.nrCols)] for j in range(self.nrCols)]
		visited = [[False for i in range(self.nrCols)] for j in range(self.nrCols)]
		
		self.mymap=mymap
		self.visited=visited
		mymoves=['whatever']
		self.mymoves=mymoves
	
		self.dirty_cells=[]

		self.artificial_trues=[]
	def build_path(self,came_from, start, end):
		path = []
		path.append(end)
		while (end != start):
			end = came_from.get(end)

			path.append(end)

		return path[::-1] 	
	def BFS(self, currentCell,neighborup,neighborright,neighbordown,neighborleft,sign):
					frontier=[currentCell]
					explored=[currentCell]					
					came_from={tuple(currentCell):None}
					
					vlist=[]
					ylist=[]
					zlist=[]
					while len(frontier)>0 :

							path=[]

							v=frontier.pop(0)

							vlist.append(v)
							for w in [[v[0]-1,v[1]], [v[0],v[1]+1],[v[0]+1,v[1]],[v[0],v[1]-1]]:

								if (self.mymap[w[0]][w[1]]=='.' or self.mymap[w[0]][w[1]]=='#') and w not in explored:

									came_from[tuple(w)]=tuple(v)

									frontier.append(w)
									explored.append(w)
							
					for y in vlist:
						for z in [[y[0]-1,y[1]],[y[0],y[1]+1],[y[0]+1,y[1]],[y[0],y[1]-1]]:
							
							if self.mymap[z[0]][z[1]]==sign:
								ylist.append(y)
					if len(ylist)>0:
						
						end=tuple(ylist[0])
						path=(self.build_path(came_from, tuple(currentCell), end))  	
				

					for a in path:
						a=list(a)
						
						if a ==neighborright:
							
							return RIGHT
						if a ==neighborup:
							return UP
						if a ==neighbordown:
							return DOWN						
						if a ==neighborleft:
							return LEFT				

	

	def	nextMove(self,	currentCell,	currentEnergy,	vision,	remainingStainCells):
##################################################################################### MAPS
		for a in range(-1,2):
			for b in range(-1,2):
				self.mymap[currentCell[0]+a][currentCell[1]+b]=vision[a+1][b+1]
				if self.mymap[currentCell[0]+a][currentCell[1]+b]=='x':
					self.visited[currentCell[0]+a][currentCell[1]+b]=True
				
				
				
		for a in self.mymap:
				print(a)
				pass

		# for a in self.visited:
		# 		print(a)
	 	
##################################################################################### DFS
		neighborup       =[currentCell[0]-1,currentCell[1]]
		neighborright    =[currentCell[0],currentCell[1]+1]
		neighbordown     =[currentCell[0]+1,currentCell[1]]
		neighborleft     =[currentCell[0],currentCell[1]-1]
		
		myneighbors      =[ neighborup, neighborleft, neighborright, neighbordown]
				
		directions       =[UP, LEFT, RIGHT, DOWN]
		count=-1
	
		self.visited[currentCell[0]][currentCell[1]]=True	
		for a in range(1,3):
			try:
				if self.mymoves[-1]=='up':

						if self.visited[currentCell[0]+1][currentCell[1]+a]==False:	
							self.artificial_trues.append([currentCell[0]+1,currentCell[1]+a])
							self.visited[currentCell[0]+1][currentCell[1]+a]=True	

						if self.visited[currentCell[0]+1][currentCell[1]-a]==False:	
							self.artificial_trues.append([currentCell[0]+1,currentCell[1]-a])
							self.visited[currentCell[0]+1][currentCell[1]-a]=True	


				if self.mymoves[-1]=='left':

						if self.visited[currentCell[0]+a][currentCell[1]+1]==False:	
							self.artificial_trues.append([currentCell[0]+a,currentCell[1]+1])
							self.visited[currentCell[0]+a][currentCell[1]+1]=True	
				if self.mymoves[-1]=='right':


						if self.visited[currentCell[0]+a][currentCell[1]-1]==False:	
							self.artificial_trues.append([currentCell[0]+a,currentCell[1]-1])
							self.visited[currentCell[0]+a][currentCell[1]-1]=True	
			except:
				pass

		for a in myneighbors:
			if self.mymap[a[0]][a[1]]=='@':
				self.dirty_cells.append(a)
			
		for a in self.dirty_cells:	
			if self.mymap[a[0]][a[1]]!='@':
				self.dirty_cells.remove(a)
				

		for a in self.dirty_cells:
			

			if a ==neighborright:

				return RIGHT
			if a ==neighborup:
				return UP
			if a ==neighbordown:
				return DOWN						
			if a ==neighborleft:
				return LEFT		
			
		if len(self.dirty_cells)>0:
			
					return self.BFS(currentCell,neighborup,neighborright,neighbordown,neighborleft,'@')			

		for a in myneighbors:
					count+=1

					if self.visited[a[0]][a[1]]== False:	

						self.mymoves.append(directions[count])
						return (UP, LEFT, RIGHT, DOWN)[count]
		
		if self.visited[neighborup[0]][neighborup[1]]==True and self.visited[neighborright[0]][neighborright[1]]==True and self.visited[neighbordown[0]][neighbordown[1]]==True and self.visited[neighborleft[0]][neighborleft[1]]== True:
		
					
					
					return self.BFS(currentCell,neighborup,neighborright,neighbordown,neighborleft,'$')					

