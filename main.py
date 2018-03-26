from qtido import *

w = creer(500, 500)
w.widget.setWindowTitle("Tetris")
FPS = 10

while not est_fermee(w):
	# Du contenu incoming lol
	attendre_pendant(w, 1000/FPS)
#haha
#je suis un génie