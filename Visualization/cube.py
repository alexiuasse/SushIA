from OpenGL.GL import *
from OpenGL.GLU import *

class Cube:
    """
    Object cube with vertices setup and draw.
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
        self.cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
        self.cubeVertices = self.set_vertices()

    # Um cubo tem 8 vertices
    def set_vertices(self):
        """
        Set the vertices of the cube, using bases vertices and offset.
        """

        new_vertices = []
        for vert in self.vertices:
            new_vert = []

            new_x = vert[0] + self.x
            new_y = vert[1] + self.y
            new_z = vert[2] + self.z

            new_vert.append(new_x)
            new_vert.append(new_y)
            new_vert.append(new_z)

            new_vertices.append(new_vert)

        return new_vertices

    def draw(self):
        """
        Drawing the cube with LINES
        """

        glBegin(GL_LINES)
        glRotatef(0,1,0,1)
        for cubeEdge in self.cubeEdges:
            for cubeVertex in cubeEdge:
                glVertex3fv(self.cubeVertices[cubeVertex])
        glEnd()
