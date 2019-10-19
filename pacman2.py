import os
import tty, termios
import sys
import random
import math

class Player:
	name="O"
	name1=""
	x=2
	y=2
	score=0
	flag=0
	moves=0

player=Player()


class Board:
	line="********************************"
	line1="**O ``````````````````````````**"
	line2="**   ***** ***** ***** `````` **"
	line3="**   *   * *   * ***** `````` **"
	line4="**** *   * *   * *****  ****  **"
	line5="**** ***** *   * ***  ``*  *  **"
	line6="**** **    ***** *****  ****  **"
	line7="**`  **    ** ** *****       G**"
	line8="**`  **    ** ** *****   ```  **"
	line9="**`G                          **"
	line10="** **   ******* **  *****     **"
	line11="** **   ******* **  *****     **"
	line12="**   ``````````````````````   **"
	line13="**  **  ** ***** **  * *****  **"
	line14="**G * ** * *   * * * * *   *  **"
	line15="**  *    * ***** * * * *****  **"
	line16="**  *    * ** ** *  **        **"
	line17="** ```````````````````````````**"
	line18="**```````****`````***```****``**"
	line19="********************************"

	level1=[list(line),list(line),list(line1),list(line2),list(line3),list(line4),list(line5),list(line6),list(line7),list(line8),list(line9),list(line10),list(line11),list(line12),list(line13),list(line14),list(line15),list(line16),list(line16),list(line17),list(line18),list(line19),list(line)]


	def print_board(self):
		for i in range(len(self.level1)):
			for j in range(len(self.level1[i])):
				print(self.level1[i][j], end=' ')
			print()

board=Board()

player.name1=input("Enter Player Name\n")


