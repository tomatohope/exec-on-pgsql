# -*- coding: UTF-8 -*-
import MySQLdb
from connectMysql import log

# execsql by sql
def execsql(host, user, passwd, database, sql, result):
    log.log("info", "database", database)
    log.log("info", "user", user)
    log.log("info", "host", host)
    log.log("info", "sql", sql)
    db = MySQLdb.connect(host=host, port=3306, user=user, passwd=passwd, db=database)
    cursor = db.cursor()
    cursor.execute(sql)
    results = []
    if str(result) == '1':
        results = cursor.fetchall()
    cursor.close()
    return results

# execsql by sqlfile
def execsqlfile(host, user, passwd, database, sqlfile, result):
    with open(sqlfile, 'r') as f:
        sql = f.read()
    results = execsql(host, user, passwd, database, sql, result)
    return results
