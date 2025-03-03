from django.db import connection

class UserWelcomeData():
    def getMenuOptions():
        with connection.cursor() as getMenuList:
            getMenuList.execute("call getMenuList()")
            menuoptions=getMenuList.fetchall()
            alloptions= [(option[0],option[1]) for option in menuoptions]
        return alloptions
