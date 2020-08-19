from typing import Union, List, Optional, Dict

import pandas as pd
from deprecated import deprecated
from snowflake import connector as snowflake
from snowflake.connector import SnowflakeConnection

from pyrasgo.connection import Connection
from pyrasgo.feature import Feature, FeatureList
from pyrasgo.model import Model
from pyrasgo.enums import Granularity, ModelType


class RasgoConnection(Connection):
    """
    Base connection object to handle interactions with the Rasgo API.

    Defaults to using the production Rasgo instance, which can be overwritten
    by specifying the `RASGO_DOMAIN` environment variable, eg:

    &> RASGO_DOMAIN=custom.rasgoml.com python
    >>> from pyrasgo import RasgoConnection
    >>> rasgo = Connection(api_key='not_a_key')
    >>> rasgo._hostname == 'custom.rasgoml.com'
    True

    """

    def __init__(self, **kwargs):
        self._user_id = None
        super().__init__(**kwargs)

    def create_model(self, name: str,
                     type: Union[str, ModelType],
                     granularity: Union[str, Granularity]) -> Model:
        """
        Creates model within Rasgo within the account specified by the API key.
        :param name: Model name
        :param model_type: Type of model specified
        :param granularity: Granularity of the data.
        :return: Model object.
        """
        self._note({'event_type': 'create_model'})
        try:
            # If not enum, convert to enum first.
            model_type = type.name
        except AttributeError:
            model_type = ModelType(type)

        try:
            # If not enum, convert to enum first.
            granularity = granularity.name
        except AttributeError:
            granularity = Granularity(granularity)

        # TODO: API should really have _some_ validation for the schema of this post.
        response = self._post("/models", _json={"name": name,
                                                "type": model_type.value,
                                                # TODO: This post should only be `granularity` for future compatibility
                                                #       Coordinate with API development to relax domain specificity
                                                "timeSeriesGranularity": granularity.value})
        return Model(api_key=self._api_key, api_object=response.json())

    def add_feature_to(self, model: Model, feature: Feature):
        model.add_feature(feature)

    def add_features_to(self, model: Model, features: FeatureList):
        model.add_features(features)

    def generate_training_data_for(self, model: Model):
        raise NotImplementedError

    def get_models(self) -> List[Model]:
        """
        Retrieves the list of models from Rasgo within the account specified by the API key.
        """
        self._note({'event_type': 'get_models'})
        response = self._get("/models", {"join": ["features", "author"],
                                         "filter": "isDeleted||$isnull"})
        return [Model(api_key=self._api_key, api_object=entry) for entry in response.json()]

    def get_model(self, model_id) -> Model:
        """
        Retrieves the specified model from Rasgo within the account specified by the API key.
        """
        self._note({'event_type': 'get_model'})
        response = self._get(f"/models/{model_id}", {"join": ["features", "author"]})
        return Model(api_key=self._api_key, api_object=response.json())

    def get_feature(self, feature_id) -> Feature:
        """
        Retrieves the specified feature from Rasgo within the account specified by the API key.
        """
        self._note({'event_type': 'get_feature'})
        response = self._get(f"/features/{feature_id}")
        return Feature(api_key=self._api_key, api_object=response.json())

    def get_features(self) -> FeatureList:
        """
        Retrieves the features from Rasgo within account specified by the API key.
        """
        self._note({'event_type': 'get_features'})
        response = self._get("/features")
        return FeatureList(response.json())

    def get_features_for(self, model: Model) -> FeatureList:
        raise NotImplementedError()
        # self._note({'event_type': 'get_features_for'})
        # response = self._get("/features",
        #                      params={'join': f""})
        #                    # params={'filter': f"||eq||DateTime"})
        # return FeatureList(response.json())

    def get_feature_data(self, model_id: int,
                         filters: Optional[Dict[str, str]] = None,
                         limit: Optional[int] = None) -> pd.DataFrame:
        """
        Constructs the pandas dataframe for the specified model.

        :param model_id: int
        :param filters: dictionary providing columns as keys and the filtering values as values.
        :param limit: integer limit for number of rows returned
        :return: Dataframe containing feature data
        """
        self._note({'event_type': 'get_models'})
        model = self.get_model(model_id)

        conn, creds = self._snowflake_connection(model.get_author())

        table_metadata = model.snowflake_table_metadata(creds)
        query, values = self._make_select_statement(table_metadata, filters, limit)

        result_set = self._run_query(conn, query, values)
        return pd.DataFrame.from_records(iter(result_set), columns=[x[0] for x in result_set.description])

    def get_feature_sets(self):
        """
        Retrieves the feature sets from Rasgo within account specified by the API key.
        """
        self._note({'event_type': 'get_feature_sets'})
        response = self._get("/feature-sets")
        return response.json()

    def get_data_sources(self):
        """
        Retrieves the data sources from Rasgo within account specified by the API key.
        """
        self._note({'event_type': 'get_data_sources'})
        response = self._get("/data-source")
        return response.json()

    def get_dimensionalities(self):
        """
        Retrieves the data sources from Rasgo within account specified by the API key.
        """
        self._note({'event_type': 'get_dimensionalities'})
        response = self._get("/dimensionalities")
        return response.json()

    def get_user_id(self):
        """
        Gets the user id for the API key provided, or None if not available.
        NOTE: This is used for monitoring/logging purposes.
        """
        if self._user_id:
            return self._user_id
        else:
            response = self._get("/users")
            try:
                response_body = response.json()
                user = response_body['data']
                self._user_id = user.get('id')
                return self._user_id
            except Exception:
                # TODO: Split out Exceptions for error-handling?
                return None

    def _note(self, event_dict: dict) -> None:
        """
        Emit event to monitoring service.
        :param event_dict: Dictionary containing desired attributes to emit.
        :return:
        """
        event_dict['user_id'] = self.get_user_id()  # TODO: move user_id call to __init__ to cache the user id.
        event_dict['source'] = 'pyrasgo'
        event = self._event_logger.create_event(**event_dict)
        self._event_logger.log_event(event)

    @staticmethod
    def _snowflake_connection(member) -> (SnowflakeConnection, dict):
        """
        Constructs connection object for Snowflake data platform
        :param member: credentials for Snowflake data platform

        :return: Connection object to use for query execution
        """
        creds = member.snowflake_creds()
        conn = snowflake.connect(**creds)
        return conn, creds

    @staticmethod
    def _make_select_statement(table_metadata, filters, limit) -> tuple:
        """
        Constructs select * query for table
        """
        query = "SELECT * FROM {database}.{schema}.{table}".format(**table_metadata)
        values = []
        if filters:
            comparisons = []
            for k, v in filters.items():
                comparisons.append("{}=%s".format(k))
                values.append(v)
            query += " WHERE " + " and ".join(comparisons)
        if limit:
            query += " limit {}".format(limit)
        return query, values

    @staticmethod
    def _run_query(conn, query: str, params):
        """
        Execute a query on the [cloud] data platform.

        :param conn: TODO -> abstract the cloud data platform connection
        :param query: String to be executed on the data platform
        :return:
        """
        return conn.cursor().execute(query, params)

    @deprecated("This function has been deprecated, use `get_models` instead.")
    def get_lists(self) -> List[Model]:
        """
        Deprecated function.  Renamed to `get_models.`
        """
        self._note({'event_type': 'get_lists'})
        return self.get_models()

    @deprecated("This function has been deprecated, use `get_model` instead.")
    def get_feature_list(self, list_id) -> Model:
        """
        Deprecated function.  Renamed to `get_model.`
        """
        self._note({'event_type': 'get_feature_list'})
        return self.get_model(model_id=list_id)