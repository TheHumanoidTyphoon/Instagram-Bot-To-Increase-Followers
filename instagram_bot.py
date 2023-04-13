from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from random import randint
from time import sleep, strftime
import pandas as pd
import sys
import glob


options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

path = Service("D:/Program Files/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(options=options, service=path)
sleep(2)

website = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
driver.get(website)
sleep(5)

insta_cookies = driver.find_element(
    By.XPATH, "/html/body/div[4]/div/div/button[1]")
insta_cookies.click()
sleep(4)

username = driver.find_element(
    By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
username.send_keys("USERNAME")
sleep(1)

password = driver.find_element(
    By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")
password.send_keys("PASSWORD")

login_button = driver.find_element(
    By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button")
login_button.click()
sleep(8)

# line that disable the pop up asking about notifications
info_button = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button")
info_button.click()
sleep(4)


alert_button = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
alert_button.click()

hashtag_list = ["hashtag1", "hashtag2", "hashtag3"]

timecode = strftime("%d/%m/%Y_%Hh%Mm%Ss")

path_name = "D:/Python - Projects\Python - Automated Projects/Instagram Automations/Instagram Bot To Increase Followers/*.csv"
csv_files = glob.glob(path_name)
last_file = csv_files[-1]
list_count = int(last_file[-6:-4])

user_list = []

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0


def next_arrow():
    driver.find_element(By.XPATH, "/html").send_keys(Keys.ARROW_RIGHT)


for hashtag in hashtag_list:
    tag += 1
    driver.get(f"https://www.instagram.com/explore/tags/{hashtag_list[tag]}/")
    sleep(20)
    first_thumbnail = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div/div[1]/div[1]/a/div/div[2]")
    first_thumbnail.click()
    sleep(randint(2, 4))

    try:
        for x in range(1, 100):
            username = driver.find_element(By.XPATH(
                "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/div/span/a")).text

            try:
                follow_button = driver.find_element(
                    By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button")

                follow_button.click()
                new_followed.append(username)
                followed += 1

                # liking the picture
                like_button = driver.find_element(By.XPATH(
                    "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"))

                like_button.click()
                likes += 1

                sleep(randint(10, 20))

                # comments and tracker
                comm_prob = randint(1, 10)

                if comm_prob >= 5:
                    comment_check = True
                    comment_button = driver.find_element(
                        By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button")
                    comment_button.click()

                    comment_box = driver.find_element(
                        By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")

                    if comm_prob == 5:
                        comment_box.send_keys("Awesome!")
                        sleep(1)
                    if comm_prob == 6:
                        comment_box.send_keys("Nice!")
                        sleep(1)
                    elif comm_prob == 7:
                        comment_box.send_keys("Cool!")
                        sleep(1)
                    elif comm_prob == 8:
                        comment_box.send_keys("Great!")
                        sleep(1)
                    elif comm_prob == 9:
                        comment_box.send_keys("Super!")
                        sleep(1)
                    elif comm_prob == 10:
                        comment_box.send_keys("Fantastic!")
                        sleep(1)
                    # enter to post comment
                    comment_box.send_keys(Keys.ENTER)
                    comments += 1
                    sleep(randint(5, 10))
                else:
                    comment_check = False

                if comment_check:
                    comment_proof = "| commented"
                else:
                    comment_proof = ""

                print(
                    f"{x} | #{hashtag} | user: {username} | {strftime('%Hh%Mm%Ss')} {comment_proof}")

                next_arrow()
                sleep(randint(5, 15))

            except Exception:
                next_arrow()
                sleep(randint(10, 15))
                continue

     # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except Exception as e1:
        print(
            f"""> activated exception 2 in line: {sys.exc_info()[-1].tb_lineno} | {e1}""")
        next_arrow()
        sleep(randint(5, 10))
        continue


user_list.extend(new_followed)
list_count += 1
users_updated = pd.DataFrame(user_list)
users_updated.to_csv(f"users-followed-list_0{list_count}.csv")

print(f"""
Liked {likes} posts.
Commented on {comments} posts.
Followed {followed} new profiles.
""")


