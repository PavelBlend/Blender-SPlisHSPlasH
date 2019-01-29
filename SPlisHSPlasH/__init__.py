
bl_info = {
    'name': 'SPlisHSPlasH',
    'author': 'Pavel_Blend',
    'version': ('Demo', 0, 0, 1),
    'blender': (2, 79, 0),
    'category': 'Animation',
    'warning': 'Demo version'
}


from . import load_bgeo_cache
from . import properties


modules = [
    properties,
    load_bgeo_cache
]


def register():
    for module in modules:
        module.register()


def unregister():
    for module in reversed(modules):
        module.unregister()
