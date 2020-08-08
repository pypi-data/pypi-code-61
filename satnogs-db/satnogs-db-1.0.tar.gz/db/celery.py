# pylint: disable=C0415
"""SatNOGS DB celery task workers"""
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'db.settings')

RUN_EVERY_15 = 60 * 15
RUN_HOURLY = 60 * 60
RUN_DAILY = 60 * 60 * 24

APP = Celery('db')

APP.config_from_object('django.conf:settings', namespace='CELERY')
APP.autodiscover_tasks()


# Wrapper tasks as workaround for registering shared tasks to beat scheduler
# See https://github.com/celery/celery/issues/5059
@APP.task
def update_all_tle():
    """Wrapper task for 'update_all_tle' shared task"""
    from db.base.tasks import update_all_tle as periodic_task
    periodic_task()


@APP.task
def background_cache_statistics():
    """Wrapper task for 'background_cache_statistics' shared task"""
    from db.base.tasks import background_cache_statistics as periodic_task
    periodic_task()


@APP.task
def decode_recent_data():
    """Wrapper task for 'decocde_recent_data' shared task"""
    from db.base.tasks import decode_recent_data as periodic_task
    periodic_task()


@APP.task
def remove_old_exported_framesets():
    """Wrapper task for 'decocde_recent_data' shared task"""
    from db.base.tasks import remove_old_exported_framesets as periodic_task
    periodic_task()


@APP.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    """Initializes celery tasks that need to run on a scheduled basis"""
    sender.add_periodic_task(RUN_DAILY, update_all_tle.s(), name='update-all-tle')

    sender.add_periodic_task(
        RUN_HOURLY, background_cache_statistics.s(), name='background-cache-statistics'
    )

    sender.add_periodic_task(
        RUN_HOURLY, remove_old_exported_framesets.s(), name='remove_old_exported_frameset'
    )

    sender.add_periodic_task(RUN_EVERY_15, decode_recent_data.s(), name='decode-recent-data')
