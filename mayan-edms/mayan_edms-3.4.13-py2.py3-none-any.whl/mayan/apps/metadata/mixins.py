from django.contrib import messages
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _


class DocumentMetadataSameTypeMixin(object):
    def dispatch(self, request, *args, **kwargs):
        result = super(DocumentMetadataSameTypeMixin, self).dispatch(
            request, *args, **kwargs
        )

        queryset = self.get_object_list()

        for document in queryset:
            document.add_as_recent_document_for_user(user=request.user)

        if queryset.values('document_type').distinct().aggregate(Count('document_type'))['document_type__count'] > 1:
            messages.error(
                message=_(
                    'Selected documents must be of the same type.'
                ), request=request
            )
            return HttpResponseRedirect(redirect_to=self.previous_url)

        return result
