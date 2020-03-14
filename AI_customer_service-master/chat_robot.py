'''
文件描述：基于微信公众号实现AI客服
作者：zzq
邮箱：1098506799@qq.com
时间：2019-7-3 13:05
'''
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import flask
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message
from wechatpy.replies import create_reply
from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import qrcode
import io
app = flask.Flask(__name__)
def get_news():
    news = ""
    url = "https://mil.news.sina.com.cn"
    try:
        f = requests.get(url, timeout=2)
        soup = BeautifulSoup(f.content, "lxml")
        for k in soup.find_all('div', class_='list_link_box'):
            a = k.find_all('li')
            for new in a:
                news += "<a href='" + new.a.get('href') + "'>" + new.string + "</a>" + '\n'
    except:
        news = str
    return news
def get_qrcode():
    url = "http://qr.itmojun.com"
    return url
def get_robot_reply(question):
    '''
    函数功能：对于特定问题进行特定回复，对于非特定问题进行智能回复
    参数描述：
    question 聊天内容或问题
    返回值：str，回复内容
    '''
    if "你叫什么" in question:
        answer = "我是小爱呀！"
    elif "你们小组编号" in question:
        answer = "第七组"
    elif "你们小组成员" in question:
        answer = "组长：周紫齐"+"\n"+"组员：徐雨洁、谭新宇、王文栋、郑道远、陈雷、帅田、卢文卓"
    elif "最新军事新闻头条" in question:
        answer = get_news()
    elif "二维码" in question:
        answer = "点击链接输入内容即可或得你要的二维码"+get_qrcode()

    else:
        try:
            # 调用NLP接口实现智能回复
            params = urllib.parse.urlencode({'msg': question}).encode()  # 接口参数需要进行URL编码
            req = urllib.request.Request("http://api.itmojun.com/chat_robot", params, method="POST")  # 创建请求对象
            answer = urllib.request.urlopen(req).read().decode()  # 调用接口（即向目标服务器发出HTTP请求，并获取服务器的响应数据）
        except Exception as e:
            answer = "AI机器人出现故障！（原因：%s）" % e

    return answer


@app.route("/wx", methods=["GET", "POST"])
def weixin_handler():
    token = "shuai"
    signature = flask.request.args.get("signature")
    timestamp = flask.request.args.get("timestamp")
    nonce = flask.request.args.get("nonce")
    echostr = flask.request.args.get("echostr")
    try:
        # 校验token
        check_signature(token, signature, timestamp, nonce)
    except InvalidSignatureException:
        # 校验token失败
        flask.abort(403)
    if flask.request.method == "GET":
        return echostr
    elif flask.request.method == "POST":
        xml = flask.request.data
        msg = parse_message(xml)
        if msg.type == 'text':
            reply = create_reply(get_robot_reply(msg.content), msg)
        else:
            reply = create_reply('Sorry, can not handle this for now', msg)
        # 转换成 XML
        xml = reply.render()
        return xml
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="80")
