import chardet
import subprocess

# args = ['ping', 'yandex.ru']
#
# sub_ping = subprocess.Popen(args, stdout=subprocess.PIPE )
#
# for line in sub_ping.stdout:
#     print(line)
"""
b'PING yandex.ru (5.255.255.88): 56 data bytes\n'
b'64 bytes from 5.255.255.88: icmp_seq=0 ttl=244 time=42.234 ms\n'
b'64 bytes from 5.255.255.88: icmp_seq=1 ttl=244 time=48.236 ms\n'
b'64 bytes from 5.255.255.88: icmp_seq=2 ttl=244 time=48.403 ms\n'
b'64 bytes from 5.255.255.88: icmp_seq=3 ttl=244 time=49.436 ms\n'
"""
# =====================================================================================================================
args = ['ping', 'yandex.ru']

sub_ping = subprocess.Popen(args, stdout=subprocess.PIPE )

for line in sub_ping.stdout:
    result = chardet.detect(line)
    # print(result)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
"""
PING yandex.ru (5.255.255.5): 56 data bytes
64 bytes from 5.255.255.5: icmp_seq=0 ttl=244 time=46.839 ms
64 bytes from 5.255.255.5: icmp_seq=1 ttl=244 time=47.277 ms
64 bytes from 5.255.255.5: icmp_seq=2 ttl=244 time=47.807 ms
64 bytes from 5.255.255.5: icmp_seq=3 ttl=244 time=47.112 ms
"""
# =====================================================================================================================




# =====================================================================================================================




# =====================================================================================================================






