#Ingólfur Óskarsson
#Lokaverkefni
from bottle import *
import pymysql
import os


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename,root='./static/')

@route('/')
def index():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
    cur = conn.cursor()
    cur.execute("SELECT * FROM todo WHERE status LIKE '1'")
    result = cur.fetchall()
    conn.close()
    output = template('lokaverktup.tpl', rows=result)
    return output

@route('/upp')
def upplysingar():
    return template('lokaverkupp.tpl')

@route('/new',method='GET')
def new_item():

    if request.GET.save:

        new = request.GET.task.strip()
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) Values('{}','{:d}')".format(new,1))

        conn.commit()
        c.close()

        return redirect('/')
    else:
        return template('lokaverknew.tpl')

@route('/edit/<no:int>', method='GET')
def edit_item(no):
    print(no)
    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()
        if status == 'open':
            print("open")
            status = int(1)
            conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
            c = conn.cursor()
            c.execute("UPDATE todo SET task = '{}', status = '{}' WHERE id  = '{:d}'".format(edit, status, no))
            conn.commit()
            conn.close()
            return redirect('/')
        else:
            print("close")
            status = int(0)
            conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
            c = conn.cursor()
            c.execute("UPDATE todo SET task = '{}', status = '{}' WHERE id  = '{:d}'".format(edit, status, no))
            conn.commit()
            conn.close()
            return redirect('/')
    else:
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id  = {:d}".format(no))
        cur_data = c.fetchone()
        print("búmm....")
        return template('edit_task.tpl', old=cur_data, no=no)



@route('/item<item:re:[0-9]+>')
def show_item(item):
    todoid = int(item)
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
    c = conn.cursor()
    c.execute("SELECT * FROM todo WHERE id = {:d}".format(todoid))
    rec = c.fetchone()
    ttitle = rec[1]
    tdesc = rec[2]
    if not rec:
        conn.close()
        return 'This item number does not exist!'

    else:
        output = template('lokaverkedit.tpl', ttitle=ttitle, tdesc=tdesc,todoid=todoid)
        conn.close()
        return output



@error(403)
def villa(error):
    return 'Ekki rétt síða!'

@error(404)
def villa(error):
    return 'Því miður, þetta er ekki til!'

run()