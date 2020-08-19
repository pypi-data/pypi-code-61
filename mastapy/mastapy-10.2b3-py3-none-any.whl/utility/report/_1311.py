'''_1311.py

DynamicCustomReportItem
'''


from mastapy._internal import constructor
from mastapy.utility.report import (
    _1292, _1275, _1280, _1281,
    _1282, _1283, _1284, _1285,
    _1287, _1288, _1289, _1290,
    _1291, _1293, _1295, _1296,
    _1299, _1300, _1301, _1303,
    _1304, _1305, _1306, _1308,
    _1309
)
from mastapy.shafts import _20
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical import _791
from mastapy.utility_gui.charts import _1512, _1513
from mastapy.bearings.bearing_results import _1583, _1586, _1594
from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2378
from mastapy.system_model.analyses_and_results.parametric_study_tools import _3570
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4858, _4862
from mastapy._internal.python_net import python_net_import

_DYNAMIC_CUSTOM_REPORT_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'DynamicCustomReportItem')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicCustomReportItem',)


class DynamicCustomReportItem(_1300.CustomReportNameableItem):
    '''DynamicCustomReportItem

    This is a mastapy class.
    '''

    TYPE = _DYNAMIC_CUSTOM_REPORT_ITEM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DynamicCustomReportItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_main_report_item(self) -> 'bool':
        '''bool: 'IsMainReportItem' is the original name of this property.'''

        return self.wrapped.IsMainReportItem

    @is_main_report_item.setter
    def is_main_report_item(self, value: 'bool'):
        self.wrapped.IsMainReportItem = bool(value) if value else False

    @property
    def inner_item(self) -> '_1292.CustomReportItem':
        '''CustomReportItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1292.CustomReportItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_shaft_damage_results_table_and_chart(self) -> '_20.ShaftDamageResultsTableAndChart':
        '''ShaftDamageResultsTableAndChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _20.ShaftDamageResultsTableAndChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ShaftDamageResultsTableAndChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_20.ShaftDamageResultsTableAndChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_cylindrical_gear_table_with_mg_charts(self) -> '_791.CylindricalGearTableWithMGCharts':
        '''CylindricalGearTableWithMGCharts: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _791.CylindricalGearTableWithMGCharts.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CylindricalGearTableWithMGCharts. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_791.CylindricalGearTableWithMGCharts)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_ad_hoc_custom_table(self) -> '_1275.AdHocCustomTable':
        '''AdHocCustomTable: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1275.AdHocCustomTable.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to AdHocCustomTable. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1275.AdHocCustomTable)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_chart(self) -> '_1280.CustomChart':
        '''CustomChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1280.CustomChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1280.CustomChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_graphic(self) -> '_1281.CustomGraphic':
        '''CustomGraphic: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1281.CustomGraphic.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomGraphic. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1281.CustomGraphic)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_image(self) -> '_1282.CustomImage':
        '''CustomImage: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1282.CustomImage.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomImage. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1282.CustomImage)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report(self) -> '_1283.CustomReport':
        '''CustomReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1283.CustomReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1283.CustomReport)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_cad_drawing(self) -> '_1284.CustomReportCadDrawing':
        '''CustomReportCadDrawing: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1284.CustomReportCadDrawing.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportCadDrawing. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1284.CustomReportCadDrawing)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_chart(self) -> '_1285.CustomReportChart':
        '''CustomReportChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1285.CustomReportChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1285.CustomReportChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_column(self) -> '_1287.CustomReportColumn':
        '''CustomReportColumn: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1287.CustomReportColumn.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportColumn. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1287.CustomReportColumn)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_columns(self) -> '_1288.CustomReportColumns':
        '''CustomReportColumns: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1288.CustomReportColumns.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportColumns. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1288.CustomReportColumns)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_definition_item(self) -> '_1289.CustomReportDefinitionItem':
        '''CustomReportDefinitionItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1289.CustomReportDefinitionItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportDefinitionItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1289.CustomReportDefinitionItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_horizontal_line(self) -> '_1290.CustomReportHorizontalLine':
        '''CustomReportHorizontalLine: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1290.CustomReportHorizontalLine.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportHorizontalLine. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1290.CustomReportHorizontalLine)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_html_item(self) -> '_1291.CustomReportHtmlItem':
        '''CustomReportHtmlItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1291.CustomReportHtmlItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportHtmlItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1291.CustomReportHtmlItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_item_container(self) -> '_1293.CustomReportItemContainer':
        '''CustomReportItemContainer: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1293.CustomReportItemContainer.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainer. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1293.CustomReportItemContainer)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_item_container_collection_base(self) -> '_1295.CustomReportItemContainerCollectionBase':
        '''CustomReportItemContainerCollectionBase: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1295.CustomReportItemContainerCollectionBase.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainerCollectionBase. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1295.CustomReportItemContainerCollectionBase)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_item_container_collection_item(self) -> '_1296.CustomReportItemContainerCollectionItem':
        '''CustomReportItemContainerCollectionItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1296.CustomReportItemContainerCollectionItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainerCollectionItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1296.CustomReportItemContainerCollectionItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_multi_property_item_base(self) -> '_1299.CustomReportMultiPropertyItemBase':
        '''CustomReportMultiPropertyItemBase: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1299.CustomReportMultiPropertyItemBase.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportMultiPropertyItemBase. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1299.CustomReportMultiPropertyItemBase)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_nameable_item(self) -> '_1300.CustomReportNameableItem':
        '''CustomReportNameableItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1300.CustomReportNameableItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportNameableItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1300.CustomReportNameableItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_named_item(self) -> '_1301.CustomReportNamedItem':
        '''CustomReportNamedItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1301.CustomReportNamedItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportNamedItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1301.CustomReportNamedItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_status_item(self) -> '_1303.CustomReportStatusItem':
        '''CustomReportStatusItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1303.CustomReportStatusItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportStatusItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1303.CustomReportStatusItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_tab(self) -> '_1304.CustomReportTab':
        '''CustomReportTab: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1304.CustomReportTab.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportTab. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1304.CustomReportTab)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_tabs(self) -> '_1305.CustomReportTabs':
        '''CustomReportTabs: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1305.CustomReportTabs.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportTabs. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1305.CustomReportTabs)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_report_text(self) -> '_1306.CustomReportText':
        '''CustomReportText: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1306.CustomReportText.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportText. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1306.CustomReportText)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_sub_report(self) -> '_1308.CustomSubReport':
        '''CustomSubReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1308.CustomSubReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomSubReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1308.CustomSubReport)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_table(self) -> '_1309.CustomTable':
        '''CustomTable: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1309.CustomTable.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomTable. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1309.CustomTable)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_dynamic_custom_report_item(self) -> 'DynamicCustomReportItem':
        '''DynamicCustomReportItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if DynamicCustomReportItem.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to DynamicCustomReportItem. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(DynamicCustomReportItem)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_line_chart(self) -> '_1512.CustomLineChart':
        '''CustomLineChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1512.CustomLineChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomLineChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1512.CustomLineChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_custom_table_and_chart(self) -> '_1513.CustomTableAndChart':
        '''CustomTableAndChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1513.CustomTableAndChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomTableAndChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1513.CustomTableAndChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_loaded_bearing_chart_reporter(self) -> '_1583.LoadedBearingChartReporter':
        '''LoadedBearingChartReporter: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1583.LoadedBearingChartReporter.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedBearingChartReporter. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1583.LoadedBearingChartReporter)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_loaded_bearing_temperature_chart(self) -> '_1586.LoadedBearingTemperatureChart':
        '''LoadedBearingTemperatureChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1586.LoadedBearingTemperatureChart.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedBearingTemperatureChart. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1586.LoadedBearingTemperatureChart)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_loaded_roller_element_chart_reporter(self) -> '_1594.LoadedRollerElementChartReporter':
        '''LoadedRollerElementChartReporter: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1594.LoadedRollerElementChartReporter.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedRollerElementChartReporter. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_1594.LoadedRollerElementChartReporter)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_shaft_system_deflection_sections_report(self) -> '_2378.ShaftSystemDeflectionSectionsReport':
        '''ShaftSystemDeflectionSectionsReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2378.ShaftSystemDeflectionSectionsReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ShaftSystemDeflectionSectionsReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_2378.ShaftSystemDeflectionSectionsReport)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_parametric_study_histogram(self) -> '_3570.ParametricStudyHistogram':
        '''ParametricStudyHistogram: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3570.ParametricStudyHistogram.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ParametricStudyHistogram. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_3570.ParametricStudyHistogram)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_campbell_diagram_report(self) -> '_4858.CampbellDiagramReport':
        '''CampbellDiagramReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4858.CampbellDiagramReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CampbellDiagramReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_4858.CampbellDiagramReport)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None

    @property
    def inner_item_of_type_per_mode_results_report(self) -> '_4862.PerModeResultsReport':
        '''PerModeResultsReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _4862.PerModeResultsReport.TYPE not in self.wrapped.InnerItem.__class__.__mro__:
            raise CastException('Failed to cast inner_item to PerModeResultsReport. Expected: {}.'.format(self.wrapped.InnerItem.__class__.__qualname__))

        return constructor.new(_4862.PerModeResultsReport)(self.wrapped.InnerItem) if self.wrapped.InnerItem else None
