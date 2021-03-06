import requests
import re

def get_resposta(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text

def prepare_urls(matches):
    return list({match.replace("\\u0026", "&") for match in matches})

url = input('Coloque a url do Instagram: ')
resposta = get_resposta(url)

vid_matches = re.findall('"video_url":"([^"]+)"', resposta)
pic_matches = re.findall('"display_url":"([^"]+)"', resposta)

vid_urls = prepare_urls((vid_matches))
pic_urls = prepare_urls(pic_matches)

if vid_urls:
    print('Detected Videos:\n{0}'.format('\n'.join(vid_urls)))

if pic_urls:
    print('Detected Pictures:\n{0}'.format('\n'.join(pic_urls)))

if not (vid_urls or pic_urls):
    print('Não foi possível reconhecer a mídia no URL fornecido.')