from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# 配置 ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 设置 ChromeDriver 的路径
chromedriver_path = '/home/wood/github/chrome-win64/chrome.exe'  # 替换为你的 chromedriver 路径

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 打开微博登录页面
driver.get("https://weibo.com/login.php")

# 登录微博
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//a[@action-type='btn_submit']")

username.send_keys("your_username")  # 替换为你的微博用户名
password.send_keys("your_password")  # 替换为你的微博密码
login_button.click()

# 等待登录完成（根据需要调整等待时间）
time.sleep(10)

# 搜索关键词 "北京环球影城"
search_box = driver.find_element(By.XPATH, "//input[@node-type='searchInput']")
search_box.send_keys("北京环球影城")
search_box.send_keys(Keys.RETURN)

# 等待搜索结果加载（根据需要调整等待时间）
time.sleep(5)

# 获取搜索结果
tweets = driver.find_elements(By.XPATH, "//div[@class='content']")

# 打印爬取的内容
for tweet in tweets:
    print(tweet.text)

# 关闭浏览器
driver.quit()
