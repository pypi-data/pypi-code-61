
from obspy.core.event.origin import Arrival
from obspy.core.event.origin import Origin
from obspy.core.event.origin import OriginQuality, OriginUncertainty
from obspy.core.event.origin import Pick
from obspy.core.event.base import CreationInfo
from obspy.core.event.base import QuantityError
from obspy.core.event.base import WaveformStreamID
from obspy.core.utcdatetime import UTCDateTime
from obspy.core.event.magnitude import Magnitude

FIELD_UNSET = -9 # This should likely be changed in parse_y2k_line to something more like NaN 

def seisan_type4_to_arrival(type4, origin):
    '''
    Convert a seisan type4 phase dict to obspy arrival

    :param type4: parsed type4 line
    :type type4: python dict

    :return: converted phase 
    :rtype: obspy arrival and pick
    '''

    arrival = Arrival()
    phase = type4['Phase']
    arrival.phase = phase

    net='UNK'
    sta=type4['sta']
    waveform_id = WaveformStreamID(net, sta)
    channel_code = "%sH%s" % (type4['Instrument_type'], type4['Component'])
    waveform_id.channel_code = channel_code

    if type4['Azimuth_at_the_source'] != FIELD_UNSET:
        arrival.azimuth = type4['Azimuth_at_the_source']
    if type4['Azimuth_residual'] != FIELD_UNSET:
        arrival.backazimuth_residual = type4['Azimuth_residual']   # Could be wrong - is it even in the seisan manual ??
    if type4['Epicentral_distance'] != FIELD_UNSET:
        arrival.distance = type4['Epicentral_distance'] / 111.19   # obspy dist in deg
    if type4['Angle_of_incidence'] != FIELD_UNSET:
        arrival.takeoff_angle = type4['Angle_of_incidence']        # No idea if these are measured with same convention
    if type4['Travel_time_residual'] != FIELD_UNSET:
        arrival.time_residual = type4['Travel_time_residual']

    # Unmapped:              type4 field
    # somehow type4 I2      L   Weight ==> needs to map to arrival.time_weight (=float) ?
    #               I1      L   Weighting_indicator     (1-4) 0 or bank = full weight, 1=75%, 2=50%, 3=25%, 4=0%

    pick = Pick()
    arrival.pick_id = pick.resource_id
    pick.waveform_id = waveform_id
    year = origin.time.year
    mo = origin.time.month
    dd = origin.time.day
    hh = type4['Hour']
    mi = type4['Minutes']
    ss = type4['Seconds']
    date = "%s-%s-%sT%s:%s:%s" % (year, mo, dd, hh, mi, ss)
    pick.time = UTCDateTime(date)

    if type4['Phase_velocity'] != FIELD_UNSET:
        pick.horizontal_slowness = 111.19 / type4['Phase_velocity'] # km/s --> s/deg
    if type4['Direction_of_approach'] != FIELD_UNSET:
        pick.backazimuth = type4['Direction_of_approach']     # This is a guess - is it explained in the manual ??

    onset = type4['Quality_indicator']

    if onset == 'I':
        pick.onset = "impulsive"
    elif onset == 'E':
        pick.onset = "emergent"

    pick.phase_hint = phase

    if phase == 'P':
        if type4['First_motion'] == 'C':
            pick.polarity == 'positive'
        elif type4['First_motion'] == 'D':
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

    # time_errors = QuantityError() 
    # time_errors.uncertainty = _calc_code(y2k_phase['%swtCode' % phase])
    # pick.time_errors = time_errors

    return arrival, pick


def seisan_hdr_to_origin(seisan_hdr):
    '''
    Convert a seisan type1 or typeH line to quakeml Origin

    :param seisan_hdr: seisan type1/typeH parsed line
    :type seisan_hdr: python dict

    :return: converted origin 
    :rtype: obspy.core.event.origin.Origin
    '''

    origin = Origin()

    year = seisan_hdr['Year']

    mo = seisan_hdr['Month']
    dd = seisan_hdr['Day']
    hh = seisan_hdr['Hour']
    mi = seisan_hdr['Minutes']
    ss = seisan_hdr['Seconds']

    date = "%s-%s-%sT%s:%s:%s" % (year, mo, dd, hh, mi, ss)
    origin.time = UTCDateTime(date)

    origin.longitude = seisan_hdr['Longitude']
    origin.latitude = seisan_hdr['Latitude']
    origin.depth = seisan_hdr['Depth'] * 1.e3  # seisan depth [km] --> obspy depth [m]

    if 'Depth_indicator'in seisan_hdr:
        if seisan_hdr['Depth_indicator'] == 'F':
            origin.depth_type = "operator assigned"
    if 'Fix_o_time' in seisan_hdr:
        if seisan_hdr['Fix_o_time'] == 'F':
            origin.time_fixed = True

    quality = OriginQuality()
    if 'Number_of_stations_used' in seisan_hdr:
        quality.used_station_count = seisan_hdr['Number_of_stations_used']
    if 'RMS_of_time_residuals' in seisan_hdr:
        quality.standard_error  = seisan_hdr['RMS_of_time_residuals']

    origin.quality = quality

    creation_info = CreationInfo()
    if 'Hypocenter_reporting_agency' in seisan_hdr:
        creation_info.agency_id = seisan_hdr['Hypocenter_reporting_agency']
    origin.creation_info = creation_info

    return origin

