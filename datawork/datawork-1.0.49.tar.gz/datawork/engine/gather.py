from datetime import datetime, date
from networktools.path import home_path
import asyncio
import functools
from asyncio import shield, wait_for
from pathlib import Path
# NetworkTools methods and classes:
from data_rdb import Rethink_DBS
from data_geo import GeoJSONData
from data_amqp import AMQPData


from networktools.library import my_random_string, check_gsof
from networktools.colorprint import gprint, bprint, rprint
from networktools.geo import (radius, deg2rad,
                              ecef2llh, llh2ecef)
from networktools.time import get_datetime_di
from networktools.library import geojson2json

# log module
from basic_logtools.filelog import LogFile

# TaskTools for concurrency loop
from tasktools.taskloop import TaskLoop
from tasktools.scheduler import TaskScheduler

# Async Socket
# from gnsocket.gn_socket import GNCSocket


# Maths
import time
from multiprocessing import Lock
import json

# RethinkDB module
from rethinkdb import RethinkDB
rdb = RethinkDB()
rdb.set_loop_type('asyncio')


def default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()


def qjson(x):
    return json.loads(
        json.dumps(x,
                   sort_keys=True,
                   indent=1,
                   default=default)
    )


class DragonGather(TaskScheduler):
    log_manager = {}

    def __init__(self, queue_list, *args, **kwargs):
        # super().__init__()

        self.key = 'DT_GEN'
        self.ipt = kwargs.get('ipt')
        self.ico = kwargs.get('ico')
        self.process_queue = kwargs.get('process_queue')
        self.gui_queue = kwargs.get('gui_queue')
        self.proc_tasks = kwargs.get("proc_tasks")
        self.queue_client_n2t = kwargs.get("queue_client_n2t")
        self.queue_client_t2n = kwargs.get("queue_client_t2n")
        self.queue2client = kwargs.get("queue2client")
        self.stations = kwargs.get("stations")
        self.position = kwargs.get("position")
        self.db_data = kwargs.get("db_data")
        self.lnproc = kwargs.get("nproc")
        self.sta_init = kwargs.get("sta_init")
        self.bridge = kwargs.get("bridge")
        self.common = kwargs.get("common")
        self.rethinkdb_address = kwargs.get('rdb_address')
        self.rethinkdb_enu_address = kwargs.get('rdb_enu_address')
        self.rethinkdb_dbname = kwargs.get('rdb_dbname', 'test')
        self.sta_init = kwargs.get('status_tasks')
        self.status_tasks = kwargs.get('status_tasks')
        self.assigned_tasks = kwargs.get('assigned_tasks')
        self.group = kwargs.get('group')
        self.gui_group = kwargs.get('gui_group')
        self.gui_set = kwargs.get('gui_set')
        self.signals = kwargs.get('signals')
        self.isg = kwargs.get('isg')
        self.sigid = kwargs.get('sigid')
        self.sc = kwargs.get('send_control')
        self.dbus_queue = kwargs.get('dbus_queue')
        self.dbus_geojson_queue = kwargs.get('dbus_geojson_queue')
        self.status_keys = kwargs.get('status_keys', {'BATT_MEM', 'DOP'})
        args = []
        # call superior class
        super().__init__(*args, **kwargs)
        #
        self.enqueued = kwargs.get('enqueued')
        self.rq = queue_list[0]
        self.wq = queue_list[1]
        self.queue_list = queue_list
        self.start = 0
        self.signal = None
        self.origin_objects = {"RethinkDB": Rethink_DBS}
        self.rethinkdb = None
        self.rethinkdb_origin = {}
        self.rethinkdb_enu_origin = {}
        self.lock = None
        self.msg_process = dict(
            GET_LST={'STATION': self.load_stations,
                     'DBDATA': self.load_dbdata}
        )
        self.msg_server_process = dict(
            GET_STA=self.get_sta
        )

        coros_callback_dict = {
            'run_task': self.gather_data,
        }
        self.set_new_run_task(**coros_callback_dict)
        self.log_path = Path(home_path(kwargs.get('log_path', '~/log')))

    @property
    def class_name(self):
        return self.__class__.__name__

    def set_isg(self, uin=4):
        """
        Defines a new id for task related to collect data insice a worker,
        check if exists
        """
        isg = my_random_string(uin)
        while True:
            if isg not in self.isg:
                self.isg.append(isg)
                break
            else:
                isg = my_random_string(uin)
        return isg

    def msg_network_task(self):
        # get from queue status from SOCKET
        # send result
        # read_queue -> rq
        # process msg -> f(msg)
        queue_list = [self.rq, self.wq]
        time.sleep(3)
        loop = asyncio.get_event_loop()
        self.load_data_task(loop)
        # gprint("XDX Gestionando mensajes en engine", flush=True)
        try:
            args = []
            # Create instances

            task_client = TaskLoop(self.check_client_status, args, {},
                                   **{"name": "check_client_status"})

            task = TaskLoop(self.check_status, args, {},
                            **{"name": "check_status"})

            task_client.create()
            task.create()

            if not loop.is_running():
                loop.run_forever()
        except Exception as ex:
            print("Error o exception que se levanta con %s" %
                  format(queue_list))
            print(ex)
            raise ex

    async def check_client_status(self, *args, **kwargs):
        q2client = self.queue2client
        wq = self.queue_client_n2t
        rq = self.queue_client_t2n
        await asyncio.sleep(.5)
        try:
            # first read the msgs from system and send to client
            # check if is dict
            # check if has the main keys....(?)
            if not q2client.empty():
                for i in range(q2client.qsize()):
                    msg = q2client.get()
                    if isinstance(msg, dict):
                        wq.put(msg)
            # read the queue that receive the data on client
            # process the msg
            # do something...
            if not rq.empty():
                for i in range(rq.qsize()):
                    msg = rq.get()
                    result = await self.client_interpreter(msg)
                    rprint("Resultado recibido de client:%s" % result)
                    """
                    if not None:
                        wq.put({'msg': result,
                                'idc': idc})
                    """
            # bprint(self.instances.keys())
        except Exception as ex:
            print(ex)
            raise ex
        return args, kwargs

    async def client_interpreter(self, msg_in):
        # msg is a string JSON
        self.lock = Lock()
        result = []
        msg = msg_in.get('dt').get('msg')
        print("Msg recv")
        if isinstance(msg, dict):
            command = msg.get('command').get('action')
            answer = msg.get('command').get('answer')
            result = {}
            gprint("*"*20)
            bprint(answer.keys())
            gprint("*"*20)
            if command in self.msg_process and answer:
                rprint("Creating...")
                varname = msg.get('command').get('varname')
                def print_dict(x): return [print(
                    "%s->%s" % (k, v) for k, v in x.items())]
                msg_process = self.msg_process.get(
                    command, {}).get(varname, print_dict)
                bprint("msg process _> %s" % msg_process)
                result = msg_process(answer)
                rprint(f"Result from process list {result}")
        return result

    async def check_status(self, *args, **kwargs):
        wq = self.queue_list[0]
        rq = self.queue_list[1]
        await asyncio.sleep(.5)
        try:
            if not rq.empty():
                for i in range(rq.qsize()):
                    msg = rq.get()
                    try:
                        m = msg.get('dt')
                        idc = msg.get('idc')
                        result = await self.interpreter(m)
                        if result:
                            wq.put({'msg': result,
                                    'idc': idc})
                    except Exception as ex:
                        print("Error al transformar")
                        print(ex)
                        print(msg)
                        print(type(msg))
                        raise ex
            # bprint(self.instances.keys())
        except Exception as ex:
            print(ex)
            raise ex
        return args, kwargs

    async def interpreter(self, msg):
        # msg is a string JSON
        self.lock = Lock()
        command = msg.get('command', 'GET_STA')
        args = msg.get('args', [])
        result = None
        if command == 'init_gui':
            # if self.gui_group empty:
            if not self.gui_group:
                with self.lock:
                    self.sc.value = not self.sc.value
            # add group and id
            idg = args[0]
            group = args[1]
            # relationship between a gui and a group of stations
            self.gui_group.update({idg: group})

        if command in self.msg_server_process:
            result = self.msg_server_process.get(command)(*args)
        return result

    def get_sta(self, *answer):
        stations = self.stations
        # gprint("XDX stations keys : %s" %stations.keys())
        for ids in stations.keys():
            # bprint("XDX Cargando data a process")
            dataset = stations[ids]
            try:
                if dataset.get('code') in self.group or 'ALL' in self.group:
                    # if self.sc.value:
                    self.dbus_queue.put({
                        'command': 'station',
                        'data': {ids: self.stations[ids]}})
                    self.dbus_queue.put({
                        'command': 'position',
                        'data': {ids: self.position[ids]}})
                    self.gui_set.append(dataset['code'])
                    # print("XDX .sds", flush=True)

                # gprint(self.queue_process.qsize())
            except Exception as exc:
                print("Error al cargar ids a queue")
                raise exc
        self.dbus_queue.put({
            'channel': 'data',
            'command': 'load_chart',
            'data': []})
        return json.dumps({
            'channel': 'data',
            'command': 'GET_STA',
            'args': ['dbus']
        })

    def add_process_queue(self, process_queue):
        self.process_queue = process_queue

    def load_stations(self, msg):
        qs = msg
        POSITION = dict()
        for ids in qs:
            qs[ids]['STATUS'] = 'OFF'
            POSITION[ids] = dict()
            POSITION[ids]['ECEF'] = dict()
        for ids in qs:
            self.stations[ids] = qs.get(ids)
            print("Station", qs.get(ids))
            if 'ECEF_Z' in qs[ids]:
                Z = qs[ids]['ECEF_Z']
                POSITION[ids]['ECEF'].update({'Z': Z})
            if 'ECEF_X' in qs[ids]:
                X = qs[ids]['ECEF_X']
                POSITION[ids]['ECEF'].update({'X': X})
            if 'ECEF_Y' in qs[ids]:
                Y = qs[ids]['ECEF_Y']
                POSITION[ids]['ECEF'].update({'Y': Y})
            if 'position' in qs[ids]:
                pst = json.loads(qs[ids]['position'])
                coords = pst['coordinates']
                [lat, lon] = deg2rad(*coords)
                POSITION[ids].update({'lat': lat})
                POSITION[ids].update({'lon': lon})
                POSITION[ids].update({'radius': radius(lat)[0]})
                XYZ = llh2ecef(lat, lon, Z)
                # bprint(XYZ) ok, correct
                POSITION[ids].update({'ECEF': dict(zip(['X', 'Y', 'Z'], XYZ))})
            x = POSITION[ids]['ECEF']['X']
            y = POSITION[ids]['ECEF']['Y']
            z = POSITION[ids]['ECEF']['Z']
            (lat, lon, h) = ecef2llh(x, y, z)
            POSITION[ids].update({'llh': {'lat': lat, 'lon': lon, 'z': h}})
            self.position[ids] = POSITION[ids]
            if 'code' in qs:
                self.common[qs][ids] = dict()
            dataset = self.stations.get(ids)
            # code = dataset.get('code')
            self.process_queue.put(ids)
            self.enqueued.append(ids)
            self.gui_set.append(dataset['code'])
            for k, s in self.stations.items():
                bprint(f"{k} : {s}")

    def load_dbdata(self, msg):
        for k, v in msg.items():
            self.db_data[k] = v

    def msg_load_stations(self):
        get_lst = {'user': 'admin',
                   'group': 'admin',
                   'command': {'action': 'GET_LST',
                               'varname': 'STATION'}}
        return get_lst

    def msg_load_dbdata(self):
        get_lst = {'user': 'admin',
                   'group': 'admin',
                   'command': {'action': 'GET_LST',
                               'varname': 'DBDATA'}}
        return get_lst

    def init_datawork_data(self):
        rprint("Inicializando datawork data")
        msg_list = [self.msg_load_stations(), self.msg_load_dbdata()]
        for msg in msg_list:
            print("Mensaje ->", msg)
            self.queue2client.put(msg)

    def activate_stations(self, stations):
        for ids in stations.keys():
            dataset = stations.get(ids)
            self.activate_station(dataset, ids)

    def activate_station(self, dataset, ids):
        try:
            if dataset['code'] in self.group:
                self.process_queue.put(ids)
                self.gui_set.append(dataset['code'])
        except Exception as exc:
            print("Error al cargar ids a queue")
            raise exc

    async def load_data(self, *args, **kwargs):
        """
        Load main data at the beggining
        In the future, must handle messages betwen
        DragonDataWork and Collector

        """
        if self.start == 0:
            print("Enviando msg inicial")
            self.init_datawork_data()
            self.start = 1
            ###
        else:
            await asyncio.sleep(25)
        return args, kwargs

    def load_data_task(self, loop):
        # bprint("Load data task")
        args = []
        task = TaskLoop(self.load_data, args, {}, **{"name": "load_data_task"})
        task.create()

    def add_sta_instance_origin(self, ids, loop):
        # create bridge instance
        # bprint("Station %s and port %s" % (self.stations[ids]['code'], self.bridge))
        # gprint("Bridge: %s" % format(self.bridge))
        # local_port = self.create_bridge(ids)
        # rprint("Local port %s" %local_port)
        code = self.stations[ids]['code']
        code_db = self.stations[ids]['db']
        # idd = self.get_id_by_code('DBDATA', code_db)
        # bprint("The db_data's id: %s" % idd)
        print("Conexión source", self.rethinkdb_address,
              f"DBNAME -> {self.rethinkdb_dbname}")
        db_datos = dict(host='localhost',
                        name="Source_%s" % code_db,
                        code=code_db,
                        port=self.rethinkdb_address[1],
                        address=self.rethinkdb_address,
                        dbname=self.rethinkdb_dbname,
                        io_loop=loop,
                        log_path=str(self.log_path/"source_rdb"),
                        env='gather_%s' % code)
        name = 'RethinkDB'
        self.sta_init[ids] = True
        if name == 'RethinkDB':
            self.rethinkdb_origin[ids] = True
        try:
            RDB_C = self.origin_objects[name]
            rethinkdb_c = RDB_C(**db_datos)
            time.sleep(.5)
            return rethinkdb_c
        except Exception as ex:
            print("Error al inicializar conexión %s" % ex)
            raise ex

    def add_sta_instance_destiny(self, ids, loop):
        # create bridge instance
        # bprint("Station %s and port %s" % (self.stations[ids]['code'], self.bridge))
        # gprint("Bridge: %s" % format(self.bridge))
        # local_port = self.create_bridge(ids)
        # rprint("Local port %s" %local_port)
        code = self.stations[ids]['code']
        code_db = self.stations[ids]['db']
        # idd = self.get_id_by_code('DBDATA', code_db)
        # bprint("The db_data's id: %s" % idd)
        print("Conexión enu", self.rethinkdb_enu_address)
        db_datos_enu = dict(host='localhost',
                            name="Destiny_enu",
                            code='enu',
                            port=self.rethinkdb_enu_address[1],
                            address=self.rethinkdb_enu_address,
                            dbname='enu_data',
                            io_loop=loop,
                            log_path=str(self.log_path/"enu_rdb"),
                            env='enu_%s' % code)

        name = 'RethinkDB'
        self.sta_init[ids] = True
        if name == 'RethinkDB':
            self.rethinkdb_enu_origin[ids] = True
        try:
            RDB_C = self.origin_objects[name]
            rethinkdb_c_enu = RDB_C(**db_datos_enu)
            time.sleep(.5)
            return rethinkdb_c_enu
        except Exception as ex:
            print("Error al inicializar conexión %s" % ex)
            raise ex

        # self.common[code] = dict()
    # CREATE QUEUE INSTANCES

    # GET DATA AND SEND TO PLOT
    #
    #

    def add_process_instance(self, ids):
        CODE = self.stations[ids]['protocol'].upper()
        station = self.stations[ids]['code']
        kwargs = dict()
        kwargs['code'] = CODE
        kwargs['station'] = self.stations[ids]
        kwargs['position'] = self.position[ids]
        kwargs['log_path'] = str(self.log_path/'geo_json_data')
        process_instance = GeoJSONData(**kwargs)
        return process_instance

    def add_ew_instance(self, ids):
        ew_host = '10.54.218.81'
        creds = ('seismic', 'secret')
        CODE = self.stations[ids]['protocol'].upper()
        station = self.stations[ids]['code']
        kwargs = dict()
        kwargs['code'] = CODE
        kwargs['station'] = self.stations[ids]
        kwargs['position'] = self.position[ids]
        kwargs['host'] = ew_host
        kwargs['credentials'] = creds
        ew_instance = AMQPData(**kwargs)
        return ew_instance

    async def gather_data(self, ipt, ids, *args, **kwargs):
        """
        This method it's maybe the most important because generate
        the instances and gather the data in a general loop

        The logging system is a task by process
        """
        # input : ids, loop, sta
        uin = 3
        idi = my_random_string(uin)
        loop = asyncio.get_event_loop()
        v = int(args[0])
        sta = args[1]
        di, control, (rc, rc_enu), process_data = sta
        sta_init_flag = self.sta_init.get(ids)
        code = self.stations[ids]['code']
        code_db = self.stations[ids]['db']
        log = kwargs.get('log')
        # self.rethinkdb_origin[ids] = True
        # self.rethinkdb_enu_origin[ids] = True
        """
        Objetos centrales, de operacion
        """
        body, origin, destiny = False, False, False
        await asyncio.sleep(.5)

        if not sta_init_flag:
            # para controlar que?
            control = None
            # punto de inicio a consultar
            di = rdb.iso8601(get_datetime_di(delta=30))
            # el operador o procesador de la info
            process_data = self.add_process_instance(ids)
            self.sta_init[ids] = True
            body = True

        """
        Iniciar objeto database fuente
        """
        if not self.rethinkdb_origin.get(ids):
            # las dos instancias a dbs rethinkdb
            # rc: origen
            # rec_enu: destino
            rc = self.add_sta_instance_origin(ids, loop)
            try:
                conn = await wait_for(rc.async_connect(), timeout=10)
                rc.set_defaultdb(self.rethinkdb_dbname)
                await rc.list_dbs()
                await rc.select_db(self.rethinkdb_dbname)
                table_name = self.stations[ids]['db']  # created on datawork
                indexes = await rc.get_indexes(table_name)
                await rc.list_tables(rc.default_db)
                origin = True
            except asyncio.TimeoutError as e:
                idex = my_random_string(uin)
                kwargs["origin_exception"] = "PD_TO1_00 + %s" % (idex, code)
                log.exception(kwargs["origin_exception"])
                self.rethinkdb_origin[ids] = False
                rc.close()
                del rc
                rc = None
                return [ipt, ids, v,
                        [di, control, (rc, rc_enu),
                         process_data]], kwargs
        """
        Iniciar objeto database destino
        """
        if not self.rethinkdb_enu_origin.get(ids):
            # las dos instancias a dbs rethinkdb
            # rc: origen
            # rec_enu: destino
            rc_enu = self.add_sta_instance_destiny(ids, loop)
            try:
                await rc_enu.async_connect()
                await rc_enu.list_dbs()
                await rc_enu.select_db('enu_data')
                table_name = self.stations[ids]['db']  # created on datawork
                await rc_enu.create_table(table_name, rc_enu.default_db)
                if 'DT_GEN' not in indexes:
                    await rc_enu.create_index(table_name, index='DT_GEN')
                indexes = await rc_enu.get_indexes(table_name)
                await rc_enu.list_tables(rc_enu.default_db)
                destiny = True
            except asyncio.TimeoutError as e:
                idex = my_random_string(uin)
                kwargs["origin_exception"] = f"PD_TO1_00 + {code}"
                log.exception(kwargs["origin_exception"])
                self.rethinkdb_origin_enu[ids] = False
                bprint(kwargs)
                rc_enu.close()
                del rc_enu
                rc_enu = None
                return [ipt, ids, v,
                        [di, control, (rc, rc_enu),
                         process_data]], kwargs
        if body or origin or destiny:
            v = 2
            wargs = [ipt, ids, v, [di, control, (rc, rc_enu), process_data]]
            return wargs, kwargs
        elif sta_init_flag:
            code = self.stations[ids]['code']
            table_name = self.stations[ids]['db']
            key = self.key
            try:
                df = rdb.iso8601(get_datetime_di(delta=0))  # now
                filter_opt = {'left_bound': 'open', 'index': key}
                try:
                    future = rc.get_data_filter(table_name,
                                                [di, df],
                                                filter_opt,
                                                key)
                    cursor = await wait_for(future, timeout=60)
                except Exception as e:
                    log.exception(e)
                    print("=====Algo pasa =====")
                    print(table_name, key)
                if len(cursor) >= 1:
                    gprint("____")
                    bprint(
                        f"Cursor len {len(cursor)} in {table_name}, Destiniy>{rc_enu}")
                    gprint("____")

            except asyncio.TimeoutError as e:
                idex = my_random_string(uin)
                kwargs["origin_exception"] = "PD_TO3_00 + %s" % code
                log.exception(kwargs["origin_exception"])
                self.rethinkdb_origin[ids] = False
                bprint(kwargs)
                rc.close()
                del rc
                rc = None
                wargs = [ipt, ids, v, [
                    di, control, (rc, rc_enu), process_data]]
                return wargs, kwargs
            except Exception as ex:
                idex = my_random_string(uin)
                print("IDEX %s Exception" % idex, ex)
                print("Error en obtención de data desde rethinkdb")
                rc.logerror(
                    "IDEX = %s, Error en la obtención de datos para estación %s en %s" % (
                        idex, code, di))
                kwargs["origin_exception"] = "PD_TO4_00 + %s" % code
                log.exception(kwargs["origin_exception"])
                self.rethinkdb_origin[ids] = False
                rc.close()
                del rc
                rc = None
                wargs = [ipt, ids, v, [
                    di, control, (rc, rc_enu), process_data]]
                return wargs, kwargs

            # signal.message({"msg":"cursor len %s" %len(cursor)})
            list_ok = []
            for c in cursor:
                if check_gsof(c):
                    try:
                        result = process_data.manage_data(c)
                        # to_plot = geojson2json(result)
                        to_db = geojson2json(result, destiny='db')
                        # result_enu =
                        try:
                            await wait_for(
                                rc_enu.save_data(table_name, to_db),
                                timeout=60)
                        except Exception as e:
                            bprint(f"Algo pasa con rc_enu....{e}")
                        # send normal json
                        msg_result = qjson(result)
                        send = {
                            'channel': 'earlybird',
                            'command': 'add_data',
                            'data': msg_result}
                        self.dbus_queue.put(send)
                        # send to earlybird
                        await asyncio.sleep(.1)
                        send_eb = {
                            'channel': 'earlybird',
                            'command': 'add_data',
                            'data': msg_result}
                        try:
                            self.dbus_queue.put(send_eb)
                        except Exception as e:
                            rprint("Error al enviar send_ev")
                            bprint(e)
                        intersection = self.status_keys.intersection(c.keys())
                        if intersection:
                            data_msg = {key: qjson(c.get(key))
                                        for key in intersection}
                            send = {
                                'channel': 'status',
                                'command': 'add_status',
                                'station': code,
                                'data': data_msg}
                            self.dbus_queue.put(send)
                        if self.dbus_geojson_queue:
                            self.dbus_geojson_queue.put(send)
                    except asyncio.TimeoutError as e:
                        kwargs["origin_exception"] = f"PD_TO5_01 + {code} + {e}"
                        log.exception(kwargs["origin_exception"])
                        self.rethinkdb_origin_enu[ids] = False
                        rc_enu.close()
                        del rc_enu
                        rc_enu = None
                        wargs = [ipt, ids, v, [
                            di, control, (rc, rc_enu), process_data]]
                        return wargs, kwargs
                    except Exception as ex:
                        print("WS Error al enviar %s a cola %s" %
                              (code, ex), flush=True)
                        kwargs["origin_exception"] = "PD_TO5_02 + %s" % code
                        log.exception(kwargs["origin_exception"])
                        bprint(kwargs)
                        rc_enu.close()
                        del rc_enu
                        rc_enu = None
                        return [ipt, ids, v,
                                [di, control,
                                 (rc, rc_enu),
                                 process_data]], kwargs

                    list_ok.append(c)
                else:
                    msg = "Error en estacixon %s  ----> %s" % (code, c)
                    await rc.msg_log(msg, "DEBUG")
            if cursor:
                dt_recv = cursor[-1].get('DT_RECV')
                di = cursor[-1].get('DT_GEN', dt_recv)
                control = True
            return [
                ipt, ids, v,
                [di, control, (rc, rc_enu), process_data]
            ], kwargs
        return [ipt, ids, v, sta], kwargs

    def set_pst(self, ids, args, kwargs):
        return [args[0], ids, *args[1:]], kwargs

    def set_init_args_kwargs(self, ipt):
        """
        This definition is for collector instance
        """
        rprint(f"Init log..... for ipt {ipt}")
        log = print
        log = LogFile("Engine@Datawork", "CORE_%s" %
                      ipt, "localhost@pineiden",
                      path=str(self.log_path/"engine"))
        self.log_manager[ipt] = log
        return [ipt, 1, (None, None, (None, None), None)], {"log": log}
