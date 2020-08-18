from pytz import timezone
from datetime import datetime, timedelta
import asyncio
from rethinkdb import r as rdb

host = 'localhost'
port = 28015
loop = asyncio.get_event_loop()
rdb.set_loop_type('asyncio')
conn = loop.run_until_complete(rdb.connect(db='test', host=host, port=port))
first = datetime.utcnow() - timedelta(seconds=200)
tz = timezone("UTC")
firsttz = tz.localize(first)
firstrdb = rdb.iso8601(firsttz.isoformat())
post = datetime.utcnow()
posttz = tz.localize(post)
postrdb = rdb.iso8601(posttz.isoformat())
table = "STATION"
filter_opt = {'left_bound': 'open', 'index': "DT_GEN"}
print(f"Desde {firstrdb}, hasta {postrdb}")
query = rdb.db("test").table(table).between(firstrdb, postrdb,
                                            **filter_opt).run(conn)
result = loop.run_until_complete(query)
print(result)
