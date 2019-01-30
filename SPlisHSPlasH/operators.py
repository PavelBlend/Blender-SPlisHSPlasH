
import bpy


class SPlisHSPlasHFluidAdd(bpy.types.Operator):
    bl_idname = "splish_splash.add"
    bl_label = "Add SPlisHSPlasH fluid object"
    bl_options = {'REGISTER'}

    def execute(self, context):
        obj = context.scene.objects.active
        obj.splish_splash.is_active = True
        return {'FINISHED'}


class SPlisHSPlasHFluidRemove(bpy.types.Operator):
    bl_idname = "splish_splash.remove"
    bl_label = "Remove SPlisHSPlasH fluid object"
    bl_options = {'REGISTER'}

    def execute(self, context):
        obj = context.scene.objects.active
        obj.splish_splash.is_active = False
        obj.splish_splash.splish_slpash_type = 'NONE'
        return {'FINISHED'}


__CLASSES__ = [
    SPlisHSPlasHFluidAdd,
    SPlisHSPlasHFluidRemove
]


def register():
    for class_ in __CLASSES__:
        bpy.utils.register_class(class_)


def unregister():
    for class_ in reversed(__CLASSES__):
        bpy.utils.unregister_class(class_)
