#!/usr/bin/python
# -*- coding: utf-8 -*-
from fbchat import Client
import random

loichuc = []
for line in open("loichuc.txt", 'r', encoding='utf-8'):
    loichuc.append(line)
send = open("send.txt", 'a', encoding='utf-8')

class Echobot(Client):
    #author_id: id của người gửi
    #message_object = thông tin tin nhắn nhận được -> message_object.text: nội dung tin nhắn
    #thread_id:  id của cuộc trò chuyện
    def onMessage(self,author_id, message_object, thread_id, thread_type, **kwargs):
        user = client.fetchUserInfo(author_id)[author_id]
        if author_id != self.uid:
            print('Đã nhận được tin nhắn từ "{}" có ID = "{}" với nội dung là: "{}"'.format(user.name, author_id, message_object.text))
            temp = message_object.text
            temp = str(temp).split(' ')
            for text in temp:
                if text in open("template.txt", "r", encoding='utf-8').read():
                    if author_id not in open("send.txt", 'r', encoding='utf-8').read():
                        if message_object.text is not None:
                            msg = random.choice(loichuc)
                            self.sendMessage(msg, thread_id=thread_id, thread_type=thread_type)
                            print('Đã gửi tin nhắn cho "{}" với nội dung là: "{}"'.format(user.name, msg))
                            send = open("send.txt", 'a', newline='', encoding='utf-8')
                            send.write(author_id + "\n")
                            break


def main():
    global client
    user_inp = input("Nhap User: ")
    pass_inp = input("Nhap Pass: ")
    client = Echobot(user_inp, pass_inp)
    client.listen()

main()