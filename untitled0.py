# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 10:38:12 2021

@author: kevin
"""

import tkinter as tk

window = tk.TK()

window.title ("Menu")

window.geometry("500x500")

meenuBer = tk.Menu(window)

filemenu = tk.Menu(menuBar,tearoff=False)

filemenu.add_command(label="開始遊戲")

filemenu.add_command(label="作弊指令")

filemenu.add_separator()

filemenu.add_command(label="Exit")

menuBer.add_cascade(label="檔案  ",menu=fileMenu)

filemenu = tk.Menu(menuBar,tearoff=False)

filemenu2.add_command(label="遊戲設定")

filemenu2.add_command(label="畫面設定")

menuBer.add_cascade(label="選項  ",menu=fileMenu2)

filemenu = tk.Menu(menuBar,tearoff=False)

filemenu.add_command(label="畫面存取")

filemenu.add_command(label="名子設定")



menuBer.add_cascade(label="額外設定  ",menu=fileMenu)

filemenu3 = tk.Menu(menuBar,tearoff=False)

filemenu3.add_command(label="拍照")

filemenu3.add_command(label="結束")

menuBer.add_cascade(label=" 選項 ",menu=fileMenu2)

menuBer.add_cascade(label="  ",menu=fileMenu)

submenu = tk.Menu(menuBar,tearoff=False)

submenu.add_command(label="簡單模式")

submenu.add_command(label="困難模式")

menuBer.add_cascade(label="開始遊戲  ",menu=subMenu)
menuBer.add_cascade(label="檔案  ",menu=fileMenu)
window.config(menu=menuBar)

window.mainloop()