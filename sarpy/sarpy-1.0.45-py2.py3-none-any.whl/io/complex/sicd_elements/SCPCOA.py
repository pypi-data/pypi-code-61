# -*- coding: utf-8 -*-
"""
The SCPCOAType definition.
"""

import numpy
from numpy.linalg import norm

from .base import Serializable, DEFAULT_STRICT, \
    _StringEnumDescriptor, _FloatDescriptor, _SerializableDescriptor
from .blocks import XYZType

from sarpy.geometry import geocoords


__classification__ = "UNCLASSIFIED"
__author__ = "Thomas McCullough"


class GeometryCalculator(object):
    """
    Performs the necessary SCPCOA geometry element calculations.
    """

    def __init__(self, SCP, ARPPos, ARPVel):
        self.SCP = SCP
        self.ARP = ARPPos
        self.ARP_vel = ARPVel
        self.LOS = (self.SCP - self.ARP)
        # unit vector versions
        self.uSCP = self._make_unit(self.SCP)
        self.uARP = self._make_unit(self.ARP)
        self.uARP_vel = self._make_unit(self.ARP_vel)
        self.uLOS = self._make_unit(self.LOS)
        self.left = numpy.cross(self.uARP, self.uARP_vel)
        self.look = numpy.sign(self.left.dot(self.uLOS))
        # Earth Tangent Plane (ETP) at the SCP is the plane tangent to the surface of constant height
        # above the WGS 84 ellipsoid (HAE) that contains the SCP. The ETP is an approximation to the
        # ground plane at the SCP.
        self.ETP = geocoords.wgs_84_norm(SCP)
        # slant plane unit normal
        self.uSPZ = self._make_unit(self.look*numpy.cross(self.ARP_vel, self.uLOS))
        # perpendicular component of range vector wrt the ground plane
        self.uGPX = self._make_unit(-self.uLOS + numpy.dot(self.ETP, self.uLOS)*self.ETP)
        self.uGPY = numpy.cross(self.ETP, self.uGPX)  # already unit vector
        # perpendicular component of north wrt the ground plane
        self.uNORTH = self._make_unit(numpy.array([0, 0, 1]) - self.ETP[2]*self.ETP)
        self.uEAST = numpy.cross(self.uNORTH, self.ETP)  # already unit vector

    @staticmethod
    def _make_unit(vec):
        vec_norm = norm(vec)
        if vec_norm < 1e-6:
            raise ValueError(
                'input vector has norm {}, this is likely a mistake'.format(vec_norm))
        return vec/vec_norm

    @property
    def ROV(self):
        """
        float: Range over velocity
        """
        return float(norm(self.LOS)/norm(self.ARP_vel))

    @property
    def SideOfTrack(self):
        return 'R' if self.look < 0 else 'L'

    @property
    def SlantRange(self):
        return float(norm(self.LOS))

    @property
    def GroundRange(self):
        return norm(self.SCP) * numpy.arccos(self.uSCP.dot(self.uARP))

    @property
    def DopplerConeAngle(self):
        return float(numpy.rad2deg(numpy.arccos(self.uARP_vel.dot(self.uLOS))))

    def get_graze_and_incidence(self):
        graze_ang = -float(numpy.rad2deg(numpy.arcsin(self.ETP.dot(self.uLOS))))
        return graze_ang, 90 - graze_ang

    @property
    def TwistAngle(self):
        return float(-numpy.rad2deg(numpy.arcsin(self.uGPY.dot(self.uSPZ))))

    @property
    def SquintAngle(self):
        return float(numpy.rad2deg(
            numpy.arctan2(self.uARP_vel.dot(self.uGPX), self.uARP_vel.dot(self.uGPY))))

    @property
    def SlopeAngle(self):
        return float(numpy.rad2deg(numpy.arccos(self.ETP.dot(self.uSPZ))))

    @property
    def AzimuthAngle(self):
        azim_ang = numpy.rad2deg(numpy.arctan2(self.uGPX.dot(self.uEAST), self.uGPX.dot(self.uNORTH)))
        azim_ang = azim_ang if azim_ang > 0 else azim_ang + 360
        return float(azim_ang)

    def get_layover(self):
        layover_ground = self.ETP - self.ETP.dot(self.uSPZ)*self.uSPZ
        layover_ang = numpy.rad2deg(
            numpy.arctan2(layover_ground.dot(self.uEAST), layover_ground.dot(self.uNORTH)))
        layover_ang = layover_ang if layover_ang > 0 else layover_ang + 360
        return float(layover_ang), float(norm(layover_ground))

    def get_shadow(self):
        S = self.ETP - self.uLOS/self.uLOS.dot(self.ETP)
        Sprime = S - self.uSPZ*(S.dot(self.ETP)/self.uSPZ.dot(self.ETP))
        shadow_angle = numpy.rad2deg(numpy.arctan2(Sprime.dot(self.uGPX), Sprime.dot(self.uGPY)))
        return float(shadow_angle), float(norm(Sprime))


