import logging

from django.conf import settings
from django.db.models import ProtectedError, Sum

from isc_common import Stack, Wrapper
from isc_common.common import blinkString, new
from isc_common.datetime import DateToStr
from isc_common.json import StrToJson
from isc_common.number import DecimalToStr, Set, ToDecimal
from kaf_pas.planing.models.production_order_values import Production_order_values
from kaf_pas.planing.operation_typesStack import NoLaunch, MADE_OPRS_MNS_TSK

logger = logging.getLogger(__name__)


class Production_orderWrapper(Wrapper):
    all_childs = None
    childs = None
    childs_launch = None
    color = None
    color_id = None
    date = None
    description = None
    ed_izm = None
    edizm = None
    edizm_id = None
    id = None
    item = None
    item_id = None
    launch = None
    launch__date = None
    launch_id = None
    location = None
    location_fin = None
    location_fin_id = None
    location_id = None
    num = None
    old_num = None
    operation = None
    operation_item = None
    operation_materials = None
    operations = None
    parent = None
    parent_id = None
    parent_launch = None
    parent_launch_id = None
    parentRecord = None
    production_operation = None
    production_operation_attrs = None
    production_operation_color = None
    production_operation_colors = None
    production_operation_color_id = None
    production_operation_edizm = None
    production_operation_edizm_id = None
    production_operation_id = None
    production_operation_num = None
    production_operation_qty = None
    qty = None
    resource = None
    resource_fin = None
    resource_fin_id = None
    resource_id = None
    this = None
    user = None
    user_id = None
    value = None
    value1_sum = None
    value1_sum_len = None
    value_made = None
    value_start = None
    value_sum = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if isinstance(kwargs.get('childs'), list):
            self.operations = [Production_orderWrapper(**c) for c in sorted(kwargs.get('childs'), key=lambda x: x['production_operation_num'])]
            self.childs = None

        if self.color_id:
            from isc_common.models.standard_colors import Standard_colors
            from kaf_pas.planing.models.operation_color_view import Operation_color_view

            if isinstance(self.color_id, str):
                self.color_id = StrToJson(self.color_id)
                self.color_id = self.color_id.get('color_id')

            if self.color_id != None:
                try:
                    self.color = Standard_colors.objects.get(id=self.color_id)
                    self.color_id = self.color.id
                except Standard_colors.DoesNotExist:
                    self.color = Operation_color_view.objects.get(id=self.color_id).color
                    self.color_id = self.color.id

        if isinstance(self.color, int):
            from isc_common.models.standard_colors import Standard_colors
            self.color = Standard_colors.objects.get(id=self.color)

        if isinstance(self.production_operation_color_id, int):
            from isc_common.models.standard_colors import Standard_colors
            self.color = Standard_colors.objects.get(id=self.production_operation_color_id)
            self.color_id = self.color.id

        if isinstance(self.production_operation_color, int):
            from isc_common.models.standard_colors import Standard_colors
            self.color = Standard_colors.objects.get(id=self.production_operation_color)
            self.color_id = self.color.id

        if self.edizm_id:
            from kaf_pas.ckk.models.ed_izm import Ed_izm
            self.ed_izm = Ed_izm.objects.get(id=self.edizm_id)

        if self.production_operation_id:
            from kaf_pas.production.models.operations import Operations
            self.production_operation = Operations.objects.get(id=self.production_operation_id)

        if isinstance(self.production_operation, int):
            from kaf_pas.production.models.operations import Operations
            self.production_operation = Operations.objects.get(id=self.production_operation)

        if self.production_operation_color_id:
            from isc_common.models.standard_colors import Standard_colors
            self.production_operation_color = Standard_colors.objects.get(id=self.production_operation_color_id)

        if self.production_operation_edizm_id:
            from kaf_pas.ckk.models.ed_izm import Ed_izm
            self.production_operation_edizm = Ed_izm.objects.get(id=self.production_operation_edizm_id)

        if self.id != None:
            from kaf_pas.planing.models.operations import Operations
            self.this = Operations.objects.get(id=self.id)

        if self.parent_id:
            from kaf_pas.planing.models.operations import Operations
            from kaf_pas.planing.models.operation_item import Operation_item
            from kaf_pas.planing.models.operation_launches import Operation_launches
            from kaf_pas.planing.models.operation_refs import Operation_refs
            from kaf_pas.planing.models.production_order import Production_order
            from kaf_pas.planing.models.production_order_opers import Production_order_opers

            self.parent = Operations.objects.get(id=self.parent_id)
            self.parent.launch = Operation_launches.objects.get(operation_id=self.parent_id).launch
            self.parent_launch = self.parent.launch
            self.parent_launch_id = self.parent_launch.id

            self.parent.item = Operation_item.objects.get(operation_id=self.parent_id).item
            self.item = self.parent.item
            self.item_id = self.item.id

            self.childs = Production_order_opers.objects.filter(parent_id=self.parent.id, deleted_at=None).order_by('production_operation_num')
            self.all_childs = Production_order_opers.objects.filter(parent_id=self.parent.id).order_by('production_operation_num')

        if self.item_id != None:
            from kaf_pas.ckk.models.item import Item
            self.item = Item.objects.get(id=self.item_id)

        if isinstance(self.item, int):
            from kaf_pas.ckk.models.item import Item
            self.resource = Item.objects.get(id=self.item)

        if self.location_id:
            from kaf_pas.ckk.models.locations import Locations

            if self.location == None:
                self.location = Locations.objects.get(id=self.location_id)

            if self.resource == None:
                self.resource = self.location.resource

        if isinstance(self.location, int):
            from kaf_pas.ckk.models.locations import Locations

            self.location = Locations.objects.get(id=self.location)

            if self.resource == None:
                self.resource = self.location.resource

        if self.location_fin_id:
            from kaf_pas.ckk.models.locations import Locations

            self.location_fin = Locations.objects.get(id=self.location_fin_id)

            if self.resource_fin == None:
                self.resource_fin = self.location_fin.resource

        if isinstance(self.location_fin, int):
            from kaf_pas.ckk.models.locations import Locations

            self.location_fin = Locations.objects.get(id=self.location_fin)

            if self.resource_fin == None:
                self.resource_fin = self.location_fin.resource

        if self.resource_id:
            from kaf_pas.production.models.resource import Resource
            from kaf_pas.ckk.models.locations import Locations

            self.resource = Resource.objects.get(id=self.resource_id)

            if self.resource.location != self.location:
                self.location = self.resource.location

        if isinstance(self.resource, int):
            from kaf_pas.production.models.resource import Resource
            from kaf_pas.ckk.models.locations import Locations

            self.resource = Resource.objects.get(id=self.resource)
            if self.resource.location != self.location:
                self.location = self.resource.location

        if self.resource_fin_id:
            from kaf_pas.production.models.resource import Resource
            from kaf_pas.ckk.models.locations import Locations

            self.resource_fin = Resource.objects.get(id=self.resource_fin_id)

            if self.resource_fin.location != self.location_fin:
                self.location_fin = self.resource_fin.location

        if isinstance(self.resource_fin, int):
            from kaf_pas.production.models.resource import Resource
            from kaf_pas.ckk.models.locations import Locations

            self.resource_fin = Resource.objects.get(id=self.resource_fin)

            if self.resource_fin.location != self.location_fin:
                self.location_fin = self.resource_fin.location

        if self.launch_id:
            from kaf_pas.production.models.launches import Launches

            self.launch = Launches.objects.get(id=self.launch_id)
            if self.launch.parent == None:
                self.childs_launch = Launches.objects.filter(parent=self.launch)

        if isinstance(self.launch, int):
            from kaf_pas.production.models.launches import Launches
            self.launch = Launches.objects.get(id=self.launch)

        if self.user_id != None:
            from isc_common.auth.models.user import User
            self.user = User.objects.get(id=self.user_id)

        if isinstance(self.parentRecord, dict):
            from kaf_pas.planing.models.production_order_opers import Production_order_opers
            self.parentRecord = Production_orderWrapper(**self.parentRecord)
            self.parentRecord.childs = Production_order_opers.objects.filter(parent_id=self.parentRecord.this.id, deleted_at=None).order_by('production_operation_num')
            self.parentRecord.all_childs = Production_order_opers.objects.filter(parent_id=self.parentRecord.this.id).order_by('production_operation_num')


