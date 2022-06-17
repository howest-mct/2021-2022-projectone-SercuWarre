import re
from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    @staticmethod
    def read_historiek():
        sql = "SELECT volgnummer,actiedatum,commentaar from historiek where commentaar like 'deur%' ORDER BY actiedatum desc limit 50"
        return Database.get_rows(sql)
    @staticmethod
    def read_user():
        sql="SELECT * from user"
        return Database.get_rows(sql)

    @staticmethod
    def read_frigo_historiek():
        sql="SELECT U.naam,F.datum,D.biernaam,F.aantal FROM frigohistoriek as F join user as U on F.user_RFid=U.RFid  join drinks as D on F.drinks_iddrinks=D.drankenid order by datum desc limit 50"
        return Database.get_rows(sql)
    @staticmethod
    def read_temp():
        sql="SELECT * from historiek where commentaar like 'temp%' ORDER BY actiedatum desc  limit 50"
        return Database.get_rows(sql)

    @staticmethod 
    def read_bar():
        sql="SELECT U.naam,F.datum,D.biernaam,sum(F.aantal) as 'aantal' FROM frigohistoriek as F join user as U on F.user_RFid=U.RFid join drinks as D on F.drinks_iddrinks=D.drankenid group by  biernaam,naam order by naam"
        return Database.get_rows(sql)
    @staticmethod
    def Read_drinks():
        sql="SELECT aantal from drinks "
        return Database.get_rows(sql)
    
    @staticmethod 
    def create_historiek(deviceid,actieid,actiedatum,waarde,commentaar):
        sql = "INSERT INTO historiek (deviceid, actieid,actiedatum, waarde, commentaar) VALUES (%s,%s,%s,%s,%s)"
        params = [deviceid,actieid, actiedatum, waarde, commentaar]
        return Database.execute_sql(sql, params)
    
    @staticmethod
    def create_frigo_historiek(userid,drinks_drinksid,datum,aantal):
        sql="INSERT INTO frigohistoriek (user_RFid,drinks_iddrinks, datum, aantal) VALUES (%s,%s,%s,%s)"
        params=[userid,drinks_drinksid,datum,aantal]
        return Database.execute_sql(sql,params)
    
    @staticmethod
    def update_drinks_min(aantal_drank,id):
        sql='update drinks SET aantal= aantal-%s where drankenid=%s'
        params=[aantal_drank,id]
        return Database.execute_sql(sql,params)
    @staticmethod
    def update_drinks_plus(aantal_drank,id):
        sql='update drinks SET aantal= aantal+%s where drankenid=%s'
        params=[aantal_drank,id]
        return Database.execute_sql(sql,params)
        