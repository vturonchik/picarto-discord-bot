import time

import requests


def check_online_status(headers):
    isOnline = False
    isOffline = False
    response = requests.get('https://api.picarto.tv/api/v1/channel/id/Impostor/streams', headers=headers)
    online_status = response.json()['channel']['online']
    if not online_status:
        wait_online()
    else:
        wait_offline()
    print(online_status)
    time.sleep(5)


if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/91.0.4472.101 Safari/537.36'
    headers_dict = {
        'accept': '*/*',
        'X-CSRF-TOKEN': '',
        'User-Agent': user_agent
    }

    check_online_status(headers_dict)
