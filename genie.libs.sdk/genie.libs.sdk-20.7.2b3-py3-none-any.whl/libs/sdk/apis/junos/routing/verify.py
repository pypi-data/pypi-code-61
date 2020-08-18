"""Common verify functions for routing"""

# Python
import re
import logging
from prettytable import PrettyTable
import operator

# pyATS
from pyats.utils.objects import find, R
from genie.utils import Dq

# Genie
from genie.utils.timeout import Timeout
from genie.libs.sdk.libs.utils.normalize import GroupKeys
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BGP
from genie.libs.sdk.apis.iosxe.bgp.get import (
    get_ip_bgp_summary,
    get_bgp_route_from_neighbors,
    get_bgp_neighbors_advertised_routes,
)

# ROUTING
from genie.libs.sdk.apis.iosxe.routing.get import (
    get_routing_routes,
    get_routing_repair_path_information)

log = logging.getLogger(__name__)
            
def verify_ip_cef_nexthop_label(device,
                                ip,
                                table=None,
                                expected_label=None,
                                vrf=None,
                                max_time=30,
                                check_interval=10):
    """ Verify nexthop does (not) have expected label

        Args:
            device (`obj`): Device object
            ip (`str`): IP address
            expected_label (`str`): Expected label. None if no label expected
            vrf (`str`): Not used on JuniperOS
            table (`str`): Route table
            max_time (`int`): Max time, default: 30
            check_interval (`int`): Check interval, default: 10
        Returns:
            result (`bool`): Verified result
        Raises:
            N/A
    """

    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        try:
            if table:
                out = device.parse('show route table {table} {ip}'.format(
                    table=table, ip=ip))
            else:
                out = device.parse('show route {ip}'.format(ip=ip))
        except SchemaEmptyParserError:
            log.info('Failed to parse. Device output might contain nothing.')
            timeout.sleep()
            continue

        for table_name in out.get('table_name', {}):
            if table and table_name not in table:
                continue

            for route in out['table_name'][table_name].get('routes', {}):
                if ip in route:
                    hop_index_dict = out['table_name'][table_name]['routes'][
                        route]
                    for index in hop_index_dict.get('next_hop', {}).get(
                            'next_hop_list', {}):
                        if '>' in hop_index_dict['next_hop']['next_hop_list'][
                                index].get('best_route', ''):
                            found_label = hop_index_dict['next_hop'][
                                'next_hop_list'][index].get('mpls_label')
                            if expected_label and expected_label in found_label:
                                log.info(
                                    'Found the expected label "{}"'.format(
                                        found_label))
                                return True
                            elif not expected_label and not found_label:
                                log.info(
                                    'No label found. No label is expected')
                                return True

        timeout.sleep()
    return False


def verify_routing_static_routes(device,
                                 destination_address,
                                 to=None,
                                 not_to=None,
                                 known_via=None,
                                 tag=None,
                                 preference=None,
                                 protocol_name=None,
                                 extensive=False,
                                 max_time=60,
                                 check_interval=10):
    """ Verify static route exists

        Args:
            device ('str'): Device str
            destination_address ('str'): destination ip address
            to ('str'): to value
            not_to ('str'): not to value
            known_via ('str'): known via value
            tag ('str'): Tag value
            preference ('str'): Preference value
            protocol_name ('str'): Protocol name
            extensive ('bool'): if command with extensive at the end
            max_time (`int`): Max time, default: 60
            check_interval (`int`): Check interval, default: 10
        Returns:
            True / False
        Raises:
            None

    """
    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        try:
            if extensive:
                out = device.parse('show route protocol static extensive')
            else:
                out = device.parse('show route protocol static')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # Example dictionary structure:
        #         {
        #             "rt": [
        #                 {
        #                     "rt-destination": "10.169.14.240/32",
        #                     "rt-entry": {
        #                         "nh": [
        #                             {
        #                                 "to": "10.169.14.121",
        #                                 "via": "ge-0/0/1.0"
        #                             }
        #                         ],
        #                         "rt-tag": "100",
        #                         "preference": "5",
        #                         "protocol-name": "Static"
        #                     }
        #                 }
        #             ],
        #             "table-name": "inet.0",
        #             "total-route-count": "240"
        #         },
        rt_list = Dq(out).get_values("rt")
        rt_destination_ = None
        for rt_dict in rt_list:
            current_rt_destination = Dq(rt_dict).get_values(
                "rt-destination", 0)
            if current_rt_destination:
                rt_destination_ = current_rt_destination
            if not rt_destination_:
                continue
            if not rt_destination_.startswith(destination_address):
                continue

            if not_to:
                not_to_ = Dq(rt_dict).get_values("to", 0)
                if not_to_.startswith(not_to):
                    continue
            if to:
                to_ = Dq(rt_dict).get_values("to", 0)
                if not to_.startswith(to):
                    continue
            if known_via:
                via_ = Dq(rt_dict).get_values("via", 0)
                if not via_.startswith(known_via):
                    continue
            if tag:
                tag_ = Dq(rt_dict).get_values("rt-tag", 0)
                if str(tag_) != str(tag):
                    continue
            if preference:
                preference_ = Dq(rt_dict).get_values("preference", 0)
                if str(preference_) != str(preference):
                    continue
            if protocol_name:
                protocol_ = Dq(rt_dict).get_values("protocol-name", 0)
                if protocol_.upper() != protocol_name.upper():
                    continue
            return True
        timeout.sleep()
    return False


def verify_routing_interface_preference(device,
                                        protocol,
                                        interface,
                                        preference,
                                        extensive=None,
                                        max_time=60,
                                        check_interval=10):
    """ Verify routing interface preference

        Args:
            device ('str'): Device str
            protocol ('str'): Protocol name
            interface ('str'): Interface name
            preference ('int'): Preference value
            extensive ('bool'): Check with extensive command
            max_time (`int`): Max time, default: 60
            check_interval (`int`): Check interval, default: 10
        Returns:
            True / False
        Raises:
            None

    """
    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        try:
            if extensive:
                out = device.parse(
                    'show route protocol {protocol} extensive'.format(
                        protocol=protocol))
            else:
                out = device.parse(
                    'show route protocol {protocol}'.format(protocol=protocol))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # Example dictionary structure:
        #         {
        #             "rt": [
        #                 {
        #                     "rt-destination": "10.169.14.240/32",
        #                     "rt-entry": {
        #                         "nh": [
        #                             {
        #                                 "to": "10.169.14.121",
        #                                 "via": "ge-0/0/1.0"
        #                             }
        #                         ],
        #                         "rt-tag": "100",
        #                         "preference": "5",
        #                         "protocol-name": "Static"
        #                     }
        #                 }
        #             ],
        #             "table-name": "inet.0",
        #             "total-route-count": "240"
        #         },
        rt_list = Dq(out).get_values("rt")
        for rt_dict in rt_list:
            via_ = Dq(rt_dict).get_values("via", 0)
            if not via_ or not via_.startswith(interface):
                continue
            preference_ = Dq(rt_dict).get_values("preference", 0)
            if not preference_ or preference_ != str(preference):
                continue
            return True
        timeout.sleep()
    return False


