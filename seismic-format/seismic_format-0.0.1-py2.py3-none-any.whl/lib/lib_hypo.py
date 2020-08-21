
from obspy.core.event.origin import Arrival
from obspy.core.event.origin import Origin
from obspy.core.event.origin import OriginQuality, OriginUncertainty
from obspy.core.event.origin import Pick
from obspy.core.event.base import CreationInfo
from obspy.core.event.base import QuantityError
from obspy.core.event.base import WaveformStreamID
from obspy.core.utcdatetime import UTCDateTime

def y2k_to_origin(y2k_origin):
    '''
    Convert a y2k_origin to quakeml Origin

    :param y2k_origin: origin to convert
    :type origin: y2k origin dict

    :return: converted origin 
    :rtype: obspy.core.event.origin.Origin
    '''

    origin = Origin()

    year = y2k_origin['year']
    mo = y2k_origin['moddhhmi'][0:2]
    dd = y2k_origin['moddhhmi'][2:4]
    hh = y2k_origin['moddhhmi'][4:6]
    mi = y2k_origin['moddhhmi'][6:8]
    ss = y2k_origin['seconds']
    date = "%s-%s-%sT%s:%s:%s" % (year, mo, dd, hh, mi, ss)
    origin.time = UTCDateTime(date)

    longitude = y2k_origin['lon_deg'] + y2k_origin['lon_min']/60.0
    if y2k_origin['e_or_w'] != 'E':
        longitude *= -1

    latitude = y2k_origin['lat_deg'] + y2k_origin['lat_min']/60.0
    if y2k_origin['n_or_s'] == 'S':
        longitude *= -1

    origin.longitude = longitude
    origin.latitude = latitude
    origin.depth = y2k_origin['depth'] * 1.e3  # y2k depth [km] --> obspy depth [m]
    origin.depth_errors = y2k_origin['error_vertical'] * 1.e3  # y2k depth [km] --> obspy depth [m]
    if y2k_origin['program_remark'] == " -":
        origin.depth_type = "operator assigned"
    origin.region = y2k_origin['region']

    quality = OriginQuality()
    #quality.associated_phase_count
    #quality.used_phase_count
    quality.standard_error = y2k_origin['rms']
    quality.azimuthal_gap = y2k_origin['azgap']
    quality.minimum_distance = y2k_origin['min_dist']
    quality.used_phase_count = y2k_origin['n_P_and_S_times']
    quality.associated_phase_count = y2k_origin['n_valid_P_and_S_reads']
    origin.quality = quality

    uncertainty = OriginUncertainty()
    uncertainty.horizontal_uncertainty = y2k_origin['error_horizontal'] * 1.e3 # km --> m
    uncertainty.max_horizontal_uncertainty = y2k_origin['pri_error_size'] * 1.e3
    uncertainty.azimuth_max_horizontal_uncertainty = y2k_origin['pri_error_az']
    uncertainty.min_horizontal_uncertainty = y2k_origin['sm_error_size'] * 1.e3
    origin.origin_uncertainty = uncertainty

    creation_info = CreationInfo()
    creation_info.agency_id = y2k_origin['authority']
    creation_info.version = y2k_origin['version_info']
    origin.creation_info = creation_info

    return origin