def seisan_hdr_to_magnitudes(seisan_hdr):
    '''
    Convert a seisan type1 or typeH line to quakeml magnitudes

    :param seisan_hdr: seisan type1/typeH parsed line
    :type seisan_hdr: python dict

    :return: obspy magnitudes
    :rtype: list
    '''

    seisan_mag_types = {'L':'ML', 'b':'mb', 'B':'mB', 's':'Ms', 'S':'MS', 'W':'Mw', 'G':'MbLg', 'C':'Mc'}

    creation_info = None
    if seisan_hdr['Magnitude_reporting_agency'] != FIELD_UNSET and \
       len(seisan_hdr['Magnitude_reporting_agency'].strip()) > 0:
        creation_info = CreationInfo()
        creation_info.agency_id = seisan_hdr['Magnitude_reporting_agency']

    magnitudes = []
    for i in range(2):
        field = 'Magnitude_no_%d' % (i+1)
        if seisan_hdr[field] > FIELD_UNSET:
            #print("field:%s has value:%f" % (field, seisan_hdr[field]))
            magnitude = Magnitude()
            magnitude.mag = seisan_hdr[field]
            if seisan_hdr['Type_of_magnitude'] == FIELD_UNSET:
                mag_type = 'M' # default = unspecified
            elif seisan_hdr['Type_of_magnitude'] in seisan_mag_types:
                mag_type = seisan_mag_types[seisan_hdr['Type_of_magnitude']]
            else: # Use as is
                mag_type = seisan_hdr['Type_of_magnitude']

            magnitude.magnitude_type = mag_type
            # This is probably wrong - likely better to count the # of type4 line amp measurements
            magnitude.station_count = seisan_hdr['Number_of_stations_used'] 
            if creation_info:
                magnitude.creation_info = creation_info

            magnitudes.append(magnitude)

    return magnitudes


def add_seisan_errors_to_origin(seisan_errs, origin):
    '''
    seisan_errs = parsed seisan typeE line
    '''

    longitude_errors = QuantityError()
    longitude_errors.uncertainty = seisan_errs['Longitude_error']
    origin.longitude_errors = longitude_errors

    latitude_errors = QuantityError()
    latitude_errors.uncertainty = seisan_errs['Latitude_error']
    origin.latitude_errors = latitude_errors

    depth_errors = QuantityError()
    depth_errors.uncertainty = seisan_errs['Depth_error']
    origin.depth_errors = depth_errors

    time_errors = QuantityError()
    time_errors.uncertainty = seisan_errs['Origin_time_error']
    origin.time_errors = time_errors

    ''' What to do with this ?
    uncertainty = OriginUncertainty()
    seisan_hdrs['Covariance_xy']
    seisan_hdrs['Covariance_xz']
    seisan_hdrs['Covariance_yz']
    uncertainty.
    origin.uncertainty = uncertainty
horizontal_uncertainty (float, optional)
Circular confidence region, given by single value of horizontal uncertainty. Unit: m
min_horizontal_uncertainty (float, optional)
Semi-minor axis of confidence ellipse. Unit: m
max_horizontal_uncertainty (float, optional)
Semi-major axis of confidence ellipse. Unit: m
azimuth_max_horizontal_uncertainty (float, optional)
Azimuth of major axis of confidence ellipse. Measured clockwise from South-North direction at epicenter. Unit: deg
confidence_ellipsoid (ConfidenceEllipsoid, optional)
Confidence ellipsoid
preferred_description (str, optional)
Preferred uncertainty description. See OriginUncertaintyDescription for allowed values.
confidence_level (float, optional)
Confidence level of the uncertainty, given in percent.
    '''

    return