def verify_routing_ip_exist(device,
                            destination_address,
                            protocol=None,
                            metric=None,
                            max_time=60,
                            check_interval=10,
                            extensive=None,
                            exact=None,
                            known_via=None,
                            ):
    """ Verify routing ip exists

        Args:
            device ('str'): Device str
            destination_address ('str'): Destination address
            protocol ('str'): Protocol name
            max_time (`int`): Max time, default: 60
            metric (`int`): Metric of routing protocol
            check_interval (`int`): Check interval, default: 10
            extensive ('bool'): Is extensive
            exact ('bool'): Is exact
        Returns:
            True / False
        Raises:
            None

    """
    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        out = None
        try:
            if extensive:
                if exact:
                    out = device.parse(
                        'show route extensive {destination_address} exact'.
                        format(destination_address=destination_address))
                else:
                    out = device.parse(
                        'show route extensive {destination_address}'.format(
                            destination_address=destination_address))
            elif protocol:
                out = device.parse(
                    'show route protocol {protocol}'.format(protocol=protocol))
            else:
                out = device.parse('show route')

        except SchemaEmptyParserError:
            timeout.sleep()
            continue
        rt_list = Dq(out).get_values("rt")

        for rt_dict in rt_list:
            rt_destination_ = Dq(rt_dict).get_values("rt-destination", 0)
            
            if not rt_destination_.startswith(str(destination_address)):
                continue
            
            if metric:
                destination_metric = Dq(rt_dict).get_values("metric", [0])
                if destination_metric != str(metric):
                    continue

            if known_via:
                via_ = Dq(rt_dict).get_values("via", 0)
                if not via_.startswith(known_via):
                    continue
            
            return True
        timeout.sleep()

    return False


def verify_default_route_protocol(device,
                                  route,
                                  ip_type='ipv4',
                                  inet_type='inet.0',
                                  expect_output=True,
                                  max_time=60,
                                  check_interval=10,
                                  subnet_mask_number=True,
                                  protocol=None):
    """ Verifies if route is displayed in output of show route command

        Args:
            device ('obj'): device to use
            route ('str'): ipv4/ipv6 default route
            ip_type ('str'): Either ipv4/ipv6
            inet_type ('str'): type of ip
            expect_output ('bool'): Flag, either expecting output or no output
            max_time ('int'): Maximum time to keep checking
            check_interval ('int'): How often to check
            subnet_mask_number ('bool'): Flag, to include/exclude subnet masknumber in comparison
            protocol ('str'): Type of protocol (ex.ospf,ospf3,ect)

        Returns:
            True/False

        Raises:
            N/A
    """
    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            if protocol:
                output = device.parse(
                    'show route protocol {}'.format(protocol))
            else:
                output = device.parse('show route extensive')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue
        route_tables = output.q.get_values('route-table')
        
        for routes in route_tables:

            #'table-name': 'inet.0'
            table_name = routes.get('table-name', [])

            if Dq(routes).contains('table-name').contains(inet_type):
                route_values = Dq(routes).contains('rt').get_values(
                    'rt-destination')
                for element in route_values:
                    route_value = element if subnet_mask_number else element.split(
                        '/')[0]
                    if route_value == route:
                        if expect_output:
                            return True
                        else:
                            timeout.sleep()
                            continue

        timeout.sleep()

    return False

def verify_route_advertised_protocol_community(device,
                                               route,
                                               community_list,
                                               ip_address,
                                               protocol,
                                               protocol_type,
                                               invert=False,
                                               max_time=60,
                                               check_interval=10                      
                                              ):
    """Verify community has the given community_list against criteria

        Args:
            device ('obj'): Device object
            route ('str'): Target route to check
            community_list ('list(str)'): List of communities to verify
            ip_address ('str'): IP address to check
            protocol ('str'): Protocol name that passed in command
            protocol_type ('str'): Protocol type in show command, e.g., advertising-protocol or receive-protocol
            invert(bool, optional): Inverts from equals to not equals. Defaults to False.
            max_time ('int', optional): Maximum time to keep checking, default 60 seconds
            check_interval ('int', optional): How often to check, default 10 seconds

        Returns:
            True/False

        Raises:
            N/A 
    """
    op = operator.eq
    if invert:
        op = operator.ne
    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            output = device.parse(
                "show route {protocol_type}-protocol {protocol} {ip_address} {route} detail".format(
                    protocol=protocol,
                    protocol_type=protocol_type,
                    ip_address=ip_address,
                    route=route
                ))
        
        except SchemaEmptyParserError:
            timeout.sleep()
            continue
        
        for rt_table_entry in output.q.get_values('route-table'):
            
            rt_entry = rt_table_entry.get('rt-entry')
            
            if rt_entry:
                
                # Check communities
                if op(rt_entry.get('communities').split(), community_list):
                    return True
            
        timeout.sleep()
        
    return False

