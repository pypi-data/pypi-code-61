# Honeybee: A Plugin for Environmental Analysis (GPL)
# This file is part of Honeybee.
#
# Copyright (c) 2019, Ladybug Tools.
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Visualize room geometry in the Rhino scene organized by object and face type.
-

    Args:
        _rooms: Honeybee Rooms for which you would like to preview geometry
            in the Rhino scene based on type. This can also be an entire
            honeybee Model.
    
    Returns:
        walls: Rhino geometry for the Walls with an Outdoors or Ground boundary
            condition.
        interior_walls: Rhino geometry for the Walls with a Surface or Adiabatic
            boundary condition.
        roofs: Rhino geometry for the RoofCeilings with an Outdoors or Ground
            boundary condition.
        ceilings: Rhino geometry for the RoofCeilings with a Surface or Adiabatic
            boundary condition.
        exterior_floors: Rhino geometry for the Floors with an Outdoors or Ground
            boundary condition.
        interior_floors: Rhino geometry for the Floors with a Surface or Adiabatic
            boundary condition.
        air_walls: Rhino geometry for the AirWalls.
        apertures: Rhino geometry for the Apertures with an Outdoors or Ground
            boundary condition.
        interior_apertures: Rhino geometry for the Apertures with an Surface or
            Adiabatic boundary condition.
        doors: Rhino geometry for the Doors with an Outdoors or Ground boundary
            condition.
        interior_doors: Rhino geometry for the Doors with an Surface or Adiabatic
            boundary condition.
        outdoor_shades: Rhino geometry for the Shades assigned to the outdoors
            of their parent objects.
        indoor_shades: Rhino geometry for the Shades assigned to the indoors
            of their parent objects.
        wire_frame: A list of lines representing the outlines of the rooms.
"""

ghenv.Component.Name = 'HB Visualize by Type'
ghenv.Component.NickName = 'VizByType'
ghenv.Component.Message = '0.3.1'
ghenv.Component.Category = 'Honeybee'
ghenv.Component.SubCategory = '1 :: Visualize'
ghenv.Component.AdditionalHelpFromDocStrings = '5'

try:  # import the ladybug dependencies
    from ladybug.color import Colorset
except ImportError as e:
    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))

try:  # import the core honeybee dependencies
    from honeybee.model import Model
    from honeybee.boundarycondition import Surface
    from honeybee.facetype import Wall, RoofCeiling, Floor, AirBoundary
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

try:  # import the ladybug_rhino dependencies
    from ladybug_rhino.fromgeometry import from_face3ds_to_colored_mesh, \
        from_face3d_to_wireframe
    from ladybug_rhino.grasshopper import all_required_inputs
except ImportError as e:
    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))

try:  # import the honeybee-energy extension
    from honeybee.boundarycondition import Adiabatic
except ImportError:  # honeybee-energy not installed
    Adiabatic = None  # don't worry about Aidabatic; Surface is the only interior bc


if all_required_inputs(ghenv.Component):
    # lists of rhino geometry to be filled with content
    _walls = []
    _interior_walls = []
    _roofs = []
    _ceilings = []
    _exterior_floors = []
    _interior_floors = []
    _air_walls = []
    _apertures = []
    _interior_apertures = []
    _doors = []
    _interior_doors = []
    _outdoor_shades = []
    _indoor_shades = []

    # method to add shades
    def add_shade(hb_obj):
        _outdoor_shades.extend([shd.geometry for shd in hb_obj.outdoor_shades])
        _indoor_shades.extend([shd.geometry for shd in hb_obj.indoor_shades])

    # extract any rooms from input Models
    rooms = []
    for hb_obj in _rooms:
        if isinstance(hb_obj, Model):
            rooms.extend(hb_obj.rooms)
            _outdoor_shades.extend([shd.geometry for shd in hb_obj.orphaned_shades])
        else:
            rooms.append(hb_obj)

    # loop through all objects and add them
    for room in rooms:
        add_shade(room)
        for face in room:
            add_shade(face)
            bc = face.boundary_condition
            type = face.type
            if isinstance(type, Wall):
                if isinstance(bc, (Surface, Adiabatic)):
                    _interior_walls.append(face.punched_geometry)
                else:
                    _walls.append(face.punched_geometry)
            elif isinstance(type, RoofCeiling):
                if isinstance(bc, (Surface, Adiabatic)):
                    _ceilings.append(face.punched_geometry)
                else:
                    _roofs.append(face.punched_geometry)
            elif isinstance(type, Floor):
                if isinstance(bc, (Surface, Adiabatic)):
                    _interior_floors.append(face.punched_geometry)
                else:
                    _exterior_floors.append(face.punched_geometry)
            elif isinstance(type, AirBoundary):
                _air_walls.append(face.punched_geometry)

            # add the apertures, doors, and shades
            for ap in face.apertures:
                add_shade(ap)
                if isinstance(bc, Surface):
                    _interior_apertures.append(ap.geometry)
                else:
                    _apertures.append(ap.geometry)
            for dr in face.doors:
                add_shade(dr)
                if isinstance(bc, Surface):
                    _interior_doors.append(dr.geometry)
                else:
                    _doors.append(dr.geometry)

    # color all of the geometry with its respective surface type
    palette = Colorset.openstudio_palette()
    walls = from_face3ds_to_colored_mesh(_walls, palette[0]) \
        if len(_walls) != 0 else None
    interior_walls = from_face3ds_to_colored_mesh(_interior_walls, palette[1]) \
        if len(_interior_walls) != 0 else None
    roofs = from_face3ds_to_colored_mesh(_roofs, palette[3]) \
        if len(_roofs) != 0 else None
    ceilings = from_face3ds_to_colored_mesh(_ceilings, palette[4]) \
        if len(_ceilings) != 0 else None
    exterior_floors = from_face3ds_to_colored_mesh(_exterior_floors, palette[6]) \
        if len(_exterior_floors) != 0 else None
    interior_floors = from_face3ds_to_colored_mesh(_interior_floors, palette[7]) \
        if len(_interior_floors) != 0 else None
    air_walls = from_face3ds_to_colored_mesh(_air_walls, palette[12]) \
        if len(_air_walls) != 0 else None
    apertures = from_face3ds_to_colored_mesh(_apertures, palette[9]) \
        if len(_apertures) != 0 else None
    interior_apertures = from_face3ds_to_colored_mesh(_interior_apertures, palette[9]) \
        if len(_interior_apertures) != 0 else None
    doors = from_face3ds_to_colored_mesh(_doors, palette[10]) \
        if len(_doors) != 0 else None
    interior_doors = from_face3ds_to_colored_mesh(_interior_doors, palette[10]) \
        if len(_interior_doors) != 0 else None
    outdoor_shades = from_face3ds_to_colored_mesh(_outdoor_shades, palette[11]) \
        if len(_outdoor_shades) != 0 else None
    indoor_shades = from_face3ds_to_colored_mesh(_indoor_shades, palette[11]) \
        if len(_indoor_shades) != 0 else None

    # create the wire frame
    all_geo = _walls + _interior_walls + _roofs + _ceilings + _exterior_floors + \
        _interior_floors + _air_walls + _apertures + _interior_apertures + _doors + \
        _interior_doors + _outdoor_shades + _indoor_shades
    wire_frame = [from_face3d_to_wireframe(face) for face in all_geo]