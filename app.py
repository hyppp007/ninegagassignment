from flask import Flask
import requests
from time import strftime

app = Flask(__name__)

mem = {}


@app.route('/9gag-awesome', methods=['GET'])
def awesome_get():
    try:
        now_time = strftime('%a,%d %b %Y %H:%M:%S')
        if 'last_time_awesome' not in mem or (now_time[:-2] != mem['last_time_awesome'][:-2]) or (now_time[-2:] - mem['last_time_awesome'][-2:]) > 2:
            r = requests.get('https://9gag-rss.com/api/rss/get?code=9GAGAwesomeNoGif&format=2')

            xml = r.content.decode("utf-8")

            if r.status_code == 200:

                date_position_start = xml.find('lastBuildDate') + 14

                date_position_end = xml.find('</lastBuildDate>') - 2

                date = xml[date_position_start:date_position_end]

                mem['last_time_awesome'] = date
                mem['last_content_awesome'] = r.content

            return r.content, r.status_code
        else:

            return mem['last_content_awesome'], 200

    except Exception as e:
        return ""



@app.route('/9gag-comic', methods=['GET'])
def comic_get():
    try:
        now_time = strftime('%a,%d %b %Y %H:%M:%S')
        if 'last_time_comic' not in mem or (now_time[:-2] != mem['last_time_comic'][:-2]) or (
                now_time[-2:] - mem['last_time_comic'][-2:]) > 2:
            r = requests.get('https://9gag-rss.com/api/rss/get?code=9GAGComic&format=2')
            xml = r.content.decode("utf-8")
            if r.status_code == 200:
                date_position_start = xml.find('lastBuildDate') + 14
                date_position_end = xml.find('</lastBuildDate>') - 2
                date = xml[date_position_start:date_position_end]
                mem['last_time_comic'] = date
                mem['last_content_comic'] = r.content
            return r.content, r.status_code
        else:
            return mem['last_content_comic'], 200

    except Exception as e:
        return ""


@app.route('/9gag-darkhumor', methods=['GET'])
def darkhumor_get():
    try:
        now_time = strftime('%a,%d %b %Y %H:%M:%S')
        if 'last_time_darkhumor' not in mem or (now_time[:-2] != mem['last_time_darkhumor'][:-2]) or (
                now_time[-2:] - mem['last_time_darkhumor'][-2:]) > 2:
            r = requests.get('https://9gag-rss.com/api/rss/get?code=9GAGDarkHumor&format=2')
            xml = r.content.decode("utf-8")
            if r.status_code == 200:
                date_position_start = xml.find('lastBuildDate') + 14
                date_position_end = xml.find('</lastBuildDate>') - 2
                date = xml[date_position_start:date_position_end]
                mem['last_time_darkhumor'] = date
                mem['last_content_darkhumor'] = r.content
            return r.content, r.status_code
        else:
            return mem['last_content_darkhumor'], 200

    except Exception as e:
        return ""


@app.route('/9gag-fresh', methods=['GET'])
def fresh_get():
    try:
        now_time = strftime('%a,%d %b %Y %H:%M:%S')
        if 'last_time_fresh' not in mem or (now_time[:-2] != mem['last_time_fresh'][:-2]) or (
                now_time[-2:] - mem['last_time_fresh'][-2:]) > 2:
            r = requests.get('https://9gag-rss.com/api/rss/get?code=9GAGFresh&format=2')
            xml = r.content.decode("utf-8")
            if r.status_code == 200:
                date_position_start = xml.find('lastBuildDate') + 14
                date_position_end = xml.find('</lastBuildDate>') - 2
                date = xml[date_position_start:date_position_end]
                mem['last_time_fresh'] = date
                mem['last_content_fresh'] = r.content
            return r.content, r.status_code
        else:
            return mem['last_content_fresh'], 200

    except Exception as e:
        return ""


if __name__ == '__main__':
    app.run()