
import bpy


class SPlisHSPlasHObstaclePanel(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "physics"
    bl_label = "SPlisHSPlasH Obstacle"

    @classmethod
    def poll(cls, context):
        splishsplash = context.object.splish_splash
        return splishsplash.is_active and splishsplash.splish_slpash_type == 'OBSTACLE'

    def draw(self, context):
        obj = context.object
        splishsplash = context.object.splish_splash
        lay = self.layout

        # create ui elements
        lay.prop(splishsplash, 'splish_slpash_type')
        lay.prop(splishsplash, 'is_wall')


class SPlisHSPlasHEmitterPanel(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "physics"
    bl_label = "SPlisHSPlasH Emitter"

    @classmethod
    def poll(cls, context):
        splishsplash = context.object.splish_splash
        return splishsplash.is_active and splishsplash.splish_slpash_type == 'EMITTER'

    def draw(self, context):
        obj = context.object
        splishsplash = context.object.splish_splash
        lay = self.layout

        # create ui elements
        lay.prop(splishsplash, 'splish_slpash_type')
        lay.prop(splishsplash, 'emitter_type')


class SPlisHSPlasHFluidPanel(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "physics"
    bl_label = "SPlisHSPlasH Fluid"

    @classmethod
    def poll(cls, context):
        splishsplash = context.object.splish_splash
        return splishsplash.is_active and splishsplash.splish_slpash_type == 'FLUID'

    def draw(self, context):
        obj = context.object
        splishsplash = context.object.splish_splash
        lay = self.layout

        # create ui elements
        lay.prop(splishsplash, 'splish_slpash_type')
        lay.prop(splishsplash, 'initial_velocity')


class SPlisHSPlasHSolverPanel(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "physics"
    bl_label = "SPlisHSPlasH"

    @classmethod
    def poll(cls, context):
        splishsplash = context.object.splish_splash
        return splishsplash.is_active and splishsplash.splish_slpash_type == 'SOLVER'


class SPlisHSPlasHGeneralPanel(SPlisHSPlasHSolverPanel):
    bl_label = "SPlisHSPlasH General"

    def draw(self, context):
        obj = context.object
        splishsplash = context.object.splish_splash
        lay = self.layout

        # create ui elements
        lay.prop(splishsplash, 'splish_slpash_type')
        lay.prop(splishsplash, 'pause')
        lay.prop(splishsplash, 'pause_at')
        lay.prop(splishsplash, 'stop_at')


class SPlisHSPlasHPanel(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "physics"
    bl_label = "SPlisHSPlasH"

    @classmethod
    def poll(cls, context):
        splishsplash = context.object.splish_splash
        return splishsplash.is_active and splishsplash.splish_slpash_type == 'NONE'

    def draw(self, context):
        obj = context.object
        splishsplash = context.object.splish_splash
        lay = self.layout

        # create ui elements
        lay.prop(splishsplash, 'splish_slpash_type')


def splishsplash_fluid_button(self, context):
    obj = context.scene.objects.active
    if not obj.type == 'MESH':
        return

    column = self.layout.column(align=True)
    split = column.split(percentage=0.5)
    column_left = split.column()
    column_right = split.column()

    if obj.splish_splash.is_active:
        column_right.operator(
            "splish_splash.remove", 
            text="SPlisHSPlasH Fluid", 
            icon='X'
        )
    else:
        column_right.operator(
            "splish_splash.add", 
            text="SPlisHSPlasH Fluid", 
            icon='MOD_FLUIDSIM'
        )


__CLASSES__ = [
    SPlisHSPlasHPanel,
    SPlisHSPlasHGeneralPanel,
    SPlisHSPlasHFluidPanel,
    SPlisHSPlasHEmitterPanel,
    SPlisHSPlasHObstaclePanel
]


def register():
    bpy.types.PHYSICS_PT_add.append(splishsplash_fluid_button)
    for class_ in __CLASSES__:
        bpy.utils.register_class(class_)


def unregister():
    for class_ in reversed(__CLASSES__):
        bpy.utils.unregister_class(class_)
    bpy.types.PHYSICS_PT_add.remove(splishsplash_fluid_button)
