import requests
import os
# 定义一个请求头，防止请求不到数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
# 获取电影列表
def get_movie_list():
    page_limit = 20
    init_start = 0
    movies = []
    # 获取100条数据
    while (init_start < 100):        
        resp = requests.get('https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=' + str(init_start), headers=headers)        
        for movie in resp.json()['subjects']:
            movies.append(movie)
        init_start += page_limit
    return movies
def save_movie_as_img(obj, index):
    img = requests.get(obj['cover'])
    with open(str(index) + '-' + obj['title']+'.jpg', 'wb') as f:
        # 将请求到的内容写入到图片文件
        f.write(img.content)
        f.close()
# 创建文件夹并进入        
def createFile(file_path):
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    os.chdir(file_path)
    
def main():
    # 要保存图片的文件夹
    createFile('doubanMovie')
    for movieObj in  get_movie_list():
        save_movie_as_img(movieObj,get_movie_list().index(movieObj))

if(__name__ == '__main__'):
    main()
