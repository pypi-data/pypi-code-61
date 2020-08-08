"""
This module is home to the ReportJob class
"""
from pyecobee.ecobee_object import EcobeeObject


class ReportJob(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/ReportJob.shtml

    Attribute names have been generated by converting ecobee property
    names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value
    of READONLY is "no".

    An __init__ argument without a default value has been generated if
    the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated
    if the value of REQUIRED is "no".
    """

    __slots__ = ['_job_id', '_status', '_message', '_files']

    attribute_name_map = {
        'job_id': 'jobId',
        'jobId': 'job_id',
        'status': 'status',
        'message': 'message',
        'files': 'files',
    }

    attribute_type_map = {
        'job_id': 'six.text_type',
        'status': 'six.text_type',
        'message': 'six.text_type',
        'files': 'List[six.text_type]',
    }

    def __init__(self, job_id=None, status=None, message=None, files=None):
        """
        Construct a ReportJob instance
        """
        self._job_id = job_id
        self._status = status
        self._message = message
        self._files = files

    @property
    def job_id(self):
        """
        Gets the job_id attribute of this ReportJob instance.

        :return: The value of the job_id attribute of this ReportJob
        instance.
        :rtype: six.text_type
        """

        return self._job_id

    @property
    def status(self):
        """
        Gets the status attribute of this ReportJob instance.

        :return: The value of the status attribute of this ReportJob
        instance.
        :rtype: six.text_type
        """

        return self._status

    @property
    def message(self):
        """
        Gets the message attribute of this ReportJob instance.

        :return: The value of the message attribute of this ReportJob
        instance.
        :rtype: six.text_type
        """

        return self._message

    @property
    def files(self):
        """
        Gets the files attribute of this ReportJob instance.

        :return: The value of the files attribute of this ReportJob
        instance.
        :rtype: List[six.text_type]
        """

        return self._files
