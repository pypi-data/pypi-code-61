import argparse
import copy
import os
import sys

from obspy.core.event import Catalog
from obspy.core.event.event import Event

from . import get_format_dir
from .lib.liblog import getLogger
from .lib.lib_y2k import parse_y2k_line, read_format
from .lib.lib_seisan import *

def main():

    logger = getLogger()

    seisan_file = processCmdLine()

    '''
    Note: Type 1 line must be the first, all type 4 lines should be together and the last line must be blank
          Type E Line (Optional): Hyp error estimates
          Type H line, High accuracy hypocenter line
    '''

    formats = {}
    #nordic_types = ['1', '4', '6', '7', 'E', 'H', 'I']
    nordic_types = ['1', '4', 'E', 'H']

    formats_dir = get_format_dir()
    logger.info("formats_dir=%s" % formats_dir)

    for ntype in nordic_types:
        #format_file = '../formats/format.nordic.type%s' % ntype
        format_file = os.path.join(formats_dir, 'format.nordic.type%s' % ntype)
        formats[ntype]= read_format(format_file)

    f = open(seisan_file, 'r')
    lines = f.readlines()

    line_1 = None
    line_E = None
    line_H = None

    for line in lines:
        if line[79].strip() == "1":
            line_1 = line
        elif line[79].strip() == "H":
            line_H = line
        elif line[79].strip() == "E":
            line_E = line

    origin = None
    origin_hypo = None
    magnitudes = []
    if line_1:
        seisan_hdr = parse_y2k_line(line_1, formats['1'])
        origin = seisan_hdr_to_origin(seisan_hdr)
        magnitudes = seisan_hdr_to_magnitudes(seisan_hdr)
    if line_H:
        seisan_hypo = parse_y2k_line(line_H, formats['H'])
        origin_hypo = seisan_hdr_to_origin(seisan_hypo)
    if line_E:
        seisan_errs = parse_y2k_line(line_E, formats['E'])
        add_seisan_errors_to_origin(seisan_errs, origin)
        origin.quality.azimuthal_gap = seisan_errs['Gap']

    if origin_hypo:
        origin.time = origin_hypo.time
        origin.latitude = origin_hypo.latitude
        origin.longitude = origin_hypo.longitude
        origin.depth = origin_hypo.depth

    for magnitude in magnitudes:
        magnitude.azimuthal_gap = origin.quality.azimuthal_gap

    ntype = '4'
    arrivals = []
    picks = []
    for line in lines:
        if len(line.strip()) == 0:
            break
        if not line[79] in ['4', ' ']:
            continue

        parsed_type4 = parse_y2k_line(line, formats[ntype])
        arrival, pick = seisan_type4_to_arrival(parsed_type4, origin)
        arrivals.append(arrival)
        picks.append(pick)

    origin.arrivals = arrivals
    event = Event()
    event.origins = [origin]
    event.picks = picks
    event.preferred_origin_id = origin.resource_id.id
    event.magnitudes = magnitudes
    event.preferred_magnitude_id = magnitudes[0].resource_id.id

    catalog = Catalog(events=[event])
    catalog.write("test.xml", format="QUAKEML")
    print(event)
    print(event.preferred_magnitude())

    return

def processCmdLine():

    parser = argparse.ArgumentParser()
    optional = parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")

    required.add_argument("--infile", type=str, metavar='Path to seisan file', required=True)

    args, unknown = parser.parse_known_args()

    return args.infile



if __name__ == "__main__":
    main()
