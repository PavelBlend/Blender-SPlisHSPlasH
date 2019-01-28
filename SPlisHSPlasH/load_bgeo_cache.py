
import os
import gzip
import struct

import bpy


DATA_NAME = 'SPlisHSPlasH'


class Header:
    def __init__(self):
        points_count = 0
        prims_count = 0
        point_groups_count = 0
        prim_groups_count = 0
        point_attributes_count = 0
        vertex_attributes_count = 0
        prim_attributes_count = 0
        attributes_count = 0


class Particles:
    def __init__(self):
        self.locations = []
        self.velocities = []
        self.indices = []


def remove_old_mesh():
    if bpy.data.meshes.get(DATA_NAME):
        old_mesh = bpy.data.meshes[DATA_NAME]
        old_mesh.name = DATA_NAME + '_Temp'
    else:
        old_mesh = None
    if bpy.data.objects.get(DATA_NAME):
        bpy_object = bpy.data.objects[DATA_NAME]
        bpy_mesh = bpy.data.meshes.new(DATA_NAME)
        bpy_object.data = bpy_mesh
    if old_mesh:
        bpy.data.meshes.remove(old_mesh)


def import_particles(particles):
    if bpy.data.meshes.get(DATA_NAME):
        old_mesh = bpy.data.meshes[DATA_NAME]
        old_mesh.name = DATA_NAME + '_Temp'
    else:
        old_mesh = None
    bpy_mesh = bpy.data.meshes.new(DATA_NAME)
    if not bpy.data.objects.get(DATA_NAME):
        bpy_object = bpy.data.objects.new(DATA_NAME, bpy_mesh)
        bpy.context.scene.objects.link(bpy_object)
    else:
        bpy_object = bpy.data.objects[DATA_NAME]
        bpy_object.data = bpy_mesh
    bpy_mesh.from_pydata(particles.locations, (), ())
    if old_mesh:
        bpy.data.meshes.remove(old_mesh)


def read_attributes(header, data, position):
    particles = Particles()

    for particle_index in range(header.points_count):
        location = struct.unpack('>3f', data[position : position + 12])
        position += 12

        velocity = struct.unpack('>3f', data[position : position + 12])
        position += 12

        unknown = struct.unpack('>I', data[position : position + 4])[0]
        position += 4

        index = struct.unpack('>I', data[position : position + 4])[0]
        position += 4

        particles.locations.append((location[0], location[2], location[1]))
        particles.velocities.append((velocity[0], velocity[2], velocity[1]))
        particles.indices.append(index)

    return particles


def read_particles(data, position, header):
    if (
            header.prims_count != 0 or \
            header.point_groups_count != 0 or \
            header.prim_groups_count != 0 or \
            header.vertex_attributes_count != 0 or \
            header.prim_attributes_count != 0 or \
            header.attributes_count != 0
        ):
        raise BaseException('Unsupported data types')

    if header.point_attributes_count != 2:
        raise BaseException('Unsupported point attributes count')

    attributes = []
    sizes = []
    data_formats = {
        1: '>I',
        5: '>3f'
    }
    for attribute_index in range(header.point_attributes_count):
        length = struct.unpack('>H', data[position : position + 2])[0]
        position += 2

        attribute_name = struct.unpack('>{}s'.format(length), data[position : position + length])[0]
        position += length
        attributes.append(attribute_name)

        dimention = struct.unpack('>H', data[position : position + 2])[0]
        position += 2
        sizes.append(dimention)

        # 0 - float, 1 - int, 5 - vector
        data_type = struct.unpack('>I', data[position : position + 4])[0]
        position += 4

        data_format = data_formats[data_type]
        default_value = struct.unpack(data_format, data[position : position + struct.calcsize(data_format)])
        position += struct.calcsize(data_format)

    if attributes != [b'velocity', b'id']:
        raise BaseException('Unsupported attributes')

    if sizes != [3, 1]:
        raise BaseException('Incorrect attributes sizes')

    particles = read_attributes(header, data, position)
    import_particles(particles)


def read_header(data, position):
    # bgeo magic
    bgeo_magic = struct.unpack('>4s', data[position : position + 4])[0]
    position += 4
    if bgeo_magic != b'Bgeo':
        raise BaseException('Unknown Format')

    # version
    version_char = struct.unpack('>s', data[position : position + 1])[0]
    position += 1
    if version_char != b'V':
        raise BaseException('Bad bgeo file')

    version = struct.unpack('>I', data[position : position + 4])[0]
    position += 4
    if version != 5:
        raise BaseException('Unsupported version')

    # particles
    header = Header()

    header.points_count = struct.unpack('>I', data[position : position + 4])[0]
    position += 4

    header.prims_count = struct.unpack('>I', data[position : position + 4])[0]
    position += 4

    header.point_groups_count = struct.unpack('>I', data[position : position + 4])[0]
    position += 4

    header.prim_groups_count = struct.unpack('>I', data[position : position + 4])[0]
    position += 4

    header.point_attributes_count = struct.unpack('>I', data[position : position + 4])[0]
    position += 4

    header.vertex_attributes_count = struct.unpack('>I', data[position : position + 4])[0]
    position += 4

    header.prim_attributes_count = struct.unpack('>I', data[position : position + 4])[0]
    position += 4

    header.attributes_count = struct.unpack('>I', data[position : position + 4])[0]
    position += 4

    return header, position


def read_bgeo(data):
    position = 0
    header, position = read_header(data, position)
    read_particles(data, position, header)


def decompress_gzip_archive(file_path):
    gzip_file = gzip.open(file_path, 'rb')
    gzip_data = gzip_file.read()
    gzip_file.close()
    return gzip_data


@bpy.app.handlers.persistent
def import_bgeo(scene):
    cache_folder = 'D:\\sources\\fluid_simulations\\SPlisHSPlasH\\SPlisHSPlasH-master\\bin\\output\\CoilingModel_Weiler2018\\partio\\'
    file_path = cache_folder + 'ParticleData_Fluid_{}.bgeo'.format(bpy.context.scene.frame_current)
    if os.path.exists(file_path):
        bgeo_data = decompress_gzip_archive(file_path)
        read_bgeo(bgeo_data)
    else:
        remove_old_mesh()


def register():
    bpy.app.handlers.frame_change_pre.append(import_bgeo)


def unregister():
    bpy.app.handlers.frame_change_pre.remove(import_bgeo)
