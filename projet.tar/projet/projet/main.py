from viewerGL import ViewerGL
import glutils
from mesh import Mesh
from cpe3d import Object3D, Camera, Transformation3D, Text
import numpy as np
import OpenGL.GL as GL
import pyrr
import random 

def main():
    viewer = ViewerGL()

    viewer.set_camera(Camera())
    viewer.cam.transformation.translation.y = 2
    viewer.cam.transformation.rotation_center = viewer.cam.transformation.translation.copy()

    program3d_id = glutils.create_program_from_file('shader.vert', 'shader.frag')
    programGUI_id = glutils.create_program_from_file('gui.vert', 'gui.frag')

    m = Mesh.load_obj('fermierdebout.obj')
    m.normalize()
    m.apply_matrix(pyrr.matrix44.create_from_scale([2, 2, 2, 1]))
    tr = Transformation3D()
    tr.translation.y = -np.amin(m.vertices, axis=0)[1]
    tr.translation.z = -5
    tr.rotation_center.z = 0.2
    texture = glutils.load_texture('farmer.jpg')
    o = Object3D(m.load_to_gpu(), m.get_nb_triangles(), program3d_id, texture, tr)
    viewer.add_object(o)

    m = Mesh()
    p0, p1, p2, p3 = [-25, 0, -25], [25, 0, -25], [25, 0, 25], [-25, 0, 25]
    n, c = [0, 1, 0], [1, 1, 1]
    t0, t1, t2, t3 = [0, 0], [1, 0], [1, 1], [0, 1]
    m.vertices = np.array([[p0 + n + c + t0], [p1 + n + c + t1], [p2 + n + c + t2], [p3 + n + c + t3]], np.float32)
    m.faces = np.array([[0, 1, 2], [0, 2, 3]], np.uint32)
    texture = glutils.load_texture('grass.jpg')
    o = Object3D(m.load_to_gpu(), m.get_nb_triangles(), program3d_id, texture, Transformation3D())
    viewer.add_object(o)

    vao = Text.initalize_geometry()
    texture = glutils.load_texture('fontB.jpg')
    o = Text('La ferme de moutons', np.array([-0.8, 0.3], np.float32), np.array([0.8, 0.8], np.float32), vao, 2, programGUI_id, texture)
    viewer.add_object(o)


#création des moutons
    m = Mesh.load_obj('mouton.obj')
    m.normalize()
    m.apply_matrix(pyrr.matrix44.create_from_scale([1, 1, 1, 1]))
    vao = m.load_to_gpu()
    tr = Transformation3D()
    tr.translation.y = -np.amin(m.vertices, axis=0)[1]
    tr.translation.z = 0
    tr.translation.x = 6
    tr.rotation_euler = pyrr.euler.create(roll=90, pitch=0.0, yaw=0.0, dtype=None)
    tr.rotation_center.z = 0.2
    texture = glutils.load_texture('fourrure mouton.jpg')
    o = Object3D(vao, m.get_nb_triangles(), program3d_id, texture, tr)
    viewer.add_object(o)

#ajout des autres moutons
    t2 = Transformation3D()
    t2.translation.y = -np.amin(m.vertices, axis=0)[1]
    t2.translation.z = 3
    t2.rotation_euler = pyrr.euler.create(roll=90, pitch=0.0, yaw=0.0, dtype=None)
    t2.translation.z = 10
    o = Object3D(vao, m.get_nb_triangles(), program3d_id, texture, t2)
    viewer.add_object(o)

    t3 = Transformation3D()
    t3.translation.y = -np.amin(m.vertices, axis=0)[1]
    t3.translation.z = -5
    t3.rotation_euler = pyrr.euler.create(roll=90, pitch=0.0, yaw=0.0, dtype=None)
    t3.translation.z = -10
    o = Object3D(vao, m.get_nb_triangles(), program3d_id, texture, t3)
    viewer.add_object(o)

    t4 = Transformation3D()
    t4.translation.y = -np.amin(m.vertices, axis=0)[1]
    t4.translation.z = 0
    t4.translation.x = -6
    t4.rotation_euler = pyrr.euler.create(roll=90, pitch=0.0, yaw=0.0, dtype=None)
    t4.translation.z = -10
    o = Object3D(vao, m.get_nb_triangles(), program3d_id, texture, t4)
    viewer.add_object(o)
    
    for i in range(5,15):
        ti = Transformation3D()
        ti.translation.y = -np.amin(m.vertices, axis=0)[1]
        ti.translation.z = random.random()*20-10
        ti.translation.x = random.random()*20-10
        ti.rotation_euler = pyrr.euler.create(roll=90, pitch=0.0, yaw=0.0, dtype=None)
        o = Object3D(vao, m.get_nb_triangles(), program3d_id, texture, ti)
        viewer.add_object(o)


    viewer.run()


if __name__ == '__main__':
    main()