class Ghost:
	name="G"  
	def dstnc(self,x1,y1,x2,y2):  
	    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
	#move_list=["w","s","a"."d"]
	def move(self):
		while True:
			if player.x<self.x and board.level1[self.y][self.x-1]!="*" and board.level1[self.y][self.x-1]!=ghost.name:
				if self.prev=="`":
					board.level1[self.y][self.x]="`"
				else:
					board.level1[self.y][self.x]=" "
				self.x-=1
				self.prev=board.level1[self.y][self.x]
				board.level1[self.y][self.x]=self.name
				break
			elif player.x>self.x and board.level1[self.y][self.x+1]!="*" and board.level1[self.y][self.x+1]!=ghost.name :
				if self.prev=="`":
					board.level1[self.y][self.x]="`"
				else:
					board.level1[self.y][self.x]=" "
				self.x+=1
				self.prev=board.level1[self.y][self.x]
				board.level1[self.y][self.x]=self.name
				break
			elif player.y<self.y and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name: 
				if self.prev=="`":
					board.level1[self.y][self.x]="`"
				else:
					board.level1[self.y][self.x]=" "
				self.y-=1
				self.prev=board.level1[self.y][self.x]
				board.level1[self.y][self.x]=self.name
				break
			elif player.y>self.y and board.level1[self.y+1][self.x]!="*" and board.level1[self.y+1][self.x]!=ghost.name:
				if self.prev=="`":
					board.level1[self.y][self.x]="`"
				else:
					board.level1[self.y][self.x]=" "
				self.y+=1
				self.prev=board.level1[self.y][self.x]
				board.level1[self.y][self.x]=self.name
				break
			elif player.y<=self.y and board.level1[self.y-1][self.x]=="*":
				if self.dstnc(player.x,player.y,self.x-1,self.y)>=self.dstnc(player.x,player.y,self.x+1,self.y) and board.level1[self.y][self.x-1]!="*" and board.level1[self.y][self.x-1]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.x-=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				elif self.dstnc(player.x,player.y,self.x-1,self.y)<=self.dstnc(player.x,player.y,self.x+1,self.y) and board.level1[self.y][self.x+1]!="*" and board.level1[self.y][self.x+1]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.x+=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				else:
					next=random.randint(0,4)
					while True:
						if next%4==0 and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==1 and board.level1[self.y+1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==2 and board.level1[self.y][self.x-1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==3 and board.level1[self.y][self.x+1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						else:
							break
						next+=1
			elif player.y<=self.y and board.level1[self.y-1][self.x]=="G":
				if self.dstnc(player.x,player.y,self.x-1,self.y)>=self.dstnc(player.x,player.y,self.x+1,self.y) and board.level1[self.y][self.x-1]!="*" and board.level1[self.y][self.x-1]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.x-=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				elif self.dstnc(player.x,player.y,self.x-1,self.y)<=self.dstnc(player.x,player.y,self.x+1,self.y) and board.level1[self.y][self.x+1]!="*" and board.level1[self.y][self.x+1]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.x+=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				else:
					next=random.randint(0,4)
					while True:
						if next%4==0 and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==1 and board.level1[self.y+1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==2 and board.level1[self.y][self.x-1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==3 and board.level1[self.y][self.x+1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						else:
							break
						next+=1
			elif player.y>=self.y and board.level1[self.y+1][self.x]=="*":
				if self.dstnc(player.x,player.y,self.x-1,self.y)>=self.dstnc(player.x,player.y,self.x+1,self.y) and board.level1[self.y][self.x-1]!="*" and board.level1[self.y][self.x-1]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.x-=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				elif self.dstnc(player.x,player.y,self.x-1,self.y)<=self.dstnc(player.x,player.y,self.x+1,self.y) and board.level1[self.y][self.x+1]!="*" and board.level1[self.y][self.x+1]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.x+=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				else:
					next=random.randint(0,4)
					while True:
						if next%4==0 and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==1 and board.level1[self.y+1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==2 and board.level1[self.y][self.x-1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==3 and board.level1[self.y][self.x+1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						else:
							break
						next+=1
			elif player.y>=self.y and board.level1[self.y-1][self.x]=="G":
				if self.dstnc(player.x,player.y,self.x-1,self.y)>=self.dstnc(player.x,player.y,self.x+1,self.y) and board.level1[self.y][self.x-1]!="*" and board.level1[self.y][self.x-1]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.x-=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				elif self.dstnc(player.x,player.y,self.x-1,self.y)<=self.dstnc(player.x,player.y,self.x+1,self.y) and board.level1[self.y][self.x+1]!="*" and board.level1[self.y][self.x+1]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.x+=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				else:
					next=random.randint(0,4)
					while True:
						if next%4==0 and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==1 and board.level1[self.y+1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==2 and board.level1[self.y][self.x-1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==3 and board.level1[self.y][self.x+1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						else:
							break
						next+=1
			elif player.x<=self.x and board.level1[self.y][self.x-1]=="*":
				if self.dstnc(player.x,player.y,self.x,self.y-1)>=self.dstnc(player.x,player.y,self.x,self.y+1) and board.level1[self.y+1][self.x]!="*" and board.level1[self.y+1][self.x-1]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.y+=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				elif self.dstnc(player.x,player.y,self.x,self.y-1)<=self.dstnc(player.x,player.y,self.x,self.y+1) and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.y-=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				else:
					next=random.randint(0,4)
					while True:
						if next%4==0 and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==1 and board.level1[self.y+1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==2 and board.level1[self.y][self.x-1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==3 and board.level1[self.y][self.x+1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						else:
							break
						next+=1
			elif player.x<=self.x and board.level1[self.y][self.x-1]=="G":
				if self.dstnc(player.x,player.y,self.x,self.y+1)>=self.dstnc(player.x,player.y,self.x,self.y-1) and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.y-=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				elif self.dstnc(player.x,player.y,self.x,self.y+1)<=self.dstnc(player.x,player.y,self.x,self.y-1) and board.level1[self.y+1][self.x]!="*" and board.level1[self.y+1][self.x]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.y+=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				else:
					next=random.randint(0,4)
					while True:
						if next%4==0 and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==1 and board.level1[self.y+1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==2 and board.level1[self.y][self.x-1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==3 and board.level1[self.y][self.x+1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						else:
							break
						next+=1
			elif player.x>=self.x and board.level1[self.y][self.x+1]=="*":
				if self.dstnc(player.x,player.y,self.x,self.y-1)>=self.dstnc(player.x,player.y,self.x,self.y+1) and board.level1[self.y+1][self.x]!="*" and board.level1[self.y+1][self.x]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.y+=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				elif self.dstnc(player.x,player.y,self.x,self.y-1)<=self.dstnc(player.x,player.y,self.x,self.y+1) and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.y-=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				else:
					next=random.randint(0,4)
					while True:
						if next%4==0 and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==1 and board.level1[self.y+1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==2 and board.level1[self.y][self.x-1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==3 and board.level1[self.y][self.x+1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						else:
							break
						next+=1
			elif player.x>=self.x and board.level1[self.y-1][self.x+1]=="G":
				if self.dstnc(player.x,player.y,self.x,self.y-1)>=self.dstnc(player.x,player.y,self.x,self.y+1) and board.level1[self.y+1][self.x]!="*" and board.level1[self.y+1][self.x]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.y+=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				elif self.dstnc(player.x,player.y,self.x,self.y-1)<=self.dstnc(player.x,player.y,self.x,self.y+1) and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
					if self.prev=="`":
						board.level1[self.y][self.x]="`"
					else:
						board.level1[self.y][self.x]=" "
					self.y-=1
					self.prev=board.level1[self.y][self.x]
					board.level1[self.y][self.x]=self.name
					break
				else:
					next=random.randint(0,4)
					while True:
						if next%4==0 and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==1 and board.level1[self.y+1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.y+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==2 and board.level1[self.y][self.x-1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x-=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						elif next%4==3 and board.level1[self.y][self.x+1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
							if self.prev=="`":
								board.level1[self.y][self.x]="`"
							else:
								board.level1[self.y][self.x]=" "
							self.x+=1
							self.prev=board.level1[self.y][self.x]
							board.level1[self.y][self.x]=self.name
							break
						else:
							break
						next+=1
			else:
				next=random.randint(0,4)
				while True:
					if next%4==0 and board.level1[self.y-1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
						if self.prev=="`":
							board.level1[self.y][self.x]="`"
						else:
							board.level1[self.y][self.x]=" "
						self.y-=1
						self.prev=board.level1[self.y][self.x]
						board.level1[self.y][self.x]=self.name
						break
					elif next%4==1 and board.level1[self.y+1][self.x]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
						if self.prev=="`":
							board.level1[self.y][self.x]="`"
						else:
							board.level1[self.y][self.x]=" "
						self.y+=1
						self.prev=board.level1[self.y][self.x]
						board.level1[self.y][self.x]=self.name
						break
					elif next%4==2 and board.level1[self.y][self.x-1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
						if self.prev=="`":
							board.level1[self.y][self.x]="`"
						else:
							board.level1[self.y][self.x]=" "
						self.x-=1
						self.prev=board.level1[self.y][self.x]
						board.level1[self.y][self.x]=self.name
						break
					elif next%4==3 and board.level1[self.y][self.x+1]!="*" and board.level1[self.y-1][self.x]!=ghost.name:
						if self.prev=="`":
							board.level1[self.y][self.x]="`"
						else:
							board.level1[self.y][self.x]=" "
						self.x+=1
						self.prev=board.level1[self.y][self.x]
						board.level1[self.y][self.x]=self.name
						break
					else:
						break
					next+=1





ghost=Ghost()
class Ghost1(Ghost):
	prev=" "
	x=3
	y=10
ghost1=Ghost1()

class Ghost2(Ghost):
	prev=" "
	x=2
	y=15

ghost2=Ghost2()
class Ghost3(Ghost):
	prev=" "
	x=29
	y=8
ghost3=Ghost3()


def getch():
  import sys, tty, termios
  old_settings = termios.tcgetattr(0)
  new_settings = old_settings[:]
  new_settings[3] &= ~termios.ICANON
  try:
    termios.tcsetattr(0, termios.TCSANOW, new_settings)
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(0, termios.TCSANOW, old_settings)
  return ch

while True:
	os.system('clear')
	board.print_board() 
	print (player.name1,"     ","Position: ",player.x,player.y,"    Score: ",player.score,"     Moves:",player.moves)
	move=getch()
	if move=="w" or move=="a" or move=="s" or move=="d":
		ghost1.move()
		ghost2.move()
		ghost3.move()

	if move=="w" and board.level1[player.y-1][player.x]!="*":
		if board.level1[player.y][player.x]!=ghost.name:
			board.level1[player.y][player.x]=" "
		player.y=player.y-1
		if board.level1[player.y][player.x]=="`":
			player.score+=1
		board.level1[player.y][player.x]=player.name
	elif move=="s" and board.level1[player.y+1][player.x]!="*":
		if board.level1[player.y][player.x]!=ghost.name:
			board.level1[player.y][player.x]=" "
		player.y=player.y+1
		if board.level1[player.y][player.x]=="`":
			player.score+=1
		board.level1[player.y][player.x]=player.name
	elif move=="a" and board.level1[player.y][player.x-1]!="*":
		if board.level1[player.y][player.x]!=ghost.name:
			board.level1[player.y][player.x]=" "
		player.x=player.x-1
		if board.level1[player.y][player.x]=="`":
			player.score+=1
		board.level1[player.y][player.x]=player.name
	elif move=="d" and board.level1[player.y][player.x+1]!="*":
		if board.level1[player.y][player.x]!=ghost.name:
			board.level1[player.y][player.x]=" "
		player.x=player.x+1
		if board.level1[player.y][player.x]=="`":
			player.score+=1
		board.level1[player.y][player.x]=player.name
	
	if player.score==112:
		player.flag=1;
		break
	elif ghost1.x==player.x and ghost1.y==player.y:
		break
	elif ghost2.x==player.x and ghost2.y==player.y:
		break
	elif ghost3.x==player.x and ghost3.y==player.y:
		break
	player.moves+=1

if player.flag==0:
	os.system('clear')
	print ("Sorry You Lost!!")
	print ("Try Again!!")
	print ("Your Score was:",player.score)
elif player.flag==1:
	print ("You Won in ",player.moves,".You can improve further!!")
