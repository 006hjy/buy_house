#from fake_useragent import UserAgent
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
    # 当前版本仅支持订阅一个手机号码
    _list = [
        ['18888888888', '张三']
    ]
    _run(_list)


def _run(_list):
    delay = 0
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

    citys = ["jn", "qingdao", "yantai", "dongying", "weihai", "zibo", "weifang", "liaocheng", "heze", "rizhao", "linyi",
             "dezhou", "jining", "zaozhuang", "binzhou", "taian", "laiwu", "laiyang", "xintai", "hf", "liuan", "anqing",
             "xuancheng", "ahsuzhou", "chaohu", "chizhou", "huainan", "chuzhou", "wuhu", "bengbu", "tongling", "fuyang",
             "maanshan", "huangshan", "huaibei", "bozhou", "dangtu", "huoqiu", "sh", "hz", "ningbo", "shaoxing", "taizhou",
             "jinhua", "wenzhou", "jiaxing", "lishui", "huzhou", "zhoushan", "quzhou", "nj", "suzhou", "wuxi", "xuzhou",
             "changzhou", "nantong", "huaian", "changshu", "kunshan", "yx", "yangzhou", "jiangyin", "tz", "zhenjiang", "suqian",
             "lyg", "taicang", "yancheng", "zhangjiagang", "liyang", "donghai", "baoying", "rugao", "yizheng", "haian", "haimen",
             "gaoyou", "qidong", "rudong", "xinghua", "jingjiang", "taixing", "nc", "ganzhou", "shangrao", "jxfc", "jiujiang",
             "jingan", "yichun", "xinyu", "ruijin", "jian", "pingxiang", "jingdezhen", "fuzhou", "yingtan", "ys", "quanzhou",
             "fz", "xiamen", "zhangzhou", "putian", "longyan", "nanping", "sanming", "ningde", "gz", "sz", "foshan", "zhongshan",
             "dongguan", "zhuhai", "shantou", "zhaoqing", "jiangmen", "huizhou", "jieyang", "meizhou", "heyuan", "qingyuan",
             "zhanjiang", "yangjiang", "shaoguan", "maoming", "yunfu", "chaozhou", "shanwei", "puning", "sanya", "hn", "hk",
             "guilin", "nn", "liuzhou", "beihai", "qinzhou", "laibin", "yulin", "fangchenggang", "guigang", "wuzhou", "chongzuo",
             "hechi", "baise", "hezhou", "hengxian", "by", "wh", "yichang", "huangshi", "jingzhou", "lhk", "yicheng", "zaoyang",
             "shiyan", "xianning", "xiaogan", "jingmen", "xiangyang", "huanggang", "ezhou", "suizhou", "xiantao", "tianmen",
             "qianjiang", "enshi", "shennongjia", "zz", "luoyang", "jiaozuo", "xinyang", "nanyang", "shangqiu", "anyang",
             "pingdingshan", "ruzhou", "xinxiang", "wugang", "zhumadian", "kaifeng", "xuchang", "luohe", "hebi", "sanmenxia",
             "zhoukou", "puyang", "yuzhou", "yongcheng", "changge", "yanling", "cs", "xiangtan", "zhuzhou", "changde", "chenzhou",
             "hengyang", "huaihua", "loudi", "yiyang", "yongzhou", "yueyang", "zjj", "shaoyang", "xiangxi", "changshada", "heb",
             "hailin", "daqing", "zhaoyuan", "zhaozhou", "mudanjiang", "qiqihaer", "suihua", "jixi", "jiamusi", "heihe",
             "hljyichun", "zhaodong", "anda", "shuangyashan", "hegang", "qitaihe", "sy", "dl", "anshan", "panjin", "yingkou",
             "huludao", "wafangdian", "zhuanghe", "jinzhou", "dandong", "chaoyang", "benxi", "liaoyang", "fushun", "fuxin",
             "tieling", "cc", "jl", "huadian", "yanbian", "siping", "baishan", "baicheng", "songyuan", "dehui", "tonghua", "nongan",
             "liaoyuan", "jlys", "gongzhuling", "gy", "zunyi", "bijie", "qianxinan", "qiandongnan", "qiannan", "tongren", "anshun",
             "lps", "cd", "mianyang", "leshan", "nanchong", "meishan", "yibin", "bazhong", "guangyuan", "luzhou", "guanghan",
             "renshou", "deyang", "neijiang", "anyue", "suining", "guangan", "dazhou", "ziyang", "panzhihua", "zigong", "yaan",
             "liangshan", "ganzi", "abazhou", "cq", "hechuan", "km", "dali", "qujing", "yuxi", "xishuangbanna", "lijiang",
             "baoshan", "dehong", "zhaotong", "wenshan", "chuxiong", "honghe", "puer", "lincang", "diqing", "lasa", "rkz",
             "changdu", "linzhi", "ty", "yuncheng", "huairen", "linfen", "datong", "jinzhong", "changzhi", "yangquan", "lvliang",
             "shuozhou", "jc", "xinzhou", "hhht", "eerduosi", "baotou", "wlcb", "byne", "chifeng", "xam", "wuhai", "tl", "hlbe",
             "xlglm", "alsm", "sjz", "tangshan", "baoding", "qinhuangdao", "handan", "zhangjiakou", "hengshui", "xingtai",
             "langfang", "chengde", "sanhe", "yuxian", "cangzhou", "wenan", "yanjiao", "dachang", "zhuozhou", "guan", "xianghe",
             "yongqing", "hbbz", "dingzhou", "gaobeidian", "changli", "xiongan", "bj", "tj", "wuqing", "wlmq", "bazhou", "yili",
             "kashi", "akesu", "changji", "kzls", "hami", "klmy", "bedl", "ht", "shz", "tlf", "wjq", "qt", "kel", "alt", "tc", "lz",
             "gannan", "tianshui", "qingyang", "dingxi", "pingliang", "zhangye", "jiuquan", "wuwei", "longnan", "yongdeng",
             "baiyin", "yuzhong", "jinchang", "jiayuguan", "xn", "haidong", "guoluo", "haibei", "haixi", "yushu", "huangnan", "yc",
             "guyuan", "wuzhong", "zhongwei", "shizuishan", "xa", "xianyang", "baoji", "weinan", "hanzhong", "ankang", "tongchuan",
             "shangluo", "yl", "yanan"]
    #citys = ['xm']

    # 遍历城市列表
    for city in citys:
        # 打开page页
        for page in range(start_page, end_page+1):
            href = "http://"+city + \
                ".jiwu.com/loupan/list-page"+str(page)+".html"
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
            urls = driver.find_elements(
                By.XPATH, "//div[@class='box new_house']/div[@class='img']/a")
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
                    # 删除遮挡元素
                    try:
                        js = "document.getElementsByClassName('dialing-box')[0].remove();"
                        driver.execute_script(js)
                    except:
                        pass
                    # 操作
                    try:
                        for person in _list:
                            if(duanxin != 0):
                                ## 发送地址给手机 ##
                                try:
                                    driver.find_element(
                                        By.LINK_TEXT, "[发地址到手机]").click()
                                except:
                                    pass

                                # 输入电话
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[type='tel']").send_keys(person[0])
                                except:
                                    pass
                                # 点击领取
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='btn btn-green ok']").click()
                                except:
                                    pass
                                # 关闭窗口
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='close-pop']").click()
                                except:
                                    pass
                                time.sleep(delay)

                            if(dingyue != 0):
                                ## 降价通知 ##
                                try:
                                    driver.find_element(
                                        By.LINK_TEXT, "降价通知我").click()
                                except:
                                    pass
                                # 输入电话
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[type='tel']").send_keys(person[0])
                                except:
                                    pass

                                # 点击提交
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='btn btn-green ok']").click()
                                except:
                                    pass
                                # 关闭窗口
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='close-pop']").click()
                                except:
                                    pass
                                time.sleep(delay)

                                ## 组团砍价 ##
                                try:
                                    driver.find_element(
                                        By.LINK_TEXT, "立即报名").click()
                                except:
                                    pass
                                # 输入电话
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[type='tel']").send_keys(person[0])
                                except:
                                    pass

                                # 点击提交
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='btn btn-green ok']").click()
                                except:
                                    pass
                                # 关闭窗口
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='close-pop']").click()
                                except:
                                    pass
                                time.sleep(delay)

                                ## 新信息通知 ##
                                try:
                                    driver.find_element(
                                        By.LINK_TEXT, "新信息通知").click()
                                except:
                                    pass
                                # 输入电话
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[type='tel']").send_keys(person[0])
                                except:
                                    pass

                                # 点击提交
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='btn btn-green ok']").click()
                                except:
                                    pass
                                # 关闭窗口
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='close-pop']").click()
                                except:
                                    pass
                                time.sleep(delay)

                                ## 开盘通知我 ##
                                try:
                                    driver.find_element(
                                        By.LINK_TEXT, "[开盘通知我]").click()
                                except:
                                    pass

                                # 输入电话
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[type='tel']").send_keys(person[0])
                                except:
                                    pass
                                # 点击领取
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='btn btn-green ok']").click()
                                except:
                                    pass
                                # 关闭窗口
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='close-pop']").click()
                                except:
                                    pass
                                time.sleep(delay)

                                ## 新动态通知我 ##
                                try:
                                    driver.find_element(
                                        By.LINK_TEXT, "新动态通知我").click()
                                except:
                                    pass
                                # 输入电话
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[type='tel']").send_keys(person[0])
                                except:
                                    pass

                                # 点击提交
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='btn btn-green ok']").click()
                                except:
                                    pass
                                # 关闭窗口
                                try:
                                    driver.find_element(
                                        By.CSS_SELECTOR, "[class='close-pop']").click()
                                except:
                                    pass
                    except:
                        pass
                except:
                    pass


if __name__ == "__main__":
    main()
