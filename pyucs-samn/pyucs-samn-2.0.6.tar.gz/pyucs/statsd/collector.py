
import logging
from multiprocessing.pool import Pool, MapResult, mapstar, starmapstar, RUN, CLOSE, TERMINATE
from multiprocessing import cpu_count
from pyucs.log.decorators import addClassLogger
from pyucs.statsd.portstats import EthPortStat, FcPortStat, EthPortChannelStat, FcPortChannelStat
from ucsmsdk import mometa
from ucsmsdk.mometa.storage.StorageItem import StorageItem
from ucsmsdk.mometa.vnic.VnicFc import VnicFc
from ucsmsdk.mometa.vnic.VnicEther import VnicEther
from ucsmsdk.mometa.ether.EtherPIo import EtherPIo
from ucsmsdk.mometa.fc.FcPIo import FcPIo
from ucsmsdk.mometa.fabric.FabricEthLanPc import FabricEthLanPc
from ucsmsdk.mometa.fabric.FabricFcSanPc import FabricFcSanPc
from ucsmsdk.mometa.sw.SwSystemStatsHist import SwSystemStatsHist


@addClassLogger
class CollectorProcessPool(Pool):
    """
        Strictly for debugging purposes. There is no other value here for this class.
    """

    def map(self, func, iterable, chunksize=None):
        return self._map_async(func, iterable, mapstar, chunksize).get()

    def _map_async(self, func, iterable, mapper, chunksize=None, callback=None,
            error_callback=None):
        '''
        Helper function to implement map, starmap and their async counterparts.
        '''
        if self._state != RUN:
            raise ValueError("Pool not running")
        if not hasattr(iterable, '__len__'):
            iterable = list(iterable)

        if chunksize is None:
            chunksize, extra = divmod(len(iterable), len(self._pool) * 4)
            if extra:
                chunksize += 1
        if len(iterable) == 0:
            chunksize = 0

        task_batches = Pool._get_tasks(func, iterable, chunksize)
        result = MapResult(self._cache, chunksize, len(iterable), callback,
                           error_callback=error_callback)
        self._taskqueue.put(
            (
                self._guarded_task_generation(result._job,
                                              mapper,
                                              task_batches),
                None
            )
        )
        return result


