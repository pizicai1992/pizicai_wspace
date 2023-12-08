# -*- coding: utf-8 -*-
import argparse
import sys
import os
import requests
import json
import hashlib
import random
import time
from textwrap import dedent


class HttpGet:
    URL = 'https://partner.oceanengine.com/union/media/open/api/report/slot'
    USER_ID = '15147'
    HEADERS = {'content-type': 'application/json'}
    SECURE_KEY = '1e1a2f292bdf8ce23ca8d85f085224aa'

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.nonce = str(random.randint(10000000, 99999999))
        self.timestamp = str(int(time.time()))

    def signature_gen(self):
        keys = [HttpGet.SECURE_KEY, self.timestamp, self.nonce]
        keys.sort()
        keystr = ''.join(keys)
        signature = hashlib.sha1(keystr).hexdigest()
        return signature

    def get_data(self):
        headers = {'content-type': 'application/json'}
        sign = self.signature_gen()
        params = {'sign': sign, 'user_id': HttpGet.USER_ID, 'nonce': self.nonce,
                  'timestamp': self.timestamp, 'start_date': self.start_date, 'end_date': self.end_date}
        res = requests.get(url=HttpGet.URL, params=params, headers=headers)
        if res.status_code != requests.codes.ok:
            res.raise_for_status()
            sys.exit(1)
        get_cnt = 0
        while res.text is None:
            res = requests.get(url=HttpGet.URL, params=params, headers=headers)
            get_cnt += 1
            if get_cnt == 36:
                break
            time.sleep(300)

        user_data = json.loads(res.text)
        res_data = user_data['data']
        return res_data


def write_local_data(data_text, data_date):
    file_path = '/usr/local/app/wlk/%s' % data_date
    log_name = 't_sd_qqbook_ad_csj_income.log'
    file_name = os.path.join(file_path, log_name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    data_lines = []
    for line in data_text:
        ad_id = str(line['ad_id'])
        ad_name = str(line['ad_name'])
        column = [ad_id, ad_name]
        line_text = '|'.join(column)
        line_text = line_text + '\n'
        data_lines.append(line_text)

    with open(file_name, 'w') as f:
        f.writelines(data_lines)


def input_args_parse():
    if len(sys.argv[1:]) < 1:
        print(dedent("""\
        Warning : 参数不能为空
        Usage   : python get_csj_apidata.py -d YYYY-MM-DD"""))
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Get ad data from CSJ-API by HTTP-GET", conflict_handler='resolve')
    parser.add_argument('-d', '--date', required=True, help='数据的日期,格式YYYY-MM-DD')
    args = parser.parse_args()
    long_date = args.date
    # short_date = long_date.replace('-', '')
    return  long_date


def main():
    long_date = input_args_parse()
    short_date = long_date.replace('-', '')
    http_get = HttpGet(start_date=long_date, end_date=long_date)
    result_data = http_get.get_data()
    write_local_data(result_data, short_date)


if __name__ == '__main__':
    main()