class Launch_release(Wrapper):
    # last_operation = None
    color = None
    edizm = None
    item = None
    # Последняя выполенная операция над деталью входящец в поглощающую операцию
    detal_last_operation = None
    launch = None
    location_fin = None
    operation_made = None
    production_order = None
    resource_fin = None
    value = None

    def copy(self):
        return Launch_release(**self.__dict__)


class Launch_releases(Stack):
    stack = []

    @property
    def launches_ids(self):
        return Set(list(map(lambda x: x.launch.id, self.stack))).get_set_sorted_as_original

    def launch_releases(self, launch_id):
        return filter(lambda x: x.launch.id == launch_id, self.stack)


class Production_order_values_ext:
    enableMinus = settings.ENABLE_MINUS_ODD

    def blockMakeAll(self, data, user):

        from django.conf import settings
        from django.db import transaction
        from django.forms import model_to_dict

        from isc_common import setAttr
        from isc_common.bit import TurnBitOn
        from isc_common.common import new
        from isc_common.progress import managed_progress, ProgressDroped, progress_deleted
        from kaf_pas.planing.models.production_ext import Production_ext
        from kaf_pas.planing.models.production_order import Production_order
        from kaf_pas.planing.models.production_order_opers import Production_order_opers
        from kaf_pas.ckk.models.ed_izm import Ed_izm
        from kaf_pas.planing.models.production_order import Production_orderManager
        from kaf_pas.planing.models.production_ext import Operation_executor_stack

        _res = []

        production_ext = Production_ext()
        records = data.get('records')
        if isinstance(records, list):

            with managed_progress(
                    id=f'blockMakeAll_{user.id}',
                    qty=len(records),
                    user=user,
                    message='Внесение данных по выпуску.',
                    title='Выполнено',
                    props=TurnBitOn(0, 0)
            ) as progress:
                with transaction.atomic():
                    def except_func():
                        settings.LOCKS.release(key)

                    progress.except_func = except_func

                    operation_executor_stack = Operation_executor_stack()
                    for record in records:
                        operation = Production_order.objects.get(id=record.get('id'))

                        key = f'''get_setStartStatus_{operation.id}'''
                        settings.LOCKS.acquire(key)

                        edizm = Ed_izm.objects.get(code='шт')
                        _data = dict(
                            id=operation.id,
                            launch_id=operation.launch.id,
                            edizm_id=edizm.id
                        )
                        qty = operation.value_sum

                        if operation.status.id == settings.OPERS_TYPES_STACK.PRODUCTION_TASK_STATUSES.get(new).id and operation.cnt_opers == 1:
                            production_ext.start(
                                _data=_data,
                                qty=qty,
                                user=user,
                                lock=False,
                                operation_executor_stack=operation_executor_stack
                            )

                            setAttr(record, 'childs', [model_to_dict(production_order_opers) for production_order_opers in Production_order_opers.objects.filter(parent_id=operation.id)])
                            setAttr(record, 'value', operation.value_sum)
                            setAttr(record, 'edizm__name', edizm.name)
                            setAttr(record, 'edizm_id', edizm.id)
                            setAttr(record, 'value_start', qty)

                            res, _ = self.makeAll(
                                data=record,
                                user=user,
                                lock=False
                            )

                            # !!!!!!!!!!!!!!!!!!!! Не убирать !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                            Production_orderManager.update_redundant_planing_production_order_table(res)
                            Production_orderManager.refresh_all(
                                ids=res,
                                buffer_refresh=True,
                                item_operations_refresh=True,
                                production_order_values_refresh=True,
                                production_order_opers_refresh=True,
                            )
                            res = model_to_dict(res)
                            _res.append(res)
                            # END !!!!!!!!!!!!!!!!!!!! Не убирать !!!!!!!!!!!!!!!!!!!!!!!!!!!!

                        if progress.step() != 0:
                            settings.LOCKS.release(key)
                            raise ProgressDroped(progress_deleted)

            for operation_executor in operation_executor_stack:
                settings.EVENT_STACK.EVENTS_PRODUCTION_ORDER_CREATE.send_message(
                    message=blinkString(f'<h4>Вам направлено: {operation_executor.qty} новых заданий на производство.</h4>', bold=True),
                    users_array=[operation_executor.executor],
                )
                Production_orderManager.fullRows(suffix=f'''_user_id_{operation_executor.executor.id}''')
            settings.LOCKS.release(key)
            return _res
        else:
            raise Exception('Не сделан выбор.')

    def rec_item_releases(self, launch_release, value, user):
        from django.conf import settings
        from kaf_pas.planing.models.operation_refs import Operation_refs

        #
        release_item_operation = self.rec_operation(
            color=launch_release.color,
            edizm=launch_release.edizm,
            item=launch_release.item,
            launch=launch_release.launch,
            location_fin=launch_release.location_fin,
            opertype=settings.OPERS_TYPES_STACK.MADE_OPERATIONS_MNS_TASK,
            resource=launch_release.resource,
            resource_fin=launch_release.resource_fin,
            status=settings.OPERS_TYPES_STACK.MADE_OPERATIONS_MNS_STATUSES.get(new),
            value=value,
            user=user,
        )
        logger.debug(f'Created release_item :  {release_item_operation}')
        # res.append(model_to_dict(release_item_operation))

        # Связываем с приходной операцией
        operation_refs, created = Operation_refs.objects.get_or_create(
            child=release_item_operation,
            parent=launch_release.operation_made.this,
            props=Operation_refs.props.product_making
        )
        if created:
            logger.debug(f'Created operation_refs :  {operation_refs}')

        # Связываем с операцией тезнологической операций поглощаемого элемента
        operation_refs, created = Operation_refs.objects.get_or_create(
            child=release_item_operation,
            parent=launch_release.detal_last_operation.this,
            props=Operation_refs.props.product_making
        )
        if created:
            logger.debug(f'Created operation_refs :  {operation_refs}')

    def rec_items_releases(self, launches_values, user):
        from kaf_pas.production.models.launch_item_prod_order_view import Launch_item_order_view
        from kaf_pas.accounting.models.buffers import Buffers
        from kaf_pas.planing.models.production_order_opers_per_launch import Production_order_opers_per_launch
        from kaf_pas.production.models.launches import Launches

        if launches_values.size() == 0:
            return

        item = launches_values.top().item

        for launch_id in launches_values.launches_ids:
            launch_releases = list(launches_values.launch_releases(launch_id=launch_id))

            for launch_release in launch_releases:
                for launch_item in Launch_item_order_view.objects.filter(parent=item):
                    logger.debug(f'launch_item: {launch_item}')

                    launch = launch_release.launch if launch_release.launch.parent != None else Launches.objects.filter(parent=launch_release.launch)[0]
                    # Ищем составную часть в производственной спецификации для определения необходимого кол-во
                    launch_item_order_view = Launch_item_order_view.objects.filter(
                        item=launch_item.child,
                        launch_ids__overlap=[launch.id]
                    )
                    qty = launch_item_order_view.count()

                    if qty == 0:
                        raise Exception(f'Товарная позиция: {launch_item.child.item_name} не найдена в деталировке')
                    elif qty == 1:

                        qty_need = launch_item_order_view[0].qty_per_one * launch_release.value
                        logger.debug(f'qty_need: {qty_need}')

                        production_order_opers_per_launch = Production_order_opers_per_launch.objects.filter(item=launch_item.child, launch=launch).order_by("-operation_operation_num")[0]
                        launch_release.detal_last_operation = production_order_opers_per_launch
                        launch_release.resource = production_order_opers_per_launch.resource
                        launch_release.resource_fin = production_order_opers_per_launch.resource_fin
                        launch_release.location_fin = production_order_opers_per_launch.location_fin
                        launch_release.item = production_order_opers_per_launch.item
                        color = self.get_color(launch_release.color, production_order_opers_per_launch.production_operation)
                        launch_release.color = color

                        logger.debug(f'production_order_opers_per_launch.child: {production_order_opers_per_launch}')

                        buffers_query = Buffers.objects.filter(item=launch_item.child, launch=launch_release.launch, color=launch_item.color)
                        cnt = buffers_query.count()
                        if cnt == 1:
                            exists_qty = buffers_query[0].value
                            if exists_qty < qty_need:
                                message = f'Недостаточно комплектации по: {launch_release.item.item_name}, в наличии {DecimalToStr(exists_qty)} а необходимо {DecimalToStr(qty_need)}'
                                self.warnings.push(message)

                        elif cnt == 0:
                            message = f'Недостаточно комплектации по: {launch_release.item.item_name}, в наличии 0 а необходимо {DecimalToStr(qty_need)}'
                            self.warnings.push(message)

                        else:
                            raise Exception('Not clear situation.')

                        self.rec_item_releases(
                            launch_release=launch_release,
                            value=qty_need,
                            user=user
                        )

                    else:
                        raise Exception('Not clear situation.')

    def get_color(self, color, operation):
        from isc_common.common.functions import ExecuteStoredProc
        colors = ExecuteStoredProc('get_operation_colors', [operation.parent_id, operation.id])

        if colors == None:
            return None

        if color != None and isinstance(colors, list):
            if color.id not in colors:
                color = None
        return color

    def rec_launch_releases(
            self,
            prev_tech_operation,
            this_tech_operation,
            edizm,
            item,
            launch,
            value,
            user,
            color=None,
    ):
        from kaf_pas.production.models.launches_view import Launches_viewManager
        from django.conf import settings
        from kaf_pas.planing.models.operation_refs import Operation_refs

        # Пишем вычитающую операцию
        previos_minus_operation = None
        if prev_tech_operation != None:
            _color = self.get_color(color=color, operation=this_tech_operation)

            previos_minus_operation = self.rec_operation(
                color=_color,
                edizm=edizm,
                item=item,
                launch=launch,
                location_fin=prev_tech_operation.location_fin,
                opertype=settings.OPERS_TYPES_STACK.MADE_OPERATIONS_MNS_TASK,
                resource=prev_tech_operation.resource,
                resource_fin=prev_tech_operation.resource_fin,
                status=settings.OPERS_TYPES_STACK.MADE_OPERATIONS_MNS_STATUSES.get(new),
                value=value,
                user=user,
            )
            logger.debug(f'Created previos_minus_operation :  {previos_minus_operation}')

            # ===== Связываем с предыдущей технологической
            if previos_minus_operation:
                operation_refs = Operation_refs.objects.create(
                    child=previos_minus_operation,
                    parent=prev_tech_operation.this,
                    props=Operation_refs.props.product_making,
                )
                logger.debug(f'Created operation_refs :  {operation_refs}')

        # Пишем прибавляющую операцию
        this_plus_operation = self.rec_operation(
            color=color,
            edizm=edizm,
            item=item,
            launch=launch,
            location_fin=this_tech_operation.location_fin,
            opertype=settings.OPERS_TYPES_STACK.MADE_OPERATIONS_PLS_TASK,
            resource=this_tech_operation.resource,
            resource_fin=this_tech_operation.resource_fin,
            status=settings.OPERS_TYPES_STACK.MADE_OPERATIONS_PLS_STATUSES.get(new),
            value=value,
            user=user,
        )
        logger.debug(f'Created launch_release_operation :  {this_plus_operation}')
        # ===== Связываем с текущей технологической
        operation_refs = Operation_refs.objects.create(
            child=this_plus_operation,
            parent=this_tech_operation.this,
            props=Operation_refs.props.product_making,
        )
        logger.debug(f'Created operation_refs :  {operation_refs}')

        # ===== Связываем операции вычитающую и прибавляющую чтобы потом удалять вместе
        if previos_minus_operation:
            operation_refs = Operation_refs.objects.create(
                child=this_plus_operation,
                parent=previos_minus_operation,
                props=Operation_refs.props.product_making,
            )
            logger.debug(f'Created operation_refs :  {operation_refs}')

        Launches_viewManager.refreshRows(ids=launch.id)
        if launch.parent != None:
            Launches_viewManager.refreshRows(ids=launch.parent.id)

        this_plus_operation = Production_orderWrapper(**this_plus_operation.__dict__)
        this_plus_operation.location_fin = this_tech_operation.location_fin
        this_plus_operation.resource = this_tech_operation.resource
        this_plus_operation.resource_fin = this_tech_operation.resource_fin
        return this_plus_operation

    def rec_operation(
            self,
            color,
            edizm,
            item,
            location_fin,
            launch,
            opertype,
            resource,
            resource_fin,
            status,
            value,
            user,
    ):
        from datetime import datetime
        from kaf_pas.planing.models.operation_color import Operation_color
        from kaf_pas.planing.models.operation_item import Operation_item
        from kaf_pas.planing.models.operation_resources import Operation_resources
        from kaf_pas.planing.models.operation_value import Operation_value
        from kaf_pas.planing.models.operations import Operations
        from kaf_pas.planing.models.operation_launches import Operation_launches

        operation = Operations.objects.create(
            creator=user,
            date=datetime.now(),
            deliting=False,
            editing=False,
            opertype=opertype,
            status=status,
        )
        logger.debug(f'Created release_item :  {operation}')

        operation_value = Operation_value.objects.create(
            operation=operation,
            value=value,
            edizm=edizm,
            props=Operation_value.props.used_in_release
        )
        logger.debug(f'Created operation_value :  {operation_value}')

        operation_launch = Operation_launches.objects.create(
            operation=operation,
            launch=launch,
        )
        logger.debug(f'Created operation_launch :  {operation_launch}')

        if color != None:
            operation_color = Operation_color.objects.create(
                operation=operation,
                color=color,
            )
            logger.debug(f'Created operation_color :  {operation_color}')

        operation_item = Operation_item.objects.create(
            operation=operation,
            item=item,
        )
        logger.debug(f'Created operation_item :  {operation_item}')

        operation_resource = Operation_resources.objects.create(
            resource=resource,
            resource_fin=resource_fin,
            location_fin=location_fin,
            operation=operation,
        )
        logger.debug(f'Created operation_resource :  {operation_resource}')

        return operation

    def get_launches(self, parent_launch, item):
        from django.db import connection
        from kaf_pas.production.models.launches import Launches

        with connection.cursor() as cursor:
            cursor.execute('''select distinct prdl.id, prdl.priority, sd.date_sign, sd.date
                                                        from sales_demand as sd
                                                            join production_launches prdl on sd.id = prdl.demand_id
                                                            join planing_operation_launches polc on prdl.id = polc.launch_id
                                                            join planing_operation_item poit on poit.operation_id = polc.operation_id
                                                        where prdl.parent_id = %s
                                                        and poit.item_id = %s
                                                        order by prdl.priority, sd.date_sign, sd.date''', [parent_launch.id, item.id])
            # 1. Приоритет
            # 2. Срок поставки из заказа на продажу
            # 3. Дата составления заказа на продажу
            rows = cursor.fetchall()
            return [Launches.objects.get(id=row[0]) for row in rows]

    def make_launch_release(
            self,
            # Предыдущая техноглогическая операция
            prev_tech_operation,
            # Текущая техноглогическая операция
            this_tech_operation,
            data,
            item,
            production_order,
            min_value_made,
            parent_launch,
            user,
            do_rec_items_releases=False,
            # do_rec_order_releases=False
    ):
        from kaf_pas.production.models.launch_item_prod_order_view import Launch_item_order_view
        from kaf_pas.planing.models.production_order_opers_per_launch import Production_order_opers_per_launch

        launches_values = Launch_releases()

        if not this_tech_operation.production_operation.is_launched or data.launch == None:

            # Получаем список запусков связанных с заказами
            launches = self.get_launches(parent_launch=parent_launch, item=item)
            for launch in launches:
                # Остаток по выполнеию

                value_odd = ToDecimal(Production_order_opers_per_launch.objects.filter(
                    parent_id=production_order.id,
                    production_operation=this_tech_operation.production_operation,
                    item=item,
                    launch=launch
                ).aggregate(Sum('value_odd')).get('value_odd__sum'))

                if value_odd > min_value_made:
                    value = min_value_made
                    min_value_made = 0
                else:
                    value = value_odd
                    min_value_made -= value_odd

                if value > 0:
                    this_plus_operation = self.rec_launch_releases(
                        color=data.color,
                        edizm=data.ed_izm,
                        item=item,
                        launch=launch if data.launch == None else data.launch,
                        prev_tech_operation=prev_tech_operation,
                        this_tech_operation=this_tech_operation,
                        user=user,
                        value=value,
                    )

                    launches_values.push(Launch_release(
                        color=data.color,
                        edizm=data.ed_izm,
                        item=item,
                        launch=launch if data.launch == None else data.launch,
                        operation_made=this_plus_operation,
                        production_order=production_order,
                        value=value,
                    ))

                if min_value_made == 0:
                    break

        if min_value_made > 0:
            this_plus_operation = self.rec_launch_releases(
                color=data.color,
                edizm=data.ed_izm,
                item=item,
                launch=parent_launch if data.launch == None else data.launch,
                prev_tech_operation=prev_tech_operation,
                this_tech_operation=this_tech_operation,
                user=user,
                value=min_value_made,
            )

            launches_values.push(Launch_release(
                operation_made=this_plus_operation,
                color=data.color,
                edizm=data.ed_izm,
                item=item,
                launch=parent_launch,
                production_order=production_order,
                value=min_value_made,
            ))

        if do_rec_items_releases:
            if Launch_item_order_view.objects.filter(parent=item).count() > 0:
                self.rec_items_releases(
                    launches_values=launches_values,
                    user=user,
                )

    def get_prev_tech_operation(self, production_operation_num, production_order):
        from kaf_pas.planing.models.production_order_opers import Production_order_opers
        self.all_operations = list(Production_order_opers.objects.filter(
            parent_id=production_order.id,
            deleted_at=None).order_by('production_operation_num'))  # !! Не менять на parent  у Production_order_opers его нет, есть тольо parent_id
        idx = production_operation_num - 2
        if idx >= 0:
            return self.all_operations[production_operation_num - 2]
        else:
            return None

    warnings = Stack()

    def makeAll(self, data, user, lock=True):
        from decimal import Decimal
        from django.conf import settings
        from django.db.models import Min
        from isc_common.common.functions import ExecuteStoredProc
        from isc_common.number import DecimalToStr
        from isc_common.number import IntToDecimal
        from kaf_pas.planing.models.production_order_opers import Production_order_opers
        from kaf_pas.planing.models.production_order_values import Production_order_valuesManager
        from kaf_pas.planing.models.production_order_opers_per_launch import Production_order_opers_per_launch

        self.warnings.clear()

        data = Production_orderWrapper(**data)
        if isinstance(data.value, int):
            value = IntToDecimal(data.value)
        elif isinstance(data.value, Decimal):
            value = data.value
        else:
            raise Exception('value mast be int or Decimal type.')

        operations = data.operations
        operations_ids = list(map(lambda x: x.id, operations))

        # Первая операция в технологичской цепочке
        first_production_order_oper = operations[0]

        # Задание на производство
        production_order = first_production_order_oper.parent

        # Товарная позиция
        item = first_production_order_oper.item

        # Запуск верхний (шапка)
        parent_launch = first_production_order_oper.launch

        # Все операции технологичской цепочки
        all_operations = list(Production_order_opers.objects.filter(parent_id=production_order.id, deleted_at=None).order_by('production_operation_num'))  # !! Не менять на parent  у Production_order_opers его нет, есть тольо parent_id

        key = f'Production_order_valuesManager.makeAll_{production_order.id}'
        if lock:
            settings.LOCKS.acquire(key)

        try:
            # ========================================Проверяем заполнение предыдущей операции===================================================
            for operation in operations:
                if operation.production_operation_num != 1:
                    value_previos = ExecuteStoredProc('get_previos_operation_value', [production_order.id, operation.production_operation_num])
                    value_curent = ExecuteStoredProc('get_previos_operation_value1', [production_order.id, operation.production_operation_num])

                    value_enabled = value_previos - value_curent
                    if value_enabled < value:
                        if lock:
                            settings.LOCKS.release(key)
                        raise Exception(f'Не достаточно выпуска в предыдущей операции № п/п {operation.production_operation_num}. Возможное количество {DecimalToStr(value_enabled)}')

                    if data.color != None:
                        value_on_coors = ExecuteStoredProc('get_operation_colors_qty1', [production_order.id, first_production_order_oper.id, data.color.id])
                        if value_on_coors != None and ToDecimal(value_on_coors) < value:
                            if lock:
                                settings.LOCKS.release(key)
                            Production_order_valuesManager.fullRows()
                            raise Exception(f'Не достаточно изделий данного цвета. Возможное количество {DecimalToStr(value_on_coors)}')

                break
            # ===================================================================================================================================

            # ========================================Проверяем на выбор сплошного сегмента операций===================================================
            old_num = None
            for operation in operations:
                if old_num != None:
                    if old_num != operation.production_operation_num - 1:
                        if lock:
                            settings.LOCKS.release(key)
                        raise Exception('Выбран не сплошной сегмент операций.')
                old_num = operation.production_operation_num
            # ===================================================================================================================================

            # ===============================Проверяем остатки по всем выбраным операциям  чтобы были не меньше вводимой величины================
            min_value_made = Production_order_opers.objects.filter(
                parent_id=production_order.id,
                id__in=operations_ids).aggregate(Min('value_odd')).get('value_odd__min')

            if min_value_made < value:
                if lock:
                    settings.LOCKS.release(key)
                Production_order_valuesManager.fullRows()
                raise Exception(f'Превышение количества остатка (Запущено - Выполнено). Максимально возможное: {DecimalToStr(min_value_made)}')
            else:
                min_value_made = value
            # ===================================================================================================================================

            # ===============================Записываем выполнение выбранных операций =================================================================
            first_step = True

            for operation in operations:
                # Получаем предыдущую техноглогическую операцию
                prev_tech_operation = self.get_prev_tech_operation(
                    production_operation_num=operation.production_operation_num,
                    production_order=production_order
                )

                do_rec_items_releases = False
                # Вычисляем необходимость вычета комплектующих если эта операция поглощающая
                if do_rec_items_releases == False and operation.production_operation.is_absorption:
                    do_rec_items_releases = True

                # или последняя в технологической цепочке
                # Необходимость выполнеия отгрузки
                if operation.production_operation_num == all_operations[-1].production_operation_num:
                    r = list(filter(lambda x: x.production_operation.is_absorption, filter(lambda x: x.production_operation_num != operation.production_operation_num, all_operations)))
                    do_rec_items_releases = len(r) == 0
                    # do_rec_order_releases = True

                if operation.production_operation.is_launched and data.launch != None and first_step:
                    if data.launch.code == NoLaunch:
                        value_odd = value
                    else:
                        value_odd = Production_order_opers_per_launch.objects.filter(
                            parent_id=production_order.id,
                            launch=data.launch,
                            production_operation=operation.production_operation).value_odd()

                    first_step = False
                    if value_odd < value:
                        if data.color != None:
                            raise Exception(f'Превышение остатка, по запуску {data.launch.code} от {DateToStr(data.launch.date)}, в операции {operation.production_operation.full_name}, возможное количество: {DecimalToStr(value_odd)}')
                        else:
                            raise Exception(f'Превышение остатка, по запуску {data.launch.code} от {DateToStr(data.launch.date)}, в операции {operation.production_operation.full_name}, возможное количество: {DecimalToStr(value_odd)}')

                # Записываем действия по выполнению
                self.make_launch_release(
                    prev_tech_operation=prev_tech_operation,
                    this_tech_operation=operation,
                    data=data,
                    item=item,
                    production_order=production_order,
                    min_value_made=min_value_made,
                    parent_launch=parent_launch,
                    user=user,
                    do_rec_items_releases=do_rec_items_releases,
                    # do_rec_order_releases=do_rec_order_releases,
                )

            # ===================================================================================================================================

            if lock:
                settings.LOCKS.release(key)

            # выводим предупридительные сообщения, или прекращаем выполнение оперраций
            if self.warnings.size() > 0:
                if not self.enableMinus:
                    raise Exception('\n'.join(self.warnings))
                else:
                    from isc_common.ws.webSocket import WebSocket
                    WebSocket.send_warning_message(
                        host=settings.WS_HOST,
                        port=settings.WS_PORT,
                        channel=f'common_{user.username}',
                        message='<br/><br/>'.join(self.warnings),
                        logger=logger
                    )

        except Exception as ex:
            if lock:
                settings.LOCKS.release(key)
                Production_order_valuesManager.fullRows()
            raise ex

        return production_order, all_operations

    def delete_minus_operation(self, operation):
        from kaf_pas.planing.models.operation_refs import Operation_refs
        from kaf_pas.planing.operation_typesStack import MADE_OPRS_MNS_TSK

        # MADE_OPRS_MNS_TSK, - Удалаляем минусующую операцию
        for operation_ref in Operation_refs.objects.filter(
                child=operation,
                props=Operation_refs.props.product_making,
                parent__opertype__code__in=[
                    MADE_OPRS_MNS_TSK,
                ]):
            # Operation_refs.objects.delete_m2m(operation_refs=operation_ref)
            self.delete_operation(operation=operation_ref.parent, check=False)

            deleted = operation_ref.delete()
            logger.debug(f'deleted: {deleted}')

            # Удаляем минусующую операциею
            logger.debug(f'operation_ref.parent: {operation_ref.parent}')
            deleted = operation_ref.parent.delete()
            logger.debug(f'deleted: {deleted}')

    def delete_operation(self, operation, check=True):
        from kaf_pas.planing.models.operation_refs import Operation_refs
        from kaf_pas.planing.operation_typesStack import DETAIL_OPERS_PRD_TSK, MADE_OPRS_PLS_TSK, PRD_TSK
        from kaf_pas.planing.models.production_order_opers import Production_order_opers

        if check:
            parent = Operation_refs.objects.filter(child=operation, parent__opertype__code__in=[DETAIL_OPERS_PRD_TSK])[0].parent
            detail_order_opers_operation = Production_order_opers.objects.get(id=parent.id)
            value_made = detail_order_opers_operation.value_made

            value_query = Production_order_values.objects.filter(id=operation.id, opertype__code__in=[MADE_OPRS_PLS_TSK])
            if value_query.count() > 0:
                value = value_query[0].value
            else:
                value = 0

            order_operation = Operation_refs.objects.filter(child=parent, parent__opertype__code__in=[PRD_TSK])[0].parent
            detail_order_opers_operations = [Production_order_opers.objects.get(id=operation_refs.child.id) for operation_refs in Operation_refs.objects.filter(parent=order_operation, child__opertype__code__in=[DETAIL_OPERS_PRD_TSK])]
            detail_order_opers_operation_next = [dt for dt in detail_order_opers_operations if dt.production_operation_num == detail_order_opers_operation.production_operation_num + 1]
            value_made_next = detail_order_opers_operation_next[0].value_made if len(detail_order_opers_operation_next) > 0 else 0

            if value_made - value_made_next < value:
                raise Exception(f'Сумму: {DecimalToStr(value)} удалить не могу т.к. она уже была использована в последующей операции. Максимально возможная сумма к удалению {DecimalToStr(value_made - value_made_next)}')

        # Связи с релизами
        # RELEASE_TSK_PLS - выпуск изделия
        # MADE_OPRS_MNS_TSK - расход комплектующих
        for release_items in Operation_refs.objects.filter(parent=operation, child__opertype__code__in=[MADE_OPRS_MNS_TSK]):
            deleted = release_items.delete()
            logger.debug(f'deleted: {deleted}')

            for child_release_items in Operation_refs.objects.filter(child=release_items.child, parent__opertype__code__in=[PRD_TSK, DETAIL_OPERS_PRD_TSK]):
                deleted = child_release_items.delete()
                logger.debug(f'deleted: {deleted}')

            self.delete_minus_operation(operation=release_items.child)
            deleted = release_items.child.delete()
            logger.debug(f'deleted: {deleted}')

        self.delete_minus_operation(operation=operation)

        # DETAIL_OPERS_PRD_TSK - Связь с операцией по которой сделано это ввполнение
        # MADE_OPRS_PLS_TSK  - Связь с родительским выполнением
        for operation_ref in Operation_refs.objects.filter(
                child=operation,
                props=Operation_refs.props.product_making,
                parent__opertype__code__in=[
                    MADE_OPRS_PLS_TSK,
                    DETAIL_OPERS_PRD_TSK
                ]):
            deleted = operation_ref.delete()
            logger.debug(f'deleted: {deleted}')

    def delete_sums(self, operations, func_refreshed=None, parent=None):
        from django.conf import settings

        res = 0

        for operation in operations:
            key = f'Production_order_valuesManager.delete_sums_{operation.id}'
            try:
                settings.LOCKS.acquire(key)

                self.delete_operation(operation=operation)

                deleted, _ = operation.delete()
                res += deleted

                if callable(func_refreshed):
                    func_refreshed()

                settings.LOCKS.release(key)

            except ProtectedError as ex:
                settings.LOCKS.release(key)
                raise ex

            except Exception as ex:
                settings.LOCKS.release(key)
                raise ex

        return res