def origin_to_y2k(origin, hdr_format):
    '''
    Convert a quakeml origin to y2k_origin dict

    Only reason for passing in hdr_format is so we can auto initialize
      all the y2k fields = None

    :param origin: origin to convert
    :type origin: obspy.core.event.origin.Origin

    :return: converted origin 
    :rtype: python dict

    '''

    y2k_origin = {}

    for k,v in hdr_format.items():
        y2k_origin[k] = None

    t = {}
    for x in {'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond'}:
        t[x] = getattr(origin.time, x)
    y2k_origin['year'] = t['year']
    y2k_origin['moddhhmi'] = "%02d%02d%02d%02d" % (t['month'], t['day'], t['hour'], t['minute'])
    y2k_origin['seconds'] = t['second'] + t['microsecond']/1e6

    lat = abs(origin.latitude)
    y2k_origin['lat_deg'] = int(lat)
    y2k_origin['lat_min'] = (lat - int(lat))/60.
    y2k_origin['n_or_s'] = '' if origin.latitude >= 0. else 'S'

    lon = abs(origin.longitude)
    y2k_origin['lon_deg'] = int(lon)
    y2k_origin['lon_min'] = (lon - int(lon))/60.
    y2k_origin['e_or_w'] = '' if origin.longitude <= 0. else 'E'

    y2k_origin['depth'] = origin.depth/1.e3
    y2k_origin['error_vertical'] = origin.depth_errors.uncertainty/1.e3

    if origin.depth_type == "operator assigned":
        #program_remark       Auxiliary remark from program (i.e. "-" for depth fixed, etc
        y2k_origin['program_remark'] = '-'

    y2k_origin['authority'] = origin.creation_info.agency_id
    y2k_origin['version_info'] = origin.creation_info.version

    #number_S_times          Number of S times with weights greater than 0.1.
    #number_P_first_motions  Number of P first motions. *

    y2k_origin['azgap'] = origin.quality.azimuthal_gap
    y2k_origin['n_P_and_S_times'] = origin.quality.used_phase_count
    y2k_origin['n_valid_P_and_S_reads'] = origin.quality.associated_phase_count
    y2k_origin['rms'] = origin.quality.standard_error

    y2k_origin['pri_error_az']   = origin.origin_uncertainty.confidence_ellipsoid.major_axis_azimuth
    y2k_origin['pri_error_dip']  = origin.origin_uncertainty.confidence_ellipsoid.major_axis_plunge
    y2k_origin['pri_error_size'] = origin.origin_uncertainty.confidence_ellipsoid.semi_major_axis_length/1.e3

    #These don't exist
    #y2k_origin['int_error_az']   = origin.origin_uncertainty.confidence_ellipsoid.major_axis_azimuth
    #y2k_origin['int_error_dip']  = origin.origin_uncertainty.confidence_ellipsoid.major_axis_plunge
    #y2k_origin['int_error_size'] = origin.origin_uncertainty.confidence_ellipsoid.semi_minor_axis_length/1.e3

    y2k_origin['error_horizontal'] = origin.origin_uncertainty.horizontal_uncertainty/1.e3
    y2k_origin['error_vertical'] = origin.depth_errors.uncertainty/1.e3

    return y2k_origin

def y2k_phase_to_arrival(y2k_phase, phase):
    '''
    Convert a y2k phase dict to obspy arrival

    :param phase: 'P' or 'S'
    :type phase: str
    :param y2k_phase: y2k_phase
    :type y2k_phase: python dict

    :return: converted phase 
    :rtype: obspy arrival
    '''

    arrival = Arrival()
    arrival.phase = phase
    if y2k_phase['Azim'] > 0:
        arrival.azimuth = y2k_phase['Azim']
    # epicentral dist in deg
    if y2k_phase['Dist'] > 0:
        arrival.distance = y2k_phase['Dist'] / 111.19  #Convert y2k dist [km] to obspy dist [deg]
    # takeoff angle (deg) measured from downward vertical
    if y2k_phase['Angle'] > 0:
        arrival.takeoff_angle = y2k_phase['Angle']    ###   Verify y2k uses same takeoff angle convention (?)
    arrival.time_residual = y2k_phase['%srms' % phase]
    arrival.time_weight = y2k_phase['%swtUsed' % phase]

    waveform_id = WaveformStreamID(y2k_phase['net'], y2k_phase['sta'])
    waveform_id.channel_code = y2k_phase['chan']
    if y2k_phase['loc'] != -9:
        waveform_id.location_code = y2k_phase['loc']

    pick = Pick()
    pick.waveform_id = waveform_id
    year = y2k_phase['year']
    mo = y2k_phase['moddhhmi'][0:2]
    dd = y2k_phase['moddhhmi'][2:4]
    hh = y2k_phase['moddhhmi'][4:6]
    mi = y2k_phase['moddhhmi'][6:8]
    ss = y2k_phase['%ssec' % phase]
    date = "%s-%s-%sT%s:%s:%s" % (year, mo, dd, hh, mi, ss)
    pick.time = UTCDateTime(date)
    #pick.backazimuth = 

    arrival.pick_id = pick.resource_id

    onset = y2k_phase['%srmk' % phase][0]

    if onset == 'I':
        pick.onset = "impulsive"
    elif onset == 'E':
        pick.onset = "emergent"
    pick.phase_hint = phase

    if phase == 'P':
        if y2k_phase['PUpDown'] == 'U':
            pick.polarity == 'positive'
        elif y2k_phase['PUpDown'] == 'D':
            pick.polarity == 'negative'

    def _calc_code(x):
