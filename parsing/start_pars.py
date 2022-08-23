import aiohttp
from bs4 import BeautifulSoup

from database.sqlite_db import Database
import config as cfg
from create_kwork import bot




url = 'https://kwork.ru/projects?c=41&attr=3587'

async def get_data(url_, page, tgid):
    db = Database(cfg.path_to_db)

    _url = f'{url_}&page={page}'
    async with aiohttp.ClientSession() as session:
        response = await session.get(_url)
        soup = BeautifulSoup(await response.text(), 'lxml')
        data = soup.find_all('div', class_='wants-card__header-title first-letter breakwords pr250')

        kwork_names = []
        for ii in await db.get_kwork_names():
            kwork_names.append(ii[0])

        for i in data:
            link = i.find('a').get('href')
            name = i.find('a').text

            if name not in kwork_names:
                mes_text = '<b>Уведомление 🔔</b>' \
                           f'<a href="{link}">Появился новый заказ!</a>\n' \

                await bot.send_message(tgid, mes_text, parse_mode='HTML')
                await db.add_kwork(name)



async def get_page(tgid):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        soup = BeautifulSoup(await response.text(), 'lxml')
        count_page = soup.find('div', class_='paging').find_all('a')[-2].text


    for page in range(1, int(count_page) + 1):
        await get_data(url, page, tgid)



async def start_pars(tgid):
    db = Database(cfg.path_to_db)
    status = db.get_status_user(tgid)
    if status[0] == 'active':
        await get_page(tgid)
    else:
        print('Парсинг невозможен')