def verify_routing_route(device,
                         route,
                         expected_protocol_name=None,
                         expected_community=None,
                         extensive=True,
                         max_time=60,
                         check_interval=10,
                         expected_table_name=None,
                         expected_active_tag='*',
                         expected_tag=None,
                         expected_protocol_nexthop=None,
                         expected_load_balance_label=None,
                         invert=False):
    """Verify show route exists against critera

    Args:
        route ('str'): Route to check
        expected_protocol_name ('str'): Expected protol in route
        expected_community ('str'): Expected community in route
        extensive ('bool): Whether to use extensive or not
        expected_table_name ('str'): Table name to check for
        expected_active_tag ('str'): Route table active tag to check, default: '*'
        expected_tag ('str'): Route table tag to check for
        invert (bool, optional): Inverts from equals to not equals. Defaults to False.

    Raise: None

    Returns: Boolean

    """
    op = operator.eq
    if invert:
        op = operator.ne
    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        out = None

        try:
            if extensive:
                out = device.parse(
                    "show route {route} extensive".format(route=route))
            else:
                out = device.parse("show route {route}".format(route=route))

        except SchemaEmptyParserError:
            timeout.sleep()
            continue
        
        for table_entry in out.q.get_values('route-table'):
            
            if expected_table_name:
                    table_name_ = table_entry.get('table-name')
                    if table_name_ != expected_table_name:
                        timeout.sleep()
                        continue                

            for rt in table_entry.get('rt', []):

                # Check values. If value is wrong then skip

                if expected_protocol_name and rt.get("rt-entry", {}).get(
                        "protocol-name", None) != expected_protocol_name:
                    continue
                
                if expected_active_tag:
                    a_tags_ = Dq(rt).get_values('active-tag')
                    if str(expected_active_tag) not in a_tags_:
                        continue
                
                if expected_community:
                    
                    # Put all communities into a string for regex to match
                    community_str = " ".join(expected_community)
                    
                    regexp = re.compile('Communities: +{community}'.format(
                        community=community_str))
                    if op(not regexp.search(rt.get('tsi', {}).get("#text", None)), True):
                        continue
    
                if expected_tag:
                    tags_ = Dq(rt).get_values('rt-tag')
                    if str(expected_tag) not in tags_:
                        continue
                
                if expected_protocol_nexthop:
                    result = False
                    for protocol_nh_dict in Dq(rt).get_values('protocol-nh'):
                        protocol_nexthop_ = protocol_nh_dict.get('to', None)
                        if protocol_nexthop_ == expected_protocol_nexthop:
                            result = True
                            break
                    if not result:
                        continue
                
                if expected_load_balance_label:
                    load_balance_label_ = Dq(rt).get_values('load-balance-label', 0)
                    if expected_load_balance_label not in load_balance_label_:
                        continue


                return True
            
            timeout.sleep()

    return False

def verify_routing_routes(device,
                          addr_list,
                          protocol,
                          contains,
                          max_time=60,
                          check_interval=10):
    """Verifies address list agianst 'show route protocol {protocol}'

    Args:
        addr_list('list'): List to verify
        protocol ('str'): Protocol type to check in show route
        contains ('boolean'): flag to check if addr_list is contained/excluded
        max_time ('int'): Maximum time to keep checking
        check_interval ('int'): How often to check

    Returns:
        True/False

    Raises:
        N/A
    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            output = device.parse(
                "show route protocol {protocol}".format(protocol=protocol))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        active_list = []

        for table_entry in output.q.get_values('route-table'):
            for route in table_entry.get('rt', []):
                active_list.append(route.get('rt-destination', None))

        timeout.sleep()

        if contains == True:
            if set(active_list).issuperset(set(addr_list)):
                return True
            else:
                continue
        else:
            if len(set(active_list).intersection(set(addr_list))) > 0:
                return False
            else:
                continue

    if contains:
        return False
    else:
        return True

                            
def _search_table_for_metric(op, **kwargs):
    route_tables = Dq(kwargs['output']).get_values('route-table')

    for route_table in route_tables:
        for rt in Dq(route_table).get_values('rt'):

            destination_address_ = Dq(rt).get_values('rt-destination', 0)
            if kwargs['address_exceptions'] and destination_address_ in kwargs['address_exceptions']:
                continue

            metric_ = Dq(rt).get_values('metric', 0)

            if op(int(metric_), int(kwargs['metric'])):
                return False
    return True


def verify_routing_no_ospf_metric_match(device, 
                                        metric, 
                                        address_exceptions=None,
                                        max_time=60, 
                                        check_interval=10):
    """Verify that no OSPF routes have given metric

    Args:
        device (obj): Device object
        metric (int): Metric to check for
        address_exceptions (list, optional): List of addresses to not check. Defaults to None.
        max_time (int, optional): Maximum timeout time. Defaults to 60.
        check_interval (int, optional): Check interval. Defaults to 10.
    """
    

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            output = device.parse(
                "show route protocol ospf")
        except SchemaEmptyParserError:
            timeout.sleep()
            continue
    
        if _search_table_for_metric(operator.eq, **locals()):
            return True
        else:
            timeout.sleep()
            continue
    return False


def verify_routing_ospf_metric_match_or_greater(device, 
                                        metric, 
                                        address_exceptions=None,
                                        max_time=60, 
                                        check_interval=10):
    """Verify that all OSPF routes have given metric

    Args:
        device (obj): Device object
        metric (int): Metric to check for
        address_exceptions (list, optional): List of addresses to not check. Defaults to None.
        max_time (int, optional): Maximum timeout time. Defaults to 60.
        check_interval (int, optional): Check interval. Defaults to 10.
    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            output = device.parse(
                "show route protocol ospf")
        except SchemaEmptyParserError:
            timeout.sleep()
            continue
    
        if _search_table_for_metric(operator.lt, **locals()):
            return True
        else:
            timeout.sleep()
            continue
    return False


def verify_metric_in_route(device, address, expected_metric, table_name, 
                          max_time=60,
                          check_interval=10):
    """Verify metric in 'show route {address}' when given table_name

        Args:
            device ('obj'): Device to use
            address ('str'): IP address in show command
            expected_metric ('int'): Expected metric number
            table_name ('str'): Table name. E.g. "inet.3".
            max_time ('int', optional): Maximum time to keep checking. Default to 60.
            check_interval ('int', optional): How often to check. Default to 10.

        Returns:
            True/False

        Raises:
            N/A
    """  

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:

            out = device.parse("show route {address}".format(address=address))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue
        
        # Sample output  
        #  {'route-information': {'route-table': [{'active-route-count': '8',
        #                                         'destination-count': '8',
        #                                         'hidden-route-count': '0',
        #                                         'holddown-route-count': '0',
        #                                         'rt': [{'rt-destination': '106.187.14.240/32',
        #                                                 'rt-entry': {'active-tag': '*',
        #                                                             'age': {'#text': '00:07:19'},
        #                                                             'metric': '1',  <-------------------------- 
        #                                                             'nh': [{'to': '106.187.14.157',
        #                                                                     'via': 'ge-0/0/0.0'}],
        #                                                             'preference': '10',
        #                                                             'protocol-name': 'OSPF'}}],
        #                                         'table-name': 'inet.0', <--------------------------
        #                                         'total-route-count': '8'},
        #                                     {'active-route-count': '1',
        #                                         'destination-count': '1',
        #                                         'hidden-route-count': '0',
        #                                         'holddown-route-count': '0',
        #                                         'rt': [{'rt-destination': '106.187.14.240/32',
        #                                                 'rt-entry': {'active-tag': '*',
        #                                                             'age': {'#text': '00:07:19'},
        #                                                             'metric': '1',  <--------------------------
        #                                                             'nh': [{'to': '106.187.14.157',
        #                                                                     'via': 'ge-0/0/0.0'}],
        #                                                             'preference': '9',
        #                                                             'protocol-name': 'LDP'}}],
        #                                         'table-name': 'inet.3', <--------------------------
        #                                         'total-route-count': '1'}]}}

        # Filter the outputs:
        # Input:        out.q.contains('metric|inet.3', regex=True).reconstruct()
        # Output:       {'route-information': {'route-table': [{'rt': [{'rt-entry': {'metric': '1'}}]},
        #                                                      {'rt': [{'rt-entry': {'metric': '1'}}],
        #                                                                    'table-name': 'inet.3'}
        #                                                     ]}}
        filtered_output = out.q.contains('metric|{table_name}'.format(table_name=table_name), regex=True).reconstruct()

        rt_list = filtered_output['route-information']['route-table']

        for rt in rt_list:
            if 'table-name' in rt and rt['table-name'] == table_name:
                if expected_metric == int(Dq(rt).get_values('metric', 0)):
                    return True

        timeout.sleep()
    return False 