class SCPCOAType(Serializable):
    """
    Center of Aperture (COA) for the Scene Center Point (SCP).
    """

    _fields = (
        'SCPTime', 'ARPPos', 'ARPVel', 'ARPAcc', 'SideOfTrack', 'SlantRange', 'GroundRange', 'DopplerConeAng',
        'GrazeAng', 'IncidenceAng', 'TwistAng', 'SlopeAng', 'AzimAng', 'LayoverAng')
    _required = _fields
    _numeric_format = {
        'SCPTime': '0.16G', 'SlantRange': '0.16G', 'GroundRange': '0.16G', 'DopplerConeAng': '0.16G',
        'GrazeAng': '0.16G', 'IncidenceAng': '0.16G', 'TwistAng': '0.16G', 'SlopeAng': '0.16G',
        'AzimAng': '0.16G', 'LayoverAng': '0.16G'}
    # class variables
    _SIDE_OF_TRACK_VALUES = ('L', 'R')
    # descriptors
    SCPTime = _FloatDescriptor(
        'SCPTime', _required, strict=DEFAULT_STRICT,
        docstring='*Center Of Aperture time for the SCP (t_COA_SCP)*, relative to collection '
                  'start in seconds.')  # type: float
    ARPPos = _SerializableDescriptor(
        'ARPPos', XYZType, _required, strict=DEFAULT_STRICT,
        docstring='Aperture position at *t_COA_SCP* in ECF coordinates.')  # type: XYZType
    ARPVel = _SerializableDescriptor(
        'ARPVel', XYZType, _required, strict=DEFAULT_STRICT,
        docstring='ARP Velocity at *t_COA_SCP* in ECF coordinates.')  # type: XYZType
    ARPAcc = _SerializableDescriptor(
        'ARPAcc', XYZType, _required, strict=DEFAULT_STRICT,
        docstring='ARP Acceleration at *t_COA_SCP* in ECF coordinates.')  # type: XYZType
    SideOfTrack = _StringEnumDescriptor(
        'SideOfTrack', _SIDE_OF_TRACK_VALUES, _required, strict=DEFAULT_STRICT,
        docstring='Side of track.')  # type: str
    SlantRange = _FloatDescriptor(
        'SlantRange', _required, strict=DEFAULT_STRICT,
        docstring='Slant range from the aperture to the *SCP* in meters.')  # type: float
    GroundRange = _FloatDescriptor(
        'GroundRange', _required, strict=DEFAULT_STRICT,
        docstring='Ground Range from the aperture nadir to the *SCP*. Distance measured along spherical earth model '
                  'passing through the *SCP* in meters.')  # type: float
    DopplerConeAng = _FloatDescriptor(
        'DopplerConeAng', _required, strict=DEFAULT_STRICT,
        docstring='The Doppler Cone Angle to SCP at *t_COA_SCP* in degrees.')  # type: float
    GrazeAng = _FloatDescriptor(
        'GrazeAng', _required, strict=DEFAULT_STRICT, bounds=(0., 90.),
        docstring='Grazing Angle between the SCP *Line of Sight (LOS)* and *Earth Tangent Plane (ETP)*.')  # type: float
    IncidenceAng = _FloatDescriptor(
        'IncidenceAng', _required, strict=DEFAULT_STRICT, bounds=(0., 90.),
        docstring='Incidence Angle between the *LOS* and *ETP* normal.')  # type: float
    TwistAng = _FloatDescriptor(
        'TwistAng', _required, strict=DEFAULT_STRICT, bounds=(-90., 90.),
        docstring='Angle between cross range in the *ETP* and cross range in the slant plane.')  # type: float
    SlopeAng = _FloatDescriptor(
        'SlopeAng', _required, strict=DEFAULT_STRICT, bounds=(0., 90.),
        docstring='Slope Angle from the *ETP* to the slant plane at *t_COA_SCP*.')  # type: float
    AzimAng = _FloatDescriptor(
        'AzimAng', _required, strict=DEFAULT_STRICT, bounds=(0., 360.),
        docstring='Angle from north to the line from the *SCP* to the aperture nadir at *COA*. Measured '
                  'clockwise in the *ETP*.')  # type: float
    LayoverAng = _FloatDescriptor(
        'LayoverAng', _required, strict=DEFAULT_STRICT, bounds=(0., 360.),
        docstring='Angle from north to the layover direction in the *ETP* at *COA*. Measured '
                  'clockwise in the *ETP*.')  # type: float

    def __init__(self, SCPTime=None, ARPPos=None, ARPVel=None, ARPAcc=None, SideOfTrack=None,
                 SlantRange=None, GroundRange=None, DopplerConeAng=None, GrazeAng=None, IncidenceAng=None,
                 TwistAng=None, SlopeAng=None, AzimAng=None, LayoverAng=None, **kwargs):
        """

        Parameters
        ----------
        SCPTime : float
        ARPPos : XYZType|numpy.ndarray|list|tuple
        ARPVel : XYZType|numpy.ndarray|list|tuple
        ARPAcc : XYZType|numpy.ndarray|list|tuple
        SideOfTrack : str
        SlantRange : float
        GroundRange : float
        DopplerConeAng : float
        GrazeAng : float
        IncidenceAng : float
        TwistAng : float
        SlopeAng : float
        AzimAng : float
        LayoverAng : float
        kwargs : dict
        """

        self._ROV = None
        self._squint = None
        self._shadow = None
        self._shadow_magnitude = None
        self._layover_magnitude = None

        if '_xml_ns' in kwargs:
            self._xml_ns = kwargs['_xml_ns']
        if '_xml_ns_key' in kwargs:
            self._xml_ns_key = kwargs['_xml_ns_key']
        self.SCPTime = SCPTime
        self.ARPPos, self.ARPVel, self.ARPAcc = ARPPos, ARPVel, ARPAcc
        self.SideOfTrack = SideOfTrack
        self.SlantRange, self.GroundRange = SlantRange, GroundRange
        self.DopplerConeAng, self.GrazeAng, self.IncidenceAng = DopplerConeAng, GrazeAng, IncidenceAng
        self.TwistAng, self.SlopeAng, self.AzimAng, self.LayoverAng = TwistAng, SlopeAng, AzimAng, LayoverAng
        super(SCPCOAType, self).__init__(**kwargs)

    @property
    def look(self):
        """
        int: An integer version of `SideOfTrack`:

            * None if `SideOfTrack` is not defined

            * -1 if SideOfTrack == 'R'

            * 1 if SideOftrack == 'L'
        """

        if self.SideOfTrack is None:
            return None
        else:
            return -1 if self.SideOfTrack == 'R' else 1

    @property
    def ROV(self):
        """
        float: The Ratio of Range to Velocity at Center of Aperture time.
        """

        return self._ROV

    @property
    def ThetaDot(self):
        """
        float: Derivative of Theta as a function of time at Center of Aperture time.
        """

        return float(numpy.sin(numpy.deg2rad(self.DopplerConeAng))/self.ROV)

    @property
    def MultipathGround(self):
        """
        float: The anticipated angle of multipath features on the ground in degrees.
        """

        return numpy.rad2deg(
            -numpy.arctan(numpy.tan(numpy.deg2rad(self.TwistAng))*numpy.sin(numpy.deg2rad(self.GrazeAng))))

    @property
    def Multipath(self):
        """
        float: The anticipated angle of multipath features in degrees.
        """

        return numpy.mod(self.AzimAng - 180 + self.MultipathGround, 360)

    @property
    def Shadow(self):
        """
        float: The anticipated angle of shadow features in degrees.
        """

        return self._shadow

    @property
    def ShadowMagnitude(self):
        """
        float: The anticipated relative magnitude of shadow features.
        """

        return self._shadow_magnitude

    @property
    def Squint(self):
        """
        float: The squint angle, in degrees.
        """

        return self._squint

    @property
    def LayoverMagnitude(self):
        """
        float: The anticipated relative magnitude of layover features.
        """

        return self._layover_magnitude

    def _derive_scp_time(self, Grid):
        """
        Expected to be called by SICD parent.

        Parameters
        ----------
        Grid : sarpy.io.complex.sicd_elements.GridType

        Returns
        -------
        None
        """

        if Grid is None or Grid.TimeCOAPoly is None:
            return  # nothing can be done

        scp_time = Grid.TimeCOAPoly.Coefs[0, 0]
        self.SCPTime = scp_time

    def _derive_position(self, Position):
        """
        Derive aperture position parameters, if necessary. Expected to be called by SICD parent.

        Parameters
        ----------
        Position : sarpy.io.complex.sicd_elements.Position.PositionType

        Returns
        -------
        None
        """

        if Position is None or Position.ARPPoly is None or self.SCPTime is None:
            return  # nothing can be derived

        # set aperture position, velocity, and acceleration at scptime from position
        # polynomial, if necessary
        poly = Position.ARPPoly
        scptime = self.SCPTime

        self.ARPPos = XYZType.from_array(poly(scptime))
        self.ARPVel = XYZType.from_array(poly.derivative_eval(scptime, 1))
        self.ARPAcc = XYZType.from_array(poly.derivative_eval(scptime, 2))

    def _derive_geometry_parameters(self, GeoData):
        """
        Expected to be called by SICD parent.

        Parameters
        ----------
        GeoData : sarpy.io.complex.sicd_elements.GeoData.GeoDataType

        Returns
        -------
        None
        """

        if GeoData is None or GeoData.SCP is None or GeoData.SCP.ECF is None or \
                self.ARPPos is None or self.ARPVel is None:
            return  # nothing can be derived

        # construct our calculator
        calculator = GeometryCalculator(
            GeoData.SCP.ECF.get_array(), self.ARPPos.get_array(), self.ARPVel.get_array())
        # set all the values
        self._ROV = calculator.ROV
        self.SideOfTrack = calculator.SideOfTrack
        self.SlantRange = calculator.SlantRange
        self.GroundRange = calculator.GroundRange
        self.DopplerConeAng = calculator.DopplerConeAngle
        self.GrazeAng, self.IncidenceAng = calculator.get_graze_and_incidence()
        self.TwistAng = calculator.TwistAngle
        self._squint = calculator.SquintAngle
        self.SlopeAng = calculator.SlopeAngle
        self.AzimAng = calculator.AzimuthAngle
        self.LayoverAng, self._layover_magnitude = calculator.get_layover()
        self._shadow, self._shadow_magnitude = calculator.get_shadow()
