# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['falocalrepo']

package_data = \
{'': ['*']}

install_requires = \
['faapi==2.5.0', 'filetype==1.0.7']

entry_points = \
{'console_scripts': ['falocalrepo = falocalrepo.__main__:main']}

setup_kwargs = {
    'name': 'falocalrepo',
    'version': '3.0.0b9',
    'description': "Pure Python program to download any user's gallery/scraps/favorites and more from FurAffinity forum in an easily handled database.",
    'long_description': '# FALocalRepo\nPure Python program to download any user\'s gallery/scraps/favorites and more from FurAffinity forum in an easily handled database.\n\n**Warning:** New version under development in pre-alpha stage. Current version 2.11.2 does not work.\n\n**Warning**: A cookie file named FA.cookies.json in json format is needed.<br>\n**Warning**: You need to set the theme to \'beta\' on FurAffinity<br>\n**Warning**: On Windows safe interruption does NOT work prior to version 2.10<br>\n**Warning**: On Unix system the provided binaries require installing the pypi modules used in this software (See `Build instructions`)\n\n## Introduction\nThis program was born with the desire to provide a relatively easy-to-use method for FA users to download submissions that they care about from the forum. At the moment its a little more than a text interface in a terminal window with only basic search functionality, a GUI will be hopefully added in the near future.\n\n## Contents\n1. [Usage](#usage)\n    1. [Download & Update](#download--update)\n    2. [Search](#search)\n    3. [Repair database](#repair-database)\n    4. [Interrupt](#interrupt)\n2. [Database](#database)\n3. [Upgrade](#upgrading-from-earlier-versions)\n4. [Cookies](#cookies)\n5. [Build instructions](#build-instructions)\n6. [Troubleshooting & Logging](#troubleshooting--logging)\n    1. [Opening Issues](#opening-issues)\n7. [Appendix](#appendix)\n\n## Usage\nUse the provided binaries or build your own (build instructions at the end) and run from the command line on Linux or double click on Windows.<br>\n`[FA|FA.exe] [options]`\n\nOptions:\n* `--raise`<br>\nAllow exceptions to raise without special handling, useful for troubleshooting\n* `--log`<br>\nLog major program operations to a file named \'FA.log\'\n* `--logv`<br>\nLog all operations (including sub-steps)\n\nTo always use specific options please consult a guide on how to modify default arguments for your operative system.\n\n<br>\nWhen the program starts a simple menu will appear, type the indicated number or key to select an option, there is no need to press ENTER.\n\n### Download & Update\nThis menu allows to download a user gallery, scraps, favorites, extras or to update specific users and/or sections for the database.\n\nWhen a submission is downloaded all its informations (except for the comments and user-made folders) are downloaded into a database located in the same folder the program is launched in. The file (artwork, story, audio, etc...) is saved inside a folder named \'FA.files\' which contains all submissions in a tiered structure based on their ID (e.g submission \'3704554\' will be saved in the folder \'FA.files/0/3/704/0003704554\'). Backup .txt and .html files are also saved with the file, they contain the basic informations and the description and are there for safety (in case the database is accidentally deleted). For a guide on the database structure see `Database` below.\n\n1. `Username: `<br>\nFirst field is reserved for users. To download or sync a specific user/s insert the username/s (url or userpage name are both valid). Usernames can be separated with spaces or commas.\n\n2. `Sections: `<br>\nSecond field is reserved for sections. These can be:\n    * `g` - Gallery\n    * `s` - Scraps\n    * `f` - Favorites\n    * `e` - Extras partial<br>\n    Searches submissions that contain \':iconusername:\' OR \':usernameicon:\' in the description and are not from the user\'s gallery/scraps.\n    * `E` - Extras full<br>\n    Like partial but also searches for \'username\' in the description, keywords and title.\n\n    Sections can be omitted if \'update\' option is used.\n\n3. `Options: `<br>\nLast field is reserved for options. These can be:\n    * `sync`<br>\n    Stops download when a submission already present in the user database entry is encountered.\n    * `update`<br>\n    Reads usernames from the database and downloads new submissions in the respective sections. This option can be used without specifying users or sections, if either is specified then the update will be limited to those user/s and/or section/s.\n    * `forceN`<br>\n    Prevents update and sync from stopping the download at the first already present submission. Download stops at the first downloaded submission from page N+1. Example: \'force4\' will download the first 4 pages with no interruption and will allow the download to stop from page 5.\n    * `all`<br>\n    Like \'force\' but it will prevent interrupting the download for the whole section (this means **ALL** pages from each user will be checked, only use for a limited amount of users).\n    * `slow`<br>\n    Use lowest possible download speed and make sure each submission doesn\'t take less than 1.5 seconds.\n    * `noindex`<br>\n    Do not update indexes after completing the download.\n    * `dbonly`<br>\n    Do not save any file during download/update, save submissions only in the database.\n    * `quit`<br>\n    Quits the program when the current operation is completed.\n\n    Note: options can be inserted with or without spaces between them.\n\n4. After inserting the necessary usernames/sections/options (and making sure their combination is valid) the program will:\n    1. Check connection to FA website\n    2. Build a Session object and add the provided cookies\n    3. Check validity of cookies and bypass cloudflare\n\n    If all these steps are completed without errors then the program will proceed to download the targets. As a bonus feature the program will also handle filetypes to make sure the submission files have the correct extension.<br>\n    If the the program cannot verify the cookies and connect to the forum then it will abort the download and check the cookies for some common errors.\n\n    The program throttles download speed down to 100KB/sec to avoid taxing the forum\'s servers with a huge number of requests and downloads close to each other.\n\n### Search\nThis menu allows to search in the database using one or more among user (with or w/o sections), title, tags, category, species, gender and rating.<br>\n\n1. `User`<br>\nSearch users. Multiple users can be matched.\n\n    * `Section`<br>\n    If a user is selected the search can be restricted to a specific section/s using g, s, f, e.\n\n2. `Title`<br>\nSearch titles.\n\n3. `Description`<br>\nSearch inside submissions\' descriptions.\n\n3. `Tags`<br>\nTags are sorted automatically before search.\n\n4. `Category` \\*<br>\nMatches the category of submissions, like \'Artwork\', \'Story\', etc...\n\n5. `Species` \\*<br>\nSearch species, like \'Vulpine\', \'Feline\', etc...\n\n6. `Gender` \\*<br>\nGender can be \'Male\', \'Female\', \'Any\'.\n\n7. `Rating` \\*<br>\nThe rating can be \'general\', \'mature\' or \'adult\'.\n\n8. `Options`<br>\nThere are two possible options:\n    * `regex`<br>\n    Use regular expressions to search the database. Full regex syntax is supported in all fields.\n    * `case`<br>\n    Turn on case sensitivity on ALL fields. This works in both normal and regex mode.\n    * `web`<br>\n    Search on the website directly. Only user, title, tags, description and rating will be used.\n\nIf indexes aren\'t up to date, and web option wasn\'t used, they will be updated.\n\nResults are ordered by username and date.<br>\nWhen turned on case sensitivity will be enabled for all fields, this means that, for example, \'tiger\' won\'t match anything as the species is saved as \'Tiger\' on FA.<br>\nIf no results can be found in the local database the program will prompt to run the search on the website instead.\n\n\\* *As shown on the submission page on the main site.*\n\n### Repair database\nSelecting this entry will open the database repair menu. There are 6 possible choices.\n1. `Submissions`<br>\nThis will start the analysis and repair of the SUBMISSIONS table.\n    1. `ID`<br>\n    Missing IDs will be flagged.<br>\n    This error type doesn\'t have a fix yet as there is no clear way to identify the submission on FA. However the program cannot create this type of error.\n    2. `Fields`<br>\n    If the id passes the check then the other fields in the submission entry will be searched for misplaced empty strings, incorrect value types and incorrect location.<br>\n    The program will try and fix the errors in-place, replacing NULL values with empty strings. If the automatic fixes are successful then the submission will be checked for missing files, if any is missing then the submission will be passed to the next step. However if the automatic fixes do not work then the corrupted entry will be erased from the database, the files (if any present) deleted and the submission downloaded again, thus also fixing eventual missing files.\n    3. `Files`<br>\n    If the previous checks have passed then the program will check that all submission files are present.<br>\n    The program will simply erase the submission folder to remove any stray file (if any is present) and then download them again.\n\n    Indexes will be redone and database optimized with sqlite `VACUUM` function.\n\n2. `Submission files`<br>\nThis will start the analysis of the submission table in search of submissions whose `FILENAME` column was set to 0 (i.e. an error during the download or in the file itself) and whose `SERVER` column is not 0 (i.e. that are still present on the main website as far the database knows).<br>\nThis missing submission files will be downloaded from scratch again.\n\n3. `Users`<br>\n    1. `Empty users`<br>\n    Users with no folders and no submissions saved will be deleted.\n    3. `Repeating users`<br>\n    Users with multiple entries.<br>\n    All the entries will be merged, the copies deleted and a new entry created. This new entry will be checked for incorrect `FOLDERS` and empty sections.\n    3. `Names`<br>\n    Usernames with capital letters or underscores will be updated to lowercase and the underscores removed.\n    4. `Full names`<br>\n    Full usernames that do not match with their url version will be collected from the submissions database or the website. If both fail they will be substituted with the url version.\n    5. `No folders`<br>\n    Users whose folders entry is empty or missing sections with saved submissions (See `Database`&rarr;`USERS`&rarr;`FOLDERS`) will be updated with said sections (e.g. user \'tiger\' has submissions saved in the `GALLERY` and `FAVORITES` sections but the `FOLDERS` column only contains \'g\' so \'g\' will be added to `FOLDERS`).\n    6. `Empty sections`<br>\n    Users with folders but no submissions saved (e.g. `FOLDERS` contains `s` but the `SCRAPS` column is empty) will be redownloaded from FA (submissions already present in the database won\'t be downloaded again but simply added to the user\'s database entry).\n\n    Indexes will be redone and database optimized with sqlite `VACUUM` function.\n\n4. `Infos`<br>\n    1. `Repeated entries`<br>\n    Repeated entries will be deleted.\n    2. `Version error`<br>\n    If the database version is missing or incorrect it will be fixed.\n    3. `Database name`<br>\n    If the database name is not set to \'\' it will be fixed.\n    4. `Numbers errors`<br>\n    Missing or incorrect totals will be fixed.\n    5. `Update & Download time`<br>\n    Missing or incorrect epoch and duration of last update and download will be reset to 0.\n    5. `Index flag`<br>\n    Missing or not 0/1 `INDEX` flag value.\n\n    Indexes will be redone and database optimized with sqlite `VACUUM` function.\n\n4. `All`<br>\nSubmissions, submission files, users and infos will all be checked and the database re-indexed and optimized.\n\n5. `Analyze`<br>\nSearch for errors in all three tables but do not repair them.\n\n6. `Index`<br>\nIndexes will be updated.\n\n7. `Optimize`<br>\nDatabase will be optimized with sqlite `VACUUM` function.\n\n### Interrupt\nWhile the program is running you can use CTRL-C to interrupt the current operation safely. If a download is in progress it will complete the current submission and exit at the first safe point. Safe interrupt works in all sections of the program.<br>\nIf you\'re using a version of the program lower than 2.10 safe interruption won\'t work on Windows systems.\n\n## Database\nThe database (named \'FA.db\') contains three tables:\n1. `INFOS`<br>\n    * `DBNAME`<br>\n    Database custom name, unused at the moment.\n    * `VERSION`<br>\n    Database version, this can differ from the program version.\n    * `USERN`<br>\n    Number of users in `USERS` table.\n    * `SUBN`<br>\n    Number of submissions in the `SUBMISSIONS` table.\n    * `LASTUP`<br>\n    Time when the last update was started (epoch time, in seconds).\n    * `LASTUPT`<br>\n    Duration of last update (in seconds).\n    * `LASTDL`<br>\n    Time when the last download was started (epoch time).\n    * `LASTDLT`<br>\n    Duration of last download (in seconds).\n    * `INDEX`<br>\n    Boolean value indicating whether indexes were updated after the last download/update.\n\n2. `USERS`<br>\nThe USERS table contains a list of all the users that have been download with the program. Each entry contains the following:\n    * `USER`<br>\n    The url username of the user (no caps and no underscores).\n    * `USERFULL`<br>\n    The full username as chosen by the user (with caps and underscores if present).\n    * `FOLDERS`<br>\n    The sections downloaded for that specific user. A \'!\' beside a section means that the user was disabled, it is used as a flag for the program.*&#42;*\n    * `GALLERY`, `SCRAPS`, `FAVORITES`, `EXTRAS`<br>\n    These contain a list of the submissions IDs downloaded for each section.*&#42;*\n\n    *&#42; For a guide on what each section means see `Usage`&rarr;`Sections`*\n\n\n3. `SUBMISSIONS`<br>\nThe last table is a list of all the single submissions downloaded by the program. Each entry has 14 different values:\n    * `ID`<br>\n    The id of the submission\n    * `AUTHOR`, `AUTHORURL`<br>\n    The author username in normal format and url format (e.g. \'Flying_Tiger\' and \'flyingtiger\')\n    * `TITLE`<br>\n    The title\n    * `UDATE`<br>\n    Upload date\n    * `DESCRIPTION`<br>\n    Description in html format.\n    * `TAGS`<br>\n    The submission\'s keywords sorted alphanumerically\n    * `CATEGORY`, `SPECIES`, `GENDER`, `RATING`<br>\n    The category, species, gender and rating as listed on the submission\'s page on the forum\n    * `FILELINK`, `FILENAME`<br>\n    The link to the submission file on the forum and the name of the downloaded file (all files are named \'submission\' + their proper extension) (an empty or 0 value means the file has an error on the forum and has not been downloaded)\n    * `LOCATION`<br>\n    The location in the current folder of the submission\'s file, description and backup informations file.\n    * `SERVER`<br>\n    This last field is defaulted to 1 and only updated to 0 if the program checks the submission on the forum and finds it missing (because the uploaded has either disabled or deleted it)\n\nThe database is built using sqlite so it can be easily opened and searched with a vast number of third-party programs. A good one is \'DB Browser for SQLite\' (http://sqlitebrowser.org/) which is open source, cross-platform and has a project page here on GitHub.\n\n## Upgrading from earlier versions\nWhen the program is started it will check the database for its version. If the database version is lower than the program then it will update it depending on the difference between the two.\n* `0.x` to `1.x` &rarr; `2.x`<br>\nNew informations handled by version 2 and onward will be downloaded and added to the database, these include submission category, rating, gender and species. Depending on the size of the database to be updated this process may take a long time.<br>\nThe older version of the database will be saved as \'FA.v1.db\'\n* `2.0` to `2.2` &rarr; `2.3`<br>\nFull versions of users\' nicknames will be collected from the submissions database or the website. If both fail the url version will be used instead.<br>\nThe older version of the database will be saved as \'FA.v2.db\'\n* `2.3` &rarr; `2.6`<br>\nTwo columns in the `USERS` will be renamed (`NAME`&rarr;`USER` and `NAMEFULL`&rarr;`USERFULL`) and descriptions will be moved inside the database. It is recommended to run `Repair` (See `Usage`&rarr;`Repair database` for details) with a version lower than 2.6 to make sure all description files are present. When the upgrade is completed indexes will be created for all fields.<br>\nSize of the database will increase by about 2,8KB per submission (averaged on a database of over 234k submissions which increased by about 653MB).<br>\nThe older version of the database will be saved as \'FA.v2_3.db\'\n* `2.6` &rarr; `2.7`<br>\nEntry `INDEX` will be added to `INFOS` table.\nThis upgrade cannot be interrupted and resumed later, however it is very fast being mostly a copy-paste.\n\nAt each update step the program will save a backup copy of the database.\n\nUpdate can be interrupted and resumed later without losing progress.\n\n**Warning**: The update cannot be skipped, to keep using a specific version of the database you need to download the release relative to that version\n\n## Cookies\nThe program needs to use cookies from a login session to successfully connect to FA. These cookies need to be in json format and can be easily extracted from Firefox/Chrome/Opera/Vivaldi/etc... using extensions or  manually. The value must be written in a file named FA.cookies.json<br>\n(The value is fake)\n```json\n[\n  {\n    "domain": ".furaffinity.net",\n    "expirationDate": 1511387940,\n    "hostOnly": false,\n    "httpOnly": false,\n    "name": "__asc",\n    "path": "/",\n    "sameSite": "no_restriction",\n    "secure": false,\n    "session": false,\n    "storeId": "0",\n    "value": "kee3gpzjurkaq9fbyrubhys7epk",\n    "id": 1\n  },\n]\n```\nThe following cookie names are needed in order to successfully connect:\n* \\_\\_asc\n* \\_\\_auc\n* \\_\\_cfduid\n* \\_\\_gads\n* \\_\\_qca\n* a\n* b\n* \\_adb\n\nOnly \'name\' and \'value\' are needed for each cookie so the file can also be composed by entries like this:\n```json\n[\n  {\n    "name": "__asc",\n    "value": "kee3gpzjurkaq9fbyrubhys7epk",\n  },\n]\n```\n\n## Build Instructions\nThis program is written with Python 3.x, Python 2.x will **NOT** work.\n\nTo run and/or build the program you will need the following pypi modules:\n* [requests](https://github.com/requests/requests)\n* [cfscrape](https://github.com/Anorov/cloudflare-scrape)\n* [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)\n* [lxml](https://github.com/lxml/lxml/)\n* [filetype](https://github.com/h2non/filetype.py)\n\nThe following non-pypi modules (already included in this repo as submodules):\n* [PythonRead](https://gitlab.com/MatteoCampinoti94/PythonRead)\n* [SignalBlock](https://gitlab.com/MatteoCampinoti94/PythonSignalBlocking-CrossPlatform)\n\nThe following modules are used but available by default:\n* [json](https://docs.python.org/3/library/json.html)\n* [os](https://docs.python.org/3.1/library/os.html)\n* [re](https://docs.python.org/3.1/library/re.html)\n* [signal](https://docs.python.org/3.1/library/signal.html) (only for Unix)\n* [sqlite3](https://docs.python.org/3.1/library/sqlite3.html)\n* [sys](https://docs.python.org/3.1/library/sys.html)\n* [time](https://docs.python.org/3.1/library/time.html)\n\nOnce these modules are installed (suggest using `pip`) then the program can be run through the Python 3.x interpreter or built using `pyinstaller` or any other software.\n\n## Troubleshooting & Logging\nThe program is set up so that any unforeseen error interrupts the program after displaying the error details. To get extra information the program can be run with the `--raise` argument which will allow exceptions to raise normally.\n\nTo get details of all operations the program can be run with \'--log\' or \'--logv\' arguments, warning and errors are saved regardless of the settings. Details will be saved in a file named \'FA.log\' with the format: "`YYYY-MM-DD hh:mm:ss.ssssss | LOG TYPE [N|V|W] | OPERATION -> detail`". Using \'--log\' will only log major passages; \'--logv\' will log all operations to file.\n\n### Opening issues\nBefore opening an issue please run the program with \'--raise\' and \'--logv\' arguments and copy the resulting log and exception/s details printed on screen.\n\n## Appendix\n### Unverified commits\nAll commits before the 27th of January 2018 show as unverified because I accidentally revoked my old GPG key before adding a new one. They have all been added by me and can vouch for their authenticity.<br>\nSome commits before e76e993b show as unverified, these were done with GitHub\'s editor and thus their GPG signature cannot be verified by GitLab.\nCommits 96143db5-7d40880b (09-10/07/2018) are unverified because of an error with the GPG key.\n\n### Early releases\nRelease binaries before and including v2.10.2 can be found on GitHub -> [Releases](https://github.com/MatteoCampinoti94/FALocalRepo/releases)\n',
    'author': 'Matteo Campinoti',
    'author_email': 'matteo.campinoti94@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/MatteoCampinoti94/FALocalRepo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
