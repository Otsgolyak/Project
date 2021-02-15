import requests
from faker import Faker

def leadogenerator(url, login, password, sum, order):

    fake = Faker('ru_RU')
    res = requests.get('https://{}/auth/generate_token?login={}&password={}'.format(url, login, password))
    print(res.text)
    token = res.text.split(':')[1][1:-2]
    with open('leadgen_log.txt', 'a', encoding='UTF-8') as file:
        file.write('\n' + "Заявка №" + order + '\n')
    for i in range(int(sum)):
        data = {
            'name': fake.name(),
            'phone': str(fake.country_calling_code())+str(fake.pyint(min_value=999999999, max_value=9999999999, step=1)),
            'email': fake.email(),
            'leadorder_id': order
        }

        r = requests.post('https://{}/crm/create_lead?token={}'.format(url, token), data=data)
        print(r.text, data)
        with open('leadgen_log.txt', 'a', encoding='UTF-8') as file:
            file.write(r.text)
            file.write(str(data) + '\n')
    print('Респонсы записаны в файл leadgen_log.txt')


