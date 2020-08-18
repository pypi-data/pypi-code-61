# --------------------------------------------------------------- Imports ---------------------------------------------------------------- #

# System
from typing import Optional
import os, random

# Pip
from kcu import kjson, kpath
from tinydb import TinyDB, Query

# ---------------------------------------------------------------------------------------------------------------------------------------- #



# ----------------------------------------------------------- class: RandomUA ------------------------------------------------------------ #

class RandomUA:

    # -------------------------------------------------------- Public methods -------------------------------------------------------- #

    # THE JSON SHOULD HAVE THIS FORMAT
    # [
    #     {
    #         "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
    #         "bf": "firefox",
    #         "bv": 61
    #     },
    #     {
    #         "ua": "Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0",
    #         "bf": "firefox",
    #         "bv": 61
    #     },
    #     ...
    # ]
    @classmethod
    def load(
        cls,
        uas_path: Optional[str] = None,
        db_path: Optional[str] = None
    ) -> None:
        db_path = db_path or kpath.path_for_subpath_in_current_folder('db.json')

        if os.path.exists(db_path):
            cls.db = TinyDB(db_path)
            cls.__loaded = True

            return

        cls.json = kjson.load(uas_path or kpath.path_for_subpath_in_current_folder('uas.json'))
        cls.db = TinyDB(db_path)

        for e in cls.json:
            cls.db.insert(e)

        cls.__loaded = True

    @classmethod
    def random(
        cls,
        browser_name: Optional[str] = None,
        min_browser_version: Optional[int] = None,
        max_browser_version: Optional[int] = None
    ) -> Optional[str]:
        cls.__optionally_load()

        if not browser_name and not min_browser_version and not max_browser_version:
            return random.choice(cls.json)['ua']
        
        min_browser_version = min_browser_version or 0
        max_browser_version = max_browser_version or 999999999

        UA = Query()
        return random.choice(
            cls.db.search((UA.bf == browser_name) & (UA.bv >= min_browser_version) & (UA.bv <= max_browser_version)
        ))['ua']

    @classmethod
    def firefox(
        cls,
        min_browser_version: Optional[int] = None,
        max_browser_version: Optional[int] = None
    ) -> Optional[str]:
        return cls.random(browser_name='firefox', min_browser_version=min_browser_version, max_browser_version=max_browser_version)

    @classmethod
    def safari(
        cls,
        min_browser_version: Optional[int] = None,
        max_browser_version: Optional[int] = None
    ) -> Optional[str]:
        return cls.random(browser_name='safari', min_browser_version=min_browser_version, max_browser_version=max_browser_version)

    @classmethod
    def chrome(
        cls,
        min_browser_version: Optional[int] = None,
        max_browser_version: Optional[int] = None
    ) -> Optional[str]:
        return cls.random(browser_name='chrome', min_browser_version=min_browser_version, max_browser_version=max_browser_version)


    # ------------------------------------------------------ Private properties ------------------------------------------------------ #

    __loaded = False


    # ------------------------------------------------------- Private methods -------------------------------------------------------- #

    @classmethod
    def __optionally_load(cls) -> None:
        if cls.__loaded:
            return False

        cls.load()


# ---------------------------------------------------------------------------------------------------------------------------------------- #