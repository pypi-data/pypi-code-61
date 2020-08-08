#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

import logging
import os

from ocean_utils.agreements.service_agreement import ServiceAgreement
from ocean_utils.agreements.service_types import ServiceTypes

logger = logging.getLogger(__name__)


def download_asset_files(
        service_index,
        asset,
        consumer_wallet,
        destination,
        token_address,
        token_transfer_tx_id,
        data_provider,
        index=None
):
    """
    Download asset data files or result files from a compute job.

    :param service_index: identifier of the service inside the asset DDO, str
    :param asset: Asset instance
    :param consumer_wallet: Wallet instance of the consumer
    :param destination: Path, str
    :param token_address: hex str the address of the DataToken smart contract
    :param token_transfer_tx_id: hex str the token transfer transaction id (hash)
    :param data_provider: DataServiceProvider instance
    :param index: Index of the document that is going to be downloaded, int
    :return: Asset folder path, str
    """
    _files = asset.metadata['main']['files']
    sa = ServiceAgreement.from_ddo(ServiceTypes.ASSET_ACCESS, asset)
    service_endpoint = sa.service_endpoint
    if not service_endpoint:
        logger.error(
            'Consume asset failed, service definition is missing the "serviceEndpoint".')
        raise AssertionError(
            'Consume asset failed, service definition is missing the "serviceEndpoint".')

    if not os.path.isabs(destination):
        destination = os.path.abspath(destination)
    if not os.path.exists(destination):
        os.mkdir(destination)

    asset_folder = os.path.join(
        destination,
        f'datafile.{asset.asset_id}.{service_index}'
    )
    if not os.path.exists(asset_folder):
        os.mkdir(asset_folder)

    if index is not None:
        assert isinstance(index, int), logger.error('index has to be an integer.')
        assert index >= 0, logger.error('index has to be 0 or a positive integer.')
        assert index < len(_files), logger.error(
            'index can not be bigger than the number of files')
        indexes = [index]
    else:
        indexes = range(len(_files))

    for i in indexes:
        data_provider.download_service(
            asset.did,
            service_endpoint,
            consumer_wallet,
            _files,
            asset_folder,
            service_index,
            token_address,
            token_transfer_tx_id,
            i
        )
    return asset_folder
