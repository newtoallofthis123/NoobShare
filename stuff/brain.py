from datetime import datetime, date
import json
import random
import string
import requests
from stuff import app, db
from stuff.models import Bin

def hash_gen_engine():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    whole =  lower + upper + digits
    hash_string = random.sample(whole, 8)
    hash = "".join(hash_string)
    return hash

def time_cal():
    current_t = datetime.now()
    current_date = str(date.today())
    current_t_f = current_t.strftime("%H:%M:%S")
    timeAnddate = (f'{current_t_f} {current_date}')
    return timeAnddate

def add_reserve(content, author, password, time, hash):
    add_content = Bin(author=author, content=content, password=password, hash=hash, time=time)
    db.session.add(add_content)
    db.session.commit()
    db.session.refresh(add_content)
    content_info = {"author": author, "content": content, "password": password, "time": time, "hash": hash}
    return content_info

def creation_engine(author, password, content):
    time = time_cal()
    hash = hash_gen_engine()
    content_info = add_reserve(content, author, password, time, hash)
    return content_info

def custom_hash(hash):
    hash_check = Bin.query.filter_by(hash=hash).first()
    if hash_check:
        return hash_gen_engine()
    else:
        return hash

def check_dups(hash):
    hash_check = Bin.query.filter_by(hash=hash).first()
    if hash_check:
        return True
    else:
        return False

def custom_creation_engine(author, content, password, hash):
    time = time_cal()
    hash = custom_hash(hash)
    content_info = add_reserve(content, author, password, time, hash)
    return content_info

def get_og(hash):
    content = Bin.query.filter_by(hash=hash).first()
    if content == None:
        return "No Such Stuff"
    else:
        return content

def debug_engine(table):
    debug_content = table.query.all()
    return debug_content

def undo():
    db.session.rollback()

def tinyurl(url):
    tinyurl_page = str(requests.get(f'https://tinyurl.com/api-create.php?url={url}').content).replace("b'", "").replace("'", "")
    return tinyurl_page

def ran_quote():
    quotes_page = json.loads(requests.get("https://api.quotable.io/random?maxLength=120").content)
    quote_list = [quotes_page["content"], quotes_page["author"]]
    return quote_list

def ran_fact():
    fact_page = json.loads(requests.get("https://useless-facts.sameerkumar.website/api").content)
    fact = fact_page["data"]
    return fact

def qr_code_engine(url):
    import pyqrcode
    qr_code = pyqrcode.create(url)
    qr_code.svg('shortener/static/assets/images/qr_code.svg', background="white", scale=8)

def ran_color():
    color_list = ("red", "yellow", "green", "blue")
    color = random.choice(color_list)
    colors = {
        "main": "main_" + color,
        "body": "body_" + color
    }
    return colors