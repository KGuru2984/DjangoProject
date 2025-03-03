from django.db import connection

class ProductCatalogClass():
    def addProductRecord(prodcategory,prodname,proddesc,prodprice,prodimage):
        with connection.cursor() as addrecord:
            addrecord.execute("select @msg='';")
            addrecord.execute("call addproduct(%s,%s,%s,%s,%s,@msg);",[prodcategory,prodname,proddesc,prodprice,prodimage])
            addrecord.execute("select @msg;")
            resultMsg=addrecord.fetchone()[0]
        return resultMsg
    
    def getProductCategories():
        with connection.cursor() as getrecord:
            getrecord.execute("call getproductcategories();")
            categories=getrecord.fetchall()
        
        prodcategories= [(category[0],category[1]) for category in categories]
        return prodcategories
    
    def getAllProduct():
        with connection.cursor() as getprod:
            getprod.execute("call getallproduct()")
            proddetails=getprod.fetchall()
        allprod=[(prod[0],prod[1],prod[2],prod[3],prod[4],prod[5]) for prod in proddetails]
        return allprod
    
    def getproductbyproductid(productid):
        with connection.cursor() as getprodid:
            getprodid.execute("call getproductbyid(%s);",[productid])
            proddetails=getprodid.fetchall()
            # productrecord=[(product[0],product[1],product[2],product[3],product[4],product[5],product[6]) for product in proddetails]
        return proddetails
    
    def changeproductbyid(vpid,vpcategory,vpname,vpdesc,vpimg,vpprice,vpflag):
        with connection.cursor() as changeprod:
            changeprod.execute("set @msg='';")
            changeprod.execute("call changeproductdetails(%s,%s,%s,%s,%s,%s,%s,@msg);",[vpid,vpcategory,vpname,vpdesc,vpimg,vpprice,vpflag])
            changeprod.execute("select @msg;")
            result=changeprod.fetchone()[0]
        return result
    
    def removalbyproductid(vid):
        print(vid)
        with connection.cursor() as remid:
            remid.execute("set @msg='';")
            remid.execute("call removalproductstatus(%s,@msg);",[vid])
            remid.execute("select @msg;")
            result=remid.fetchone()[0]
        return result
    
    def getbasketviewcount(p_userid):
        with connection.cursor() as basketcnt:
            basketcnt.execute("set @cnt='';")
            basketcnt.execute("call getbasketcountbyuser(%s,@cnt);",[p_userid])
            basketcnt.execute("select @cnt;")
            resultcnt=basketcnt.fetchone()[0]
        return resultcnt
    
    def addbasketdata(p_userid,p_productid,p_productqty):
        with connection.cursor() as basketadd:
            basketadd.execute("set @msg='';")
            basketadd.execute("call addtempbasket(%s,%s,%s,@msg);",[p_userid,p_productid,p_productqty])
            basketadd.execute("select @msg;")
            resultadd=basketadd.fetchone()[0]
        return resultadd
    
    def getbasketrec(p_userid):
        with connection.cursor() as basketr:
            basketr.execute("call getbasketrecord(%s);",[p_userid])
            basketdata=basketr.fetchall()
        return basketdata
    
    def modifybasketquantity(p_basketid,p_prodqty):
        with connection.cursor() as modifyrec:
            modifyrec.execute("call modifybasketquantity(%s,%s)",[p_basketid,p_prodqty])
        
        