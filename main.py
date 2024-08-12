# -*- coding: utf-8 -*-
import requests

def main(your_file_path: str, your_access_token=None, your_refresh_token=None):
    '''

    :param your_file_path: 你的文件在百度网盘中的路径，'/我的资源/...'
    :param your_access_token: access_token
    :param your_refresh_token: refresh_token用于获取access_token，访问https://alist.nn.ci/zh/guide/drivers/baidu.html获取
    :return:对应文件的下载直链，搭配aria下载
    '''
    file_path = your_file_path
    refresh_token = your_refresh_token

    if your_refresh_token:
        access_token_json = requests.get('https://openapi.baidu.com/oauth/2.0/token', params={
                        'grant_type': 'refresh_token',
                        'refresh_token': f'{refresh_token}',
                        'client_id': 'iYCeC9g08h5vuP9UqvPHKKSVrKFXGa1v',
                        'client_secret': 'jXiFMOPVPCWlO2M5CwWQzffpNPaGTRBG',
                    }).json()
        access_token = access_token_json['access_token']
    else:
        access_token = your_access_token
    resp = requests.get('https://pan.baidu.com/api/filemetas', params={
          'target': f'["{file_path}"]',
          'dlink': 1,
          'web': 5,
          'origin': 'dlna',
          'access_token': f'{access_token}',
      }, headers={
          'User-Agent': 'netdisk',
      })
    download_link = f"{resp.json()['info'][0]['dlink']}&access_token={your_access_token}"
    print(download_link)


if __name__ == '__main__':
    your_file_path = ''
    your_access_token = ''
    your_refresh_token = ''
    if not your_access_token and not your_refresh_token:
        raise '请输入your_access_token或者your_refresh_token'
    main()
