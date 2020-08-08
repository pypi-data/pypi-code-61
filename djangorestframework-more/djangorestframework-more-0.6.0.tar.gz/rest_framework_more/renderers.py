from rest_framework_csv.renderers import CSVRenderer
from drf_renderer_xlsx.renderers import XLSXRenderer


class NonPaginatedCSVRenderer(CSVRenderer):
    format = "csv (non-paginated)"

    def render(self, data, accepted_media_type, renderer_context):
        response = renderer_context["response"]

        if response.status_code != 200:
            return ""

        view = renderer_context["view"]
        request = renderer_context["request"]

        queryset = view.queryset
        query_params = request.query_params.dict()
        query_params.pop("format", None)

        # ignore the page parameter
        query_params.pop("page", None)

        # filter out keys with empty strings
        filters = {k: v for k, v in query_params.items() if v != ""}

        queryset = queryset.filter(**filters)

        serializer = view.serializer_class

        data = serializer(queryset, many=True).data

        return super(NonPaginatedCSVRenderer, self).render(
            data, accepted_media_type, renderer_context
        )


class NonPaginatedXLSXRenderer(XLSXRenderer):
    format = "xlsx (non-paginated)"

    def render(self, data, accepted_media_type, renderer_context):
        response = renderer_context["response"]

        if response.status_code != 200:
            return ""

        view = renderer_context["view"]
        request = renderer_context["request"]

        queryset = view.queryset
        query_params = request.query_params.dict()
        query_params.pop("format", None)

        # ignore the page parameter
        query_params.pop("page", None)

        # filter out keys with empty strings
        filters = {k: v for k, v in query_params.items() if v != ""}

        queryset = queryset.filter(**filters)

        serializer = view.serializer_class

        data = serializer(queryset, many=True).data

        return super(NonPaginatedXLSXRenderer, self).render(
            data, accepted_media_type, renderer_context
        )
