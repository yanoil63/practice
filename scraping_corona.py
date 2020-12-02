#コロナのデータ取得
import selenium
from selenium import webdriver
from selenium.webdriver import Chrome,ChromeOptions
import time
import pandas as pd
import datetime


def getData():
    options=webdriver.ChromeOptions()
    #options.add_argument("--headless")
    driver=webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe",options=options)


    baseUrl="https://austin.maps.arcgis.com/apps/opsdashboard/index.html#/39e4f8d4acb0433baae6d15a931fa984"

    #driver起動
    driver.get(baseUrl)
    #起動時間を保持(このサイトは特に起動が遅いので長めにとってます)
    time.sleep(15)


    #データを保持するための空リスト作成
    data_list=[]

    #日付を取得
    d_today = datetime.date.today()
    data_list.append(d_today)



    #それぞれのデータの取得(htmlから取り出し)
    #class名からの取得

    # pra=driver.find_elements_by_class_name("responsive-text-label")
    # for i in range(len(pra)):
    #     print(pra[i].text)

    cases=driver.find_elements_by_class_name("responsive-text-label")[0].text
    #リストに格納
    data_list.append(cases)
 
    #print("cases: " +cases)

    death_num=driver.find_elements_by_class_name("responsive-text-label")[3].text

    data_list.append(death_num)

    #print("death_num: "+death_num)

    estimated_num=driver.find_elements_by_class_name("responsive-text-label")[1].text

    data_list.append(estimated_num)

    #print("estimated_num: "+estimated_num)
 
    hosp_num=driver.find_elements_by_class_name("responsive-text-label")[16].text

    data_list.append(hosp_num)

    #print("hos_num: "+hosp_num)

    active_num=driver.find_elements_by_class_name("responsive-text-label")[2].text

    data_list.append(active_num)

    #print("active_num: "+active_num)

    icu=driver.find_elements_by_class_name("responsive-text-label")[17].text

    data_list.append(icu)

    #print("ICU: "+icu)

    venti=driver.find_elements_by_class_name("responsive-text-label")[18].text

    data_list.append(venti)

    #print("Ventilators: "+venti)


    baseUrl_2="https://austin.maps.arcgis.com/apps/opsdashboard/index.html#/0ad7fa50ba504e73be9945ec2a7841cb"

    #driver起動
    driver.get(baseUrl_2)
    #起動時間を保持(このサイトは特に起動が遅いので長めにとってます)
    time.sleep(15)

    #それぞれのデータの取得(htmlから取り出し)
    #class名からの取得

    # pra=driver.find_elements_by_class_name("responsive-text-label")
    # for i in range(len(pra)):
    #     print(pra[i].text)

    new_admission=driver.find_elements_by_class_name("responsive-text-label")[1].text
 
    data_list.append(new_admission)
 
    #print("New_admission: " +new_admission)

    return data_list



def StoreToCsv():
    data_list=getData()
    df = pd.DataFrame([
            data_list],
            columns=["DATE","CASES","Deaths","Active","Hospitalized","Active","ICU","Ventilator","New_admission"]
        )

    #csvファイルとして出力
    

    #一回目はこちらを使ってください
    #df.to_csv("austin_corona.csv", mode="a",index=False)

    #データの表示
    #df.head(3)

    #2回目以降はこちらをご利用ください。(header=False)
    df.to_csv("austin_corona.csv", mode="a", index=False, header=False)


if __name__ == "__main__":
    StoreToCsv()



