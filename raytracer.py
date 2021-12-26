import numpy as np


diffuse_rays = 1000


'''
This class contains the scene. It computes ray collisions with all the available materials
'''
class Geometry:
    def __init__(self):
        pass

    '''
    This function calculated the next hit of every ray in the numpy arrays.
    The rays consist of a position, direction and property object located at
    equal indices in the three arrays.
    
    In this function the ray_dir array will be changed, so that the length of the
    rays matches the found collisions.
    
    This function returns three new arrays which represent the new reflected rays.
    The returned ray_dir are normalized (2D unit vectors)
    '''
    def hit(self, ray_pos: np.ndarray, ray_dir: np.ndarray, ray_props: np.ndarray):
        # TODO collide the rays with the geometry and return new rays
        raise NotImplementedError()


def create_point_light_rays(x, y, props=None):
    ray_pos = np.array([(x, y)] * diffuse_rays)
    ray_dir = np.array([(np.cos(i/diffuse_rays*2*np.pi), np.sin(i/diffuse_rays*2*np.pi)) for i in range(diffuse_rays)])
    ray_props = np.array([props] * diffuse_rays)
    return ray_pos, ray_dir, ray_props


def create_spot_light_rays(x, y, dir_x, dir_y, angle, props=None):
    ray_pos = np.array([(x, y)] * diffuse_rays)
    ray_dir = np.array([(np.cos(i/diffuse_rays*2*np.pi), np.sin(i/diffuse_rays*2*np.pi)) for i in range(diffuse_rays)])
    ray_props = np.array([props] * diffuse_rays)
    return ray_pos, ray_dir, ray_props
