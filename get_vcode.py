import requests
import time
from io import BytesIO
import PIL.Image


class GetVerifyCode:
    def __init__(self):
        self.ver_code_url = 'http://jwglxt.qau.edu.cn/verifycode.servlet'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }
        self.proxies_url = 'http://dps.kdlapi.com/api/getdps/?orderid=928357199059918&num=1&pt=1&sep=1'
        self.proxie = {
            'http' : '',
            'https' : '',
        }

    def change_poxies(self):
        p = requests.get(self.proxies_url).text
        self.proxie['http'] = p
        self.proxie['https'] = p

    def start_process(self, times):
        sum = 0
        total_num = 0
        print("开始爬取")
        for file_name in range(sum, times):
            try:
                verify_code_response = requests.get(self.ver_code_url, headers=self.headers, proxies=self.proxie)
                if verify_code_response.status_code == 200:
                    byte_img = BytesIO(verify_code_response.content)
                    image_name = 'vcode_imgs\\' + str(sum) + ".png"
                    a = PIL.Image.open(byte_img)
                    a.save(image_name)
                    sum += 1
                    total_num += 1
                    time.sleep(0.1)
                    if total_num == 300:  # 每30s切换一个代理
                        self.change_poxies()
                        total_num = 0
                        print("成功爬取一组 总共爬取{}张".format(sum))
                else:
                    print("请求超时1次 等待切换代理")
            except:
                sum -= 1
                total_num -= 1
                self.change_poxies()
                print("出现未知错误 已直接换代理")


if __name__ == '__main__':
    GVC = GetVerifyCode()
    GVC.change_poxies()
    GVC.start_process(8646)