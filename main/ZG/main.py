#from fake_useragent import UserAgent
from types import SimpleNamespace
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


# 订阅,0关闭
dingyue = 1
# 短信,0关闭
duanxin = 1
# 设置翻页范围
start_page = 1
end_page = 1


def main():
    _list = [
        ['18888888888', '张三']
    ]
    _run(_list)


def _run(_list):
    delay = 1
    option = webdriver.ChromeOptions()
    # option.add_argument('--disable-gpu')
    option.add_argument('--incognito')
    option.add_argument('blink-settings=imagesEnabled=false')
    option.add_argument('--headless')
    ua = 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
    option.add_argument('--user-agent={}'.format(ua))
    driver = webdriver.Chrome(options=option)
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                           'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    driver.maximize_window()
    driver.get("https://www.baidu.com/")

    title = '/html/body/div[5]/div[3]/div[1]/div[2]/ul/li[$]/div/a'
    citys = ['bj', 'tj', 'dl', 'qd', 'jn', 'sy', 'cc', 'yt', 'heb', 'sjz', 'taiyuan', 'wf', 'zb', 'hhht', 'sh', 'hz', 'su', 'nj', 'wx', 'nb', 'nt', 'cz', 'hf', 'sx', 'jx', 'yz', 'jh',
             'ks', 'gz', 'sz', 'fs', 'fz', 'dg', 'xm', 'nn', 'zh', 'zs', 'huizhou', 'jm', 'sanya', 'hk', 'qz', 'cd', 'wh', 'cq', 'cs', 'zz', 'xa', 'km', 'nc', 'gy', 'wlmq', 'lz', 'yc', 'ly']
    # citys = ['tj']

    # 遍历城市列表
    for city in citys:
        # 打开page页
        for page in range(start_page, end_page+1):
            href = "http://"+city+".xinfang.zhuge.com/page/"+str(page)+"/"
            driver.execute_script(f'window.open("{href}", "_blank");')
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(3)
            try:
                driver.switch_to.alert.dismiss()
                time.sleep(delay)
            except:
                pass
            urls = driver.find_elements(By.CLASS_NAME, "imgbox")
            houses = []
            # 从page页获取楼盘链接存入houses[]
            for url in urls:
                houses.append(url.get_attribute("href"))
            # 逐个打开楼盘页并处理
            for house in houses:
                os.system('cls')
                print(
                    '正在第{}/{}个城市{}订阅第{}/{}页，当页进度:{}/{}'.format(str(citys.index(city)+1), str(len(citys)),  city, str(page), str(end_page), str(houses.index(house)+1), str(len(houses))))
                try:
                    # 打开楼盘页
                    driver.execute_script(f'window.open("{house}", "_blank");')
                    driver.switch_to.window(driver.window_handles[0])
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    # 关闭广告
                    try:
                        driver.find_element(
                            By.CSS_SELECTOR, "[class='ad_button']").click()
                    except:
                        pass
                    # 删除遮挡元素
                    try:
                        js = "document.getElementsByClassName('customer-service')[0].remove();document.getElementsByClassName('hover-side-bar hover-side-bar-top')[0].remove();"
                        driver.execute_script(js)
                    except:
                        pass
                    '''
                    # 滚动到指定位置
                    js = 'window.scrollTo(0,1500)'
                    driver.execute_script(js)
                    '''
                    # 操作
                    try:
                        for person in _list:
                            if(duanxin != 0):
                                ## 发送地址给手机 ##
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='appointment-look lpdz']").click()
                                except:
                                    pass

                                # 输入电话
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='phoneNum']").send_keys(person[0])
                                except:
                                    pass
                                # 点击领取
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='entry-submit j_entrySubmit liuzi-dialog-btn']").click()
                                except:
                                    pass
                                time.sleep(delay)
                                # 关闭弹窗
                                try:
                                    driver.switch_to.alert.accept()
                                    time.sleep(delay)
                                except:
                                    pass

                            if(dingyue != 0):
                                ## 预约看房 ##
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='appointment-look yuyue']").click()
                                except:
                                    pass
                                # 输入电话
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='phoneNum']").send_keys(person[0])
                                except:
                                    pass
                                # 输入名字
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='nameInput']").send_keys(person[1])
                                except:
                                    pass
                                # 点击提交
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='entry-submit j_entrySubmit liuzi-dialog-btn']").click()
                                except:
                                    pass
                                # 关闭弹窗
                                time.sleep(delay)
                                try:
                                    driver.switch_to.alert.accept()
                                except:
                                    pass

                                ## 一键订阅 ##
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='dingyue-dongtai li_diff']").click()
                                except:
                                    pass
                                # 输入电话
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='a_input input-phone j_dingyueInput']").send_keys(person[0])
                                except:
                                    pass
                                # 勾选项目
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[yid='1']").click()
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[yid='2']").click()
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[yid='3']").click()
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[yid='5']").click()
                                except:
                                    pass
                                # 点击订阅
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='submit_btn btn-take-dingyue']").click()
                                except:
                                    pass
                                time.sleep(delay)
                                # 关闭弹窗
                                try:
                                    driver.switch_to.alert.accept()
                                    time.sleep(delay)
                                except:
                                    pass

                                ## 余房查询 ##
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='appointment-look ylcx']").click()
                                except:
                                    pass
                                # 输入电话
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='phoneNum']").send_keys(person[0])
                                except:
                                    pass
                                # 点击领取
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='entry-submit j_entrySubmit liuzi-dialog-btn']").click()
                                except:
                                    pass
                                time.sleep(delay)
                                # 关闭弹窗
                                try:
                                    driver.switch_to.alert.accept()
                                    time.sleep(delay)
                                except:
                                    pass

                                ## 预约算价 ##
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='appointment-look yusuan']").click()
                                except:
                                    pass
                                # 输入电话
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='phoneNum']").send_keys(person[0])
                                except:
                                    pass
                                # 点击领取
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='entry-submit j_entrySubmit liuzi-dialog-btn']").click()
                                except:
                                    pass
                                time.sleep(delay)
                                # 关闭弹窗
                                try:
                                    driver.switch_to.alert.accept()
                                    time.sleep(delay)
                                except:
                                    pass
                    except:
                        pass
                except:
                    pass


if __name__ == "__main__":
    main()
