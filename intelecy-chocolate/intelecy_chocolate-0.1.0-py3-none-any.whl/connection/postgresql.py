import codecs
import gc
import pickle
from contextlib import contextmanager

import dataset

from ..base import Connection


class PostgresConnection(Connection):
    """Connection to a Postgres database.

    TODO: Fix
    The library uses locks on the Connection, which Postgres does not seem to need
    For now there is only an ugly "pass" lock that will of course fail any real lock test
    (it does not actually lock anything)

    We use `dataset <https://dataset.readthedocs.io>`_ under the hood allowing
    us to manage a Postgres database just like a list of dictionaries. Thus no
    need to predefine any schema nor maintain it explicitly. You can treat this
    database just as a list of dictionaries.

    Args:
        url (str): Full url to the database, as described in the `SQLAlchemy
            documentation
            <http://docs.sqlalchemy.org/en/latest/core/engines.html#postgres>`_.
            The url is parsed to find the database path.
        result_table (str): Table used to store the experiences and their results.
        complementary_table (str): Table used to store complementary information necessary
            to the optimizer.
        space_table (str): Table used to save the optimization :class:`Space`.

    Raises:
        RuntimeError: When an invalid name is given, see error message for precision.
    """

    def __init__(self, url, result_table="results", complementary_table="complementary", space_table="space"):
        super(PostgresConnection, self).__init__()
        if url.endswith("/"):
            raise RuntimeError("Empty database name {}".format(url))

        if url.endswith((" ", "\t")):
            raise RuntimeError("Database name ends with space {}".format(url))

        if not url.startswith("postgresql://"):
            raise RuntimeError("Missing 'postgresql://' at the begin of url".format(url))

        self.url = url
        self.result_table_name = result_table
        self.complementary_table_name = complementary_table
        self.space_table_name = space_table

        # with self.lock():
        #     db = dataset.connect(self.url)

        #     # Initialize a result table and ensure float for loss
        #     results = db[self.result_table_name]
        #     results.create_column("_loss", sqlalchemy.Float)

    @contextmanager
    def lock(self, timeout=-1, poll_interval=0.05):
        """
        Always passes with postgresql, dataset handles locking
        """
        yield

    def all_results(self):
        """Get a list of all entries of the result table. The order is
        undefined.
        """
        # Only way to ensure old db instances are closed is to force garbage collection
        # See dataset note : https://dataset.readthedocs.io/en/latest/api.html#notes
        gc.collect()
        db = dataset.connect(self.url)
        return list(db[self.result_table_name].all())

    def find_results(self, filter):
        """Get a list of all results associated with *filter*. The order is
        undefined.
        """
        gc.collect()
        db = dataset.connect(self.url)
        return list(db[self.result_table_name].find(**filter))

    def insert_result(self, document):
        """Insert a new *document* in the result table. The columns must not
        be defined nor all present. Any new column will be added to the
        database and any missing column will get value None.
        """
        gc.collect()
        db = dataset.connect(self.url)
        return db[self.result_table_name].insert(document)

    def update_result(self, filter, values):
        """Update or add *values* of given rows in the result table.

        Args:
            filter: An identifier of the rows to update.
            values: A mapping of values to update or add.
        """
        gc.collect()
        filter = filter.copy()
        keys = list(filter.keys())
        filter.update(values)
        db = dataset.connect(self.url)
        return db[self.result_table_name].update(filter, keys)

    def count_results(self):
        """Get the total number of entries in the result table.
        """
        gc.collect()
        db = dataset.connect(self.url)
        return db[self.result_table_name].count()

    def all_complementary(self):
        """Get all entries of the complementary information table as a list.
        The order is undefined.
        """
        gc.collect()
        db = dataset.connect(self.url)
        return list(db[self.complementary_table_name].all())

    def insert_complementary(self, document):
        """Insert a new document (row) in the complementary information table.
        """
        gc.collect()
        db = dataset.connect(self.url)
        return db[self.complementary_table_name].insert(document)

    def find_complementary(self, filter):
        """Find a document (row) from the complementary information table.
        """
        gc.collect()
        db = dataset.connect(self.url)
        return db[self.complementary_table_name].find_one(**filter)

    def get_space(self):
        """Returns the space used for previous experiments.

        Raises:
            AssertionError: If there are more than one space in the database.
        """
        gc.collect()
        db = dataset.connect(self.url)
        entry_count = db[self.space_table_name].count()
        if entry_count == 0:
            return None

        assert entry_count == 1, "Space table unexpectedly contains more than one space."

        space = db[self.space_table_name].find_one()["space"]
        # Use encoding that works well with postgres
        unpickled = pickle.loads(codecs.decode(space.encode(), "base64"))
        return unpickled

    def insert_space(self, space):
        """Insert a space in the database.

        Raises:
            AssertionError: If a space is already present in the database.
        """
        gc.collect()
        db = dataset.connect(self.url)
        assert db[self.space_table_name].count() == 0, ("Space table cannot contain more than one space, "
                                                        "clear table first.")
        # Use encoding that works well with postgres
        pickled = codecs.encode(pickle.dumps(space), 'base64').decode()
        return db[self.space_table_name].insert({"space": pickled})

    def clear(self):
        """Clear all data from the database.
        """
        gc.collect()
        db = dataset.connect(self.url)
        db[self.result_table_name].drop()
        db[self.complementary_table_name].drop()
        db[self.space_table_name].drop()
        # results = db[self.result_table_name]
        # results.create_column("_loss", sqlalchemy.Float)

    def pop_id(self, document):
        """Pops the database unique id from the document."""
        document.pop("id", None)
        return document
