import urllib.request
import urllib.parse
def get_robot_reply(question):
    if "你叫什么名字" in question:
        answer = "我是"
    elif "你多少岁" in question:
        answer = "23"
    elif "你是" in question:
        answer = "cds"
    else:
        try:
            params = urllib.parse.urlencode({'msg':question}).encode()
            req = urllib.request.Request("http://api.itmojun.com/chat_robot",params,method="POST")
            answer = urllib.request.urlopen(req).read().decode()
        except Exception as e:
            answer="AI机器人出现故障！（原因：%s)" % e
    return answer

if __name__ == '__main__':
    print(get_robot_reply("你叫什么名字"))
    print(get_robot_reply("武汉的天气"))
    print(get_robot_reply("你是男是女"))
    print(get_robot_reply("你到底是谁"))