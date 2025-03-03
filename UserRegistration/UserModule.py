from django.db import connection

class UserRecord():
    @staticmethod
    def addUserRecord(uname,uemail,upassword):
        with connection.cursor() as adduser:
            adduser.execute("set @msg='';")
            adduser.execute("call addloginrecord(%s,%s,%s,@msg);",[uname,uemail,upassword])
            adduser.execute("select @msg;")
            resultMessage=adduser.fetchone()[0]
        return resultMessage