# coding=utf-8
from QuickStart_Rhy.API import *
import requests

# alapi_token = pre_check('alapi_token')


def upimg(filePath: str, plt_type: str = 'Ali'):
    """
    上传图片或Markdown中所有的图片到多平台（免API KEY，但不保证数据安全）

    Upload images or all images from Markdown to multiple platforms (API-free KEY, but data security is not guaranteed)

    :param filePath: 图片或Markdown文件路径
    :param plt_type: 平台（使用 qs -upimg -help查看支持的平台）
    :return: None
    """
    from prettytable import PrettyTable

    def post_img(path):
        if not os.path.exists(path):
            return False
        try:
            data = {'type': plt_type}
            file = [('image', open(path, 'rb'))]
        except:
            return False
        res_json = requests.post('https://v1.alapi.cn/api/image',
                                 data=data, files=file).text
        return json.loads(res_json)

    def get_path(rt, rel):
        return os.path.abspath(rt + rel)

    def format_markdown(path):
        import re
        _user_path = os.path.expanduser('~')
        rt_path = dir_char.join(os.path.abspath(path).split(dir_char)[:-1]) + dir_char
        res_tb = PrettyTable()
        res_tb.field_names = ['File', 'Status', 'url']
        img_set = {}
        with open(path, 'r') as fp:
            ct = fp.read()
        aims = re.findall('!\[.*?]\((.*?)\)', ct, re.M)
        for aim in aims:
            raw_path = aim
            aim = aim.replace('~', _user_path)
            aim = aim if aim.startswith(dir_char) else get_path(rt_path, aim)
            if aim not in img_set:
                res_dict = post_img(aim)
                if not res_dict:
                    res_tb.add_row([aim.split(dir_char)[-1], 'No File', ''])
                    img_set[aim] = False
                else:
                    res_tb.add_row([aim.split(dir_char)[-1], res_dict['msg'],
                                    '' if res['code'] != 200 else (
                                        res_dict['data']['url'][plt_type]
                                        if res_dict['data']['url'][plt_type].lower() != 'null'
                                        else plt_type + ' failed')]
                                   )
                    if res_dict['code'] != 200:
                        break
                    img_set[aim] = res_dict['data']['url'][plt_type] if res_dict['code'] != 200 else False
            if img_set[aim]:
                ct = ct.replace(raw_path, img_set[aim])
        with open(path, 'w') as fp:
            fp.write(ct)
        print(res_tb)

    try:
        is_md = filePath.endswith('.md')
    except IndexError:
        exit('Usage: qs {*.md} | {picture}')
    else:
        if is_md:
            format_markdown(filePath)
        else:
            res = post_img(filePath)
            tb = PrettyTable(['File', 'Status', 'url'])
            if not res:
                tb.add_row([filePath.split(dir_char)[-1], 'No File', ''])
            else:
                tb.add_row([filePath.split(dir_char)[-1], res['msg'],
                            '' if res['code'] != 200 else (
                                res['data']['url'][plt_type]
                                if str(res['data']['url'][plt_type].lower()) not in ['false', 'null']
                                else plt_type + ' failed')]
                           )
            print(tb)


def translate(text: str, from_lang: str = None, to_lang: str = user_lang):
    """
    获取翻译结果

    Get the translation results.
    
    :param text: 待翻译内容 | Content to be translated.
    :param from_lang: 语种来源 | Source language
    :param to_lang: 翻译成的语种 | Translated into the language
    :return: 翻译的文本 | Translated text
    """
    from urllib.parse import quote
    request_info = 'q={}&from={}&to={}'.format(quote(text, 'utf-8'), from_lang, to_lang) if from_lang \
        else 'q={}&to={}'.format(quote(text, 'utf-8'), to_lang)
    res = requests.post('https://v1.alapi.cn/api/fanyi', data=request_info,
                        headers={'Content-Type': "application/x-www-form-urlencoded"})
    if res.status_code == requests.codes.ok:
        res = json.loads(res.text)
    if res['code'] != 200:
        return "[ERROR] {}".format(res['msg'])
    return res['data']['trans_result'][0]['dst']


def bili_cover(url: str):
    """
    获取BiliBili视频封面

    Get the BiliBili video cover

    :param url: BiliBili视频链接或视频号 | BiliBili video link or video number
    :return:
    """
    import re
    from QuickStart_Rhy.NetTools.normal_dl import normal_dl
    res = requests.post('https://v1.alapi.cn/api/bbcover', data='c='+url,
                        headers={'Content-Type': 'application/x-www-form-urlencoded'})
    if res.status_code == requests.codes.ok:
        res = json.loads(res.text)
        if res['code'] != 200 or res['msg'] != 'success':
            print("[ERROR] Get cover with: %s failed")
            return
        res = res['data']
        res['description'] = res['description'].replace('<br />', '\n\t')
        res['description'] = res['description'].replace('&nbsp;', ' ')
        res['description'] = re.sub('<.*?>', '', res['description']).strip()
        print('[TITLE] %s' % res['title'])
        print('[INFO ]\n', end='\t')
        print(res['description'], end='\n\n')
        normal_dl(res['cover'], res['title'] + '.' + res['cover'].split('.')[-1])
    else:
        print("[ERROR] Get cover with: %s failed" % url)


def ip_info(ip: str):
    """
    获取ip的运营商、地理位置等数据

    Get IP operator, geographic location and other data

    :param ip: ipv4, ipv6, empty means current machine
    :return: data dict
    """
    res = requests.post('https://v1.alapi.cn/api/ip', data="ip=%s&format=json" % ip,
                        headers={'Content-Type': "application/x-www-form-urlencoded"} if ip else headers)
    return json.loads(res.text)['data']
