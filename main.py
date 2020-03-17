import telebot
import os
from bs4 import BeautifulSoup
import requests

token = os.environ.get('TOKEN', )
bot = telebot.TeleBot(token)


def conjugation(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    content = response.text
    soup = BeautifulSoup(content, "lxml")
    yo = []
    tu = []
    el = []
    nosotros = []
    vosotros = []
    ellos = []
    all_blocks = soup.findAll('table', {'class': 'blok'})
    try:
        for i in range(0, len(all_blocks)):
            all_part = all_blocks[i].findAll('td')
            if i != 18 and i != 19:
                yo.append(all_part[1].text)
                tu.append(all_part[3].text)
                el.append(all_part[5].text)
                nosotros.append(all_part[7].text)
                vosotros.append(all_part[9].text)
                ellos.append(all_part[11].text)
            elif i == 18:
                tu.append(all_part[1].text)
                el.append(all_part[3].text)
                nosotros.append(all_part[5].text)
                vosotros.append(all_part[7].text)
                ellos.append(all_part[9].text)
            elif i == 19:
                tu.append(all_part[0].text)
                el.append(all_part[1].text)
                nosotros.append(all_part[2].text)
                vosotros.append(all_part[3].text)
                ellos.append(all_part[4].text)
        result_list = []
        result = ''
        result1 = ''
        result2 = ''
        result3 = ''
        result += '*Indicativo*\n'
        result += 'Presente:\n' + 'yo - ' + yo[0] + '\n' + 'tú - ' + tu[0] + '\n' + 'él - ' + el[0] + '\n' + 'nosotros - ' + \
                  nosotros[0] + '\n' + 'vosotros - ' + vosotros[0] + '\n' + 'ellos - ' + ellos[0] + '\n'
        result += 'Pretérito perfecto compuesto:\n' + 'yo - ' + yo[1] + '\n' + 'tú - ' + tu[1] + '\n' + 'él - ' + el[
            1] + '\n' + 'nosotros - ' + \
                  nosotros[1] + '\n' + 'vosotros - ' + vosotros[1] + '\n' + 'ellos - ' + ellos[1] + '\n'
        result += 'Pretérito imperfecto:\n' + 'yo - ' + yo[2] + '\n' + 'tú - ' + tu[2] + '\n' + 'él - ' + el[
            2] + '\n' + 'nosotros - ' + \
                  nosotros[2] + '\n' + 'vosotros - ' + vosotros[2] + '\n' + 'ellos - ' + ellos[2] + '\n'
        result += 'Pretérito pluscuamperfecto:\n' + 'yo - ' + yo[3] + '\n' + 'tú - ' + tu[3] + '\n' + 'él - ' + el[
            3] + '\n' + 'nosotros - ' + \
                  nosotros[3] + '\n' + 'vosotros - ' + vosotros[3] + '\n' + 'ellos - ' + ellos[3] + '\n'
        result += 'Pretérito perfecto simple:\n' + 'yo - ' + yo[4] + '\n' + 'tú - ' + tu[4] + '\n' + 'él - ' + el[
            4] + '\n' + 'nosotros - ' + \
                  nosotros[4] + '\n' + 'vosotros - ' + vosotros[4] + '\n' + 'ellos - ' + ellos[4] + '\n'
        result += 'Pretérito anterior:\n' + 'yo - ' + yo[5] + '\n' + 'tú - ' + tu[5] + '\n' + 'él - ' + el[
            5] + '\n' + 'nosotros - ' + \
                  nosotros[5] + '\n' + 'vosotros - ' + vosotros[5] + '\n' + 'ellos - ' + ellos[5] + '\n'
        result += 'Futuro:\n' + 'yo - ' + yo[6] + '\n' + 'tú - ' + tu[6] + '\n' + 'él - ' + el[
            6] + '\n' + 'nosotros - ' + \
                  nosotros[6] + '\n' + 'vosotros - ' + vosotros[6] + '\n' + 'ellos - ' + ellos[6] + '\n'
        result += 'Futuro perfecto:\n' + 'yo - ' + yo[7] + '\n' + 'tú - ' + tu[7] + '\n' + 'él - ' + el[
            7] + '\n' + 'nosotros - ' + \
                  nosotros[7] + '\n' + 'vosotros - ' + vosotros[7] + '\n' + 'ellos - ' + ellos[7] + '\n'
        result_list.append(result)
        result += '*Subjuntivo*\n'
        result1 += 'Presente:\n' + 'yo - ' + yo[8] + '\n' + 'tú - ' + tu[8] + '\n' + 'él - ' + el[8] + '\n' + 'nosotros - ' + \
                  nosotros[8] + '\n' + 'vosotros - ' + vosotros[8] + '\n' + 'ellos - ' + ellos[8] + '\n'
        result1 += 'Pretérito perfecto:\n' + 'yo - ' + yo[9] + '\n' + 'tú - ' + tu[9] + '\n' + 'él - ' + el[
            9] + '\n' + 'nosotros - ' + \
                  nosotros[9] + '\n' + 'vosotros - ' + vosotros[9] + '\n' + 'ellos - ' + ellos[9] + '\n'
        result1 += 'Pretérito imperfecto:\n' + 'yo - ' + yo[10] + '\n' + 'tú - ' + tu[10] + '\n' + 'él - ' + el[
            10] + '\n' + 'nosotros - ' + \
                  nosotros[10] + '\n' + 'vosotros - ' + vosotros[10] + '\n' + 'ellos - ' + ellos[10] + '\n'
        result1 += 'Pretérito pluscuamperfecto:\n' + 'yo - ' + yo[11] + '\n' + 'tú - ' + tu[11] + '\n' + 'él - ' + el[
            11] + '\n' + 'nosotros - ' + \
                  nosotros[11] + '\n' + 'vosotros - ' + vosotros[11] + '\n' + 'ellos - ' + ellos[11] + '\n'
        result1 += 'Pretérito imperfecto 2:\n' + 'yo - ' + yo[12] + '\n' + 'tú - ' + tu[12] + '\n' + 'él - ' + el[
            12] + '\n' + 'nosotros - ' + \
                  nosotros[12] + '\n' + 'vosotros - ' + vosotros[12] + '\n' + 'ellos - ' + ellos[12] + '\n'
        result1 += 'Pretérito pluscuamperfecto 2:\n' + 'yo - ' + yo[13] + '\n' + 'tú - ' + tu[13] + '\n' + 'él - ' + el[
            13] + '\n' + 'nosotros - ' + \
                  nosotros[13] + '\n' + 'vosotros - ' + vosotros[13] + '\n' + 'ellos - ' + ellos[13] + '\n'
        result1 += 'Futuro:\n' + 'yo - ' + yo[14] + '\n' + 'tú - ' + tu[14] + '\n' + 'él - ' + el[
            14] + '\n' + 'nosotros - ' + \
                  nosotros[14] + '\n' + 'vosotros - ' + vosotros[14] + '\n' + 'ellos - ' + ellos[14] + '\n'
        result1 += 'Futuro perfecto:\n' + 'yo - ' + yo[15] + '\n' + 'tú - ' + tu[15] + '\n' + 'él - ' + el[
            15] + '\n' + 'nosotros - ' + \
                  nosotros[15] + '\n' + 'vosotros - ' + vosotros[15] + '\n' + 'ellos - ' + ellos[15] + '\n'
        result_list.append(result1)
        result2 += '*Condicional*\n'
        result2 += 'Condicional:\n' + 'yo - ' + yo[16] + '\n' + 'tú - ' + tu[16] + '\n' + 'él - ' + el[16] + '\n' + 'nosotros - ' + \
                  nosotros[16] + '\n' + 'vosotros - ' + vosotros[16] + '\n' + 'ellos - ' + ellos[16] + '\n'
        result2 += 'Condicional compuesto:\n' + 'yo - ' + yo[17] + '\n' + 'tú - ' + tu[17] + '\n' + 'él - ' + el[
            17] + '\n' + 'nosotros - ' + \
                  nosotros[17] + '\n' + 'vosotros - ' + vosotros[17] + '\n' + 'ellos - ' + ellos[17] + '\n'
        result_list.append(result2)
        result3 += 'Imperativo\n'
        result3 += 'Afirmativo:\n' + 'tú - ' + tu[18] + '\n' + 'él - ' + el[18] + '\n' + 'nosotros - ' + \
                  nosotros[18] + '\n' + 'vosotros - ' + vosotros[18] + '\n' + 'ellos - ' + ellos[18] + '\n'
        result3 += 'Negativo:\n' + 'tú - ' + tu[19] + '\n' + 'él - ' + el[19] + '\n' + 'nosotros - ' + \
                  nosotros[19] + '\n' + 'vosotros - ' + vosotros[19] + '\n' + 'ellos - ' + ellos[19] + '\n'
        result_list.append(result3)
        return result_list
    except:
        return 'Данные введены некоректно'

@bot.message_handler(commands=['start'])
def help_com(message):
    bot.send_message(message.from_user.id, "Введите глагол")

@bot.message_handler(content_types=['text'])
def key_answ(message):
    url = 'https://entre-amigos.ru/components-loco/conjugator/getuser.php?q='+ message.text
    if len(conjugation(url)) != 4:
        bot.send_message(message.from_user.id, conjugation(url))
    else:
        for i in range(0,4):
            bot.send_message(message.from_user.id, conjugation(url)[i])




bot.polling(none_stop=True)
