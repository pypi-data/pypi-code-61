#!/usr/bin/env Python
# coding=utf-8#
#!/usr/bin/env Python
# coding=utf-8#
#作者： tony
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from CityMaker_SDK.SDK.Common.IBinaryBuffer import IBinaryBuffer
IBinaryBuffer=IBinaryBuffer
from CityMaker_SDK.SDK.Common.ICoordSysDialog import ICoordSysDialog
ICoordSysDialog=ICoordSysDialog
from CityMaker_SDK.SDK.Common.IDoubleArray import IDoubleArray
IDoubleArray=IDoubleArray
from CityMaker_SDK.SDK.Common.IFloatArray import IFloatArray
IFloatArray=IFloatArray
from CityMaker_SDK.SDK.Common.ILicenseServer import ILicenseServer
ILicenseServer=ILicenseServer
from CityMaker_SDK.SDK.Common.IPropertySet import IPropertySet
IPropertySet=IPropertySet
from CityMaker_SDK.SDK.Common.IRuntimeInfo import IRuntimeInfo
IRuntimeInfo=IRuntimeInfo
from CityMaker_SDK.SDK.Common.IUInt16Array import IUInt16Array
IUInt16Array=IUInt16Array
from CityMaker_SDK.SDK.Common.IUInt32Array import IUInt32Array
IUInt32Array=IUInt32Array
from CityMaker_SDK.SDK.FdeCore.FeatureDataSet import FeatureDataSet
FeatureDataSet=FeatureDataSet
from CityMaker_SDK.SDK.FdeCore.IAttachment import IAttachment
IAttachment=IAttachment
from CityMaker_SDK.SDK.FdeCore.IAttachmentCollection import IAttachmentCollection
IAttachmentCollection=IAttachmentCollection
from CityMaker_SDK.SDK.FdeCore.IAttachmentManager import IAttachmentManager
IAttachmentManager=IAttachmentManager
from CityMaker_SDK.SDK.FdeCore.ICheckIn import ICheckIn
ICheckIn=ICheckIn
from CityMaker_SDK.SDK.FdeCore.ICheckOut import ICheckOut
ICheckOut=ICheckOut
from CityMaker_SDK.SDK.FdeCore.ICodedValueDomain import ICodedValueDomain
ICodedValueDomain=ICodedValueDomain
from CityMaker_SDK.SDK.FdeCore.IConflict import IConflict
IConflict=IConflict
from CityMaker_SDK.SDK.FdeCore.IConnectionInfo import IConnectionInfo
IConnectionInfo=IConnectionInfo
from CityMaker_SDK.SDK.FdeCore.IDataSource import IDataSource
IDataSource=IDataSource
from CityMaker_SDK.SDK.FdeCore.IDataSourceFactory import IDataSourceFactory
IDataSourceFactory=IDataSourceFactory
from CityMaker_SDK.SDK.FdeCore.IDataSourcePluginManager import IDataSourcePluginManager
IDataSourcePluginManager=IDataSourcePluginManager
from CityMaker_SDK.SDK.FdeCore.IDbIndexInfo import IDbIndexInfo
IDbIndexInfo=IDbIndexInfo
from CityMaker_SDK.SDK.FdeCore.IDbIndexInfoCollection import IDbIndexInfoCollection
IDbIndexInfoCollection=IDbIndexInfoCollection
from CityMaker_SDK.SDK.FdeCore.IDomain import IDomain
IDomain=IDomain
from CityMaker_SDK.SDK.FdeCore.IDomainFactory import IDomainFactory
IDomainFactory=IDomainFactory
from CityMaker_SDK.SDK.FdeCore.IEnumResName import IEnumResName
IEnumResName=IEnumResName
from CityMaker_SDK.SDK.FdeCore.IFdeCursor import IFdeCursor
IFdeCursor=IFdeCursor
from CityMaker_SDK.SDK.FdeCore.IFeatureClass import IFeatureClass
IFeatureClass=IFeatureClass
from CityMaker_SDK.SDK.FdeCore.IFeatureClassQuery import IFeatureClassQuery
IFeatureClassQuery=IFeatureClassQuery
from CityMaker_SDK.SDK.FdeCore.IFeatureDataSet import IFeatureDataSet
IFeatureDataSet=IFeatureDataSet
from CityMaker_SDK.SDK.FdeCore.IFeatureProgress import IFeatureProgress
IFeatureProgress=IFeatureProgress
from CityMaker_SDK.SDK.FdeCore.IFieldDomainInfo import IFieldDomainInfo
IFieldDomainInfo=IFieldDomainInfo
from CityMaker_SDK.SDK.FdeCore.IFieldInfo import IFieldInfo
IFieldInfo=IFieldInfo
from CityMaker_SDK.SDK.FdeCore.IFieldInfoCollection import IFieldInfoCollection
IFieldInfoCollection=IFieldInfoCollection
from CityMaker_SDK.SDK.FdeCore.IGeometryDef import IGeometryDef
IGeometryDef=IGeometryDef
from CityMaker_SDK.SDK.FdeCore.IGridIndexInfo import IGridIndexInfo
IGridIndexInfo=IGridIndexInfo
from CityMaker_SDK.SDK.FdeCore.IIndexInfo import IIndexInfo
IIndexInfo=IIndexInfo
from CityMaker_SDK.SDK.FdeCore.IIndexInfoCollection import IIndexInfoCollection
IIndexInfoCollection=IIndexInfoCollection
from CityMaker_SDK.SDK.FdeCore.IObjectClass import IObjectClass
IObjectClass=IObjectClass
from CityMaker_SDK.SDK.FdeCore.IQueryDef import IQueryDef
IQueryDef=IQueryDef
from CityMaker_SDK.SDK.FdeCore.IQueryFilter import IQueryFilter
IQueryFilter=IQueryFilter
from CityMaker_SDK.SDK.FdeCore.IRangeDomain import IRangeDomain
IRangeDomain=IRangeDomain
from CityMaker_SDK.SDK.FdeCore.IRenderIndexInfo import IRenderIndexInfo
IRenderIndexInfo=IRenderIndexInfo
from CityMaker_SDK.SDK.FdeCore.IReplication import IReplication
IReplication=IReplication
from CityMaker_SDK.SDK.FdeCore.IReplicationFactory import IReplicationFactory
IReplicationFactory=IReplicationFactory
from CityMaker_SDK.SDK.FdeCore.IResourceManager import IResourceManager
IResourceManager=IResourceManager
from CityMaker_SDK.SDK.FdeCore.IRowBuffer import IRowBuffer
IRowBuffer=IRowBuffer
from CityMaker_SDK.SDK.FdeCore.IRowBufferCollection import IRowBufferCollection
IRowBufferCollection=IRowBufferCollection
from CityMaker_SDK.SDK.FdeCore.IRowBufferFactory import IRowBufferFactory
IRowBufferFactory=IRowBufferFactory
from CityMaker_SDK.SDK.FdeCore.ISpatialFilter import ISpatialFilter
ISpatialFilter=ISpatialFilter
from CityMaker_SDK.SDK.FdeCore.ISQLCheck import ISQLCheck
ISQLCheck=ISQLCheck
from CityMaker_SDK.SDK.FdeCore.ISubTypeInfo import ISubTypeInfo
ISubTypeInfo=ISubTypeInfo
from CityMaker_SDK.SDK.FdeCore.ITable import ITable
ITable=ITable
from CityMaker_SDK.SDK.FdeCore.ITemporalCursor import ITemporalCursor
ITemporalCursor=ITemporalCursor
from CityMaker_SDK.SDK.FdeCore.ITemporalFilter import ITemporalFilter
ITemporalFilter=ITemporalFilter
from CityMaker_SDK.SDK.FdeCore.ITemporalInstance import ITemporalInstance
ITemporalInstance=ITemporalInstance
from CityMaker_SDK.SDK.FdeCore.ITemporalInstanceCursor import ITemporalInstanceCursor
ITemporalInstanceCursor=ITemporalInstanceCursor
from CityMaker_SDK.SDK.FdeCore.ITemporalManager import ITemporalManager
ITemporalManager=ITemporalManager
from CityMaker_SDK.SDK.FdeCore.ITools import ITools
ITools=ITools
from CityMaker_SDK.SDK.FdeGeometry.CirculeArc import CirculeArc
CirculeArc=CirculeArc
from CityMaker_SDK.SDK.FdeGeometry.ClosedTriMesh import ClosedTriMesh
ClosedTriMesh=ClosedTriMesh
from CityMaker_SDK.SDK.FdeGeometry.ICircle import ICircle
ICircle=ICircle
from CityMaker_SDK.SDK.FdeGeometry.ICirculeArc import ICirculeArc
ICirculeArc=ICirculeArc
from CityMaker_SDK.SDK.FdeGeometry.IClosedTriMesh import IClosedTriMesh
IClosedTriMesh=IClosedTriMesh
from CityMaker_SDK.SDK.FdeGeometry.ICompoundLine import ICompoundLine
ICompoundLine=ICompoundLine
from CityMaker_SDK.SDK.FdeGeometry.ICoordinateReferenceSystem import ICoordinateReferenceSystem
ICoordinateReferenceSystem=ICoordinateReferenceSystem
from CityMaker_SDK.SDK.FdeGeometry.ICoordinateTransformer import ICoordinateTransformer
ICoordinateTransformer=ICoordinateTransformer
from CityMaker_SDK.SDK.FdeGeometry.ICRSFactory import ICRSFactory
ICRSFactory=ICRSFactory
from CityMaker_SDK.SDK.FdeGeometry.ICurve import ICurve
ICurve=ICurve
from CityMaker_SDK.SDK.FdeGeometry.IEastNorthUpCRS import IEastNorthUpCRS
IEastNorthUpCRS=IEastNorthUpCRS
from CityMaker_SDK.SDK.FdeGeometry.IGeographicCRS import IGeographicCRS
IGeographicCRS=IGeographicCRS
from CityMaker_SDK.SDK.FdeGeometry.IGeometry import IGeometry
IGeometry=IGeometry
from CityMaker_SDK.SDK.FdeGeometry.IGeometryCollection import IGeometryCollection
IGeometryCollection=IGeometryCollection
from CityMaker_SDK.SDK.FdeGeometry.IGeometryConvertor import IGeometryConvertor
IGeometryConvertor=IGeometryConvertor
from CityMaker_SDK.SDK.FdeGeometry.IGeometryFactory import IGeometryFactory
IGeometryFactory=IGeometryFactory
from CityMaker_SDK.SDK.FdeGeometry.IGeoTransformer import IGeoTransformer
IGeoTransformer=IGeoTransformer
from CityMaker_SDK.SDK.FdeGeometry.ILine import ILine
ILine=ILine
from CityMaker_SDK.SDK.FdeGeometry.IModelPoint import IModelPoint
IModelPoint=IModelPoint
from CityMaker_SDK.SDK.FdeGeometry.IMultiCurve import IMultiCurve
IMultiCurve=IMultiCurve
from CityMaker_SDK.SDK.FdeGeometry.IMultiPoint import IMultiPoint
IMultiPoint=IMultiPoint
from CityMaker_SDK.SDK.FdeGeometry.IMultiPolygon import IMultiPolygon
IMultiPolygon=IMultiPolygon
from CityMaker_SDK.SDK.FdeGeometry.IMultiPolyline import IMultiPolyline
IMultiPolyline=IMultiPolyline
from CityMaker_SDK.SDK.FdeGeometry.IMultiSurface import IMultiSurface
IMultiSurface=IMultiSurface
from CityMaker_SDK.SDK.FdeGeometry.IMultiTriMesh import IMultiTriMesh
IMultiTriMesh=IMultiTriMesh
from CityMaker_SDK.SDK.FdeGeometry.IParametricModelling import IParametricModelling
IParametricModelling=IParametricModelling
from CityMaker_SDK.SDK.FdeGeometry.IPOI import IPOI
IPOI=IPOI
from CityMaker_SDK.SDK.FdeGeometry.IPoint import IPoint
IPoint=IPoint
from CityMaker_SDK.SDK.FdeGeometry.IPointCloud import IPointCloud
IPointCloud=IPointCloud
from CityMaker_SDK.SDK.FdeGeometry.IPolygon import IPolygon
IPolygon=IPolygon
from CityMaker_SDK.SDK.FdeGeometry.IPolyline import IPolyline
IPolyline=IPolyline
from CityMaker_SDK.SDK.FdeGeometry.IPolynomialTransformer import IPolynomialTransformer
IPolynomialTransformer=IPolynomialTransformer
from CityMaker_SDK.SDK.FdeGeometry.IProjectedCRS import IProjectedCRS
IProjectedCRS=IProjectedCRS
from CityMaker_SDK.SDK.FdeGeometry.IProximityOperator import IProximityOperator
IProximityOperator=IProximityOperator
from CityMaker_SDK.SDK.FdeGeometry.IRelationalOperator2D import IRelationalOperator2D
IRelationalOperator2D=IRelationalOperator2D
from CityMaker_SDK.SDK.FdeGeometry.IRelationalOperator3D import IRelationalOperator3D
IRelationalOperator3D=IRelationalOperator3D
from CityMaker_SDK.SDK.FdeGeometry.IRing import IRing
IRing=IRing
from CityMaker_SDK.SDK.FdeGeometry.ISegment import ISegment
ISegment=ISegment
from CityMaker_SDK.SDK.FdeGeometry.ISpatialCRS import ISpatialCRS
ISpatialCRS=ISpatialCRS
from CityMaker_SDK.SDK.FdeGeometry.ISurface import ISurface
ISurface=ISurface
from CityMaker_SDK.SDK.FdeGeometry.ISurfacePatch import ISurfacePatch
ISurfacePatch=ISurfacePatch
from CityMaker_SDK.SDK.FdeGeometry.ITerrainAnalyse import ITerrainAnalyse
ITerrainAnalyse=ITerrainAnalyse
from CityMaker_SDK.SDK.FdeGeometry.ITopoDirectedEdge import ITopoDirectedEdge
ITopoDirectedEdge=ITopoDirectedEdge
from CityMaker_SDK.SDK.FdeGeometry.ITopoFacet import ITopoFacet
ITopoFacet=ITopoFacet
from CityMaker_SDK.SDK.FdeGeometry.ITopologicalOperator2D import ITopologicalOperator2D
ITopologicalOperator2D=ITopologicalOperator2D
from CityMaker_SDK.SDK.FdeGeometry.ITopologicalOperator3D import ITopologicalOperator3D
ITopologicalOperator3D=ITopologicalOperator3D
from CityMaker_SDK.SDK.FdeGeometry.ITopoNode import ITopoNode
ITopoNode=ITopoNode
from CityMaker_SDK.SDK.FdeGeometry.ITransform import ITransform
ITransform=ITransform
from CityMaker_SDK.SDK.FdeGeometry.ITriMesh import ITriMesh
ITriMesh=ITriMesh
from CityMaker_SDK.SDK.FdeGeometry.IUnknownCRS import IUnknownCRS
IUnknownCRS=IUnknownCRS
from CityMaker_SDK.SDK.FdeGeometry.Line import Line
Line=Line
from CityMaker_SDK.SDK.FdeGeometry.MultiPoint import MultiPoint
MultiPoint=MultiPoint
from CityMaker_SDK.SDK.FdeGeometry.Point import Point
Point=Point
from CityMaker_SDK.SDK.FdeGeometry.Polygon import Polygon
Polygon=Polygon
from CityMaker_SDK.SDK.FdeGeometry.Polyline import Polyline
Polyline=Polyline
from CityMaker_SDK.SDK.Global.IGlobal import IGlobal
IGlobal=IGlobal
from CityMaker_SDK.SDK.Math.IEnvelope import IEnvelope
IEnvelope=IEnvelope
from CityMaker_SDK.SDK.Math.IEulerAngle import IEulerAngle
IEulerAngle=IEulerAngle
from CityMaker_SDK.SDK.Math.IMatrix import IMatrix
IMatrix=IMatrix
from CityMaker_SDK.SDK.Math.IVector3 import IVector3
IVector3=IVector3
from CityMaker_SDK.SDK.Network.IEdgeBarrier import IEdgeBarrier
IEdgeBarrier=IEdgeBarrier
from CityMaker_SDK.SDK.Network.IEdgeNetworkSource import IEdgeNetworkSource
IEdgeNetworkSource=IEdgeNetworkSource
from CityMaker_SDK.SDK.Network.IJunctionBarrier import IJunctionBarrier
IJunctionBarrier=IJunctionBarrier
from CityMaker_SDK.SDK.Network.IJunctionNetworkSource import IJunctionNetworkSource
IJunctionNetworkSource=IJunctionNetworkSource
from CityMaker_SDK.SDK.Network.ILogicalNetwork import ILogicalNetwork
ILogicalNetwork=ILogicalNetwork
from CityMaker_SDK.SDK.Network.INetwork import INetwork
INetwork=INetwork
from CityMaker_SDK.SDK.Network.INetworkAttribute import INetworkAttribute
INetworkAttribute=INetworkAttribute
from CityMaker_SDK.SDK.Network.INetworkBarrier import INetworkBarrier
INetworkBarrier=INetworkBarrier
from CityMaker_SDK.SDK.Network.INetworkClosestFacilitySolver import INetworkClosestFacilitySolver
INetworkClosestFacilitySolver=INetworkClosestFacilitySolver
from CityMaker_SDK.SDK.Network.INetworkConstantEvaluator import INetworkConstantEvaluator
INetworkConstantEvaluator=INetworkConstantEvaluator
from CityMaker_SDK.SDK.Network.INetworkEdge import INetworkEdge
INetworkEdge=INetworkEdge
from CityMaker_SDK.SDK.Network.INetworkEdgeCollection import INetworkEdgeCollection
INetworkEdgeCollection=INetworkEdgeCollection
from CityMaker_SDK.SDK.Network.INetworkElement import INetworkElement
INetworkElement=INetworkElement
from CityMaker_SDK.SDK.Network.INetworkElementCollection import INetworkElementCollection
INetworkElementCollection=INetworkElementCollection
from CityMaker_SDK.SDK.Network.INetworkEvaluator import INetworkEvaluator
INetworkEvaluator=INetworkEvaluator
from CityMaker_SDK.SDK.Network.INetworkEventLocation import INetworkEventLocation
INetworkEventLocation=INetworkEventLocation
from CityMaker_SDK.SDK.Network.INetworkFieldEvaluator import INetworkFieldEvaluator
INetworkFieldEvaluator=INetworkFieldEvaluator
from CityMaker_SDK.SDK.Network.INetworkFindAncestorsSolver import INetworkFindAncestorsSolver
INetworkFindAncestorsSolver=INetworkFindAncestorsSolver
from CityMaker_SDK.SDK.Network.INetworkFindConnectedSolver import INetworkFindConnectedSolver
INetworkFindConnectedSolver=INetworkFindConnectedSolver
from CityMaker_SDK.SDK.Network.INetworkFindDisconnectedSolver import INetworkFindDisconnectedSolver
INetworkFindDisconnectedSolver=INetworkFindDisconnectedSolver
from CityMaker_SDK.SDK.Network.INetworkFindLoopsSolver import INetworkFindLoopsSolver
INetworkFindLoopsSolver=INetworkFindLoopsSolver
from CityMaker_SDK.SDK.Network.INetworkJunction import INetworkJunction
INetworkJunction=INetworkJunction
from CityMaker_SDK.SDK.Network.INetworkLoader import INetworkLoader
INetworkLoader=INetworkLoader
from CityMaker_SDK.SDK.Network.INetworkLocation import INetworkLocation
INetworkLocation=INetworkLocation
from CityMaker_SDK.SDK.Network.INetworkManager import INetworkManager
INetworkManager=INetworkManager
from CityMaker_SDK.SDK.Network.INetworkRoute import INetworkRoute
INetworkRoute=INetworkRoute
from CityMaker_SDK.SDK.Network.INetworkRouteSegment import INetworkRouteSegment
INetworkRouteSegment=INetworkRouteSegment
from CityMaker_SDK.SDK.Network.INetworkRouteSolver import INetworkRouteSolver
INetworkRouteSolver=INetworkRouteSolver
from CityMaker_SDK.SDK.Network.INetworkScriptEvaluator import INetworkScriptEvaluator
INetworkScriptEvaluator=INetworkScriptEvaluator
from CityMaker_SDK.SDK.Network.INetworkSolver import INetworkSolver
INetworkSolver=INetworkSolver
from CityMaker_SDK.SDK.Network.INetworkSource import INetworkSource
INetworkSource=INetworkSource
from CityMaker_SDK.SDK.Network.INetworkTraceDownstreamSolver import INetworkTraceDownstreamSolver
INetworkTraceDownstreamSolver=INetworkTraceDownstreamSolver
from CityMaker_SDK.SDK.Network.INetworkTraceResult import INetworkTraceResult
INetworkTraceResult=INetworkTraceResult
from CityMaker_SDK.SDK.Network.INetworkTraceUpstreamSolver import INetworkTraceUpstreamSolver
INetworkTraceUpstreamSolver=INetworkTraceUpstreamSolver
from CityMaker_SDK.SDK.RenderControl.AxRenderControl import AxRenderControl
AxRenderControl=AxRenderControl
from CityMaker_SDK.SDK.RenderControl.ComplexParticleEffect import ComplexParticleEffect
ComplexParticleEffect=ComplexParticleEffect
from CityMaker_SDK.SDK.RenderControl.I3DTileLayer import I3DTileLayer
I3DTileLayer=I3DTileLayer
from CityMaker_SDK.SDK.RenderControl.I3DTileLayerPickResult import I3DTileLayerPickResult
I3DTileLayerPickResult=I3DTileLayerPickResult
from CityMaker_SDK.SDK.RenderControl.IAttackArrow import IAttackArrow
IAttackArrow=IAttackArrow
from CityMaker_SDK.SDK.RenderControl.IAttackArrowPickResult import IAttackArrowPickResult
IAttackArrowPickResult=IAttackArrowPickResult
from CityMaker_SDK.SDK.RenderControl.ICacheManager import ICacheManager
ICacheManager=ICacheManager
from CityMaker_SDK.SDK.RenderControl.ICamera import ICamera
ICamera=ICamera
from CityMaker_SDK.SDK.RenderControl.ICameraTour import ICameraTour
ICameraTour=ICameraTour
from CityMaker_SDK.SDK.RenderControl.IClipPlaneOperation import IClipPlaneOperation
IClipPlaneOperation=IClipPlaneOperation
from CityMaker_SDK.SDK.RenderControl.IComparedRenderRule import IComparedRenderRule
IComparedRenderRule=IComparedRenderRule
from CityMaker_SDK.SDK.RenderControl.IComplexParticleEffect import IComplexParticleEffect
IComplexParticleEffect=IComplexParticleEffect
from CityMaker_SDK.SDK.RenderControl.IComplexParticleEffectPickResult import IComplexParticleEffectPickResult
IComplexParticleEffectPickResult=IComplexParticleEffectPickResult
from CityMaker_SDK.SDK.RenderControl.ICurveSymbol import ICurveSymbol
ICurveSymbol=ICurveSymbol
from CityMaker_SDK.SDK.RenderControl.IDoubleArrow import IDoubleArrow
IDoubleArrow=IDoubleArrow
from CityMaker_SDK.SDK.RenderControl.IDoubleArrowPickResult import IDoubleArrowPickResult
IDoubleArrowPickResult=IDoubleArrowPickResult
from CityMaker_SDK.SDK.RenderControl.IDynamicObject import IDynamicObject
IDynamicObject=IDynamicObject
from CityMaker_SDK.SDK.RenderControl.IExportManager import IExportManager
IExportManager=IExportManager
from CityMaker_SDK.SDK.RenderControl.IFeatureClassInfo import IFeatureClassInfo
IFeatureClassInfo=IFeatureClassInfo
from CityMaker_SDK.SDK.RenderControl.IFeatureLayer import IFeatureLayer
IFeatureLayer=IFeatureLayer
from CityMaker_SDK.SDK.RenderControl.IFeatureLayerPickResult import IFeatureLayerPickResult
IFeatureLayerPickResult=IFeatureLayerPickResult
from CityMaker_SDK.SDK.RenderControl.IFeatureManager import IFeatureManager
IFeatureManager=IFeatureManager
from CityMaker_SDK.SDK.RenderControl.IFillStyle import IFillStyle
IFillStyle=IFillStyle
from CityMaker_SDK.SDK.RenderControl.IGatheringPlace import IGatheringPlace
IGatheringPlace=IGatheringPlace
from CityMaker_SDK.SDK.RenderControl.IGatheringPlacePickResult import IGatheringPlacePickResult
IGatheringPlacePickResult=IGatheringPlacePickResult
from CityMaker_SDK.SDK.RenderControl.IGeometryRender import IGeometryRender
IGeometryRender=IGeometryRender
from CityMaker_SDK.SDK.RenderControl.IGeometryRenderScheme import IGeometryRenderScheme
IGeometryRenderScheme=IGeometryRenderScheme
from CityMaker_SDK.SDK.RenderControl.IGeometrySymbol import IGeometrySymbol
IGeometrySymbol=IGeometrySymbol
from CityMaker_SDK.SDK.RenderControl.IHeatMap import IHeatMap
IHeatMap=IHeatMap
from CityMaker_SDK.SDK.RenderControl.IHeatMapPlayer import IHeatMapPlayer
IHeatMapPlayer=IHeatMapPlayer
from CityMaker_SDK.SDK.RenderControl.IHighlightHelper import IHighlightHelper
IHighlightHelper=IHighlightHelper
from CityMaker_SDK.SDK.RenderControl.IHTMLWindow import IHTMLWindow
IHTMLWindow=IHTMLWindow
from CityMaker_SDK.SDK.RenderControl.IImagePointSymbol import IImagePointSymbol
IImagePointSymbol=IImagePointSymbol
from CityMaker_SDK.SDK.RenderControl.IImageryLayer import IImageryLayer
IImageryLayer=IImageryLayer
from CityMaker_SDK.SDK.RenderControl.IKmlGroup import IKmlGroup
IKmlGroup=IKmlGroup
from CityMaker_SDK.SDK.RenderControl.ILabel import ILabel
ILabel=ILabel
from CityMaker_SDK.SDK.RenderControl.ILabelPickResult import ILabelPickResult
ILabelPickResult=ILabelPickResult
from CityMaker_SDK.SDK.RenderControl.ILabelStyle import ILabelStyle
ILabelStyle=ILabelStyle
from CityMaker_SDK.SDK.RenderControl.ILineStyle import ILineStyle
ILineStyle=ILineStyle
from CityMaker_SDK.SDK.RenderControl.IModelPointSymbol import IModelPointSymbol
IModelPointSymbol=IModelPointSymbol
from CityMaker_SDK.SDK.RenderControl.IMotionable import IMotionable
IMotionable=IMotionable
from CityMaker_SDK.SDK.RenderControl.IMotionPath import IMotionPath
IMotionPath=IMotionPath
from CityMaker_SDK.SDK.RenderControl.IObjectEditor import IObjectEditor
IObjectEditor=IObjectEditor
from CityMaker_SDK.SDK.RenderControl.IObjectManager import IObjectManager
IObjectManager=IObjectManager
from CityMaker_SDK.SDK.RenderControl.IObjectTexture import IObjectTexture
IObjectTexture=IObjectTexture
from CityMaker_SDK.SDK.RenderControl.IOperation import IOperation
IOperation=IOperation
from CityMaker_SDK.SDK.RenderControl.IOverlayLabel import IOverlayLabel
IOverlayLabel=IOverlayLabel
from CityMaker_SDK.SDK.RenderControl.IOverlayLabelPickResult import IOverlayLabelPickResult
IOverlayLabelPickResult=IOverlayLabelPickResult
from CityMaker_SDK.SDK.RenderControl.IOverlayUILabel import IOverlayUILabel
IOverlayUILabel=IOverlayUILabel
from CityMaker_SDK.SDK.RenderControl.IParticleEffect import IParticleEffect
IParticleEffect=IParticleEffect
from CityMaker_SDK.SDK.RenderControl.IParticleEffectPickResult import IParticleEffectPickResult
IParticleEffectPickResult=IParticleEffectPickResult
from CityMaker_SDK.SDK.RenderControl.IPickResult import IPickResult
IPickResult=IPickResult
from CityMaker_SDK.SDK.RenderControl.IPickResultCollection import IPickResultCollection
IPickResultCollection=IPickResultCollection
from CityMaker_SDK.SDK.RenderControl.IPlot import IPlot
IPlot=IPlot
from CityMaker_SDK.SDK.RenderControl.IPointCloudSymbol import IPointCloudSymbol
IPointCloudSymbol=IPointCloudSymbol
from CityMaker_SDK.SDK.RenderControl.IPointSymbol import IPointSymbol
IPointSymbol=IPointSymbol
from CityMaker_SDK.SDK.RenderControl.IPolygon3DSymbol import IPolygon3DSymbol
IPolygon3DSymbol=IPolygon3DSymbol
from CityMaker_SDK.SDK.RenderControl.IPosition import IPosition
IPosition=IPosition
from CityMaker_SDK.SDK.RenderControl.IPresentation import IPresentation
IPresentation=IPresentation
from CityMaker_SDK.SDK.RenderControl.IPresentationStep import IPresentationStep
IPresentationStep=IPresentationStep
from CityMaker_SDK.SDK.RenderControl.IPresentationSteps import IPresentationSteps
IPresentationSteps=IPresentationSteps
from CityMaker_SDK.SDK.RenderControl.IProject import IProject
IProject=IProject
from CityMaker_SDK.SDK.RenderControl.IProjectTree import IProjectTree
IProjectTree=IProjectTree
from CityMaker_SDK.SDK.RenderControl.IProjectTreeNode import IProjectTreeNode
IProjectTreeNode=IProjectTreeNode
from CityMaker_SDK.SDK.RenderControl.IRangeRenderRule import IRangeRenderRule
IRangeRenderRule=IRangeRenderRule
from CityMaker_SDK.SDK.RenderControl.IRasterSymbol import IRasterSymbol
IRasterSymbol=IRasterSymbol
from CityMaker_SDK.SDK.RenderControl.IReferencePlane import IReferencePlane
IReferencePlane=IReferencePlane
from CityMaker_SDK.SDK.RenderControl.IReferencePlanePickResult import IReferencePlanePickResult
IReferencePlanePickResult=IReferencePlanePickResult
from CityMaker_SDK.SDK.RenderControl.IRenderable import IRenderable
IRenderable=IRenderable
from CityMaker_SDK.SDK.RenderControl.IRenderArrow import IRenderArrow
IRenderArrow=IRenderArrow
from CityMaker_SDK.SDK.RenderControl.IRenderArrowPickResult import IRenderArrowPickResult
IRenderArrowPickResult=IRenderArrowPickResult
from CityMaker_SDK.SDK.RenderControl.IRenderControl import IRenderControl
IRenderControl=IRenderControl
from CityMaker_SDK.SDK.RenderControl.IRenderControlEvents import IRenderControlEvents
IRenderControlEvents=IRenderControlEvents
from CityMaker_SDK.SDK.RenderControl.IRenderGeometry import IRenderGeometry
IRenderGeometry=IRenderGeometry
from CityMaker_SDK.SDK.RenderControl.IRenderModelPoint import IRenderModelPoint
IRenderModelPoint=IRenderModelPoint
from CityMaker_SDK.SDK.RenderControl.IRenderModelPointPickResult import IRenderModelPointPickResult
IRenderModelPointPickResult=IRenderModelPointPickResult
from CityMaker_SDK.SDK.RenderControl.IRenderMultiPoint import IRenderMultiPoint
IRenderMultiPoint=IRenderMultiPoint
from CityMaker_SDK.SDK.RenderControl.IRenderMultiPointPickResult import IRenderMultiPointPickResult
IRenderMultiPointPickResult=IRenderMultiPointPickResult
from CityMaker_SDK.SDK.RenderControl.IRenderMultiPolygon import IRenderMultiPolygon
IRenderMultiPolygon=IRenderMultiPolygon
from CityMaker_SDK.SDK.RenderControl.IRenderMultiPolygonPickResult import IRenderMultiPolygonPickResult
IRenderMultiPolygonPickResult=IRenderMultiPolygonPickResult
from CityMaker_SDK.SDK.RenderControl.IRenderMultiPolyline import IRenderMultiPolyline
IRenderMultiPolyline=IRenderMultiPolyline
from CityMaker_SDK.SDK.RenderControl.IRenderMultiPolylinePickResult import IRenderMultiPolylinePickResult
IRenderMultiPolylinePickResult=IRenderMultiPolylinePickResult
from CityMaker_SDK.SDK.RenderControl.IRenderMultiTriMesh import IRenderMultiTriMesh
IRenderMultiTriMesh=IRenderMultiTriMesh
from CityMaker_SDK.SDK.RenderControl.IRenderMultiTriMeshPickResult import IRenderMultiTriMeshPickResult
IRenderMultiTriMeshPickResult=IRenderMultiTriMeshPickResult
from CityMaker_SDK.SDK.RenderControl.IRenderPipeLine import IRenderPipeLine
IRenderPipeLine=IRenderPipeLine
from CityMaker_SDK.SDK.RenderControl.IRenderPOI import IRenderPOI
IRenderPOI=IRenderPOI
from CityMaker_SDK.SDK.RenderControl.IRenderPoint import IRenderPoint
IRenderPoint=IRenderPoint
from CityMaker_SDK.SDK.RenderControl.IRenderPointPickResult import IRenderPointPickResult
IRenderPointPickResult=IRenderPointPickResult
from CityMaker_SDK.SDK.RenderControl.IRenderPOIPickResult import IRenderPOIPickResult
IRenderPOIPickResult=IRenderPOIPickResult
from CityMaker_SDK.SDK.RenderControl.IRenderPolygon import IRenderPolygon
IRenderPolygon=IRenderPolygon
from CityMaker_SDK.SDK.RenderControl.IRenderPolygonPickResult import IRenderPolygonPickResult
IRenderPolygonPickResult=IRenderPolygonPickResult
from CityMaker_SDK.SDK.RenderControl.IRenderPolyline import IRenderPolyline
IRenderPolyline=IRenderPolyline
from CityMaker_SDK.SDK.RenderControl.IRenderPolylinePickResult import IRenderPolylinePickResult
IRenderPolylinePickResult=IRenderPolylinePickResult
from CityMaker_SDK.SDK.RenderControl.IRenderRule import IRenderRule
IRenderRule=IRenderRule
from CityMaker_SDK.SDK.RenderControl.IRenderTriMesh import IRenderTriMesh
IRenderTriMesh=IRenderTriMesh
from CityMaker_SDK.SDK.RenderControl.IRenderTriMeshPickResult import IRenderTriMeshPickResult
IRenderTriMeshPickResult=IRenderTriMeshPickResult
from CityMaker_SDK.SDK.RenderControl.IRObject import IRObject
IRObject=IRObject
from CityMaker_SDK.SDK.RenderControl.ISimpleGeometryRender import ISimpleGeometryRender
ISimpleGeometryRender=ISimpleGeometryRender
from CityMaker_SDK.SDK.RenderControl.ISimplePointSymbol import ISimplePointSymbol
ISimplePointSymbol=ISimplePointSymbol
from CityMaker_SDK.SDK.RenderControl.ISimpleTextRender import ISimpleTextRender
ISimpleTextRender=ISimpleTextRender
from CityMaker_SDK.SDK.RenderControl.ISkinnedMesh import ISkinnedMesh
ISkinnedMesh=ISkinnedMesh
from CityMaker_SDK.SDK.RenderControl.ISkinnedMeshPickResult import ISkinnedMeshPickResult
ISkinnedMeshPickResult=ISkinnedMeshPickResult
from CityMaker_SDK.SDK.RenderControl.ISkyBox import ISkyBox
ISkyBox=ISkyBox
from CityMaker_SDK.SDK.RenderControl.ISolidSymbol import ISolidSymbol
ISolidSymbol=ISolidSymbol
from CityMaker_SDK.SDK.RenderControl.ISquadCombat import ISquadCombat
ISquadCombat=ISquadCombat
from CityMaker_SDK.SDK.RenderControl.ISquadCombatPickResult import ISquadCombatPickResult
ISquadCombatPickResult=ISquadCombatPickResult
from CityMaker_SDK.SDK.RenderControl.ISunConfig import ISunConfig
ISunConfig=ISunConfig
from CityMaker_SDK.SDK.RenderControl.ISurfaceSymbol import ISurfaceSymbol
ISurfaceSymbol=ISurfaceSymbol
from CityMaker_SDK.SDK.RenderControl.ITableLabel import ITableLabel
ITableLabel=ITableLabel
from CityMaker_SDK.SDK.RenderControl.ITableLabelPickResult import ITableLabelPickResult
ITableLabelPickResult=ITableLabelPickResult
from CityMaker_SDK.SDK.RenderControl.ITailedAttackArrow import ITailedAttackArrow
ITailedAttackArrow=ITailedAttackArrow
from CityMaker_SDK.SDK.RenderControl.ITailedAttackArrowPickResult import ITailedAttackArrowPickResult
ITailedAttackArrowPickResult=ITailedAttackArrowPickResult
from CityMaker_SDK.SDK.RenderControl.ITailedSquadCombat import ITailedSquadCombat
ITailedSquadCombat=ITailedSquadCombat
from CityMaker_SDK.SDK.RenderControl.ITailedSquadCombatPickResult import ITailedSquadCombatPickResult
ITailedSquadCombatPickResult=ITailedSquadCombatPickResult
from CityMaker_SDK.SDK.RenderControl.ITerrain import ITerrain
ITerrain=ITerrain
from CityMaker_SDK.SDK.RenderControl.ITerrain3DArrow import ITerrain3DArrow
ITerrain3DArrow=ITerrain3DArrow
from CityMaker_SDK.SDK.RenderControl.ITerrain3DArrowPickResult import ITerrain3DArrowPickResult
ITerrain3DArrowPickResult=ITerrain3DArrowPickResult
from CityMaker_SDK.SDK.RenderControl.ITerrain3DRectBase import ITerrain3DRectBase
ITerrain3DRectBase=ITerrain3DRectBase
from CityMaker_SDK.SDK.RenderControl.ITerrain3DRegBase import ITerrain3DRegBase
ITerrain3DRegBase=ITerrain3DRegBase
from CityMaker_SDK.SDK.RenderControl.ITerrainArc import ITerrainArc
ITerrainArc=ITerrainArc
from CityMaker_SDK.SDK.RenderControl.ITerrainArcPickResult import ITerrainArcPickResult
ITerrainArcPickResult=ITerrainArcPickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainArrow import ITerrainArrow
ITerrainArrow=ITerrainArrow
from CityMaker_SDK.SDK.RenderControl.ITerrainArrowPickResult import ITerrainArrowPickResult
ITerrainArrowPickResult=ITerrainArrowPickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainBoxPickResult import ITerrainBoxPickResult
ITerrainBoxPickResult=ITerrainBoxPickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainConePickResult import ITerrainConePickResult
ITerrainConePickResult=ITerrainConePickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainCylinderPickResult import ITerrainCylinderPickResult
ITerrainCylinderPickResult=ITerrainCylinderPickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainEllipse import ITerrainEllipse
ITerrainEllipse=ITerrainEllipse
from CityMaker_SDK.SDK.RenderControl.ITerrainEllipsePickResult import ITerrainEllipsePickResult
ITerrainEllipsePickResult=ITerrainEllipsePickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainHole import ITerrainHole
ITerrainHole=ITerrainHole
from CityMaker_SDK.SDK.RenderControl.ITerrainHolePickResult import ITerrainHolePickResult
ITerrainHolePickResult=ITerrainHolePickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainImageLabel import ITerrainImageLabel
ITerrainImageLabel=ITerrainImageLabel
from CityMaker_SDK.SDK.RenderControl.ITerrainImageLabelPickResult import ITerrainImageLabelPickResult
ITerrainImageLabelPickResult=ITerrainImageLabelPickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainLocation import ITerrainLocation
ITerrainLocation=ITerrainLocation
from CityMaker_SDK.SDK.RenderControl.ITerrainModifier import ITerrainModifier
ITerrainModifier=ITerrainModifier
from CityMaker_SDK.SDK.RenderControl.ITerrainModifierPickResult import ITerrainModifierPickResult
ITerrainModifierPickResult=ITerrainModifierPickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainPickResult import ITerrainPickResult
ITerrainPickResult=ITerrainPickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainPyramidPickResult import ITerrainPyramidPickResult
ITerrainPyramidPickResult=ITerrainPyramidPickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainRectangle import ITerrainRectangle
ITerrainRectangle=ITerrainRectangle
from CityMaker_SDK.SDK.RenderControl.ITerrainRectanglePickResult import ITerrainRectanglePickResult
ITerrainRectanglePickResult=ITerrainRectanglePickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainRegularPolygon import ITerrainRegularPolygon
ITerrainRegularPolygon=ITerrainRegularPolygon
from CityMaker_SDK.SDK.RenderControl.ITerrainRegularPolygonPickResult import ITerrainRegularPolygonPickResult
ITerrainRegularPolygonPickResult=ITerrainRegularPolygonPickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainRoute import ITerrainRoute
ITerrainRoute=ITerrainRoute
from CityMaker_SDK.SDK.RenderControl.ITerrainSphere import ITerrainSphere
ITerrainSphere=ITerrainSphere
from CityMaker_SDK.SDK.RenderControl.ITerrainSpherePickResult import ITerrainSpherePickResult
ITerrainSpherePickResult=ITerrainSpherePickResult
from CityMaker_SDK.SDK.RenderControl.ITerrainVideo import ITerrainVideo
ITerrainVideo=ITerrainVideo
from CityMaker_SDK.SDK.RenderControl.ITerrainVideoConfig import ITerrainVideoConfig
ITerrainVideoConfig=ITerrainVideoConfig
from CityMaker_SDK.SDK.RenderControl.ITextAttribute import ITextAttribute
ITextAttribute=ITextAttribute
from CityMaker_SDK.SDK.RenderControl.ITextRender import ITextRender
ITextRender=ITextRender
from CityMaker_SDK.SDK.RenderControl.ITextRenderScheme import ITextRenderScheme
ITextRenderScheme=ITextRenderScheme
from CityMaker_SDK.SDK.RenderControl.ITextSymbol import ITextSymbol
ITextSymbol=ITextSymbol
from CityMaker_SDK.SDK.RenderControl.IToolTipTextRender import IToolTipTextRender
IToolTipTextRender=IToolTipTextRender
from CityMaker_SDK.SDK.RenderControl.ITransformHelper import ITransformHelper
ITransformHelper=ITransformHelper
from CityMaker_SDK.SDK.RenderControl.ITripleArrow import ITripleArrow
ITripleArrow=ITripleArrow
from CityMaker_SDK.SDK.RenderControl.ITripleArrowPickResult import ITripleArrowPickResult
ITripleArrowPickResult=ITripleArrowPickResult
from CityMaker_SDK.SDK.RenderControl.IUniqueValuesRenderRule import IUniqueValuesRenderRule
IUniqueValuesRenderRule=IUniqueValuesRenderRule
from CityMaker_SDK.SDK.RenderControl.IUtility import IUtility
IUtility=IUtility
from CityMaker_SDK.SDK.RenderControl.IValueMapGeometryRender import IValueMapGeometryRender
IValueMapGeometryRender=IValueMapGeometryRender
from CityMaker_SDK.SDK.RenderControl.IValueMapTextRender import IValueMapTextRender
IValueMapTextRender=IValueMapTextRender
from CityMaker_SDK.SDK.RenderControl.IViewport import IViewport
IViewport=IViewport
from CityMaker_SDK.SDK.RenderControl.IViewshed import IViewshed
IViewshed=IViewshed
from CityMaker_SDK.SDK.RenderControl.IVisualAnalysis import IVisualAnalysis
IVisualAnalysis=IVisualAnalysis
from CityMaker_SDK.SDK.RenderControl.IVolumeMeasureOperation import IVolumeMeasureOperation
IVolumeMeasureOperation=IVolumeMeasureOperation
from CityMaker_SDK.SDK.RenderControl.IWalkGround import IWalkGround
IWalkGround=IWalkGround
from CityMaker_SDK.SDK.RenderControl.IWindowParam import IWindowParam
IWindowParam=IWindowParam
from CityMaker_SDK.SDK.RenderControl.Label import Label
Label=Label
from CityMaker_SDK.SDK.RenderControl.ParticleEffect import ParticleEffect
ParticleEffect=ParticleEffect
from CityMaker_SDK.SDK.RenderControl.RenderGeometry import RenderGeometry
RenderGeometry=RenderGeometry
from CityMaker_SDK.SDK.RenderControl.SkinnedMesh import SkinnedMesh
SkinnedMesh=SkinnedMesh
from CityMaker_SDK.SDK.RenderControl.TableLabel import TableLabel
TableLabel=TableLabel
from CityMaker_SDK.SDK.RenderControl.TerrainVideo import TerrainVideo
TerrainVideo=TerrainVideo
from CityMaker_SDK.SDK.RenderControl.TiledFeatureLayer import TiledFeatureLayer
TiledFeatureLayer=TiledFeatureLayer
from CityMaker_SDK.SDK.RenderControl.Viewshed import Viewshed
Viewshed=Viewshed
from CityMaker_SDK.SDK.Resource.IDrawGroup import IDrawGroup
IDrawGroup=IDrawGroup
from CityMaker_SDK.SDK.Resource.IDrawMaterial import IDrawMaterial
IDrawMaterial=IDrawMaterial
from CityMaker_SDK.SDK.Resource.IDrawPrimitive import IDrawPrimitive
IDrawPrimitive=IDrawPrimitive
from CityMaker_SDK.SDK.Resource.IImage import IImage
IImage=IImage
from CityMaker_SDK.SDK.Resource.IModel import IModel
IModel=IModel
from CityMaker_SDK.SDK.Resource.IModelTools import IModelTools
IModelTools=IModelTools
from CityMaker_SDK.SDK.Resource.IResourceFactory import IResourceFactory
IResourceFactory=IResourceFactory
from CityMaker_SDK.SDK.Resource.ISkinnedModel import ISkinnedModel
ISkinnedModel=ISkinnedModel
from CityMaker_SDK.SDK.UISystem.IUIDim import IUIDim
IUIDim=IUIDim
from CityMaker_SDK.SDK.UISystem.IUIEventArgs import IUIEventArgs
IUIEventArgs=IUIEventArgs
from CityMaker_SDK.SDK.UISystem.IUIImageButton import IUIImageButton
IUIImageButton=IUIImageButton
from CityMaker_SDK.SDK.UISystem.IUIMouseEventArgs import IUIMouseEventArgs
IUIMouseEventArgs=IUIMouseEventArgs
from CityMaker_SDK.SDK.UISystem.IUIRect import IUIRect
IUIRect=IUIRect
from CityMaker_SDK.SDK.UISystem.IUIStaticImage import IUIStaticImage
IUIStaticImage=IUIStaticImage
from CityMaker_SDK.SDK.UISystem.IUIStaticLabel import IUIStaticLabel
IUIStaticLabel=IUIStaticLabel
from CityMaker_SDK.SDK.UISystem.IUITextButton import IUITextButton
IUITextButton=IUITextButton
from CityMaker_SDK.SDK.UISystem.IUIWindow import IUIWindow
IUIWindow=IUIWindow
from CityMaker_SDK.SDK.UISystem.IUIWindowEventArgs import IUIWindowEventArgs
IUIWindowEventArgs=IUIWindowEventArgs
from CityMaker_SDK.SDK.UISystem.IUIWindowManager import IUIWindowManager
IUIWindowManager=IUIWindowManager
from CityMaker_SDK.Utils.Config import Config 
Config=Config
from CityMaker_SDK.Utils.RenderViewer3D import RenderViewer3D
RenderViewer3D=RenderViewer3D