#   .03 .06 .15 .3 0.5
#   0    1    2  3  4
# This code should be based on deltim = pick uncertainty, not
        if   x == 0: val = .03
        elif x == 1: val = .06
        elif x == 2: val = .15
        elif x == 3: val = .30
        elif x == 4: val = .50
        return val

    time_errors = QuantityError() 
    time_errors.uncertainty = _calc_code(y2k_phase['%swtCode' % phase])
    pick.time_errors = time_errors

    return arrival, pick


def arrival_to_y2k(arrival, y2k_format):
    '''
    Convert a quakeml arrival to y2k arrival dict

    Only reason for passing in y2k_format is so we can auto initialize
      all the y2k_phase fields = None

    :param origin: origin to convert
    :type origin: obspy.core.event.origin.Origin

    :return: converted origin 
    :rtype: python dict
    '''


    y2k_phase = {}

    for k,v in y2k_format.items():
        y2k_phase[k] = None

    pick = arrival.pick_id.get_referred_object()
    y2k_phase['sta']  = pick.waveform_id.station_code
    y2k_phase['net']  = pick.waveform_id.network_code
    y2k_phase['chan'] = pick.waveform_id.channel_code
    y2k_phase['loc']  = pick.waveform_id.location_code

    t = {}
    for x in {'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond'}:
        t[x] = getattr(pick.time, x)
    y2k_phase['year'] = t['year']
    y2k_phase['moddhhmi'] = "%02d%02d%02d%02d" % (t['month'], t['day'], t['hour'], t['minute'])

    phase = 'P'

    if arrival.phase[0] == 'S':
        phase = 'S'
    onset = " "
    if pick.onset == 'impulsive':
        onset = 'I'
    rmk = '%srmk' % (phase)
    y2k_phase[rmk] = "%1s%1s" % (onset, phase)

    if phase == 'P' and hasattr(pick, 'polarity'):
        if pick.polarity == 'positive':
            y2k_phase['PUpDown'] = 'U'
        elif pick.polarity == 'negative':
            y2k_phase['PUpDown'] = 'D'

    y2k_phase['%ssec' % phase]    = t['second'] + t['microsecond']/1e6
    y2k_phase['%srms' % phase]    = arrival.time_residual
    y2k_phase['%swtUsed' % phase] = arrival.time_weight

    def _calc_code(x):
#   .03 .06 .15 .3 0.5
#   0    1    2  3  4
# This code should be based on deltim = pick uncertainty, not
        if   x <= .03: val = 0
        elif x <= .06: val = 1
        elif x <= .15: val = 2
        elif x <= .30: val = 3
        elif x <= .50: val = 4
        else: #val = ? is this going to break something ?
            val = 5
        return val

    y2k_phase['%swtCode' % phase] =  _calc_code(pick.time_errors.uncertainty)
    if arrival.azimuth:
        y2k_phase['Azim']    = "%.2f" % arrival.azimuth
    if arrival.distance:
        y2k_phase['Dist']    = arrival.distance * 111.19 #y2k dist = km vs. obspy dist = deg
    if arrival.takeoff_angle:
        y2k_phase['Angle']   = arrival.takeoff_angle

    return y2k_phase