def verify_specific_route(device,
                          address,
                          learn_protocol,
                          max_time=60,
                          check_interval=10):
    """Verifies address list agianst 'show route protocol {protocol}'

    Args:
        device ('obj'): device to use
        address('str'): address to search for
        learn_protocol('str'): Learned protocol
        max_time ('int'): Maximum time to keep checking
        check_interval ('int'): How often to check

    Returns:
        True/False

    Raises:
        N/A
    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            output = device.parse(
                "show route {address}".format(address=address))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue
        
        #   [{'rt-entry': {'active-tag': '*', 'protocol-name': 'OSPF', 
        #   'preference': '10', 'metric': '1', 'age': {'#text': '00:00:01'}, 
        #   'nh': [{'to': '106.187.14.158', 'via': 'ge-0/0/0.0'}]}, 
        #   'rt-destination': '59.128.2.250/32'}]
        rt_destination_ = Dq(output).get_values("rt-destination", 0)

        #   [{'rt-entry': {'active-tag': '*', 'protocol-name': 'OSPF', 
        #   'preference': '10', 'metric': '1', 'age': {'#text': '00:00:01'}
        protocol_name = Dq(output).get_values("protocol-name", 0)

        if protocol_name:
            if rt_destination_.startswith(str(address)) and \
                protocol_name.lower() ==  learn_protocol.lower():
                return True
            else:
                timeout.sleep()
                continue
                
        timeout.sleep()

    return False


def is_push_present_in_route(device, address, table_name,
                           max_time=60,
                           check_interval=10):
    """Check if Push is presnt in 'show route {address}' when given table_name

        Args:
            device ('obj'): Device to use
            address ('str'): IP address in show command
            table_name ('str'): Table name. E.g. "inet.3".
            max_time ('int', optional): Maximum time to keep checking. Default to 60.
            check_interval ('int', optional): How often to check. Default to 10.

        Returns:
            True/False

        Raises:
            N/A
    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            out = device.parse("show route {address}".format(address=address))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # Example output
        # {
        #     "route-information": {
        #         "route-table": [{
        #                 "rt": [{
        #                         "rt-entry": {
        #                             "nh": [{
        #                                     "mpls-label": "Push 118420",
        #                                 }]}}],
        #                 "table-name": "inet.3",
        #             }]}}

        rt_list = out.q.contains('nh|{table_name}'.format(
            table_name=table_name), regex=True).get_values('route-table')

        for rt in rt_list:
            if rt.get('table-name') == table_name and Dq(rt).get_values(
                    'mpls-label', None):
                    return True

        timeout.sleep()
    return False


def verify_route_is_advertised_or_received(
        device,
        protocol,
        protocol_type,
        address,
        expected_route,
        max_time=60,
        check_interval=10,
):
    """ Verify the route is advertised

        Args:
            device ('obj'): Device object
            protocol ('str'): Protocol name that passed in command
            protocol_type ('str'): Protocol type in show command, e.g., advertising-protocol or receive-protocol
            expected_route ('str'): Expected route
            address ('str'): IP address
            max_time ('int', optional): Maximum time to keep checking. Default to 60
            check_interval ('int', optional): How often to check. Default to 10.     

        Returns:
            True/False
        Raises:
            None

    """
    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            out = device.parse(
                "show route {protocol_type}-protocol {protocol} {address}".format(
                    protocol_type=protocol_type,
                    protocol=protocol,
                    address=address)) 
                
        except SchemaEmptyParserError:
            timeout.sleep()
            continue                    

        # {
        #         'route-information': {
        #             'route-table': {
        #                 'active-route-count':
        #                 '10',
        #                 'destination-count':
        #                 '10',
        #                 'hidden-route-count':
        #                 '0',
        #                 'holddown-route-count':
        #                 '0',
        #                 'rt': [{
        #                     'rt-destination': '0.0.0.0/0',
        #                     'rt-entry': {
        #                         'active-tag': '*',

        rt_list = out.q.get_values('rt')
        destinations = [i.get('rt-destination') for i in rt_list]

        if expected_route in destinations:
            return True 
        
        timeout.sleep()

    return False                       

def verify_route_forwarding_type(device, label, expected_type, max_time=60, check_interval=10):
    """ Verifies route-forwarding type given a label

    Args:
        device (obj): Device object
        label (str): Label to check
        expected_type (str): Expected type
        max_time (int, optional): Maximum sleep time. Defaults to 60.
        check_interval (int, optional): Check interval. Defaults to 10.

    Returns:
        str or None: mpls out label
    """

    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        try:
            out = device.parse('show route forwarding-table label {label}'.format(
                label=label
            ))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # Example dictionary
        # {
        #     "forwarding-table-information":{
        #         "route-table": [{
        #                 "rt-entry": [{
        #                         "nh":{
        #                             "nh-type": str,
        #                         }
        #                     }]
        #             }]
        #     }
        # }

        types_ = out.q.get_values('nh-type')
        for type_ in types_:
            if expected_type in type_:
                return True
        
        timeout.sleep()

    return False

