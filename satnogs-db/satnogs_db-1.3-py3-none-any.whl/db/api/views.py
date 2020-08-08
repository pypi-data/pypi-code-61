"""SatNOGS DB API django rest framework Views"""
from django.core.files.base import ContentFile
from rest_framework import mixins, status, viewsets
from rest_framework.parsers import FileUploadParser, FormParser, \
    MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from db.api import filters, pagination, serializers
from db.api.perms import SafeMethodsWithPermission
from db.api.renderers import BrowserableJSONLDRenderer, JSONLDRenderer
from db.base.models import Artifact, DemodData, Mode, Satellite, Transmitter
from db.base.tasks import update_satellite


class ModeView(viewsets.ReadOnlyModelViewSet):  # pylint: disable=R0901
    """SatNOGS DB Mode API view class"""
    renderer_classes = [
        JSONRenderer, BrowsableAPIRenderer, JSONLDRenderer, BrowserableJSONLDRenderer
    ]
    queryset = Mode.objects.all()
    serializer_class = serializers.ModeSerializer


class SatelliteView(viewsets.ReadOnlyModelViewSet):  # pylint: disable=R0901
    """SatNOGS DB Satellite API view class"""
    renderer_classes = [
        JSONRenderer, BrowsableAPIRenderer, JSONLDRenderer, BrowserableJSONLDRenderer
    ]
    queryset = Satellite.objects.all()
    serializer_class = serializers.SatelliteSerializer
    filterset_class = filters.SatelliteViewFilter
    lookup_field = 'norad_cat_id'


class TransmitterView(viewsets.ReadOnlyModelViewSet):  # pylint: disable=R0901
    """SatNOGS DB Transmitter API view class"""
    renderer_classes = [
        JSONRenderer, BrowsableAPIRenderer, JSONLDRenderer, BrowserableJSONLDRenderer
    ]
    queryset = Transmitter.objects.all()
    serializer_class = serializers.TransmitterSerializer
    filterset_class = filters.TransmitterViewFilter
    lookup_field = 'uuid'


class TelemetryView(  # pylint: disable=R0901
        mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    """SatNOGS DB Telemetry API view class"""
    renderer_classes = [
        JSONRenderer, BrowsableAPIRenderer, JSONLDRenderer, BrowserableJSONLDRenderer
    ]
    queryset = DemodData.objects.all()
    serializer_class = serializers.TelemetrySerializer
    filterset_class = filters.TelemetryViewFilter
    permission_classes = [SafeMethodsWithPermission]
    parser_classes = (FormParser, FileUploadParser)
    pagination_class = pagination.LinkedHeaderPageNumberPagination

    def create(self, request, *args, **kwargs):
        data = {}

        norad_cat_id = request.data.get('noradID')

        if not Satellite.objects.filter(norad_cat_id=norad_cat_id).exists():
            try:
                update_satellite(norad_cat_id, update_name=True, update_tle=True)
            except LookupError:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        data['satellite'] = Satellite.objects.get(norad_cat_id=norad_cat_id).id
        data['station'] = request.data.get('source')
        timestamp = request.data.get('timestamp')
        data['timestamp'] = timestamp

        # Convert coordinates to omit N-S and W-E designators
        lat = request.data.get('latitude')
        lng = request.data.get('longitude')
        if any(x.isalpha() for x in lat):
            data['lat'] = (-float(lat[:-1]) if ('S' in lat) else float(lat[:-1]))
        else:
            data['lat'] = float(lat)
        if any(x.isalpha() for x in lng):
            data['lng'] = (-float(lng[:-1]) if ('W' in lng) else float(lng[:-1]))
        else:
            data['lng'] = float(lng)

        # Network or SiDS submission?
        if request.data.get('satnogs_network'):
            data['app_source'] = 'network'
        else:
            data['app_source'] = 'sids'

        # Create file out of frame string
        frame = ContentFile(request.data.get('frame'), name='sids')
        data['payload_frame'] = frame

        serializer = serializers.SidsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(status=status.HTTP_201_CREATED, headers=headers)


class ArtifactView(  # pylint: disable=R0901
        mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    """SatNOGS DB Artifact API view class"""
    queryset = Artifact.objects.all()
    filterset_class = filters.ArtifactViewFilter
    permission_classes = [IsAuthenticated]
    parser_classes = (FormParser, MultiPartParser)
    pagination_class = pagination.LinkedHeaderPageNumberPagination

    def get_serializer_class(self):
        """Returns the right serializer depending on http method that is used"""
        if self.action == 'create':
            return serializers.NewArtifactSerializer
        return serializers.ArtifactSerializer

    def create(self, request, *args, **kwargs):
        """Creates artifact"""
        serializer = self.get_serializer(data=request.data)
        try:
            if serializer.is_valid():
                data = serializer.save()
                http_response = {}
                http_response['id'] = data.id
                response = Response(http_response, status=status.HTTP_200_OK)
            else:
                data = serializer.errors
                response = Response(data, status=status.HTTP_400_BAD_REQUEST)
        except (ValidationError, ValueError, OSError) as error:
            response = Response(str(error), status=status.HTTP_400_BAD_REQUEST)
        return response
