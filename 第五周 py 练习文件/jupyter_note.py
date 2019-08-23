#根据 dataquest 的提示试着在 Jupyter Notebook 写代码
print('hello world')
print（'hello world(again)')

#用 shift + enter （运行并选中下一个cell，如果没有下一个cell就产生一个新的cell） 快捷键运行程序时敲打的代码
welcome_message = 'Hello, Jupyter!'
first_call = True

if first_call:
    print (welcome_message)

# use in command mode:
# Ctrl + Enter: run selected cell
# Shift + Enter: run cell, select below
# Alt + Enter: run cell, insert below
# Up: select cell above
# Down: select cell below
# Enter: enter edit mode
# A: insert cell above
# B: insert cell below
# D, D (press D twice): delete selected cell
# Z: undo cell deletion
# S: save and checkpoint
# Y: convert to code cell
# M: convert to Markdown cell

# use in edit mode:
# Ctrl + Enter: run selected cell
# Shift + Enter: run cell, select below
# Alt + Enter: run cell, insert below
# Up: move cursor up
# Down: move cursor down
# Esc: enter command mode
# Ctrl + A: select all
# Ctrl + Z: undo
# Ctrl + Y: redo
# Ctrl + S: save and checkpoint
# Tab: indent or code completion
# Shift + Tab: tooltip (提示当前光标所在地方的语法和信息备注)

#
def welcome(a_string):
    
    print('Welcome to'+ a_string + '!') 

dq = 'Dataquest'
jn = 'Jupyter Notebook'
py = 'Python'

#在 Jupyter Notebook 中使用 Markdown 注释的方法