def verify_source_of_best_path(device,
                         target_route,
                         expected_best_path,
                         max_time=60,
                         check_interval=10):
    """Verify the source of the best path

    Args:
        target_route ('str'): Route to check
        expected_best_path ('str'): Best path address
        max_time ('int', optional): Maximum time to keep checking. Default to 60.
        check_interval ('int', optional): How often to check. Default to 10.

    Raise: None

    Returns: Boolean

    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        out = None

        try:
            out = device.parse(
                "show route {route} extensive".format(route=target_route))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # Sample output
        # "route-information": {
        #     "route-table": [
        #         {"rt": [
        #                 {"rt-entry": [{
        #                     "active-tag": "*",
        #                     "gateway": "4.4.4.4",
        #                 }]

        for rt in out.q.get_values('rt'):
            if isinstance(rt.get("rt-entry"), list):
                for rt_entry_elem in rt.get("rt-entry", []):
                    if rt_entry_elem.get('active-tag') and rt_entry_elem.get(
                            'gateway') == expected_best_path:
                            return True

            elif rt.get("rt-entry", {}).get(
                    "gateway", None) == expected_best_path:
                return True

            timeout.sleep()

    return False

def verify_cluster_list_length_of_path(device,
                         target_route,
                         cluster_list_length,
                         best_route=True,
                         max_time=60,
                         check_interval=10):
    """Verify length of cluster list of path (best or non-best)

    Args:
        target_route ('str'): Route to check
        cluster_list_length ('int'): Length of cluster list
        best_route ('bool'): Whether to use best or non-best path
        max_time ('int', optional): Maximum time to keep checking. Default to 60.
        check_interval ('int', optional): How often to check. Default to 10.

    Raise: None

    Returns: Boolean

    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        out = None

        try:
            out = device.parse(
                "show route {route} extensive".format(route=target_route))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # Sample output
        # "route-information": {
        #     "route-table": [
        #         {"rt": [
        #                 {"rt-entry": [{
        #                     "active-tag": "*",
        #                     "cluster-list": "4.4.4.4",
        #                 },
        #                 {
        #                     "inactive-reason": "IGP metric",
        #                     "cluster-list": "2.2.2.2 4.4.4.4",
        #                 }]

        for rt in out.q.get_values('rt'):
            if isinstance(rt.get("rt-entry"), list):
                for rt_entry_elem in rt.get("rt-entry", []):
                    if best_route:
                        if rt_entry_elem.get('active-tag'):
                            if len(rt_entry_elem.get('cluster-list', '').split()) == \
                                    cluster_list_length:
                                return True
                    else:
                        if rt_entry_elem.get('inactive-reason'):
                            if len(rt_entry_elem.get('cluster-list', '').split()) == \
                                    cluster_list_length:
                                return True
            elif len(rt.get("rt-entry", {}).get("cluster-list", '').split()) == \
                    cluster_list_length:
                return True

            timeout.sleep()

    return False


def verify_route_table_label(device,
                             label=None,
                             php_label=None,
                             max_time=60,
                             check_interval=10):
    """ Verify the out label

        Args:
            device (`obj`): Device object
            label (`str`): show route label. Defaults to None.
            php_label (`str`): php label. Defaults to None.
            max_time ('int', optional): Maximum time to keep checking. Default to 60 seconds.
            check_interval ('int', optional): How often to check. Default to 10 seconds.
        Returns:
            result (`bool`): Verified result
        Raises:
            N/A
    """

    timeout = Timeout(max_time, check_interval)
    while timeout.iterate():
        try:
            out = device.parse('show route table mpls.0 label {label}'.format(
                label=label))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue
        
        # "next_hop_list": {
        #                     1: {
        #                         "to": "10.19.198.66",
        #                         "via": "ge-0/0/3.0",
        #                         "best_route": ">",
        #                         "mpls_label": "Swap 78",
        #                     }
        mpls_value = Dq(out).contains(label).get_values('mpls_label',0)
        if mpls_value == php_label:
            return True

        timeout.sleep()


    return False


def verify_learned_protocol(device,
                            address,
                            next_hop=None,
                            learn_protocol=None,
                            max_time=60,
                            check_interval=10):
    """Verifies learned protocol and next hop agianst 'show route {address} extensive'

    Args:
        device ('obj'): device to use
        address ('str'): IP address for show command
        next_hop ('str'): next hop ip address
        learn_protocol('str'): Learned protocol
        max_time ('int', optional): Maximum time to keep checking. Default to 60 seconds.
        check_interval ('int', optional): How often to check. Default to 10 seconds.

    Returns:
        True/False

    Raises:
        N/A
    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            output = device.parse(
                "show route {address} extensive".format(address=address))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        #   [{'rt-entry': {'active-tag': '*', 'protocol-name': 'OSPF', 
        #   'preference': '10', 'metric': '1', 'age': {'#text': '00:00:01'}, 
        #   'nh': [{'to': '106.187.14.158', 'via': 'ge-0/0/0.0'}]}, 
        #   'rt-destination': '59.128.2.250/32'}]
        if next_hop:
            protocol_next_hop = Dq(output).contains("protocol-nh").get_values("to")
            if next_hop in protocol_next_hop:
                return True
            else:
                timeout.sleep()
                continue

        #   [{'rt-entry': {'active-tag': '*', 'protocol-name': 'OSPF', 
        #   'preference': '10', 'metric': '1', 'age': {'#text': '00:00:01'}
        if learn_protocol:
            protocol_name = Dq(output).get_values("protocol-name", 0)
            if protocol_name.lower() ==  learn_protocol.lower():
                return True
            else:
                timeout.sleep()
                continue
                
        timeout.sleep()

    return False


def verify_push_present_in_show_route(device, 
                                      address, 
                                      push_value,
                                      max_time=60,
                                      check_interval=10):
    """Verify if Push value is present in 'show route {address} extensive'

        Args:
            device ('obj'): Device to use
            address ('str'): IP address for show command
            push_value ('str'): Push value in show route {address} extensive command
            max_time ('int', optional): Maximum time to keep checking. Default to 60 seconds.
            check_interval ('int', optional): How often to check. Default to 10 seconds.

        Returns:
            True/False

        Raises:
            N/A
    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            out = device.parse("show route {address} extensive".format(address=address))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # Example output
        # {
        #     "route-information": {
        #         "route-table": [{
        #                 "rt": [{
        #                         "rt-entry": {
        #                             "nh": [{
        #                                     "mpls-label": "Push 118420",
        #                                 }]}}],
        #                 "table-name": "inet.3",
        #             }]}}

        rt_list = Dq(out).get_values("route-table")

        for rt in rt_list:
            if str(push_value) == str(Dq(rt).get_values('mpls-label', 0).split()[1]):
                return True
            
        timeout.sleep()
    return False


