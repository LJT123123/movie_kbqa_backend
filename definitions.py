#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: duyi
@Email: yangty21@m.fudan.edu.cn
@Created: 2021/12/09
------------------------------------------
@Modify: 2021/12/09
------------------------------------------
@Description:
"""
import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root

DATA_DIR = str(Path(ROOT_DIR) / "data")  # This is the data of this project
OUTPUT_DIR = str(Path(ROOT_DIR) / "output")  # This is the output of this project
LOG_DIR = str(Path(ROOT_DIR) / "log")  # This is the log of this project

CHINESE_PUNCTUATION = """！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃《》「」『』【】〔〕〖
〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏"""

# label映射
LABEL_MAPPING = {
    'm': 'MOVIE',
    's': 'STAR',
    'w': 'WRITER',
    'd': 'DIRECTOR',
    'c': 'COMPANY'
}


# 电影问题的匹配模板
movie_genre = ['What type of movie is {}?', 'What genre is {}?']
movie_time = ['When is {} released?', 'When is {} coming out?']
movie_director = ['Who is the director of {}?', 'Who directed {}?']
movie_writer = ['Who is the screenwriter of {}?', 'Who wrote {}?']
movie_star = ['Who is the actor of {}?', 'Who starred in {}?']
movie_company = ['Which company produced {}?', 'Which company made {}?']

# 演员问题的匹配模板
star_movie = ['What movies did {} act in?']
star_director = ['Which director did {} cooperate with?']
star_writer = ['Which writer did {} cooperated with?']

# 导演问题的匹配模板
director_movie = ['What movies did {} direct?']
director_star = ['Which star did {} cooperate with?']
director_writer = ['Which writer did {} cooperate with?']

# 编剧问题的匹配模板
writer_movie = ['What movies did {} write?']
writer_director = ['Which director did {} cooperate with?']
writer_star = ['Which star did {} cooperate with?']

# 公司问题的匹配模板
company_movie = ['What movies did {} produce?']


# 电影问题回答模板
movie_genre_reply = 'The genre of {} is {}.'
movie_time_reply = 'The release time of {} is {}.'
movie_director_reply = 'The director of {} is {}.'
movie_writer_reply = 'The writer of {} is {}.'
movie_star_reply = 'The star of {} is {}.'
movie_company_reply = 'The produce company of {} is {}.'

# 演员问题回答模板
star_movie_reply = 'The movies {} acted in are {}.'
star_director_reply = 'The directors {} cooperated with are {}.'
star_writer_reply = 'The writers {} cooperated with are {}.'

# 编剧问题回答模板
writer_movie_reply = 'The movies {} wrote are {}.'
writer_director_reply = 'The directors {} cooperated with are {}.'
writer_star_reply = 'The stars {} cooperated with are {}.'

# 导演问题回答模板
director_movie_reply = 'The movies {} directed are {}.'
director_writer_reply = 'The writers {} cooperated with are {}.'
director_star_reply = 'The stars {} cooperated with are {}.'

# 公司问题回答模板
company_movie_reply = 'The movies {} produced are {}.'

# 电影意图模板字典
MOVIE_INTENT = {
     'movie_genre': movie_genre,
     'movie_time': movie_time,
     'movie_director': movie_director,
     'movie_writer': movie_writer,
     'movie_star': movie_star,
     'movie_company': movie_company
}

# 演员意图模板字典
STAR_INTENT = {
    'star_movie': star_movie,
    'star_writer': star_writer,
    'star_director': star_director
}

# 导演意图模板字典
DIRECTOR_INTENT = {
    'director_movie': director_movie,
    'director_star': director_star,
    'director_writer': director_writer
}

# 编剧意图模板字典
WRITER_INTENT = {
    'writer_movie': writer_movie,
    'writer_star': writer_star,
    'writer_director': writer_director
}

# 公司意图模板字典
COMPANY_INTENT = {
    'company_movie': company_movie
}


# 电影回答模板字典
MOVIE_REPLY = {
    'movie_genre': movie_genre_reply,
    'movie_time': movie_time_reply,
    'movie_director': movie_director_reply,
    'movie_writer': movie_writer_reply,
    'movie_star': movie_star_reply,
    'movie_company': movie_company_reply
}

# 演员回答模板字典
STAR_REPLY = {
    'star_movie': star_movie_reply,
    'star_writer': star_writer_reply,
    'star_director': star_director_reply
}

# 编剧回答模板字典
WRITER_REPLY = {
    'writer_movie': writer_movie_reply,
    'writer_star': writer_star_reply,
    'writer_director': writer_director_reply
}

# 导演回答模板字典
DIRECTOR_REPLY = {
    'director_movie': director_movie_reply,
    'director_star': director_star_reply,
    'director_writer': director_writer_reply
}

# 公司回答模板字典
COMPANY_REPLY = {
    'company_movie': company_movie_reply
}


class RemoteNEO4J:
    HOST = '101.132.165.84'
    PORT = 9503
    USERNAME = 'neo4j'
    PASSWORD = 'fdsefdse'
