#encoding:utf-8

from utils import get_url, weighted_random_subreddit


# Group chat https://yal.sh/dvdahoy
t_channel = '-1001065558871'
subreddit = weighted_random_subreddit({
    'ANormalDayInRussia': 1.0,
    'ANormalDayInAmerica': 0.1,
    'ANormalDayInJapan': 0.01
})


def send_post(submission, r2t):
    what, url, ext = get_url(submission)
    title = submission.title
    link = submission.shortlink
    text = '{}\n{}'.format(title, link)

    return r2t.send_gif_img(what, url, ext, text)
