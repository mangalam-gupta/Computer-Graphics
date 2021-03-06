from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def house():
	glClearColor(0, 0, 0, 0)
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPointSize(2)
	glBegin(GL_QUADS)
	glColor3f(1.0, 0, 0)
	glVertex2f(0,0)
	glVertex2f(0.20, 0.0)
	glVertex2f(0.20, 0.20)
	glVertex2f(0.0, 0.20)
	glEnd()
	glBegin(GL_QUADS)
	glColor3f(0, 0, 0)
	glVertex2f(0.05, 0.0)
	glVertex2f(0.15, 0.0)
	glVertex2f(0.15, 0.15)
	glVertex2f(0.05, 0.15)
	glEnd()
	glBegin(GL_TRIANGLES)
	glColor3f(0, 0, 1.0)
	glVertex2f(0.1,0.3)
	glVertex2f(-0.1, 0.2)
	glVertex2f(0.3, 0.20)
	glEnd()
	glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow('House')

glutDisplayFunc(house)
glutMainLoop()