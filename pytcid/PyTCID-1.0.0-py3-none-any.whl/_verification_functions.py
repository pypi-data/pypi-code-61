"""
Functions to verify cards.
"""

from urllib.request import Request, urlopen
from http.client import HTTPResponse
from xml.etree.ElementTree import Element, fromstring


def _parse_response(response: bytes, status: int) -> bool:
    """
    Parse the returned response if the status is successful.

    :param response: Response to be parsed in bytes.
    :param status: Status code of the response.
    :return: True or False, since the response is a boolean response.
    """
    if status != 200:
        return False
    root: Element = fromstring(response)
    return root[0][0][0].text == 'true'


def _send_request(url: str, service_name: str, **kwargs) -> bool:
    """
    Send a request to the NVI's API endpoints. Return
        the parsed response if successful.

    :param url: URL to be sent to be request.
    :param service_name: Service name of the request.
        Could be KisiVeCuzdanDogrula.
    :param kwargs: Parameters to be sent to the server.
    :return: The response dictionary if request is successful,
        None otherwise.
    """
    body: str = '<?xml version="1.0" encoding="utf-8"?>\n'
    body += '<soap12:Envelope xmlns:xsi=' \
            '"http://www.w3.org/2001/XMLSchema-instance" ' \
            'xmlns:xsd="http://www.w3.org/2001/XMLSchema" ' \
            'xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">\n'
    body += f'\t<soap12:Body>\n\t\t<{service_name} xmlns="http://tckimlik.nvi.gov.tr/WS">'
    body += '\n'.join(f'\t\t\t<{key}>{kwargs[key]}</{key}>' for key in kwargs) + '\n'
    body += '\t\t</KisiVeCuzdanDogrula>\n\t</soap12:Body>\n</soap12:Envelope>'
    data = bytes(body, encoding='utf-8')
    headers = {
        "Host": "tckimlik.nvi.gov.tr",
        "Content-Type": "application/soap+xml; charset=utf-8",
        "Content-Length": len(data)
    }
    request: Request = Request(url, data, headers)
    response: HTTPResponse = urlopen(request)
    return _parse_response(response.read(), response.status)


def _check_if_parameter_included(properties: dict, check: str, set_: str, **params) -> None:
    """
    Some parameters are optional for the NVI API, check if a parameter exists in the,
        given params. If it *does not* exist, set the XML tag stating its existence
        to false, if it *does* exist, set that tag to true, and set the XML element
        that carries the value of the parameter to the value of the parameter.

    :param properties: Properties dictionary for the payload.
    :param check: Name of the parameter to be checked in params.
    :param set_: Name of the parameter to be set in XML.
    :param params: Python(ic) params that carry the function parameters.
    :return: None. Dictionaries are mutable, this function sets the dictionary
        using side-effects.
    """
    if check in params:
        properties[set_] = params[check]
        properties[set_ + 'Yok'] = 'false'
    else:
        properties[set_ + 'Yok'] = 'true'


def verify_national_id(id_: int, name: str, tckkseri: str, birth_year: int,  **kwargs) -> bool:
    """
    Verify a Turkish National Identification Card using the NVI api.

    :param id_: ID Number of the card.
    :param name: Name of the card holder.
    :param tckkseri: Serial number of the TCKK identity card.
    :param birth_year: Birth year of the card holder.
    :param kwargs: Optional parameters, Birth day, month and surname
        of the card holder. Optional here refers to the fact that some
        cards may not carry this information. If a card does carry this
        information but the information is not provided, the verification
        *will* fail.
    :return: True if the identity card is verified, False otherwise.
    """
    properties: dict = {
        'TCKimlikNo': id_,
        'Ad': name,
        'TCKKSeriNo': tckkseri,
        'DogumYil': birth_year,
    }
    _check_if_parameter_included(properties, 'birth_day', 'DogumGun', **kwargs)
    _check_if_parameter_included(properties, 'birth_month', 'DogumAy', **kwargs)
    _check_if_parameter_included(properties, 'surname', 'Soyad', **kwargs)
    return _send_request('https://tckimlik.nvi.gov.tr/Service/KPSPublicV2.asmx?op=KisiVeCuzdanDogrula',
                         'KisiVeCuzdanDogrula',
                         **properties)
