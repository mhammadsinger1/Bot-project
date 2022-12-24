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
	def heuristic(self,a, b):
		(x1, y1) = a
		(x2, y2) = b
		return (abs(x1 - x2) + abs(y1 - y2))	

	

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
					count+=1

					if self.visited[a[0]][a[1]]== False:	

						self.mymoves.append(directions[count])
						return (UP, LEFT, RIGHT, DOWN)[count]
		import heapq
		if self.visited[neighborup[0]][neighborup[1]]==True and self.visited[neighborright[0]][neighborright[1]]==True and self.visited[neighbordown[0]][neighbordown[1]]==True and self.visited[neighborleft[0]][neighborleft[1]]== True:
			
						
				
						to_visit_cells = []
						visited_cells  = []
						
						g_cost = {}
						g_cost[tuple(currentCell)]=0
						
						came_from={}
						came_from[tuple(currentCell)]=None
						
						
						heapq.heappush(to_visit_cells, (0, currentCell))
						
						path=[]
						while len(to_visit_cells)>0:
							
							target=[2,1]
							
							v=heapq.heappop(to_visit_cells)[1]
							
							visited_cells.append(v)
							
							
							if v == target:
								print('goal reached')
								#print(visited_cells)
								
								while target != currentCell:
									
									target= came_from[tuple(target)]
									
									path.append(target)
								print(path[::-1])


								if target==currentCell:	
									for a in path:
										self.mymap[a[0]][a[1]]='*'	
											
											
											
# 									print('goal reached')	
# 									if target==currentCell:		
# 										

										
										
										
										
									
									
								
								
								
								
							
							for w in [[v[0]-1,v[1]], [v[0],v[1]+1],[v[0]+1,v[1]],[v[0],v[1]-1]]:
								
								new_g_cost=g_cost[tuple(v)]+1
								
								new_f_cost= new_g_cost + self.heuristic(w,target)
								
								if self.mymap[w[0]][w[1]]=='.'and w not in visited_cells: 

									if tuple(w) not in g_cost:

										g_cost[tuple(w)]=new_g_cost


										new_f_cost= g_cost[tuple(w)] + self.heuristic(w,target)
										
										came_from[tuple(w)]=v
										
										heapq.heappush(to_visit_cells, (new_f_cost, w))
										
										
										
									if tuple(w) in g_cost :	
										
										
										if new_g_cost< g_cost[tuple(w)]:
											
											g_cost[tuple(w)]= new_g_cost
											
											came_from[tuple(w)]=v
											
											heapq.heappush(to_visit_cells, (new_f_cost, w))
										

										
# 										f_score= g_cost[tuple(w)] + self.heuristic(w,target)
										
										
										
									
									
									
									
									
									
									
									
									
										#print(g_cost)
										
										
										
										
									
									
										
									
									
									
										
								
							
							
							
							
							
						
				
						# frontier.put(start, 0)
						# came_from = {}
						# cost_so_far = {}
						# came_from[start] = None
						# cost_so_far[start] = 0
						# counter = 0					
					

						
# 						qu = []
# 						heapq.heappush(qu, (0, 'data5'))

# 						heapq.heappush(qu, (6, 'data5'))
# 						heapq.heappush(qu, (5, 'data5'))
# 						heapq.heappush(qu, (1, 'data1'))
# 						heapq.heappush(qu, (4, 'data4'))
# 						heapq.heappush(qu, (2, 'data2'))
# 						heapq.heappush(qu, (4, 'data3'))

# 						for a in range(6):

# 							a=heapq.heappop(qu)
# 							print(a)						
