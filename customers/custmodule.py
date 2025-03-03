from django.db import connection

class custdetails():
    
    @staticmethod
    def addcustomerrec(cname,caddress):
        with connection.cursor() as addcustomercursor:
            addcustomercursor.execute("set @msg='';")
            addcustomercursor.execute("call addcustomerdetails(%s,%s,@msg);",[cname,caddress])
            addcustomercursor.execute("select @msg")
            result=addcustomercursor.fetchone()[0]
        return result
            
        