def verify_route_best_path(device,
                         target_route,
                         ip_address=None,
                         preference=None,
                         active_tag='*',
                         interface=None,
                         extensive=False,
                         expected_to=None,
                         expected_med=None,
                         max_time=60, 
                         check_interval=10
                        ):
    """ Verify Best path is toward $ip_address or with preference $preference

        Args:
            device (`obj`): Device object
            target_route (`str`): Target route to check
            ip_address (`str`): IP Address to verify is best path, default: None
            preference (`int`): Preference of best path, default: None
            active_tag (`str`, optional): Active tag to check, default: '*' (best path)
            interface (`str`, optional): IP address in show command. Defaults to None. 
            extensive (`bool`, optional): 'extensive' added in the show command. Defaults to None.
            expected_to (`str`, optional): Expected address that be towarded to. Defaults to None.
            expected_med (`str`, optional): Expected med that be towarded to. Defaults to None.
            max_time (`int`, optional): Max time, default: 60 seconds
            check_interval (`int`, optional): Check interval, default: 10 seconds
        
        Returns:
            result (`bool`): Verified result
        
        Raises:
            N/A 
    """    
    timeout = Timeout(max_time, check_interval)
    
    preference = str(preference)
    
    while timeout.iterate():
        try:
            if interface and extensive:
                output = device.parse('show route protocol bgp {interface} extensive'.format(interface=interface))
            else:
                output = device.parse('show route protocol bgp')
            
        except SchemaEmptyParserError:
            log.info('Failed to parse. Device output might contain nothing.')
            timeout.sleep()
            continue
        
        # schema = {
        #     "route-information": {
        #         "route-table": [
        #             {
        #                   ...
        #                 "rt": [
        #                     {
        #                         "rt-destination": str,
        #                         "rt-entry": {
        #                             "active-tag": str,
        #                             "age": {
        #                                 "#text": str,
        #                             },
        #                                   ...
        #                             "preference": str,
        #                              ...
        #                         }
        #                     }
        #                 ],
        #                 ...
        #             }
        #         ]
        #     }
        # }
        
        route_tables = output.q.get_values('route-table')
        
        for routes in route_tables:
            rt_list = routes.get('rt')
            
            if rt_list:
                for rt in rt_list:
                    rt_entry = rt.get('rt-entry')

                    # show route protocol bgp {interface} extensive

                    #  'rt-entry': {'active-tag': '*',
                    #     'announce-bits': '2',
                    #     'announce-tasks': '0-KRT 5-Resolve tree 1',
                    #     'gateway': '2.2.2.2',
                    #     'nh': [{'nh-string': 'Next hop',
                    #             'session': '45a',
                    #             'to': '20.0.0.2',
                    #             'via': 'ge-0/0/0.0'}],
                    if interface and extensive:
                        if type(rt_entry) == dict:
                            nh_list = rt_entry.get('nh')
                            for nh in nh_list:
                                if nh.get('via') == target_route:
                                    return True 
                        elif type(rt_entry) == list:
                            for r in rt_entry:
                                nh_list = r.get('nh')
                                for nh in nh_list:
                                    if nh.get('via') == target_route:
                                        return True 

                    # Check route and make sure is a best path ('*')
                    if (
                        rt.get('rt-destination') == target_route     
                        and rt_entry.get('active-tag') == active_tag
                    ):  
                        # Verify the best path towards to {expected_to}
                        if expected_to:
                            if type(rt_entry) == dict:
                                nh_list = rt_entry.get('nh')
                                for nh in nh_list:
                                    if nh.get('to') == expected_to.split('/')[0]:
                                        return True 
                            elif type(rt_entry) == list:
                                for r in rt_entry:
                                    nh_list = r.get('nh')
                                    for nh in nh_list:
                                        if nh.get('to') == expected_to.split('/')[0]:
                                            return True 

                        # Verify best path IP address or Preference to best path
                        if (
                            rt_entry.get('learned-from') == ip_address
                            or rt_entry.get('local-preference') == preference
                            or rt_entry.get('med') == expected_med
                        ):
                            return True
                    
        timeout.sleep()
    return False 


def verify_route_best_path_metric(device,
                         expected_metric,
                         ip_address,
                         metric2=False,
                         max_time=60, 
                         check_interval=10
                        ):
    """ Verify the metric of best path

        Args:
            device (`obj`): Device object
            expected_metric (`int`): Expected metric number 
            ip_address (`str`): IP address in show command. 
            metric2(`bool`, optional): Flag used to distinguish 'metric' and 'metric2', default: False
            max_time (`int`, optional): Max time, default: 60 seconds
            check_interval (`int`, optional): Check interval, default: 10 seconds
        
        Returns:
            result (`bool`): Verified result
        
        Raises:
            N/A 
    """    
    timeout = Timeout(max_time, check_interval)
        
    while timeout.iterate():
        try:
            output = device.parse('show route protocol bgp {ip_address} extensive'.format(ip_address=ip_address))

        except SchemaEmptyParserError:
            log.info('Failed to parse. Device output might contain nothing.')
            timeout.sleep()
            continue
        
        # schema = {
        #     "route-information": {
        #         "route-table": [
        #             {
        #                   ...
        #                 "rt": [
        #                     {
        #                         "rt-destination": str,
        #                         "rt-entry": {
        #                             "protocol-nh": [
        #                              {'metric': int}
        #                              ]
        #                                   ...
        #                             "preference": str,
        #                             "metric":1,
        #                             "metric2":11,
        #                              ...
        #                         }
        #                     }
        #                 ],
        #                 ...
        #             }
        #         ]
        #     }
        # }
        
        route_tables = output.q.get_values('route-table')
        metric_key = 'metric2' if metric2 else 'metric'
        for routes in route_tables:
            rt_list = routes.get('rt')
            
            if rt_list:
                for rt in rt_list:
                    rt_entry = rt.get('rt-entry')

                    if type(rt_entry) == dict:
                        metric = Dq(rt_entry).get_values(metric_key, 0)

                        if int(metric) == expected_metric:
                            return True 

                    elif type(rt_entry) == list:
                        for r in rt_entry:
                            metric = Dq(r).get_values(metric_key, 0)

                            if int(metric) == expected_metric:
                                return True

                    
        timeout.sleep()
    return False     


