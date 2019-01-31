
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
        lay.prop(splishsplash, 'color')


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
        lay.prop(splishsplash, 'velocity')
        lay.prop(splishsplash, 'emits_per_second')


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
        lay.prop(splishsplash, 'dense_mode')
        lay.prop(splishsplash, 'initial_velocity')


class SPlisHSPlasHSolverPanel(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "physics"
    bl_label = "SPlisHSPlasH"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        splishsplash = context.object.splish_splash
        return splishsplash.is_active and splishsplash.splish_slpash_type == 'SOLVER'


class SPlisHSPlasHCFLPanel(SPlisHSPlasHSolverPanel):
    bl_label = "SPlisHSPlasH CFL"

    def draw(self, context):
        obj = context.object
        splishsplash = context.object.splish_splash
        lay = self.layout

        # create ui elements
        lay.prop(splishsplash, 'cfl_method')
        lay.prop(splishsplash, 'cfl_factor')
        lay.prop(splishsplash, 'cfl_max_time_step_size')


class SPlisHSPlasHKernelPanel(SPlisHSPlasHSolverPanel):
    bl_label = "SPlisHSPlasH Kernel"

    def draw(self, context):
        obj = context.object
        splishsplash = context.object.splish_splash
        lay = self.layout

        # create ui elements
        lay.prop(splishsplash, 'kernel')
        lay.prop(splishsplash, 'grad_kernel')


class SPlisHSPlasHSimulationPanel(SPlisHSPlasHSolverPanel):
    bl_label = "SPlisHSPlasH Simulation"

    def draw(self, context):
        obj = context.object
        splishsplash = context.object.splish_splash
        lay = self.layout

        # create ui elements
        lay.prop(splishsplash, 'time_step_size')
        lay.prop(splishsplash, 'particle_padius')
        lay.prop(splishsplash, 'gravitation')
        lay.prop(splishsplash, 'max_iterations')
        lay.prop(splishsplash, 'max_error')
        lay.prop(splishsplash, 'simulation_method')
        # WCSPH
        if splishsplash.simulation_method == '0':
            lay.prop(splishsplash, 'stiffness')
            lay.prop(splishsplash, 'exponent')
        # PBF
        elif splishsplash.simulation_method == '2':
            lay.prop(splishsplash, 'velocity_update_method')
        # DFSPH
        elif splishsplash.simulation_method == '4':
            lay.prop(splishsplash, 'enable_divergence_solver')
            lay.prop(splishsplash, 'max_iterations_v')
            lay.prop(splishsplash, 'max_error_v')
        # Projective Fluids
        elif splishsplash.simulation_method == '5':
            lay.prop(splishsplash, 'stiffness_pf')


class SPlisHSPlasHExportPanel(SPlisHSPlasHSolverPanel):
    bl_label = "SPlisHSPlasH Export"

    def draw(self, context):
        obj = context.object
        splishsplash = context.object.splish_splash
        lay = self.layout

        # create ui elements
        lay.prop(splishsplash, 'enable_partio_export')
        lay.prop(splishsplash, 'partio_fps')


class SPlisHSPlasHVisualizationPanel(SPlisHSPlasHSolverPanel):
    bl_label = "SPlisHSPlasH Visualization"

    def draw(self, context):
        obj = context.object
        splishsplash = context.object.splish_splash
        lay = self.layout

        # create ui elements
        lay.prop(splishsplash, 'number_of_steps_per_render_update')
        lay.prop(splishsplash, 'color_field')
        lay.prop(splishsplash, 'color_map_type')
        lay.prop(splishsplash, 'render_min_value')
        lay.prop(splishsplash, 'render_max_value')
        lay.prop(splishsplash, 'render_walls')


class SPlisHSPlasHGeneralPanel(SPlisHSPlasHSolverPanel):
    bl_label = "SPlisHSPlasH General"
    bl_options = set()

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
    SPlisHSPlasHVisualizationPanel,
    SPlisHSPlasHExportPanel,
    SPlisHSPlasHSimulationPanel,
    SPlisHSPlasHKernelPanel,
    SPlisHSPlasHCFLPanel,
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
