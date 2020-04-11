import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from process import Process
from cube import Cube
from colors import Color
import math
import psutil
import random

# cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
# cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
# cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))

screen_height = 150
screen_width = 400

# def wireCube():
#     glBegin(GL_LINES)
#     for cubeEdge in cubeEdges:
#         for cubeVertex in cubeEdge:
#             glVertex3fv(cubeVertices[cubeVertex])
#     glEnd()
#
# def solidCube():
#     glBegin(GL_QUADS)
#     for cubeQuad in cubeQuads:
#         for cubeVertex in cubeQuad:
#             glVertex3fv(cubeVertices[cubeVertex])
#     glEnd()

def main():
    pg.init()

    display = (screen_width, screen_height)
    # screen = pg.display.set_mode(display, DOUBLEBUF|OPENGL)
    screen = pg.display.set_mode(display)

    # void gluPerspective(GLdouble fovy, GLdouble aspect, GLdouble zNear, GLdouble zFar)
    gluPerspective(90, (display[0]/display[1]), 0.1, 150.0)

    glTranslatef(0.0, 0.0, -20)

    clock = pg.time.Clock()
    current_process = Process()
    color = Color()

    x_rotate = 0
    y_rotate = 0
    z_rotate = 0

    while True:
        screen.fill(color.black)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_rotate += 1
                if event.key == pg.K_RIGHT:
                    x_rotate -= 1
                if event.key == pg.K_UP:
                    y_rotate -= 1
                if event.key == pg.K_DOWN:
                    y_rotate += 1
        clock.tick(1)
        # glTranslatef(x_rotate,y_rotate,z_rotate)
        # glRotatef(x_rotate, y_rotate, 0, 1)
        # glTranslatef(0.0, math.sin(angle), 0.0)
        # glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # solidCube()
        # wireCube()
        #
        process_list = current_process.list_by_username('alexmi')
        processed_list = current_process.list_processed(process_list)
        x_offset = 0
        cube_color = color.white
        for process_dict in processed_list:
            if processed_list[process_dict]['cpu_percent'] > 80:
                cube_color = color.red
            elif processed_list[process_dict]['cpu_percent'] < 80 and processed_list[process_dict]['cpu_percent'] > 30:
                cube_color = color.warning
            else:
                cube_color = color.ok
            for y in range(processed_list[process_dict]['max_process']):
                pg.draw.rect(screen, cube_color, (x_offset,y*20,15,15), 1)
            x_offset += 20

            # if process_sizes[process] > 1 and process_sizes[process] <= 3:
            #     cube_color = color.warning
            # elif process_sizes[process] == 1:
            #     cube_color = color.ok
            # elif process_sizes[process] > 3:
            #     cube_color = color.red

        # cube_dict = {}
        # process_sizes = current_process.get_size_by_process(current_process.get_process_list())
        # y_jump = 0
        # for process in process_sizes:
        #     for x in range(process_sizes[process]):
        #         cube = Cube(x*2.5,y_jump,1)
        #         cube_dict['%s_%d'%(process, x)] = cube
        #     y_jump += 2
        # for cube in cube_dict:
        #     cube_dict[cube].draw()

        pg.display.update()
        pg.time.wait(10)

if __name__ == "__main__":
    main()