def verify_route_non_best_path_metric(device,
                         non_expected_metric,
                         ip_address,
                         metric2=False,
                         max_time=60, 
                         check_interval=10
                        ):
    """ Verify the metric of non best path

        Args:
            device (`obj`): Device object
            non_expected_metric (`int`): Not expected metric number 
            ip_address (`str`): IP address in show command. 
            metric2(`bool`, optional): Flag used to distinguish 'metric' and 'metric2', default: False
            max_time (`int`, optional): Max time, default: 60 seconds
            check_interval (`int`, optional): Check interval, default: 10 seconds
        
        Returns:
            result (`bool`): Verified result
        
        Raises:
            N/A 
    """    
    timeout = Timeout(max_time, check_interval)
        
    while timeout.iterate():
        try:
            output = device.parse('show route protocol bgp {ip_address} extensive'.format(ip_address=ip_address))

        except SchemaEmptyParserError:
            log.info('Failed to parse. Device output might contain nothing.')
            timeout.sleep()
            continue
        
        # schema = {
        #     "route-information": {
        #         "route-table": [
        #             {
        #                   ...
        #                 "rt": [
        #                     {
        #                         "rt-destination": str,
        #                         "rt-entry": {
        #                             "protocol-nh": [
        #                              {'metric': int}
        #                              ]
        #                                   ...
        #                             "preference": str,
        #                              ...
        #                         }
        #                     }
        #                 ],
        #                 ...
        #             }
        #         ]
        #     }
        # }
        
        route_tables = output.q.get_values('route-table')
        metric_key = 'metric2' if metric2 else 'metric'

        for routes in route_tables:
            rt_list = routes.get('rt')
            
            if rt_list:
                for rt in rt_list:
                    rt_entry = rt.get('rt-entry')

                    if type(rt_entry) == dict:
                        metric = Dq(rt_entry).get_values(metric_key, 0)

                        if int(metric) != non_expected_metric:
                            return True 

                    elif type(rt_entry) == list:
                        for r in rt_entry:
                            metric = Dq(r).get_values(metric_key, 0)

                            if int(metric) != non_expected_metric:
                                return True
                    
        timeout.sleep()
    return False 


def verify_route_has_no_output(device,
                         target_route,
                         max_time=60,
                         check_interval=10):
    """Verify route has no output

    Args:
        target_route ('str'): Route to check
        max_time ('int', optional): Maximum time to keep checking. Default to 60.
        check_interval ('int', optional): How often to check. Default to 10.

    Raise: None

    Returns: Boolean

    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        out = None

        try:
            device.parse(
                "show route {route} extensive".format(route=target_route))
        except SchemaEmptyParserError:
            return True
        timeout.sleep()
    return False


def verify_next_hop_in_route(device, route,
                           expected_next_hop,
                           protocol=None,
                           protocol_type=None,
                           max_time=60,
                           check_interval=10):
    """Verify next hop in route

        Args:
            device ('obj'): Device to use
            route ('str'): IP address in show command
            expected_next_hop ('str'): Next Hop address
            protocol ('str', optional): Protocol name that passed in command. Default to None.
            protocol_type ('str', optional): Protocol type in show command, e.g., advertising-protocol
                                             or receive-protocol. Default to None.
            max_time ('int', optional): Maximum time to keep checking. Default to 60.
            check_interval ('int', optional): How often to check. Default to 10.

        Returns:
            True/False

        Raises:
            N/A
    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            if protocol and protocol_type:
                out = device.parse(
                    "show route {protocol_type}-protocol {protocol} {address}".format(
                        protocol_type=protocol_type,
                        protocol=protocol,
                        address=route))
            else:
                out = device.parse("show route {address} extensive".format(address=route))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # Example output
        # {
        #     "route-information": {
        #         "route-table": [{
        #                 "rt": [{
        #                         "rt-entry": {
        #                             "nh": [{
        #                                     "to": "30.0.0.2",
        #                                 }]}}],
        #                 "table-name": "inet.3",
        #             }]}}

        rt_list = Dq(out).get_values("rt")

        for rt in rt_list:
            if expected_next_hop in Dq(rt).get_values('to'):
                return True

        timeout.sleep()
    return False


