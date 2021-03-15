import chardet
import subprocess
import os

hostname = "google.com"
enc_format = 'utf-8'
sources_list = ['yandex.ru', 'google.com']

# На Маке, как я понял уже информация в строковом типе. Поэтому чуть по другому сделал это задание
for x in sources_list:
    args = ['ping', '-c', '4', x]
    # response = os.system("ping -c 1 " + hostname)
    # sub_ping = subprocess.call(args)
    sub_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    out = str(sub_ping.communicate()[0].decode("utf-8"))
    # print(type(out)) <class 'str'>
    print(f'Bellow statistic for resource: {x}')
    print(out)
    if sub_ping:
        print(f'The service {x} is UP')
        print('End of statistic')
        print('='*50)
    else:
        print(f'The service {x} is DOWN')
        print('End of statistic')
        print('='*50)
