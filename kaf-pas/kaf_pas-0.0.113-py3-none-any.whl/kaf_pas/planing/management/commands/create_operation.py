import logging

from django.core.management import BaseCommand

from isc_common.auth.models.user import User
from kaf_pas.planing.models.production_ext import Production_ext

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        data = {'parentRecord': {'creator__short_name': 'admin A A', 'date': '2020-08-07T14:56:35.131', 'description': None, 'edizm__name': None, 'id': 344518, 'item_id': 3173271, 'parent_item_id': 3302032, 'item__STMP_1__value_str': 'Гайка М8-6Н.5.019 ГОСТ 3032-76', 'item__STMP_2__value_str': None,
                                 'launch_id': 226, 'launch__code': '2020 / 08 / 1', 'launch__date': '2020-08-07T14:44:31.000', 'location_sector_ids': [64], 'location_sectors_full_name': '<font color="#00CCFF"</font>/ Завод / Цех №5 / Токарный участок', 'num': '805', 'isFolder': False,
                                 'cnt_opers': 1, 'value_sum': '20', 'value1_sum': '1', 'value1_sum_len': 1, 'value_made': '', 'value_made_str': '<b><div><strong><font color="blue"</font></strong></div></b>(0.00%)', 'value_start': '', 'value_odd': '0',
                                 'opertype__full_name': '/Задание на производство', 'opertype_id': 2, 'parent_id': None, 'status__code': 'new', 'status__name': '<div><strong><font color="blue"</font>Новый (с)</strong></div>', 'status_id': 3, 'isDeleted': False, 'creator_id': None, '_hmarker': None,
                                 '_recordComponents_isc_ListGrid_1': {'_rowNumberField': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, '_expansionField': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1},
                                                                      'launch__code': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'launch__date': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1},
                                                                      'num': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'date': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1},
                                                                      'status__name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'item__STMP_1__value_str': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1},
                                                                      'item__STMP_2__value_str': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1},
                                                                      'location_sectors_full_name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'cnt_opers': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1},
                                                                      'value_sum': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'value1_sum': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1},
                                                                      'value_start': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'value_made_str': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1},
                                                                      'edizm__name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'isDeleted': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1},
                                                                      'creator__short_name': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}, 'description': {'isNullMarker': True, '_embedBody': 'isc_ListGrid_1_body', '_recordComponentBatch': 1}},
                                 '_selection_29': True, '_embeddedComponents_isc_ListGrid_1': ['isc_ListGrid_1_expansionLayout'], '_expanded_isc_ListGrid_1': True, '_hasExpansionComponent_isc_ListGrid_1': True},
                'production_operation__full_name': '/Транспортировки/Транспортировочные операции линии покраски(514)/Транспортировка Линия покраски (514) - ПДО (710)', 'production_operation_edizm__name': None, 'location__full_name': None, 'production_operation_color__name': None,
                'location_fin__full_name': None, 'resource__name': None, 'resource_fin__name': None, 'production_operation_id': 231, 'production_operation_num': 2}

        old_data = None

        production_ext = Production_ext()
        production_ext.update_operation(data=data, old_data=old_data, user=User.objects.get(id=2))

        print('Done.')
