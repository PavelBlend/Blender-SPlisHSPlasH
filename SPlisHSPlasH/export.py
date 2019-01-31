
import json

import bpy


class SPlisHSPlasHExportSceneToJSON(bpy.types.Operator):
    bl_idname = "splish_splash.export"
    bl_label = "Export Scene"
    bl_options = {'REGISTER'}

    def execute(self, context):
        solver = context.scene.objects.active
        settings = solver.splish_splash
        data = {}

        # Configuration
        config = {}

        config['pause'] = settings.pause
        config['pauseAt'] = settings.pause_at
        config['stopAt'] = settings.stop_at
        config['numberOfStepsPerRenderUpdate'] = settings.number_of_steps_per_render_update
        config['colorField'] = settings.color_field
        config['colorMapType'] = int(settings.color_map_type)
        config['renderMinValue'] = settings.render_min_value
        config['renderMaxValue'] = settings.render_max_value
        config['renderWalls'] = int(settings.render_walls)
        config['enablePartioExport'] = settings.enable_partio_export
        config['enablePartioExport'] = settings.enable_partio_export
        config['partioFPS'] = settings.partio_fps
        config['timeStepSize'] = settings.time_step_size
        config['particleRadius'] = settings.particle_padius
        config['sim2D'] = False
        config['gravitation'] = [settings.gravitation[0], settings.gravitation[2], settings.gravitation[1]]
        config['maxIterations'] = settings.max_iterations
        config['maxError'] = settings.max_error
        config['simulationMethod'] = int(settings.simulation_method)
        config['stiffness'] = settings.stiffness
        config['exponent'] = settings.exponent
        config['velocityUpdateMethod'] = int(settings.velocity_update_method)
        config['enableDivergenceSolver'] = settings.enable_divergence_solver
        config['maxIterationsV'] = settings.max_iterations_v
        config['maxErrorV'] = settings.max_error_v
        config['kernel'] = int(settings.kernel)
        config['gradKernel'] = int(settings.grad_kernel)
        config['cflMethod'] = int(settings.cfl_method)
        config['cflFactor'] = settings.cfl_factor
        config['cflMaxTimeStepSize'] = settings.cfl_max_time_step_size

        data['Configuration'] = config

        fluids_objects = set()
        obstacle_objects = set()
        for obj in bpy.data.objects:
            if obj.splish_splash.splish_slpash_type == 'FLUID':
                fluids_objects.add(obj)
            elif obj.splish_splash.splish_slpash_type == 'OBSTACLE':
                obstacle_objects.add(obj)

        fluid_blocks = []
        for obj in fluids_objects:
            fluid = {}
            settings = obj.splish_splash

            fluid['start'] = obj.bound_box[0][0], obj.bound_box[0][2], obj.bound_box[0][1]
            fluid['end'] = obj.bound_box[6][0], obj.bound_box[6][2], obj.bound_box[6][1]
            fluid['translation'] = obj.location[0], obj.location[2], obj.location[1]
            fluid['scale'] = obj.scale[0], obj.scale[2], obj.scale[1]
            fluid['denseMode'] = int(settings.dense_mode)
            fluid['initialVelocity'] = settings.initial_velocity[0], settings.initial_velocity[2], settings.initial_velocity[1]

            fluid_blocks.append(fluid)

        data['FluidBlocks'] = fluid_blocks

        obstacles = []
        bpy.ops.object.select_all(action='DESELECT')
        for obj in obstacle_objects:
            obstacle = {}
            settings = obj.splish_splash

            obj.select = True
            path = '{}.obj'.format(obj.name)
            bpy.ops.export_scene.obj(
                filepath=path,
                check_existing=True,
                axis_forward='-Z',
                axis_up='Y',
                filter_glob="*.obj;*.mtl",
                use_selection=True,
                use_animation=False,
                use_mesh_modifiers=True,
                use_mesh_modifiers_render=False,
                use_edges=False,
                use_smooth_groups=False,
                use_smooth_groups_bitflags=False,
                use_normals=True,
                use_uvs=False,
                use_materials=False,
                use_triangles=True,
                use_nurbs=False,
                use_vertex_groups=False,
                use_blen_objects=False,
                group_by_object=False,
                group_by_material=False,
                keep_vertex_order=False,
                global_scale=1,
                path_mode='AUTO'
            )
            obstacle['geometryFile'] = path
            obstacle['isDynamic'] = False
            obstacle['isWall'] = settings.is_wall
            obstacle['color'] = settings.color[0], settings.color[1], settings.color[2], settings.color[3]
            obj.select = False

            obstacles.append(obstacle)

        data['RigidBodies'] = obstacles

        json_scene = open('D:\\test_scene.json', 'w')
        json.dump(data, json_scene, indent=4, sort_keys=True)
        json_scene.close()

        return {'FINISHED'}


__CLASSES__ = [
    SPlisHSPlasHExportSceneToJSON,
]


def register():
    for class_ in __CLASSES__:
        bpy.utils.register_class(class_)


def unregister():
    for class_ in reversed(__CLASSES__):
        bpy.utils.unregister_class(class_)
