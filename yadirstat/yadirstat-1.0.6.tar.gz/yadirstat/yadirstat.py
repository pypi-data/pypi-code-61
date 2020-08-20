import requests
from requests.exceptions import ConnectionError
from time import sleep
import json
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import random

# Метод для корректной обработки строк в кодировке UTF-8 как в Python 3, так и в Python 2
import sys






#Создаем класс
class yadirstat:

    def campaign(token,login,date_from,date_to):
        if sys.version_info < (3,):
            def u(x):
                try:
                    return x.encode("utf8")
                except UnicodeDecodeError:
                    return x
        else:
            def u(x):
                if type(x) == type(b''):
                    return x.decode('utf8')
                else:
                    return x

            # --- Входные данные ---
            # Адрес сервиса Reports для отправки JSON-запросов (регистрозависимый)
        ReportsURL = 'https://api.direct.yandex.com/json/v5/reports'

        # OAuth-токен пользователя, от имени которого будут выполняться запросы
        token = token

        # рандомный номер отчета
        num_report=random.randint(1, 1000000000)

        # Логин клиента рекламного агентства
        # Обязательный параметр, если запросы выполняются от имени рекламного агентства
        clientLogin = login

        # --- Подготовка, выполнение и обработка запроса ---
        # Создание HTTP-заголовков запроса
        headers = {
            # OAuth-токен. Использование слова Bearer обязательно
            "Authorization": "Bearer " + token,
            # Логин клиента рекламного агентства
            "Client-Login": clientLogin,
            # Язык ответных сообщений
            "Accept-Language": "ru",
            # Режим формирования отчета
            "processingMode": "auto",
            # Формат денежных значений в отчете
            "returnMoneyInMicros": "false",
            # Не выводить в отчете строку с названием отчета и диапазоном дат
            "skipReportHeader": "true",
            # Не выводить в отчете строку с названиями полей
            # "skipColumnHeader": "true",
            # Не выводить в отчете строку с количеством строк статистики
            "skipReportSummary": "true"
        }

        # Создание тела запроса
        body = {
            "params": {
                "SelectionCriteria": {
                    "DateFrom": date_from,
                    "DateTo": date_to,

                },
                "FieldNames": [
                    "CampaignName",
                    "Date",
                    "Impressions",
                    "Clicks",
                    "Ctr",
                    "Cost",
                    "AvgCpc",
                    "BounceRate",
                    "AvgPageviews",
                    "ConversionRate",
                    "CostPerConversion",
                    "Conversions"
                ],
                "ReportName": u(num_report),
                "ReportType": "CAMPAIGN_PERFORMANCE_REPORT",
                "DateRangeType": "CUSTOM_DATE",
                "Format": "TSV",
                "IncludeVAT": "YES",
                "IncludeDiscount": "NO"
            }
        }

        # Кодирование тела запроса в JSON
        body = json.dumps(body, indent=4)

        # Запуск цикла для выполнения запросов
        # Если получен HTTP-код 200, то выводится содержание отчета
        # Если получен HTTP-код 201 или 202, выполняются повторные запросы
        while True:
            try:
                req = requests.post(ReportsURL, body, headers=headers)
                req.encoding = 'utf-8'  # Принудительная обработка ответа в кодировке "UTF-8"
                if req.status_code == 400:
                    print("Параметры запроса указаны неверно или достигнут лимит отчетов в очереди")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код запроса: {}".format(u(body)))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break
                elif req.status_code == 200:
                    format(u(req.text))
                    break
                elif req.status_code == 201:
                    print("Отчет успешно поставлен в очередь в режиме офлайн")
                    retryIn = int(req.headers.get("retryIn", 60))
                    print("Повторная отправка запроса через {} секунд".format(retryIn))
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    sleep(retryIn)
                elif req.status_code == 202:
                    print("Отчет формируется в режиме офлайн")
                    retryIn = int(req.headers.get("retryIn", 60))
                    print("Повторная отправка запроса через {} секунд".format(retryIn))
                    print("RequestId:  {}".format(req.headers.get("RequestId", False)))
                    sleep(retryIn)
                elif req.status_code == 500:
                    print("При формировании отчета произошла ошибка. Пожалуйста, попробуйте повторить запрос позднее")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break
                elif req.status_code == 502:
                    print("Время формирования отчета превысило серверное ограничение.")
                    print(
                        "Пожалуйста, попробуйте изменить параметры запроса - уменьшить период и количество запрашиваемых данных.")
                    print("JSON-код запроса: {}".format(body))
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break
                else:
                    print("Произошла непредвиденная ошибка")
                    print("RequestId:  {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код запроса: {}".format(body))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break

            # Обработка ошибки, если не удалось соединиться с сервером API Директа
            except ConnectionError:
                # В данном случае мы рекомендуем повторить запрос позднее
                print("Произошла ошибка соединения с сервером API")
                # Принудительный выход из цикла
                break

            # Если возникла какая-либо другая ошибка
            except:
                # В данном случае мы рекомендуем проанализировать действия приложения
                print("Произошла непредвиденная ошибка")
                # Принудительный выход из цикла
                break
        # Кешируем полученные данные в csv чтобы позже вытащить из него dataframe
        file = open("cashe.csv", "w")
        file.write(req.text)
        file.close()
        # Читаем из csv dataframe
        f = pd.read_csv("cashe.csv", header=0, sep='	', parse_dates=True, index_col=1, na_values=["--"]).fillna(0)
        f['Date'] = f.index
        # Делаем из столбца с датами индексный столбец



        return f

    def criteria(token, login, date_from, date_to):
        if sys.version_info < (3,):
            def u(x):
                try:
                    return x.encode("utf8")
                except UnicodeDecodeError:
                    return x
        else:
            def u(x):
                if type(x) == type(b''):
                    return x.decode('utf8')
                else:
                    return x

        # --- Входные данные ---
        # Адрес сервиса Reports для отправки JSON-запросов (регистрозависимый)
        ReportsURL = 'https://api.direct.yandex.com/json/v5/reports'

        # OAuth-токен пользователя, от имени которого будут выполняться запросы
        token = token

        # рандомный номер отчета
        num_report = random.randint(1, 10000000)

        # Логин клиента рекламного агентства
        # Обязательный параметр, если запросы выполняются от имени рекламного агентства
        clientLogin = login

        # --- Подготовка, выполнение и обработка запроса ---
        # Создание HTTP-заголовков запроса
        headers = {
            # OAuth-токен. Использование слова Bearer обязательно
            "Authorization": "Bearer " + token,
            # Логин клиента рекламного агентства
            "Client-Login": clientLogin,
            # Язык ответных сообщений
            "Accept-Language": "ru",
            # Режим формирования отчета
            "processingMode": "auto",
            # Формат денежных значений в отчете
            "returnMoneyInMicros": "false",
            # Не выводить в отчете строку с названием отчета и диапазоном дат
            # "skipReportHeader": "true",
            # Не выводить в отчете строку с названиями полей
            # "skipColumnHeader": "true",
            # Не выводить в отчете строку с количеством строк статистики
            "skipReportSummary": "true"
        }

        # Создание тела запроса
        body = {
            "params": {
                "SelectionCriteria": {
                    "DateFrom": date_from,
                    "DateTo": date_to,

                },
                "FieldNames": [
                    "CampaignName",
                    "Criterion",
                    "Impressions",
                    "Clicks",
                    "Ctr",
                    "Cost",
                    "AvgCpc",
                    "Date"

                ],
                "ReportName": u(num_report),
                "ReportType": "CRITERIA_PERFORMANCE_REPORT",
                "DateRangeType": "CUSTOM_DATE",
                "Format": "TSV",
                "IncludeVAT": "YES",
                "IncludeDiscount": "NO"
            }
        }

        # Кодирование тела запроса в JSON
        body = json.dumps(body, indent=4)

        # Запуск цикла для выполнения запросов
        # Если получен HTTP-код 200, то выводится содержание отчета
        # Если получен HTTP-код 201 или 202, выполняются повторные запросы
        while True:
            try:
                req = requests.post(ReportsURL, body, headers=headers)
                req.encoding = 'utf-8'  # Принудительная обработка ответа в кодировке "UTF-8"
                if req.status_code == 400:
                    print("Параметры запроса указаны неверно или достигнут лимит отчетов в очереди")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код запроса: {}".format(u(body)))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break
                elif req.status_code == 200:
                    format(u(req.text))
                    break
                elif req.status_code == 201:
                    print("Отчет успешно поставлен в очередь в режиме офлайн")
                    retryIn = int(req.headers.get("retryIn", 60))
                    print("Повторная отправка запроса через {} секунд".format(retryIn))
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    sleep(retryIn)
                elif req.status_code == 202:
                    print("Отчет формируется в режиме офлайн")
                    retryIn = int(req.headers.get("retryIn", 60))
                    print("Повторная отправка запроса через {} секунд".format(retryIn))
                    print("RequestId:  {}".format(req.headers.get("RequestId", False)))
                    sleep(retryIn)
                elif req.status_code == 500:
                    print("При формировании отчета произошла ошибка. Пожалуйста, попробуйте повторить запрос позднее")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break
                elif req.status_code == 502:
                    print("Время формирования отчета превысило серверное ограничение.")
                    print(
                        "Пожалуйста, попробуйте изменить параметры запроса - уменьшить период и количество запрашиваемых данных.")
                    print("JSON-код запроса: {}".format(body))
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break
                else:
                    print("Произошла непредвиденная ошибка")
                    print("RequestId:  {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код запроса: {}".format(body))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break

            # Обработка ошибки, если не удалось соединиться с сервером API Директа
            except ConnectionError:
                # В данном случае мы рекомендуем повторить запрос позднее
                print("Произошла ошибка соединения с сервером API")
                # Принудительный выход из цикла
                break

            # Если возникла какая-либо другая ошибка
            except:
                # В данном случае мы рекомендуем проанализировать действия приложения
                print("Произошла непредвиденная ошибка")
                # Принудительный выход из цикла
                break
        # Кешируем полученные данные в csv чтобы позже вытащить из него dataframe
        file = open("cashe.csv", "w")
        file.write(req.text)
        file.close()
        # Читаем из csv dataframe
        f = pd.read_csv("cashe.csv", header=1, sep='	', index_col=0, na_values=["--"]).fillna(0)
        return f

    def query(token, login, date_from, date_to):
        if sys.version_info < (3,):
            def u(x):
                try:
                    return x.encode("utf8")
                except UnicodeDecodeError:
                    return x
        else:
            def u(x):
                if type(x) == type(b''):
                    return x.decode('utf8')
                else:
                    return x

        # --- Входные данные ---
        # Адрес сервиса Reports для отправки JSON-запросов (регистрозависимый)
        ReportsURL = 'https://api.direct.yandex.com/json/v5/reports'

        # OAuth-токен пользователя, от имени которого будут выполняться запросы
        token = token

        # рандомный номер отчета
        num_report = random.randint(1, 10000000)

        # Логин клиента рекламного агентства
        # Обязательный параметр, если запросы выполняются от имени рекламного агентства
        clientLogin = login

        # --- Подготовка, выполнение и обработка запроса ---
        # Создание HTTP-заголовков запроса
        headers = {
            # OAuth-токен. Использование слова Bearer обязательно
            "Authorization": "Bearer " + token,
            # Логин клиента рекламного агентства
            "Client-Login": clientLogin,
            # Язык ответных сообщений
            "Accept-Language": "ru",
            # Режим формирования отчета
            "processingMode": "auto",
            # Формат денежных значений в отчете
            "returnMoneyInMicros": "false",
            # Не выводить в отчете строку с названием отчета и диапазоном дат
            # "skipReportHeader": "true",
            # Не выводить в отчете строку с названиями полей
            # "skipColumnHeader": "true",
            # Не выводить в отчете строку с количеством строк статистики
            "skipReportSummary": "true"
        }

        # Создание тела запроса
        body = {
            "params": {
                "SelectionCriteria": {
                    "DateFrom": date_from,
                    "DateTo": date_to,

                },
                "FieldNames": [
                    "CampaignName",
                    "Query",
                    "Impressions",
                    "Clicks",
                    "Ctr",
                    "Cost",
                    "AvgCpc",
                    "ConversionRate",
                    "CostPerConversion",
                    "Conversions"

                ],
                "ReportName": u(num_report),
                "ReportType": "SEARCH_QUERY_PERFORMANCE_REPORT",
                "DateRangeType": "CUSTOM_DATE",
                "Format": "TSV",
                "IncludeVAT": "YES",
                "IncludeDiscount": "NO"
            }
        }

        # Кодирование тела запроса в JSON
        body = json.dumps(body, indent=4)

        # Запуск цикла для выполнения запросов
        # Если получен HTTP-код 200, то выводится содержание отчета
        # Если получен HTTP-код 201 или 202, выполняются повторные запросы
        while True:
            try:
                req = requests.post(ReportsURL, body, headers=headers)
                req.encoding = 'utf-8'  # Принудительная обработка ответа в кодировке "UTF-8"
                if req.status_code == 400:
                    print("Параметры запроса указаны неверно или достигнут лимит отчетов в очереди")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код запроса: {}".format(u(body)))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break
                elif req.status_code == 200:
                    format(u(req.text))
                    break
                elif req.status_code == 201:
                    print("Отчет успешно поставлен в очередь в режиме офлайн")
                    retryIn = int(req.headers.get("retryIn", 60))
                    print("Повторная отправка запроса через {} секунд".format(retryIn))
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    sleep(retryIn)
                elif req.status_code == 202:
                    print("Отчет формируется в режиме офлайн")
                    retryIn = int(req.headers.get("retryIn", 60))
                    print("Повторная отправка запроса через {} секунд".format(retryIn))
                    print("RequestId:  {}".format(req.headers.get("RequestId", False)))
                    sleep(retryIn)
                elif req.status_code == 500:
                    print("При формировании отчета произошла ошибка. Пожалуйста, попробуйте повторить запрос позднее")
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break
                elif req.status_code == 502:
                    print("Время формирования отчета превысило серверное ограничение.")
                    print(
                        "Пожалуйста, попробуйте изменить параметры запроса - уменьшить период и количество запрашиваемых данных.")
                    print("JSON-код запроса: {}".format(body))
                    print("RequestId: {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break
                else:
                    print("Произошла непредвиденная ошибка")
                    print("RequestId:  {}".format(req.headers.get("RequestId", False)))
                    print("JSON-код запроса: {}".format(body))
                    print("JSON-код ответа сервера: \n{}".format(u(req.json())))
                    break

            # Обработка ошибки, если не удалось соединиться с сервером API Директа
            except ConnectionError:
                # В данном случае мы рекомендуем повторить запрос позднее
                print("Произошла ошибка соединения с сервером API")
                # Принудительный выход из цикла
                break

            # Если возникла какая-либо другая ошибка
            except:
                # В данном случае мы рекомендуем проанализировать действия приложения
                print("Произошла непредвиденная ошибка")
                # Принудительный выход из цикла
                break
        # Кешируем полученные данные в csv чтобы позже вытащить из него dataframe
        file = open("cashe.csv", "w")
        file.write(req.text)
        file.close()
        # Читаем из csv dataframe
        f = pd.read_csv("cashe.csv", header=1, sep='	', index_col=0, na_values=["--"]).fillna(0)

        return f


