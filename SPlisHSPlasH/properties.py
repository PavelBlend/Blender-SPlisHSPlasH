
import bpy


class SPlisHSplaSHProps(bpy.types.PropertyGroup):
    bpy_type = bpy.types.Object

    # Solver

    # General
    pause = bpy.props.BoolProperty(default=False, name='Pause')
    pause_at = bpy.props.FloatProperty(default=-1.0, name='Pause At')
    stop_at = bpy.props.FloatProperty(default=-1.0, name='Stop At')

    # Visualization
    number_of_steps_per_render_update = bpy.props.IntProperty(
        default=0,
        name='Number of Steps Per Render Update'
    )
    color_field = bpy.props.IntProperty(name='Color Field', default=0)
    color_map_type_items = [
        ('0', 'None', ''),
        ('1', 'Jet', ''),
        ('2', 'Plasma', '')
    ]
    color_map_type = bpy.props.EnumProperty(
        items=color_map_type_items,
        name='Color Map Type',
        default='0'
    )
    render_min_value = bpy.props.FloatProperty(default=0.0, name='Render Min Value')
    render_max_value = bpy.props.FloatProperty(default=1.0, name='Render Max Value')
    render_walls_items = [
        ('0', 'None', ''),
        ('1', 'Particles (all)', ''),
        ('2', 'Particles (no walls)', ''),
        ('3', 'Geometry (all)', ''),
        ('4', 'Geometry (no walls)', '')
    ]
    render_walls = bpy.props.EnumProperty(
        items=render_walls_items,
        name='Render Walls',
        default='1'
    )

    # Export
    enable_partio_export = bpy.props.BoolProperty(default=True, name='Enable Partio Export')
    partio_fps = bpy.props.IntProperty(
        default=30,
        name='Partio FPS'
    )

    # Simulation
    time_step_size = bpy.props.FloatProperty(default=0.001, name='Time Step Size')
    particle_padius = bpy.props.FloatProperty(default=0.025, name='Particle Radius')
    # sim_2d = bpy.props.BoolProperty(default=False, name='Simulation 2D')
    gravitation = bpy.props.FloatVectorProperty(default=(0.0, 0.0, -9.8), name='Gravitation')
    max_iterations = bpy.props.IntProperty(name='Max Iterations', default=1)
    max_error = bpy.props.FloatProperty(default=0.001, name='Max Error')
    simulation_method_items = [
        ('0', 'WCSPH', ''),
        ('1', 'PCISPH', ''),
        ('2', 'PBF', ''),
        ('3', 'IISPH', ''),
        ('4', 'DFSPH', ''),
        ('5', 'Projective Fluids', '')
    ]
    simulation_method = bpy.props.EnumProperty(
        items=simulation_method_items,
        name='Simulation Method',
        default='0'
    )

    # WCSPH parameters
    stiffness = bpy.props.FloatProperty(default=1.0, name='Stiffness')
    exponent = bpy.props.FloatProperty(default=1.0, name='Exponent')

    # PBF parametres
    velocity_update_method_items = [
        ('0', 'First Order Update', ''),
        ('1', 'Second Order Update', '')
    ]
    velocity_update_method = bpy.props.EnumProperty(
        items=velocity_update_method_items,
        name='Velocity Update Method',
        default='0'
    )

    # DFSPH parameters
    enable_divergence_solver = bpy.props.BoolProperty(default=True, name='Enable Divergence Solver')
    max_iterations_v = bpy.props.IntProperty(default=1, name='Max Iterations V')
    max_error_v = bpy.props.FloatProperty(default=0.01, name='Max Error V')

    # Projective Fluids parameters
    stiffness_pf = bpy.props.FloatProperty(default=1.0, name='Stiffness')

    # Kernel
    kernel_items = [
        ('0', 'Cubic Spline', ''),
        ('1', 'Wendland Quintic C2', ''),
        ('2', 'Poly6', ''),
        ('3', 'Spiky', ''),
        ('4', 'Precomputed Cubic Spline', ''),
    ]
    kernel = bpy.props.EnumProperty(
        items=kernel_items,
        name='Kernel',
        default='0'
    )
    grad_kernel_items = [
        ('0', 'Cubic Spline', ''),
        ('1', 'Wendland Quintic C2', ''),
        ('2', 'Poly6', ''),
        ('3', 'Spiky', ''),
        ('4', 'Precomputed Cubic Spline', ''),
    ]
    grad_kernel = bpy.props.EnumProperty(
        items=grad_kernel_items,
        name='Grad Kernel',
        default='0'
    )

    # CFL
    cfl_method_items = [
        ('0', 'No Adaptive Time Stepping', ''),
        ('1', 'Use CFL Condition', ''),
        ('2', 'Use CFL Condition and Consider Number of Pressure Solver Iterations', '')
    ]
    cfl_method = bpy.props.EnumProperty(
        items=cfl_method_items,
        name='CFL Method',
        default='0'
    )
    cfl_factor = bpy.props.FloatProperty(default=1.0, name='CFL Factor')
    cfl_max_time_step_size = bpy.props.FloatProperty(default=0.01, name='CFL Max Time Step Size')

    # Fluid blocks
    dense_mode_items = [
        ('0', 'Regular Sampling', ''),
        ('1', 'More Dense Sampling', ''),
        ('2', 'Dense Sampling', '')
    ]
    dense_mode = bpy.props.EnumProperty(
        items=dense_mode_items,
        name='Dense Mode',
        default='0'
    )
    initial_velocity = bpy.props.FloatVectorProperty(default=(0.0, 0.0, 0.0), name='Initial Velocity')

    # Emitters
    type_items = [
        ('0', 'Box', ''),
        ('1', 'Circle', '')
    ]
    type = bpy.props.EnumProperty(
        items=type_items,
        name='Type',
        default='0'
    )
    velocity = bpy.props.FloatVectorProperty(default=(0.0, 0.0, 0.0), name='Velocity')
    emits_per_second = bpy.props.FloatProperty(default=1.0, name='Emits Per Second')

    # Rigid Bodies
    is_wall = bpy.props.BoolProperty(default=False, name='Is Wall')
    color = bpy.props.FloatVectorProperty(default=(1.0, 1.0, 1.0, 1.0), name='Color', size=4)

    # Fluid parameter block
    density0 = bpy.props.FloatProperty(default=1000.0, name='Density')
    # Viscosity
    viscosity_method_items = [
        ('0', 'None', ''),
        ('1', 'Standard', ''),
        ('2', 'XSPH', ''),
        ('3', 'Bender and Koschier 2017', ''),
        ('4', 'Peer et al. 2015', ''),
        ('5', 'Peer et al. 2016', ''),
        ('6', 'Takahashi et al. 2015 (improved)', ''),
        ('7', 'Weiler et al. 2018', '')
    ]
    viscosity_method = bpy.props.EnumProperty(
        items=viscosity_method_items,
        name='Viscosity Method',
        default='7'
    )
    viscosity = bpy.props.FloatProperty(default=0.0, name='Viscosity')
    visco_max_iter = bpy.props.IntProperty(default=1, name='Visco Max Iter')
    visco_max_error = bpy.props.FloatProperty(default=0.1, name='Visco Max Error')
    visco_max_iter_omega = bpy.props.IntProperty(default=1, name='Visco Max Iter Omega')
    visco_max_error_omega = bpy.props.FloatProperty(default=0.1, name='Visco Max Error Omega')
    viscosity_boundary = bpy.props.FloatProperty(default=0.0, name='Viscosity Boundary')

    # Vorticity
    vorticity_method_items = [
        ('0', 'None', ''),
        ('1', 'Micropolar Model', ''),
        ('2', 'Vorticity Confinement', '')
    ]
    vorticity_method = bpy.props.EnumProperty(
        items=vorticity_method_items,
        name='Vorticity Method',
        default='0'
    )
    vorticity = bpy.props.FloatProperty(default=0.0, name='Vorticity')
    viscosity_omega = bpy.props.FloatProperty(default=0.0, name='Vorticity Omega')
    inertia_inverse = bpy.props.FloatProperty(default=0.0, name='Inertia Inverse')

    # Drag Force
    drag_method_items = [
        ('0', 'None', ''),
        ('1', 'Macklin et al. 2014', ''),
        ('2', 'Gissler et al. 2017', '')
    ]
    drag_method = bpy.props.EnumProperty(
        items=drag_method_items,
        name='Drag Method',
        default='0'
    )

    # Surface Tension
    surface_tension_method_items = [
        ('0', 'None', ''),
        ('1', 'Becker & Teschner 2007', ''),
        ('2', 'Akinci et al. 2013', ''),
        ('3', 'He et al. 2014', '')
    ]
    surface_tension_method = bpy.props.EnumProperty(
        items=surface_tension_method_items,
        name='Surface Tension Method',
        default='0'
    )
    surface_tension = bpy.props.FloatProperty(default=0.0, name='Surface Tension')


__CLASSES__ = [
    SPlisHSplaSHProps,
]


def register():
    for class_ in __CLASSES__:
        bpy.utils.register_class(class_)
        class_.bpy_type.splish_splash = bpy.props.PointerProperty(type=class_)


def unregister():
    for class_ in reversed(__CLASSES__):
        del class_.bpy_type.splish_splash
        bpy.utils.unregister_class(class_)
