import random
import time
from auth_data import branches
from selenium import webdriver
from dataclasses import dataclass
#import value as value
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

driver = webdriver.Chrome()

total = ['barnaul',
           'https://www.avito.ru/barnaul/tovary_dlya_zhivotnyh/inkubator_lupper_2149378298',
           'https://www.avito.ru/barnaul/tovary_dlya_zhivotnyh/avtomaticheskiy_inkubator_blits-48_1003310751',
           'https://www.avito.ru/barnaul/tovary_dlya_zhivotnyh/inkubatory_blits_deli_vegas_matritsa_1030880701',
           'https://www.avito.ru/barnaul/tovary_dlya_zhivotnyh/inkubator_120_2055802763',
           'https://www.avito.ru/barnaul/tovary_dlya_zhivotnyh/inkubator_lupper_72_yaytsa_2215488796',
           'https://www.avito.ru/barnaul/tovary_dlya_zhivotnyh/inkubator_lupper_72_1927192093',
           'https://www.avito.ru/barnaul/tovary_dlya_zhivotnyh/inkubator_blits_norma_na_72_1098995839',
           'https://www.avito.ru/barnaul/tovary_dlya_zhivotnyh/inkubator_na_98_yaits_220v12v_994803125',
           'https://www.avito.ru/barnaul/tovary_dlya_zhivotnyh/inkubator_blits_norma_na_120_yaits_1362544387',
         'nalchik',
         'https://www.avito.ru/nalchik/tovary_dlya_zhivotnyh/inkubator_blits_norma_72_yaitsa_1258891758',
         'gorno_altaysk',
         'https://www.avito.ru/gorno-altaysk/tovary_dlya_zhivotnyh/prodazha_inkubatorov_2136105921',
         'https://www.avito.ru/gorno-altaysk/tovary_dlya_zhivotnyh/inkubator_parka_2148628047',
         'https://www.avito.ru/gorno-altaysk/tovary_dlya_zhivotnyh/inkubatory_parka_blits_deli_vegas_1391406744',
         'https://www.avito.ru/gorno-altaysk/tovary_dlya_zhivotnyh/avtomaticheskiy_inkubator_blits-48_1120588902',
         'stavropol',
         'https://www.avito.ru/stavropol/tovary_dlya_zhivotnyh/inkubator_lupper_1751125959',
         'https://www.avito.ru/stavropol/tovary_dlya_zhivotnyh/inkubator_lupper_2253585779',
         'https://www.avito.ru/stavropol/tovary_dlya_zhivotnyh/inkubator_blits_norma_lupper_2061303078',
         'https://www.avito.ru/stavropol/tovary_dlya_zhivotnyh/inkubator_dlya_yaits._novyy_2061360447',
         'nijniy_novgorod',
         'https://www.avito.ru/nizhniy_novgorod/tovary_dlya_zhivotnyh/avtomaticheskiy_inkubator_dlya_yaits_matritsa_deli_1226451234',
         'https://www.avito.ru/nizhniy_novgorod/tovary_dlya_zhivotnyh/inkubatory_vegas_parka_1326586665',
         'perm',
         'https://www.avito.ru/perm/tovary_dlya_zhivotnyh/inkubatory_blits_1856792970',
         'https://www.avito.ru/perm/tovary_dlya_zhivotnyh/inkubatory_blits_matritsa_deli_vegas_i_dr_1855962243',
         'https://www.avito.ru/perm/tovary_dlya_zhivotnyh/avtomaticheskiy_inkubator_blits-48_938743453',
         'https://www.avito.ru/perm/tovary_dlya_zhivotnyh/inkubator_avtomaticheskiy_blits-norma_1024072261',
         'https://www.avito.ru/perm/tovary_dlya_zhivotnyh/inkubator_avtomaticheskiy_blits-norma_1024072261',
         'https://www.avito.ru/user/db0b7881ed0e1e5377203282fc9b8306/profile?id=1210368366&src=item&page_from=from_item_card&iid=1210368366',
         'https://www.avito.ru/perm/tovary_dlya_zhivotnyh/avtomaticheskie_inkubatory_blits_48ts_i_dr._modeli_1157565673',
         'sankt_peterburg',
         'https://www.avito.ru/sankt-peterburg/tovary_dlya_zhivotnyh/inkubatory_2093415741',
         'https://www.avito.ru/sankt-peterburg/tovary_dlya_zhivotnyh/inkubator_2125347505',
         'https://www.avito.ru/sankt-peterburg/tovary_dlya_zhivotnyh/inkubator_matritsa_deli_1896019425',
         'https://www.avito.ru/sankt-peterburg/tovary_dlya_zhivotnyh/inkubator_vegas_2248811379',
         'https://www.avito.ru/sankt-peterburg/tovary_dlya_zhivotnyh/inkubator_blits_norma_1896833382',
         'https://www.avito.ru/sankt-peterburg/tovary_dlya_zhivotnyh/inkubator_norma_lupper_72_1896279840',
         'omsk',
         'https://www.avito.ru/omsk/tovary_dlya_zhivotnyh/inkubator_norma_parka_120_s10_1310986257',
         'https://www.avito.ru/omsk/tovary_dlya_zhivotnyh/inkubator_blits_norma_avtomatmatritsa_deli_1178110215',
         'https://www.avito.ru/omsk/tovary_dlya_zhivotnyh/avtomaticheskiy_inkubator_blits_48_ts_1064277326',
         'rostov',
         'https://www.avito.ru/bataysk/tovary_dlya_zhivotnyh/inkubatory_matritsa_vegas_2082761447']


def search_ads():
    temp, city, count_of_ads = 0, 0, 0
    unact_ads, ads = set(), set()

    amount_of_passage = len(total)

    for i in total:
        amount_of_passage = amount_of_passage - 1
        if 'https' in i:
            driver.get(i)
            #<div class="title-info-main"> <h1 class="title-info-title">  <span class="title-info-title-text" itemprop="name">Инкубатор Луппер</span> </h1> </div>
            #< div class ="title-info-metadata-item-redesign" > 19 ноября в 06: 00 < / div >

            try:
                name_of_ads = driver.find_element(By.CSS_SELECTOR, "h1").text
                date = driver.find_element(By.CLASS_NAME, "title-info-metadata-item-redesign").text
                count_of_ads = count_of_ads + 1
                name_of_ads = name_of_ads + date
                ads.add(name_of_ads)



            except Exception as ex:
                unact_ads.add(name_of_ads)
                pass

            time.sleep(random.uniform(2.5, 5.7))
            driver.switch_to.new_window('tab')

        else:
            if temp == 1 and city != i:
                print(f'{amount_of_passage} {city} {count_of_ads} {ads}' )
                print(f'unactvivite ads: {unact_ads}')
                count_of_ads = 0

            city = i
            temp = 1
            ads = set()
            unact_ads = set()



search_ads()

# import pygame
# pygame.init()
# song = pygame.mixer.Sound('file.mp3')
# clock = pygame.time.Clock()
# song.play()
# while True:
#     clock.tick(60)
# pygame.quit()

for i in stest:
    print(8)