def verify_protocol_next_hop_in_route(device, route,
                           expected_protocol_next_hop,
                           max_time=60,
                           check_interval=10):
    """Verify protocol next hop in route

        Args:
            device ('obj'): Device to use
            route ('str'): IP address in show command
            expected_protocol_next_hop ('str'): Protocol next Hop address
            max_time ('int', optional): Maximum time to keep checking. Default to 60.
            check_interval ('int', optional): How often to check. Default to 10.

        Returns:
            True/False

        Raises:
            N/A
    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            out = device.parse("show route {address} extensive".format(address=route))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue
        
        # Example output
        # {
        #     "route-information": {
        #         "route-table": [{
        #                 "rt": [{
        #                         "rt-entry": [{
        #                                     "protocol-nh": [
        #                                         {
        #                                             "to": "1.1.1.1",
        #                                             "indirect-nh": "0xc298604 1048574 INH Session ID: 0x3c1"
        #                                         },
        #                                         {
        #                                             "to": "1.1.1.1",
        #                                             "metric": "5",
        #                                         }
        #                                     ]}

        rt_list = Dq(out).get_values("rt")

        for rt in rt_list:
            protocol_nh_list = Dq(rt).get_values('protocol-nh')
            for nh_dict in protocol_nh_list:
                if nh_dict.get('to') == expected_protocol_next_hop:
                    return True

        timeout.sleep()
    return False


def verify_route_flag(device,
                      target_route,
                      expected_flag,
                      active_tag='*',
                      max_time=60,
                      check_interval=10
                      ):
    """ Verify the IGP/EGP flag

        Args:
            device (`obj`): Device object
            target_route ('str'): Route to check
            expected_flag (`str`): Expected IGP flag
            active_tag (`str`): Flag for 'best path'. Defaults to '*'.
            max_time (`int`, optional): Max time, default: 60 seconds
            check_interval (`int`, optional): Check interval, default: 10 seconds

        Returns:
            result (`bool`): Verified result

        Raises:
            N/A
    """
    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            output = device.parse('show route protocol bgp')

        except SchemaEmptyParserError:
            log.info('Failed to parse. Device output might contain nothing.')
            timeout.sleep()
            continue

        # schema = {
        #     "route-information": {
        #         "route-table": [
        #             {
        #                   ...
        #                 "rt": [
        #                     {
        #                         "rt-destination": str,
        #                         "rt-entry": {
        #                                   ...
        #                                   "as-path" : " (12345) I"
        #                              ...
        #                         }
        #                     }
        #                 ],
        #                 ...
        #             }
        #         ]
        #     }
        # }

        route_tables = output.q.get_values('route-table')
        as_path_with_flag = re.compile(r'.*{expected_flag}.*'.format(expected_flag=expected_flag))
        rt_destination = ''

        for routes in route_tables:
            rt_list = routes.get('rt')

            if rt_list:
                for rt in rt_list:
                    if rt.get('rt-destination'):
                        rt_destination = rt.get('rt-destination')

                    # Verify there is {target_route}
                    if rt_destination == target_route:

                        rt_entry = rt.get('rt-entry')

                        # Verify this is best path
                        if rt_entry.get('active-tag') == active_tag:
                            if type(rt_entry) == dict:

                                # Obtain the value of key 'as-path'
                                as_path = Dq(rt_entry).get_values('as-path', 0)

                                # Sample output: AS path: 3 4 I, validation-state: unverified
                                # where flag is 'I'
                                if as_path_with_flag.match(as_path):
                                    return True

                            elif type(rt_entry) == list:
                                for r in rt_entry:

                                    as_path = Dq(r).get_values('as-path', 0)

                                    if as_path_with_flag.match(as_path):
                                        return True

                        # Verify flags in other paths
                        elif (not active_tag):
                            if type(rt_entry) == dict:

                                # Obtain the value of key 'as-path'
                                as_path = Dq(rt_entry).get_values('as-path', 0)

                                # Sample output: AS path: 3 4 E, validation-state: unverified
                                # where flag is 'E'
                                if as_path_with_flag.match(as_path):
                                    return True

                            elif type(rt_entry) == list:
                                for r in rt_entry:

                                    as_path = Dq(r).get_values('as-path', 0)

                                    if as_path_with_flag.match(as_path):
                                        return True

        timeout.sleep()
    return False


def verify_route_table_mpls_label(device,
                                  table,
                                  label,
                                  expected_mpls_label,
                                  max_time=60,
                                  check_interval=10):
    """Verifies mpls label based on table name

    Args:
        device ('str'): Device object
        table ('str'): Table name
        label ('bool'): label for show command
        expected_mpls_label('str'): Expected MPLS label
        max_time ('int', optional): Maximum time to keep checking. Default to 60 seconds.
        check_interval ('int', optional): How often to check. Default to 10 seconds.

    Raise: None

    Returns: Boolean

    """

    timeout = Timeout(max_time, check_interval)
    # Dictionary
    # 'table_name': {
    #         'inet.3': {
    #             'active_route_count': 3,
    #             'destination_count': 3,
    #             'hidden_route_count': 0,
    #             'holddown_route_count': 0,
    #             'routes': {
    #                 '10.169.197.254/32': {
    #                     'active_tag': '*',
    #                     'age': '02:14:05',
    #                     'metric': '1001',
    #                     'next_hop': {
    #                         'next_hop_list': {
    #                             1: {
    #                                 'best_route': '>',
    #                                 'to': '10.49.0.1',
    #                                 'via': 'ge-0/0/2.0'
    #                             }
    #                         }
    #                     },
    #                     'preference': '9',
    #                     'protocol_name': 'LDP'
    #                 },
    #                 '192.168.36.220/32': {
    #                     'active_tag': '*',
    #                     'age': '02:03:22',
    #                     'metric': '1111',
    #                     'next_hop': {
    #                         'next_hop_list': {
    #                             1: {
    #                                 'best_route': '>',
    #                                 'mpls_label': 'Push 307742',
    #                                 'to': '192.168.220.6',
    #                                 'via': 'ge-0/0/1.0'
    #                             }
    #                         }
    #                     },
    while timeout.iterate():
        out = None

        try:
            out = device.parse(
                "show route table {table} label {label}".format(
                    table=table,
                    label=label))
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        mpls_label = out.q.contains(table).get_values('mpls_label', 0)
        if expected_mpls_label in mpls_label:
            return True

        timeout.sleep()

    return False

def _checkAsPath(rt_entry, expected_as_length):
        if isinstance(rt_entry, dict):
            as_path = Dq(rt_entry).get_values('as-path')
            if as_path and int(len(as_path[0].split())) - 1 == expected_as_length:
                return True

        elif isinstance(rt_entry, list):
            for elem in rt_entry:
                as_path = Dq(elem).get_values('as-path')
                if as_path and int(len(as_path[0].split())) == expected_as_length:
                    return True
        return False

def verify_route_as_length(device,
                          route,
                          expected_bestpath_as_length,
                          expected_nonbestpath_as_length=None,
                          max_time=60,
                          check_interval=10
                          ):
    """ Verify the length as-path of best path and non best path

        Args:
            device (`obj`): Device object
            route('str'): Target route address
            expected_bestpath_as_length (`int`): Expected best path as length
            expected_nonbestpath_as_length (`int`): Expected non best path as length, default: None
            max_time (`int`, optional): Max time, default: 60 seconds
            check_interval (`int`, optional): Check interval, default: 10 seconds

        Returns:
            result (`bool`): Verified result

        Raises:
            N/A
    """
    timeout = Timeout(max_time, check_interval)
    is_as_path_matched = False

    while timeout.iterate():
        try:
            output = device.parse('show route protocol bgp')
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # schema = {
        #     "route-information": {
        #         "route-table": [
        #             {
        #                   ...
        #                 "rt": [
        #                     {
        #                         "rt-destination": str,
        #                         "rt-entry": {
        #                             "as-path": "4 2 I"
        #                              ...

        for rt in output.q.get_values('rt'):
            rt_entry = rt.get('rt-entry', {})
            rt_destination = rt.get('rt-destination', '')

            # Check as length of best path only
            if not expected_nonbestpath_as_length:
                if rt_destination == route:
                    return _checkAsPath(rt_entry, expected_bestpath_as_length)

            # Check as length of best path and non best path
            else:
                if rt_destination == route:
                    if not _checkAsPath(rt_entry, expected_bestpath_as_length):
                        is_as_path_matched = False
                        break
                    else:
                        is_as_path_matched = True
                elif not rt_destination:
                    if not _checkAsPath(rt_entry, expected_nonbestpath_as_length):
                        is_as_path_matched = False
                        break
                    else:
                        is_as_path_matched = True

        if is_as_path_matched:
            return True

        timeout.sleep()
    return False

def verify_best_path_is_towards_to_interface(device, target_route,
                           ip_address,
                           max_time=60,
                           check_interval=10):
    """Verify best path towards to given interface

        Args:
            device ('obj'): Device to use
            target_route ('str'): target route address
            ip_address ('str'): expected interface address
            max_time ('int', optional): Maximum time to keep checking. Default to 60.
            check_interval ('int', optional): How often to check. Default to 10.

        Returns:
            True/False

        Raises:
            N/A
    """

    timeout = Timeout(max_time, check_interval)

    while timeout.iterate():
        try:
            out = device.parse("show route protocol bgp")
        except SchemaEmptyParserError:
            timeout.sleep()
            continue

        # Example output
        # {
        #     "route-information": {
        #         "route-table": [{
        #                 "rt": [{
        #                         "rt-entry": {
        #                             "nh": [{
        #                                     "to": "30.0.0.2",
        #                                 }]}}],
        #                 "table-name": "inet.3",
        #             }]}}

        rt_list = Dq(out).get_values("rt")
        for rt in rt_list:
            rt_destination = rt.get('rt-destination', '')
            if '/' in ip_address:
                ip_address = ip_address.split('/')[0]

            if rt_destination == target_route and ip_address in Dq(rt).get_values('to'):
                return True

        timeout.sleep()
    return False