@addClassLogger
class StatsCollector:
    """
        This class is used as a statistics collector of specific devices for the UCS.
        The class as a whole is designed to be run as a separate process via the method
        query_stats. A multiprocessing queue is required in order to share data between
        the processes. There is no output or stored property with the results and is only
        accessible from the queue.get() method.
    """
    def __init__(self, ucs):
        self.ucs = ucs
        # self.ucs.clear_default_properties()
        self.query_results = []
        self.thread_results = None

    def query_stats(self, statsq):
        """
            This method is used to define the devices and multiprocess pool size.
            It also formulates the function arguments that will be passed on to
            the payload process _query_stats via the protected method _query_thread_pool_map
        :param statsq: processing queue
        :return: None ( data is stored into statsq )
        """
        self.__log.info('StatsCollector statsd started')
        # Define the number os parallel processes to run, typically the best results are cpu_count()
        # experiment with the sizing to determine the best number
        parallelism_thread_count = 1
        rawdata = []
        thread_pool_args = []
        thread = 1
        dict_data = {}

        try:
            tmp = None
            # vnic_stats_dns = []
            self.__log.info(f'{self.ucs}: Collecting all vnics')
            dict_data.update({VnicEther: self.ucs.get_vnic()})
            # rawdata = rawdata.append(tmp)
            self.__log.info(f'{self.ucs}: Found {len(dict_data[VnicEther])} vnics')

            tmp = None
            self.__log.info(f'{self.ucs}: Collecting all vhbas')
            dict_data.update({VnicFc: self.ucs.get_vhba()})
            # rawdata = rawdata.__add__(tmp)
            self.__log.info(f'{self.ucs}: Found {len(dict_data[VnicFc])} vhbas')

            tmp = None
            self.__log.info(f'{self.ucs}: Collecting all fabric ether ports')
            dict_data.update({EtherPIo: self.ucs.get_fabric_etherport()})
            # rawdata = rawdata.__add__(tmp)
            self.__log.info(f'{self.ucs}: Found {len(dict_data[EtherPIo])} fabric ether ports')

            tmp = None
            self.__log.info(f'{self.ucs}: Collecting all fabric FC ports')
            dict_data.update({FcPIo: self.ucs.get_fabric_fcport()})
            # rawdata = rawdata.__add__(tmp)
            self.__log.info(f'{self.ucs}: Found {len(dict_data[FcPIo])} fabric FC ports')

            tmp = None
            self.__log.info(f'{self.ucs}: Collecting all fabric ether port channels')
            dict_data.update({FabricEthLanPc: self.ucs.get_port_channel(port_type='Ethernet')})
            # rawdata = rawdata.__add__(tmp)
            self.__log.info(f'{self.ucs}: Found {len(dict_data[FabricEthLanPc])} fabric ether port channels')

            tmp = None
            self.__log.info(f'{self.ucs}: Collecting all fabric fc port channels')
            dict_data.update({FabricFcSanPc: self.ucs.get_port_channel(port_type='Fc')})
            # rawdata = rawdata.__add__(tmp)
            self.__log.info(f'{self.ucs}: Found {len(dict_data[FabricFcSanPc])} fabric ether fc channels')

            tmp = None
            self.__log.info(f'{self.ucs}: Collecting all fabric storage data')
            dict_data.update({StorageItem: self.ucs.get_system_storage()})
            # rawdata = rawdata.__add__(tmp)
            self.__log.info(f'{self.ucs}: Found {len(dict_data[StorageItem])} storage datum')

            tmp = None
            self.__log.info(f'{self.ucs}: Collecting all fabric kernel data')
            dict_data.update({SwSystemStatsHist: self.ucs.get_system_stats(ignore_error=True)})
            # rawdata = rawdata.__add__(tmp)
            self.__log.info(f'{self.ucs}: Found {len(dict_data[SwSystemStatsHist])} kernel datum')

            # create thread pool args and launch _query_thread_pool_map to map the args to _query_stats
            #  define the threading group sizes. This will pair down the number of entities
            #  that will be collected per thread and allowing ucs to multi-thread the queries
            self.__log.info(f'{self.ucs}: Raw Data count: {len(rawdata)}')
            # for data_chunk in rawdata:
            for data_chunk in dict_data:
                thread_pool_args.append(
                    [self.ucs, {data_chunk: dict_data[data_chunk]}, thread, statsq])
                thread += 1

            # this is a custom thread throttling function.
            StatsCollector._query_thread_pool_map(thread_pool_args,
                                                  pool_size=parallelism_thread_count)
        except BaseException as e:
            self.__log.error(f'{self.ucs}: Parralelism Count: {parallelism_thread_count}, ThreadCount: {thread}, \n ThreadArgs: {thread_pool_args}')
            self.__log.exception(f'{self.ucs}: Exception: {e}, \n Args: {e.args}')

    @staticmethod
    def _query_thread_pool_map(func_args_array, pool_size=2):
        """
        This is the multithreading function that maps _query_stats with func_args_array
        :param func_args_array: An array of arguments that will be passed along to _query_stats
                                This is similar to *args
        :param pool_size: Defines the number of parallel processes to be executed at once
        """
        # TODO ERROR HANDLING HERE
        logger = logging.getLogger('pyucs.statsd.StatsCollector.ProcessMapping')
        try:
            logger.info('Mapping Processes')
            # Define the process pool size, or number of parallel processes
            p_pool = CollectorProcessPool(pool_size)
            # map the function with the argument array
            #  Looks like this StatsCollector._query_stats(*args)
            # Once the mapping is done the process pool executes immediately
            p_pool.map(StatsCollector._query_stats, func_args_array)
        except BaseException as e:
            logger.error(
                f'Parralelism Count: {pool_size} \n ThreadArgs: {func_args_array}')
            logger.exception('Exception: {}, \n Args: {}'.format(e, e.args))

    @staticmethod
    def _query_stats(thread_args):
        """ The payload processor. This method is what is called in the multiprocess pool
            to collect the stats. Once the stats have been collected they are stored into
            a statsq in which a background process churns through the queue parsing the
            data to send to influxdb.
        """
        # TODO ERROR HANDLING HERE
        data = None
        logger = logging.getLogger('pyucs.statsd.StatsCollector._query_stats')
        try:
            ucs, device_chunk, thread_id, statsq = thread_args
            logger.debug(f'{ucs.name}: Start Query Stats {thread_id}')

            # Currently the only stats being collected are vnic and vhba
            # additional stats can be collected as well and would be plugged in here.
            if device_chunk.get(VnicEther or None):
                logger.debug(f'{ucs.name}: get_vnic_stats')
                data = ucs.get_vnic_stats(vnic=device_chunk[VnicEther], ignore_error=True)
            elif device_chunk.get(VnicFc or None):
                logger.debug(f'{ucs.name}: get_vhba_stats')
                data = ucs.get_vhba_stats(vhba=device_chunk[VnicFc], ignore_error=True)
            elif device_chunk.get(FabricFcSanPc or None):
                logger.debug(f'{ucs.name}: get_fabric_fcportchannel_stats')
                data = ucs.get_fabric_fcportchannel_stats(portchannel=device_chunk[FabricFcSanPc], ignore_error=True)
            elif device_chunk.get(FabricEthLanPc or None):
                logger.debug(f'{ucs.name}: get_fabric_etherportchannel_stats')
                data = ucs.get_fabric_etherportchannel_stats(portchannel=device_chunk[FabricEthLanPc], ignore_error=True)
            elif device_chunk.get(EtherPIo or None):
                logger.debug(f'{ucs.name}: get_fabric_etherport_stats')
                data = ucs.get_fabric_etherport_stats(port=device_chunk[EtherPIo], ignore_error=True)
            elif device_chunk.get(FcPIo or None):
                logger.debug(f'{ucs.name}: get_fabric_fcport_stats')
                data = ucs.get_fabric_fcport_stats(port=device_chunk[FcPIo], ignore_error=True)
            elif device_chunk.get(StorageItem or None):
                logger.debug(f'{ucs.name}: get_system_storage_stats')
                data = ucs.get_system_storage_stats(storageitem=device_chunk[StorageItem], ignore_error=True)
            elif device_chunk.get(SwSystemStatsHist or None):
                logger.debug(f'{ucs.name}: SwSystemStatsHist')
                # actual kernel stats are being passed instead of kernel managed objects
                data = device_chunk[SwSystemStatsHist]
            else:
                logger.error(f'{ucs.name}: Object Type not Found: {type(device_chunk)}')
                data = None
            logger.debug(f'{ucs.name}: End Query Stats {thread_id}')
            if data:
                [statsq.put_nowait(d) for d in data]
                logger.debug(f'{ucs.name}: Stats_Queue Size: {statsq.qsize()}')
        except BaseException as e:
            logger.exception(f'{ucs.name}: Exception: {e}, \n Args: {e.args}')

    @staticmethod
    def _get_device_type(data):
        device_type = None
        if isinstance(data, FabricFcSanPc):
            return 'FcPortChannel'
        if isinstance(data, FabricEthLanPc):
            return 'EtherPortChannel'
        if isinstance(data, EtherPIo):
            return 'FabricEtherPort'
        if isinstance(data, FcPIo):
            return 'FabricFcPort'
        if isinstance(data, StorageItem):
            return 'FabricStorage'
        if isinstance(data, VnicFc):
            return 'VnicFc'
        if isinstance(data, VnicEther):
            return 'VnicEther'
        if isinstance(data, SwSystemStatsHist):
            return 'FabricKernel'

        return None

    @staticmethod
    def chunk_it(input_list, chunk_size=1.0):
        """ Chunk it method to slice a list into smaller chunks"""
        avg = len(input_list) / float(chunk_size)
        out = []
        last = 0.0
        while last < len(input_list):
            check_not_null = input_list[int(last):int(last + avg)]
            if check_not_null:
                out.append(check_not_null)
            last += avg
        return out


