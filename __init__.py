import bpy
import bpy.ops


bl_info = {
    "name": "Beautiful Curves",
    "author": "Vaishnav Pratap",
    "version": (1, 0),
    "blender": (4, 2, 1),  # Minimum Blender version
    "location": "View3D > Add > Mesh",
    "description": "Creates beautiful pattern of curves",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}

    


class Creating_curves(bpy.types.Operator):
    bl_idname = "node.creating_curves"
    bl_label = "Creating curves"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # initialize pattern_generator node group
        def pattern_generator_node_group():
            pattern_generator = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="Pattern Generator"
            )

            pattern_generator.color_tag = "NONE"
            pattern_generator.description = ""

            # pattern_generator interface
            # Socket Geometry
            geometry_socket = pattern_generator.interface.new_socket(
                name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
            )
            geometry_socket.attribute_domain = "POINT"

            # Socket Resolution of Curve
            resolution_of_curve_socket = pattern_generator.interface.new_socket(
                name="Resolution of Curve", in_out="INPUT", socket_type="NodeSocketInt"
            )
            resolution_of_curve_socket.default_value = 16
            resolution_of_curve_socket.min_value = 2
            resolution_of_curve_socket.max_value = 256
            resolution_of_curve_socket.attribute_domain = "POINT"

            # Socket Count
            count_socket = pattern_generator.interface.new_socket(
                name="Count", in_out="INPUT", socket_type="NodeSocketInt"
            )
            count_socket.default_value = 12
            count_socket.min_value = 1
            count_socket.max_value = 2147483647
            count_socket.subtype = "NONE"
            count_socket.attribute_domain = "POINT"

            # Socket Offset
            offset_socket = pattern_generator.interface.new_socket(
                name="Offset", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            offset_socket.default_value = 0.8299999833106995
            offset_socket.min_value = -10000.0
            offset_socket.max_value = 10000.0
            offset_socket.subtype = "NONE"
            offset_socket.attribute_domain = "POINT"

            # Socket Size
            size_socket = pattern_generator.interface.new_socket(
                name="Size", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            size_socket.default_value = 1.0
            size_socket.min_value = 0.0
            size_socket.max_value = 3.4028234663852886e38
            size_socket.subtype = "DISTANCE"
            size_socket.attribute_domain = "POINT"

            # Socket Value
            value_socket = pattern_generator.interface.new_socket(
                name="Value", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            value_socket.default_value = 0.20000004768371582
            value_socket.min_value = -10000.0
            value_socket.max_value = 10000.0
            value_socket.subtype = "NONE"
            value_socket.attribute_domain = "POINT"

            # Socket Seed
            seed_socket = pattern_generator.interface.new_socket(
                name="Seed", in_out="INPUT", socket_type="NodeSocketInt"
            )
            seed_socket.default_value = 2
            seed_socket.min_value = -10000
            seed_socket.max_value = 10000
            seed_socket.subtype = "NONE"
            seed_socket.attribute_domain = "POINT"

            # Socket Radius of Tubes
            radius_of_tubes_socket = pattern_generator.interface.new_socket(
                name="Radius of Tubes", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            radius_of_tubes_socket.default_value = 0.009999999776482582
            radius_of_tubes_socket.min_value = 0.0
            radius_of_tubes_socket.max_value = 3.4028234663852886e38
            radius_of_tubes_socket.subtype = "DISTANCE"
            radius_of_tubes_socket.attribute_domain = "POINT"

            # Socket Resolution of Tubes
            resolution_of_tubes_socket = pattern_generator.interface.new_socket(
                name="Resolution of Tubes", in_out="INPUT", socket_type="NodeSocketInt"
            )
            resolution_of_tubes_socket.default_value = 32
            resolution_of_tubes_socket.min_value = 3
            resolution_of_tubes_socket.max_value = 512
            resolution_of_tubes_socket.subtype = "NONE"
            resolution_of_tubes_socket.attribute_domain = "POINT"

            # Socket 1st Curve Segments
            _1st_curve_segments_socket = pattern_generator.interface.new_socket(
                name="1st Curve Segments", in_out="INPUT", socket_type="NodeSocketInt"
            )
            _1st_curve_segments_socket.default_value = 10
            _1st_curve_segments_socket.min_value = 1
            _1st_curve_segments_socket.max_value = 100000
            _1st_curve_segments_socket.subtype = "NONE"
            _1st_curve_segments_socket.attribute_domain = "POINT"

            # Socket 2nd Curve Segements
            _2nd_curve_segements_socket = pattern_generator.interface.new_socket(
                name="2nd Curve Segements", in_out="INPUT", socket_type="NodeSocketInt"
            )
            _2nd_curve_segements_socket.default_value = 10
            _2nd_curve_segements_socket.min_value = 1
            _2nd_curve_segements_socket.max_value = 100000
            _2nd_curve_segements_socket.subtype = "NONE"
            _2nd_curve_segements_socket.attribute_domain = "POINT"

            # initialize pattern_generator nodes
            # node Group Output
            group_output = pattern_generator.nodes.new("NodeGroupOutput")
            group_output.name = "Group Output"
            group_output.is_active_output = True

            # node Group Input
            group_input = pattern_generator.nodes.new("NodeGroupInput")
            group_input.name = "Group Input"

            # node Set Material
            set_material = pattern_generator.nodes.new("GeometryNodeSetMaterial")
            set_material.name = "Set Material"
            # Selection
            set_material.inputs[1].default_value = True
            if "Material" in bpy.data.materials:
                set_material.inputs[2].default_value = bpy.data.materials["Material"]

            # node Random Value
            random_value = pattern_generator.nodes.new("FunctionNodeRandomValue")
            random_value.name = "Random Value"
            random_value.data_type = "FLOAT"
            # Min_001
            random_value.inputs[2].default_value = 0.0
            # Max_001
            random_value.inputs[3].default_value = 1.0
            # ID
            random_value.inputs[7].default_value = 0
            # Seed
            random_value.inputs[8].default_value = 0

            # node Arc
            arc = pattern_generator.nodes.new("GeometryNodeCurveArc")
            arc.name = "Arc"
            arc.mode = "RADIUS"
            # Radius
            arc.inputs[4].default_value = 1.0
            # Start Angle
            arc.inputs[5].default_value = 0.0
            # Sweep Angle
            arc.inputs[6].default_value = 1.5707963705062866
            # Connect Center
            arc.inputs[8].default_value = False
            # Invert Arc
            arc.inputs[9].default_value = False

            # node Instance on Points
            instance_on_points = pattern_generator.nodes.new(
                "GeometryNodeInstanceOnPoints"
            )
            instance_on_points.name = "Instance on Points"
            # Selection
            instance_on_points.inputs[1].default_value = True
            # Pick Instance
            instance_on_points.inputs[3].default_value = False
            # Instance Index
            instance_on_points.inputs[4].default_value = 0
            # Rotation
            instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)

            # node Points
            points = pattern_generator.nodes.new("GeometryNodePoints")
            points.name = "Points"
            # Position
            points.inputs[1].default_value = (0.0, 0.0, 0.0)
            # Radius
            points.inputs[2].default_value = 0.09999999403953552

            # node Index
            index = pattern_generator.nodes.new("GeometryNodeInputIndex")
            index.name = "Index"

            # node Map Range
            map_range = pattern_generator.nodes.new("ShaderNodeMapRange")
            map_range.name = "Map Range"
            map_range.clamp = True
            map_range.data_type = "FLOAT"
            map_range.interpolation_type = "LINEAR"
            # From Min
            map_range.inputs[1].default_value = 1.0

            # node Realize Instances.002
            realize_instances_002 = pattern_generator.nodes.new(
                "GeometryNodeRealizeInstances"
            )
            realize_instances_002.name = "Realize Instances.002"
            # Selection
            realize_instances_002.inputs[1].default_value = True
            # Realize All
            realize_instances_002.inputs[2].default_value = True
            # Depth
            realize_instances_002.inputs[3].default_value = 0

            # node Math
            math = pattern_generator.nodes.new("ShaderNodeMath")
            math.name = "Math"
            math.operation = "SUBTRACT"
            math.use_clamp = False
            # Value_001
            math.inputs[1].default_value = 1.0

            # node Transform Geometry
            transform_geometry = pattern_generator.nodes.new("GeometryNodeTransform")
            transform_geometry.name = "Transform Geometry"
            transform_geometry.mode = "COMPONENTS"
            # Translation
            transform_geometry.inputs[1].default_value = (1.0, 1.0, 0.0)
            # Rotation
            transform_geometry.inputs[2].default_value = (0.0, 0.0, 3.1415927410125732)
            # Scale
            transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

            # node Join Geometry
            join_geometry = pattern_generator.nodes.new("GeometryNodeJoinGeometry")
            join_geometry.name = "Join Geometry"

            # node Grid
            grid = pattern_generator.nodes.new("GeometryNodeMeshGrid")
            grid.name = "Grid"

            # node Instance on Points.001
            instance_on_points_001 = pattern_generator.nodes.new(
                "GeometryNodeInstanceOnPoints"
            )
            instance_on_points_001.name = "Instance on Points.001"
            # Selection
            instance_on_points_001.inputs[1].default_value = True
            # Pick Instance
            instance_on_points_001.inputs[3].default_value = False
            # Instance Index
            instance_on_points_001.inputs[4].default_value = 0
            # Rotation
            instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)
            # Scale
            instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)

            # node Merge by Distance
            merge_by_distance = pattern_generator.nodes.new(
                "GeometryNodeMergeByDistance"
            )
            merge_by_distance.name = "Merge by Distance"
            merge_by_distance.mode = "ALL"
            # Selection
            merge_by_distance.inputs[1].default_value = True
            # Distance
            merge_by_distance.inputs[2].default_value = 0.0010000000474974513

            # node Math.001
            math_001 = pattern_generator.nodes.new("ShaderNodeMath")
            math_001.name = "Math.001"
            math_001.operation = "ADD"
            math_001.use_clamp = False
            # Value_001
            math_001.inputs[1].default_value = 1.0

            # node Transform Geometry.001
            transform_geometry_001 = pattern_generator.nodes.new(
                "GeometryNodeTransform"
            )
            transform_geometry_001.name = "Transform Geometry.001"
            transform_geometry_001.mode = "COMPONENTS"
            # Translation
            transform_geometry_001.inputs[1].default_value = (-0.5, -0.5, 0.0)
            # Rotation
            transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
            # Scale
            transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)

            # node Math.002
            math_002 = pattern_generator.nodes.new("ShaderNodeMath")
            math_002.name = "Math.002"
            math_002.operation = "SUBTRACT"
            math_002.use_clamp = False
            # Value
            math_002.inputs[0].default_value = 1.0

            # node Realize Instances
            realize_instances = pattern_generator.nodes.new(
                "GeometryNodeRealizeInstances"
            )
            realize_instances.name = "Realize Instances"
            # Selection
            realize_instances.inputs[1].default_value = True
            # Realize All
            realize_instances.inputs[2].default_value = True
            # Depth
            realize_instances.inputs[3].default_value = 0

            # node Curve to Mesh
            curve_to_mesh = pattern_generator.nodes.new("GeometryNodeCurveToMesh")
            curve_to_mesh.name = "Curve to Mesh"
            # Fill Caps
            curve_to_mesh.inputs[2].default_value = False

            # node Delete Geometry
            delete_geometry = pattern_generator.nodes.new("GeometryNodeDeleteGeometry")
            delete_geometry.name = "Delete Geometry"
            delete_geometry.domain = "POINT"
            delete_geometry.mode = "ALL"

            # node Position
            position = pattern_generator.nodes.new("GeometryNodeInputPosition")
            position.name = "Position"

            # node Vector Math
            vector_math = pattern_generator.nodes.new("ShaderNodeVectorMath")
            vector_math.name = "Vector Math"
            vector_math.operation = "LENGTH"

            # node Compare
            compare = pattern_generator.nodes.new("FunctionNodeCompare")
            compare.name = "Compare"
            compare.data_type = "FLOAT"
            compare.mode = "ELEMENT"
            compare.operation = "LESS_THAN"

            # node Store Named Attribute
            store_named_attribute = pattern_generator.nodes.new(
                "GeometryNodeStoreNamedAttribute"
            )
            store_named_attribute.name = "Store Named Attribute"
            store_named_attribute.data_type = "FLOAT"
            store_named_attribute.domain = "CURVE"
            # Selection
            store_named_attribute.inputs[1].default_value = True
            # Name
            store_named_attribute.inputs[2].default_value = "S"

            # node Math.003
            math_003 = pattern_generator.nodes.new("ShaderNodeMath")
            math_003.name = "Math.003"
            math_003.operation = "ADD"
            math_003.use_clamp = True

            # node Rotate Instances
            rotate_instances = pattern_generator.nodes.new(
                "GeometryNodeRotateInstances"
            )
            rotate_instances.name = "Rotate Instances"
            # Selection
            rotate_instances.inputs[1].default_value = True
            # Pivot Point
            rotate_instances.inputs[3].default_value = (0.5, 0.5, 0.0)
            # Local Space
            rotate_instances.inputs[4].default_value = True

            # node Math.004
            math_004 = pattern_generator.nodes.new("ShaderNodeMath")
            math_004.name = "Math.004"
            math_004.operation = "MULTIPLY"
            math_004.use_clamp = False
            # Value
            math_004.inputs[0].default_value = 1.5707963705062866

            # node Random Value.001
            random_value_001 = pattern_generator.nodes.new("FunctionNodeRandomValue")
            random_value_001.name = "Random Value.001"
            random_value_001.data_type = "INT"
            # Min_002
            random_value_001.inputs[4].default_value = 0
            # Max_002
            random_value_001.inputs[5].default_value = 3
            # ID
            random_value_001.inputs[7].default_value = 0

            # node Combine XYZ
            combine_xyz = pattern_generator.nodes.new("ShaderNodeCombineXYZ")
            combine_xyz.name = "Combine XYZ"
            # X
            combine_xyz.inputs[0].default_value = 0.0
            # Y
            combine_xyz.inputs[1].default_value = 0.0

            # node Curve Circle
            curve_circle = pattern_generator.nodes.new(
                "GeometryNodeCurvePrimitiveCircle"
            )
            curve_circle.name = "Curve Circle"
            curve_circle.mode = "RADIUS"

            # node Curve to Mesh.001
            curve_to_mesh_001 = pattern_generator.nodes.new("GeometryNodeCurveToMesh")
            curve_to_mesh_001.name = "Curve to Mesh.001"
            # Fill Caps
            curve_to_mesh_001.inputs[2].default_value = True

            # node Mesh to Curve
            mesh_to_curve = pattern_generator.nodes.new("GeometryNodeMeshToCurve")
            mesh_to_curve.name = "Mesh to Curve"
            # Selection
            mesh_to_curve.inputs[1].default_value = True

            # node Realize Instances.001
            realize_instances_001 = pattern_generator.nodes.new(
                "GeometryNodeRealizeInstances"
            )
            realize_instances_001.name = "Realize Instances.001"
            # Selection
            realize_instances_001.inputs[1].default_value = True
            # Realize All
            realize_instances_001.inputs[2].default_value = True
            # Depth
            realize_instances_001.inputs[3].default_value = 0

            # node Curve to Mesh.002
            curve_to_mesh_002 = pattern_generator.nodes.new("GeometryNodeCurveToMesh")
            curve_to_mesh_002.name = "Curve to Mesh.002"
            # Fill Caps
            curve_to_mesh_002.inputs[2].default_value = False

            # node Reroute
            reroute = pattern_generator.nodes.new("NodeReroute")
            reroute.name = "Reroute"
            # node Resample Curve
            resample_curve = pattern_generator.nodes.new("GeometryNodeResampleCurve")
            resample_curve.name = "Resample Curve"
            resample_curve.mode = "COUNT"
            # Selection
            resample_curve.inputs[1].default_value = True

            # node Resample Curve.001
            resample_curve_001 = pattern_generator.nodes.new(
                "GeometryNodeResampleCurve"
            )
            resample_curve_001.name = "Resample Curve.001"
            resample_curve_001.mode = "COUNT"
            # Selection
            resample_curve_001.inputs[1].default_value = True

            # Set locations
            group_output.location = (2279.214599609375, 0.0)
            group_input.location = (-2418.97607421875, 66.50491333007812)
            set_material.location = (2089.21484375, 208.1917724609375)
            random_value.location = (1085.0869140625, 112.96533203125)
            arc.location = (-1822.10205078125, 67.17887115478516)
            instance_on_points.location = (-1322.73046875, -10.292510986328125)
            points.location = (-1751.5244140625, 260.54656982421875)
            index.location = (-1852.261474609375, -184.05601501464844)
            map_range.location = (-1503.5899658203125, -160.14053344726562)
            realize_instances_002.location = (868.7413940429688, 285.6907958984375)
            math.location = (-1855.214599609375, -246.33856201171875)
            transform_geometry.location = (-956.4008178710938, -28.593271255493164)
            join_geometry.location = (-190.11280822753906, 90.04498291015625)
            grid.location = (-937.3075561523438, 359.9974060058594)
            instance_on_points_001.location = (169.90354919433594, 420.9173278808594)
            merge_by_distance.location = (1052.1552734375, 279.991943359375)
            math_001.location = (-1115.746337890625, 210.4761199951172)
            transform_geometry_001.location = (-743.1465454101562, 480.6075744628906)
            math_002.location = (-1746.2464599609375, -480.6075744628906)
            realize_instances.location = (-861.87451171875, -11.46346664428711)
            curve_to_mesh.location = (-640.3411254882812, -22.60354232788086)
            delete_geometry.location = (-369.6902160644531, 7.416851043701172)
            position.location = (-774.5347290039062, -266.6282958984375)
            vector_math.location = (-540.7319946289062, -198.18414306640625)
            compare.location = (-224.8619384765625, -201.2460479736328)
            store_named_attribute.location = (1595.6934814453125, 291.4112243652344)
            math_003.location = (-520.1243896484375, -324.5626525878906)
            rotate_instances.location = (688.3109741210938, 295.4272155761719)
            math_004.location = (32.0250244140625, 5.29632568359375)
            random_value_001.location = (285.4725341796875, -57.04020309448242)
            combine_xyz.location = (187.1593017578125, 116.90728759765625)
            curve_circle.location = (888.6839599609375, -229.6827392578125)
            curve_to_mesh_001.location = (1802.6951904296875, 217.06964111328125)
            mesh_to_curve.location = (1411.8367919921875, 249.61154174804688)
            realize_instances_001.location = (-894.5066528320312, 124.9803695678711)
            curve_to_mesh_002.location = (-781.9696655273438, 109.60911560058594)
            reroute.location = (-589.523681640625, -452.2474060058594)
            resample_curve.location = (-1135.9998779296875, -44.57635498046875)
            resample_curve_001.location = (-1114.779052734375, 119.53145599365234)

            # Set dimensions
            group_output.width, group_output.height = 140.0, 100.0
            group_input.width, group_input.height = 140.0, 100.0
            set_material.width, set_material.height = 140.0, 100.0
            random_value.width, random_value.height = 140.0, 100.0
            arc.width, arc.height = 140.0, 100.0
            instance_on_points.width, instance_on_points.height = 140.0, 100.0
            points.width, points.height = 140.0, 100.0
            index.width, index.height = 140.0, 100.0
            map_range.width, map_range.height = 140.0, 100.0
            realize_instances_002.width, realize_instances_002.height = 140.0, 100.0
            math.width, math.height = 140.0, 100.0
            transform_geometry.width, transform_geometry.height = 140.0, 100.0
            join_geometry.width, join_geometry.height = 140.0, 100.0
            grid.width, grid.height = 140.0, 100.0
            instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
            merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
            math_001.width, math_001.height = 140.0, 100.0
            transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
            math_002.width, math_002.height = 140.0, 100.0
            realize_instances.width, realize_instances.height = 140.0, 100.0
            curve_to_mesh.width, curve_to_mesh.height = 140.0, 100.0
            delete_geometry.width, delete_geometry.height = 140.0, 100.0
            position.width, position.height = 140.0, 100.0
            vector_math.width, vector_math.height = 140.0, 100.0
            compare.width, compare.height = 140.0, 100.0
            store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
            math_003.width, math_003.height = 140.0, 100.0
            rotate_instances.width, rotate_instances.height = 140.0, 100.0
            math_004.width, math_004.height = 140.0, 100.0
            random_value_001.width, random_value_001.height = 140.0, 100.0
            combine_xyz.width, combine_xyz.height = 140.0, 100.0
            curve_circle.width, curve_circle.height = 140.0, 100.0
            curve_to_mesh_001.width, curve_to_mesh_001.height = 140.0, 100.0
            mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
            realize_instances_001.width, realize_instances_001.height = 140.0, 100.0
            curve_to_mesh_002.width, curve_to_mesh_002.height = 140.0, 100.0
            reroute.width, reroute.height = 16.0, 100.0
            resample_curve.width, resample_curve.height = 140.0, 100.0
            resample_curve_001.width, resample_curve_001.height = 140.0, 100.0

            # initialize pattern_generator links
            # curve_to_mesh_001.Mesh -> set_material.Geometry
            pattern_generator.links.new(
                curve_to_mesh_001.outputs[0], set_material.inputs[0]
            )
            # vector_math.Value -> compare.A
            pattern_generator.links.new(vector_math.outputs[1], compare.inputs[0])
            # delete_geometry.Geometry -> join_geometry.Geometry
            pattern_generator.links.new(
                delete_geometry.outputs[0], join_geometry.inputs[0]
            )
            # mesh_to_curve.Curve -> store_named_attribute.Geometry
            pattern_generator.links.new(
                mesh_to_curve.outputs[0], store_named_attribute.inputs[0]
            )
            # combine_xyz.Vector -> rotate_instances.Rotation
            pattern_generator.links.new(
                combine_xyz.outputs[0], rotate_instances.inputs[2]
            )
            # realize_instances_001.Geometry -> curve_to_mesh_002.Curve
            pattern_generator.links.new(
                realize_instances_001.outputs[0], curve_to_mesh_002.inputs[0]
            )
            # map_range.Result -> instance_on_points.Scale
            pattern_generator.links.new(
                map_range.outputs[0], instance_on_points.inputs[6]
            )
            # curve_circle.Curve -> curve_to_mesh_001.Profile Curve
            pattern_generator.links.new(
                curve_circle.outputs[0], curve_to_mesh_001.inputs[1]
            )
            # random_value_001.Value -> math_004.Value
            pattern_generator.links.new(random_value_001.outputs[2], math_004.inputs[1])
            # instance_on_points_001.Instances -> rotate_instances.Instances
            pattern_generator.links.new(
                instance_on_points_001.outputs[0], rotate_instances.inputs[0]
            )
            # transform_geometry_001.Geometry -> instance_on_points_001.Points
            pattern_generator.links.new(
                transform_geometry_001.outputs[0], instance_on_points_001.inputs[0]
            )
            # position.Position -> vector_math.Vector
            pattern_generator.links.new(position.outputs[0], vector_math.inputs[0])
            # math.Value -> map_range.From Max
            pattern_generator.links.new(math.outputs[0], map_range.inputs[2])
            # rotate_instances.Instances -> realize_instances_002.Geometry
            pattern_generator.links.new(
                rotate_instances.outputs[0], realize_instances_002.inputs[0]
            )
            # math_004.Value -> combine_xyz.Z
            pattern_generator.links.new(math_004.outputs[0], combine_xyz.inputs[2])
            # realize_instances_002.Geometry -> merge_by_distance.Geometry
            pattern_generator.links.new(
                realize_instances_002.outputs[0], merge_by_distance.inputs[0]
            )
            # math_003.Value -> compare.B
            pattern_generator.links.new(math_003.outputs[0], compare.inputs[1])
            # realize_instances.Geometry -> curve_to_mesh.Curve
            pattern_generator.links.new(
                realize_instances.outputs[0], curve_to_mesh.inputs[0]
            )
            # transform_geometry.Geometry -> realize_instances.Geometry
            pattern_generator.links.new(
                transform_geometry.outputs[0], realize_instances.inputs[0]
            )
            # arc.Curve -> instance_on_points.Instance
            pattern_generator.links.new(arc.outputs[0], instance_on_points.inputs[2])
            # store_named_attribute.Geometry -> curve_to_mesh_001.Curve
            pattern_generator.links.new(
                store_named_attribute.outputs[0], curve_to_mesh_001.inputs[0]
            )
            # curve_to_mesh.Mesh -> delete_geometry.Geometry
            pattern_generator.links.new(
                curve_to_mesh.outputs[0], delete_geometry.inputs[0]
            )
            # math_001.Value -> grid.Vertices Y
            pattern_generator.links.new(math_001.outputs[0], grid.inputs[3])
            # math_001.Value -> grid.Vertices X
            pattern_generator.links.new(math_001.outputs[0], grid.inputs[2])
            # math_002.Value -> map_range.To Min
            pattern_generator.links.new(math_002.outputs[0], map_range.inputs[3])
            # index.Index -> map_range.Value
            pattern_generator.links.new(index.outputs[0], map_range.inputs[0])
            # random_value.Value -> store_named_attribute.Value
            pattern_generator.links.new(
                random_value.outputs[1], store_named_attribute.inputs[3]
            )
            # resample_curve.Curve -> transform_geometry.Geometry
            pattern_generator.links.new(
                resample_curve.outputs[0], transform_geometry.inputs[0]
            )
            # resample_curve_001.Curve -> realize_instances_001.Geometry
            pattern_generator.links.new(
                resample_curve_001.outputs[0], realize_instances_001.inputs[0]
            )
            # join_geometry.Geometry -> instance_on_points_001.Instance
            pattern_generator.links.new(
                join_geometry.outputs[0], instance_on_points_001.inputs[2]
            )
            # points.Points -> instance_on_points.Points
            pattern_generator.links.new(points.outputs[0], instance_on_points.inputs[0])
            # grid.Mesh -> transform_geometry_001.Geometry
            pattern_generator.links.new(
                grid.outputs[0], transform_geometry_001.inputs[0]
            )
            # compare.Result -> delete_geometry.Selection
            pattern_generator.links.new(compare.outputs[0], delete_geometry.inputs[1])
            # group_input.Count -> points.Count
            pattern_generator.links.new(group_input.outputs[1], points.inputs[0])
            # group_input.Resolution of Curve -> arc.Resolution
            pattern_generator.links.new(group_input.outputs[0], arc.inputs[0])
            # group_input.Size -> grid.Size X
            pattern_generator.links.new(group_input.outputs[3], grid.inputs[0])
            # group_input.Size -> grid.Size Y
            pattern_generator.links.new(group_input.outputs[3], grid.inputs[1])
            # group_input.Size -> math_001.Value
            pattern_generator.links.new(group_input.outputs[3], math_001.inputs[0])
            # group_input.Seed -> random_value_001.Seed
            pattern_generator.links.new(
                group_input.outputs[5], random_value_001.inputs[8]
            )
            # group_input.Offset -> map_range.To Max
            pattern_generator.links.new(group_input.outputs[2], map_range.inputs[4])
            # group_input.Offset -> math_002.Value
            pattern_generator.links.new(group_input.outputs[2], math_002.inputs[1])
            # set_material.Geometry -> group_output.Geometry
            pattern_generator.links.new(set_material.outputs[0], group_output.inputs[0])
            # group_input.Count -> math.Value
            pattern_generator.links.new(group_input.outputs[1], math.inputs[0])
            # group_input.Value -> reroute.Input
            pattern_generator.links.new(group_input.outputs[4], reroute.inputs[0])
            # reroute.Output -> math_003.Value
            pattern_generator.links.new(reroute.outputs[0], math_003.inputs[1])
            # group_input.Offset -> math_003.Value
            pattern_generator.links.new(group_input.outputs[2], math_003.inputs[0])
            # group_input.Radius of Tubes -> curve_circle.Radius
            pattern_generator.links.new(group_input.outputs[6], curve_circle.inputs[4])
            # group_input.Resolution of Tubes -> curve_circle.Resolution
            pattern_generator.links.new(group_input.outputs[7], curve_circle.inputs[0])
            # merge_by_distance.Geometry -> mesh_to_curve.Mesh
            pattern_generator.links.new(
                merge_by_distance.outputs[0], mesh_to_curve.inputs[0]
            )
            # instance_on_points.Instances -> resample_curve.Curve
            pattern_generator.links.new(
                instance_on_points.outputs[0], resample_curve.inputs[0]
            )
            # instance_on_points.Instances -> resample_curve_001.Curve
            pattern_generator.links.new(
                instance_on_points.outputs[0], resample_curve_001.inputs[0]
            )
            # group_input.1st Curve Segments -> resample_curve_001.Count
            pattern_generator.links.new(
                group_input.outputs[8], resample_curve_001.inputs[2]
            )
            # group_input.2nd Curve Segements -> resample_curve.Count
            pattern_generator.links.new(
                group_input.outputs[9], resample_curve.inputs[2]
            )
            # curve_to_mesh_002.Mesh -> join_geometry.Geometry
            pattern_generator.links.new(
                curve_to_mesh_002.outputs[0], join_geometry.inputs[0]
            )
            return pattern_generator

        pattern_generator = pattern_generator_node_group()

        # initialize creating_curves node group
        def creating_curves_node_group():
            creating_curves = bpy.data.node_groups.new(
                type="GeometryNodeTree", name="Creating curves"
            )

            creating_curves.color_tag = "NONE"
            creating_curves.description = ""

            creating_curves.is_modifier = True

            # creating_curves interface
            # Socket Geometry
            geometry_socket_1 = creating_curves.interface.new_socket(
                name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
            )
            geometry_socket_1.attribute_domain = "POINT"

            # Socket Count
            count_socket_1 = creating_curves.interface.new_socket(
                name="Count", in_out="INPUT", socket_type="NodeSocketInt"
            )
            count_socket_1.default_value = 12
            count_socket_1.min_value = 1
            count_socket_1.max_value = 2147483647
            count_socket_1.subtype = "NONE"
            count_socket_1.attribute_domain = "POINT"
            count_socket_1.description = "Number of curves "

            # Socket Size
            size_socket_1 = creating_curves.interface.new_socket(
                name="Size", in_out="INPUT", socket_type="NodeSocketInt"
            )
            size_socket_1.default_value = 4
            size_socket_1.min_value = 1
            size_socket_1.max_value = 2147483647
            size_socket_1.subtype = "NONE"
            size_socket_1.attribute_domain = "POINT"

            # Socket Offset
            offset_socket_1 = creating_curves.interface.new_socket(
                name="Offset", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            offset_socket_1.default_value = 0.800000011920929
            offset_socket_1.min_value = 0.0
            offset_socket_1.max_value = 1.0
            offset_socket_1.subtype = "NONE"
            offset_socket_1.attribute_domain = "POINT"

            # Socket Seed
            seed_socket_1 = creating_curves.interface.new_socket(
                name="Seed", in_out="INPUT", socket_type="NodeSocketInt"
            )
            seed_socket_1.default_value = 2
            seed_socket_1.min_value = -10000
            seed_socket_1.max_value = 10000
            seed_socket_1.subtype = "NONE"
            seed_socket_1.attribute_domain = "POINT"

            # Socket Grain
            grain_socket = creating_curves.interface.new_socket(
                name="Grain", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            grain_socket.default_value = 0.0
            grain_socket.min_value = 0.0
            grain_socket.max_value = 0.5
            grain_socket.subtype = "NONE"
            grain_socket.attribute_domain = "POINT"

            # Socket Resolution of curves
            resolution_of_curves_socket = creating_curves.interface.new_socket(
                name="Resolution of curves", in_out="INPUT", socket_type="NodeSocketInt"
            )
            resolution_of_curves_socket.default_value = 16
            resolution_of_curves_socket.min_value = 2
            resolution_of_curves_socket.max_value = 256
            resolution_of_curves_socket.attribute_domain = "POINT"

            # Socket Radius of Tubes
            radius_of_tubes_socket_1 = creating_curves.interface.new_socket(
                name="Radius of Tubes", in_out="INPUT", socket_type="NodeSocketFloat"
            )
            radius_of_tubes_socket_1.default_value = 0.009999999776482582
            radius_of_tubes_socket_1.min_value = 9.999999747378752e-05
            radius_of_tubes_socket_1.max_value = 3.4028234663852886e38
            radius_of_tubes_socket_1.subtype = "DISTANCE"
            radius_of_tubes_socket_1.attribute_domain = "POINT"

            # Socket Resolution of Tubes
            resolution_of_tubes_socket_1 = creating_curves.interface.new_socket(
                name="Resolution of Tubes", in_out="INPUT", socket_type="NodeSocketInt"
            )
            resolution_of_tubes_socket_1.default_value = 32
            resolution_of_tubes_socket_1.min_value = 3
            resolution_of_tubes_socket_1.max_value = 512
            resolution_of_tubes_socket_1.subtype = "NONE"
            resolution_of_tubes_socket_1.attribute_domain = "POINT"

            # Socket 1st Curve Segments
            _1st_curve_segments_socket_1 = creating_curves.interface.new_socket(
                name="1st Curve Segments", in_out="INPUT", socket_type="NodeSocketInt"
            )
            _1st_curve_segments_socket_1.default_value = 16
            _1st_curve_segments_socket_1.min_value = 1
            _1st_curve_segments_socket_1.max_value = 100000
            _1st_curve_segments_socket_1.subtype = "NONE"
            _1st_curve_segments_socket_1.attribute_domain = "POINT"

            # Socket 2nd Curve Segements
            _2nd_curve_segements_socket_1 = creating_curves.interface.new_socket(
                name="2nd Curve Segements", in_out="INPUT", socket_type="NodeSocketInt"
            )
            _2nd_curve_segements_socket_1.default_value = 16
            _2nd_curve_segements_socket_1.min_value = 1
            _2nd_curve_segements_socket_1.max_value = 100000
            _2nd_curve_segements_socket_1.subtype = "NONE"
            _2nd_curve_segements_socket_1.attribute_domain = "POINT"

            # initialize creating_curves nodes
            # node Group Output
            group_output_1 = creating_curves.nodes.new("NodeGroupOutput")
            group_output_1.name = "Group Output"
            group_output_1.is_active_output = True

            # node Group Input.003
            group_input_003 = creating_curves.nodes.new("NodeGroupInput")
            group_input_003.name = "Group Input.003"

            # node Group
            group = creating_curves.nodes.new("GeometryNodeGroup")
            group.name = "Group"
            group.node_tree = pattern_generator

            # Set locations
            group_output_1.location = (2213.55810546875, 216.89891052246094)
            group_input_003.location = (1374.5816650390625, 252.07553100585938)
            group.location = (1846.0189208984375, 278.208251953125)

            # Set dimensions
            group_output_1.width, group_output_1.height = 140.0, 100.0
            group_input_003.width, group_input_003.height = 140.0, 100.0
            group.width, group.height = 140.0, 100.0

            # initialize creating_curves links
            # group.Geometry -> group_output_1.Geometry
            creating_curves.links.new(group.outputs[0], group_output_1.inputs[0])
            # group_input_003.Grain -> group.Value
            creating_curves.links.new(group_input_003.outputs[4], group.inputs[4])
            # group_input_003.Count -> group.Count
            creating_curves.links.new(group_input_003.outputs[0], group.inputs[1])
            # group_input_003.Size -> group.Size
            creating_curves.links.new(group_input_003.outputs[1], group.inputs[3])
            # group_input_003.Seed -> group.Seed
            creating_curves.links.new(group_input_003.outputs[3], group.inputs[5])
            # group_input_003.Offset -> group.Offset
            creating_curves.links.new(group_input_003.outputs[2], group.inputs[2])
            # group_input_003.Resolution of curves -> group.Resolution of Curve
            creating_curves.links.new(group_input_003.outputs[5], group.inputs[0])
            # group_input_003.Radius of Tubes -> group.Radius of Tubes
            creating_curves.links.new(group_input_003.outputs[6], group.inputs[6])
            # group_input_003.Resolution of Tubes -> group.Resolution of Tubes
            creating_curves.links.new(group_input_003.outputs[7], group.inputs[7])
            # group_input_003.1st Curve Segments -> group.1st Curve Segments
            creating_curves.links.new(group_input_003.outputs[8], group.inputs[8])
            # group_input_003.2nd Curve Segements -> group.2nd Curve Segements
            creating_curves.links.new(group_input_003.outputs[9], group.inputs[9])
            return creating_curves

        bpy.ops.mesh.primitive_plane_add()
        creating_curves = creating_curves_node_group()

        name = bpy.context.object.name
        obj = bpy.data.objects[name]
        mod = obj.modifiers.new(name="Creating curves", type="NODES")
        mod.node_group = creating_curves
        return {"FINISHED"}


def menu_func(self, context):
    self.layout.operator(Creating_curves.bl_idname)


def register():
    bpy.utils.register_class(Creating_curves)
    bpy.types.NODE_MT_add.append(menu_func)


def unregister():
    bpy.utils.unregister_class(Creating_curves)
    bpy.types.NODE_MT_add.remove(menu_func)


if __name__ == "__main__":
    register()
