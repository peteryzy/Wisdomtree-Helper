from selenium import webdriver
import os
import requests
import time
from lxml import etree
import shutil

def makedirs(dirs,file):#复制driver
	if os.path.exists(dirs):
		print("文件已存在")
		pass
	else:
		os.makedirs(dirs)
		shutil.copy(file, dirs)

def login(url,browser,username,password):
	browser.get(url)
	browser.find_element_by_id("lUsername").send_keys(username)#账号
	browser.find_element_by_id("lPassword").send_keys(password)#密码
	browser.find_element_by_xpath("/html/body/div[2]/div/form/div/span").click()#确认
	time.sleep(10)
	browser.find_element_by_xpath('//*[@id="course_recruit_studying_ul"]/li[1]/div[2]/div[2]/a').click()#继续学习
	#browser.close()
	handles = browser.window_handles
	browser.switch_to.window(handles[1])
	time.sleep(20)
	#Html = requests.get(browser.current_url)
	#print(Html.text)
	#print(browser.current_url)
	#print(browser.page_source)



def play_video(browser):
		html_trans=etree.HTML(browser.page_source)
		now_time = html_trans.xpath("/html/body/div[3]/div[5]/div/div[3]/div/div/div[10]/div[4]/span[1]/text()")
		end_time = html_trans.xpath("/html/body/div[3]/div[5]/div/div[3]/div/div/div[10]/div[4]/span[2]/text()")
		now_time_int = int(now_time[0][3:5]) * 60 + int(end_time[0][6:8])
		end_time_int = int(end_time[0][3:5]) * 60 + int(end_time[0][6:8])
		print("现在是:%ss" % now_time_int)
		print("结束时间是:%ds" % end_time_int)
		print("还有%ds结束" % (end_time_int-now_time_int))
		sleep = end_time_int-now_time_int
		if sleep == 0:
			browser.find_element_by_xpath("/html/body/div[3]/div[5]/div/div[5]/div/a").click()#切换下一页
		else:
			time.sleep(end_time_int - now_time_int)

if __name__ == "__main__":
	username = input("用户名:")
	password = input("密码:")
	os.system("cls")
	dirs = "D://Anaconda3"
	file = "geckodriver.exe"
	makedirs(dirs,file)
	url = "https://passport.zhihuishu.com/login?service=http://online.zhihuishu.com/onlineSchool/"
	browser = webdriver.Firefox()
	login(url,browser,username,password)
	while True:
		time.sleep(5)
		play_video(browser)