#Ingólfur Óskarsson
#Lokaverkefni
from bottle import *
import pymysql
import os

#Test
"""@route('/')
def index():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
    cur = conn.cursor()
    #cur.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
    #cur.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
    cur.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
    cur.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
    cur.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
    conn.commit()
    return "index"""""


#Test
"""@route('/todo')
def todo_list():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    return str(result)"""

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
        #new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>'
    else:
        return template('lokaverknew.tpl')

@route('/edit/<no:int>', method='GET')
def edit_item(no):
    print(no)
    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()
        if status == 'open':
            status = 1
        else:
            status = 0
            conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id  = {:d}".format(edit, status, no))
        conn.commit()
        return '<p>The item number %s was successfully updated</p>' % no
    else:
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id  = {:d}".format(no))
        cur_data = c.fetchone()

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
    #tdate = convDate = datetime.datetime.strptime(rec[3], "%Y-%m-%d %H:%M:%S.f").strftime(%A %d %B %Y - %I:%M %p)
    if not rec:
        return 'This item number does not exist!'
        conn.close()
    else:
        output = template('lokaverkedit.tpl', ttitle=ttitle, tdesc=tdesc,todoid=todoid)
        return output
        conn.close()

""""@route('/edit<no:int>', method=['GET', 'POST'])
def edit_item(no):
    todoid = no
    if request.POST.get('save').strip():
        todotitle = request.POST.get('task')

        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
        cur = conn.cursor()
        cur.execute('UPDATE todo SET task = ?, status = ? WHERE id LIKE ?', (todotitle))
        conn.commit()
        rows = cur.execute('SELECT * FROM todo ORDER BY id ASC')
        return redirect('/',rows = rows)
        conn.close()
    else:
        conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='0306923069', passwd='mypassword',db='0306923069_todolist')
        cur = conn.cursor()
        cur.execute('SELECT * FROM todo WHERE id=?', (todoid,))
        rec = cur.fetchone()
        return template ('edit_task.tpl', no=no, rec=rec)
        conn.close"""


@error(403)
def villa(error):
    return 'Ekki rétt síða!'

@error(404)
def villa(error):
    return 'Því miður, þetta er ekki til!'

run()