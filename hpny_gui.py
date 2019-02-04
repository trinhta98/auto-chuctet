#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
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

def Login():
    global client
    temp_user = txt_user.get()
    temp_pass = txt_pass.get()
    root.destroy()
    client = Echobot(temp_user, temp_pass)
    client.listen()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title('Chúc tết - Auto')
        self.master.iconbitmap('fb.ico')
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        global txt_user
        global txt_pass

        lb_user = Label(self, text='Username: ')
        lb_pass = Label(self, text='Password: ')
        lb_user.place(x=40, y=5)
        lb_pass.place(x=40, y=30)

        txt_user = Entry(self)
        txt_pass = Entry(self, show='*')
        txt_user.place(x=110, y=5)
        txt_pass.place(x=110, y=30)
        login = Button(self, text='Login', command=Login)
        login.place(x=192, y=60)



def main():
    global root
    root = Tk()
    root.geometry("300x100")
    app = Window(root)
    root.mainloop()

main()