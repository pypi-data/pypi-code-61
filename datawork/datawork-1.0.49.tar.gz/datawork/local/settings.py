from station_codes import stations
from networktools.environment import get_env_variable
import multiprocessing

GUI_WORKERS = int(get_env_variable('GUI_WORKERS'))
GUI_STATIONS_BY_WORKER = int(get_env_variable('GUI_STATIONS_BY_WORKER'))

user = 'geodesia'
host = 'localhost'
#host = 'localhost'
gnsocket_port = 6677

nproc = multiprocessing.cpu_count()

SELECT_GROUP = int(get_env_variable('SELECT_GROUP'))

st_dict = dict([
    (0, ['TRPD',"CONZ"]),
    (1, ['AEDA', 'CHYT', 'CTPC', 'FMCO', 'JRGN', 'LSCH']),
    (2, ['MCLA', 'PATH', 'PAZU', 'PCCL', 'PFRJ', 'PVCA']),
    (3, ['QTAY', 'UDAT', 'UTAR', 'UAPE', 'QSCO', 'CGTC']),
    (4, ['QTAY', 'UDAT', 'UTAR', 'UAPE', 'QSCO', 'CGTC'])])

all_codes = stations

"""[
    'VALN',
    'HSCO',
    'QSCO',
    'FMCO',
    'PAZU',
    'JRGN',
    'PVCA',
    'CHYT',
    'UDAT',
    'NAVI',
    'PATH',
    'ATJN',
    'AEDA',
    'LSCH',
    'CCSN',
    'LLCH',
    'PCMU',
    'CRSC',
    'UAPE',
    'VLZL',
    'ZAPA',
    'QTAY',
    'PCCL',
    'PFRJ',
    'MCLA',
    'UTAR',
    'RCSD',
    'TRPD',
    'CGTC']
"""

#[all.extend(group) for group in st_dict.values()]

st_dict.update({"ALL": all_codes})

GROUP = st_dict.get(SELECT_GROUP, 0)
COLLECTOR_SOCKET_IP = get_env_variable('COLLECTOR_SOCKET_IP')
COLLECTOR_SOCKET_PORT = int(get_env_variable('COLLECTOR_SOCKET_PORT'))
print("Socket Port to ATLAS", COLLECTOR_SOCKET_IP, ":",COLLECTOR_SOCKET_PORT)
RDB_SOURCE_HOST = get_env_variable('RDB_SOURCE_HOST')
RDB_ENU_HOST = get_env_variable('RDB_ENU_HOST')
RDB_SOURCE = get_env_variable('RDB_SOURCE_PORT')
RDB_ENU = get_env_variable('RDB_ENU_PORT')
DATAWORK_SOCKET_IP = get_env_variable('DATAWORK_SOCKET_IP')
DATAWORK_SOCKET_PORT = int(get_env_variable('DATAWORK_SOCKET_PORT'))
