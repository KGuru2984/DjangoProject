from django.db import connection

class VerifyUser():
    @staticmethod
    def ValidateLogin(uemail,upassword):
        with connection.cursor() as validateuser:
            validateuser.execute("set @msg='';")
            validateuser.execute("call validatelogin(%s,%s,@msg);",[uemail,upassword])
            validateuser.execute("select @msg;")
            resultMessage=validateuser.fetchone()[0]
        return resultMessage