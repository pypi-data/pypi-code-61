
from typing import List

from enum import Enum

from dataclasses import dataclass
from dataclasses import field

from pyumldiagrams.Defaults import TOP_MARGIN
from pyumldiagrams.Defaults import LEFT_MARGIN
from pyumldiagrams.Defaults import DEFAULT_HORIZONTAL_GAP
from pyumldiagrams.Defaults import DEFAULT_VERTICAL_GAP

ClassName = str


@dataclass
class Position:
    """
    The x and y coordinates are in screen/display resolution.  Diagramming modules may
    convert these to appropriate positions based on the rendering technology.
    """
    x: float = 0.0
    """
    The x-axis (horizontal) abscissa
    """
    y: float = 0.0
    """
    The y-axis (vertical) ordinate
    """


@dataclass
class DiagramPadding:
    """
    todo::  These should move to the Internal package
    """

    topMargin:  int = TOP_MARGIN
    """
    The diagram's observed top margin.  See `pyumldiagrams.Defaults.TOP_MARGIN`
    """
    leftMargin: int = LEFT_MARGIN
    """
    The diagram's observed left margin.  See `pyumldiagrams.Defaults.LEFT_MARGIN`
    """

    horizontalGap: int = DEFAULT_HORIZONTAL_GAP
    """
    The horizontal gap between UML graphics added to the layout in addition to the gap imposed 
    by the actual graphics positions. See `pyumldiagrams.Defaults.DEFAULT_HORIZONTAL_GAP`
    """
    verticalGap:   int = DEFAULT_VERTICAL_GAP
    """
    The vertical gap between UML graphics added to the layout in addition to the gap imposed 
    by the actual graphics positions.  See `pyumldiagrams.Defaults.DEFAULT_VERTICAL_GAP`
    """


@dataclass
class Size:
    """
    Defines the size of the input UML definitions;
    """
    width:  float = 100
    """
    The width of a shape
    """
    height: float = 100
    """
    The height of the shape
    """


class DefinitionType(Enum):
    """
    Defines the visibility of either methods or fields
    """
    Public    = '+'
    Private   = '-'
    Protected = '#'


@dataclass
class BaseDefinition:

    __slots__ = ['name']
    name: str
    """
    The name associated with the definition.
    """


@dataclass
class ParameterDefinition(BaseDefinition):
    """
    Defines a single parameter for a method
    """
    parameterType: str = ''
    """
    A string that describes the parameter type
    """
    defaultValue:  str = ''
    """
    A string that describes a parameter default value
    """


Parameters = List[ParameterDefinition]
"""
Syntactic sugar to define a list of parameters.  
"""


@dataclass
class MethodDefinition(BaseDefinition):
    """
    Defines a single method in a UML class
    """
    visibility: DefinitionType = DefinitionType.Public
    """
    Defines the method visibility.  See `DefinitionType`
    """
    returnType: str = ''
    """
    Defines the method return type.
    """
    parameters: Parameters = field(default_factory=list)
    """
    Define the parameters for a particular method
    """


Methods = List[MethodDefinition]
"""
Syntactic sugar to define a list of methods.
"""


@dataclass
class ClassDefinition(BaseDefinition):
    """
    The class definition.  Currently, does not support instance properties.
    """
    size:     Size     = Size()
    """
    The size of UML class symbol.  See `Size`
    """
    position: Position = Position(0, 0)
    """
    The position of the UML class symbol.  See `Position`
    """
    methods: Methods   = field(default_factory=list)
    """
    The list of methods this class implements.  
    """


ClassDefinitions = List[ClassDefinition]


class LineType(Enum):
    """
    The type of UML line you wish to draw.  Currently, bare associations are not supported.
    """
    Inheritance  = 0
    Aggregation  = 1
    Composition  = 3
    Association  = 7


@dataclass
class LineDefinition:
    """
    Defines a line between two points
    """
    source: Position
    """
    The source position.  See `Position`
    """
    destination: Position
    """
    The destination position.  See `Position`
    """


@dataclass
class UmlLineDefinition(LineDefinition):
    """
    A UML Line definition includes its' type
    """
    lineType: LineType
    """
    The UML line type  See `LineType`.
    """


UmlLineDefinitions = List[UmlLineDefinition]
"""
Syntactic sugar to define a list of UML Lines.
"""


class RenderStyle(Enum):
    """
    An enumeration that determines how to draw various UML and other graphical elements
    """
    Draw     = 'D'
    """
    Just draw the outline
    """
    Fill     = 'F'
    """
    Just fill in the area associated with the shape
    """
    DrawFill = 'DF'
    """
    Do both when drawing the UML shape or figure
    """


@dataclass
class RectangleDefinition:
    """
    Defines a rectangle
    """

    renderStyle: RenderStyle = RenderStyle.Draw
    """
    How to draw the rectangle.  See `RenderStyle`
    """
    position:    Position    = Position(0, 0)
    """
    Where to put the rectangle.  See `Position`
    """
    size:        Size        = Size(0, 0)
    """
    The rectangle size.  See `Size`
    """


@dataclass
class EllipseDefinition(RectangleDefinition):
    """
    This is just typing syntactical sugar on how to define an Ellipse.
    """
    pass
