import json
import os
import unittest

from elcrawl import save_item
from elcrawl.db.sql import get_conn
from elcrawl.utils.config import get_collection, get_dedup_field
from elcrawl.constants import DedupMethod

os.environ['ELCRAWL_TASK_ID'] = 'test_task_id'
os.environ['ELCRAWL_COLLECTION'] = 'results2'
os.environ['ELCRAWL_IS_DEDUP'] = '1'
os.environ['ELCRAWL_DEDUP_FIELD'] = 'url'
os.environ['ELCRAWL_DEDUP_METHOD'] = DedupMethod.OVERWRITE
os.environ['ELCRAWL_DATA_SOURCE'] = json.dumps({
    'type': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres',
    'username': 'postgres',
    'password': 'postgres',
})

url = 'example.com'


class PostgresSaveItemTestCase(unittest.TestCase):
    def test_save_item(self):
        for i in range(10):
            save_item({'url': url, 'title': str(i)})
        dedup_field = get_dedup_field()
        table_name = get_collection()
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(f'SELECT count(*) FROM {table_name} WHERE {dedup_field} = \'{url}\'')
        conn.commit()
        res = cursor.fetchone()
        assert res[0] == 1
        cursor.execute(f'SELECT url,title FROM {table_name} WHERE {dedup_field} = \'{url}\'')
        conn.commit()
        res = cursor.fetchone()
        assert res[1] == '9'
        cursor.execute(f'DELETE FROM {table_name} WHERE {dedup_field} = \'{url}\'')
        conn.commit()
        cursor.close()


if __name__ == '__main__':
    unittest.main()
