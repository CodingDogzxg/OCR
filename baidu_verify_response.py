# encoding:utf-8
import requests
import base64
import time

'''
通用文字识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
access_token = ''  # 百度AI的token access 详情请去看文档
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}

for file_index in range(10000):
    file_name = 'vcode_imgs/' + str(file_index) + '.png'
    f_obj = open(file_name, 'rb')
    img = base64.b64encode(f_obj.read())
    f_obj.close()
    params = {"image": img}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        answer = response.content.decode().split(",")[-1].split("\"")[-2].replace(' ', '').lower()

        if len(answer) < 5:
            with open('baidu_ocr_verify_response.json', 'a') as f:
                f.write('{}:{}\n'.format(str(file_index) + '.png', answer))
        else:
            with open('baidu_ocr_verify_response.json', 'a') as f:
                f.write('{}:{}\n'.format(str(file_index) + '.png', '识别失败'))
            print('对文件{}.png的识别失败 请手动核对'.format(file_index))
    time.sleep(0.2)