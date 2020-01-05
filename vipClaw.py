from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
import time
import os

driver = webdriver.Chrome()
driver.implicitly_wait(10)

# 保存路径
save_path = 'C:/Users/Administrator/Desktop/jianguo'



# 创建文件夹
def createFile(file_path):
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    # 切换路径至上面创建的文件夹
    os.chdir(file_path)

# 创建对应的文件夹
createFile(save_path)
# 抓取三支松鼠产品

index = 1  
def index_page():
    """
    抓取索引页
    """
    print('正在爬取数据')
    url ='https://category.vip.com/suggest.php?keyword=%E4%B8%89%E5%8F%AA%E6%9D%BE%E9%BC%A0&page=1'
    driver.get(url)
    get_products()

def get_products():
    global index# 使用全局变量
    """
    提取商品信息
    """
    js = '''
    var windowHeight = window.innerHeight;//  窗口高度
    var scrollTopPercent = 1
    timer = setInterval(function(){
        var pageHeight = document.body.scrollHeight; // 页面总高度
        var scrollHeight = pageHeight - windowHeight       
        if(scrollTopPercent === 100){
            clearInterval(timer)
        }else{
            scrollTopPercent += 1
        } 
        window.scrollTo({
            top: scrollHeight * scrollTopPercent / 100
        });
    }, 20)
    '''
    # 执行js脚本，滚动到页面底部（用时两秒20 * 100）
    driver.execute_script(js)
    # 二点五秒延迟后，继续爬取数据的操作
    time.sleep(2.5)
    html = driver.page_source
    doc = pq(html)
    items = doc('#J_searchCatList .goods-list-item').items()
    for item in items:
        inser_data = {
            'image': item.find('.goods-image-link>img').attr('data-original'),
            'price':item.find('.goods-price-info .price').text() if item.find('.goods-special-price').hasClass('hidden') else item.find('.goods-special-price .title').text(),
            'title':item.find('.goods-info .J_title_link').text()
        }
        with open('坚果.txt', 'a') as fp:
            print('写入中:', index)
            index+=1
            fp.write(str(inser_data) + '\n')
            fp.close()
    # 爬完当前页，获取下一页的链接，跳转后继续爬，如果没有获取到说明最后一页了，结束爬取
    try:
        driver.get('http:' + doc('.cat-paging-next.next').attr('href'))
        get_products()
    except:
        print('爬取完成')      
index_page()
