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
        sql = "SELECT * from historiek where commentaar like 'deur%' ORDER BY actiedatum desc limit 50"
        return Database.get_rows(sql)
    @staticmethod
    def read_user():
        sql="SELECT * from user"
        return Database.get_rows(sql)

    @staticmethod
    def read_temp():
        sql="SELECT * from historiek where commentaar like 'temp%' ORDER BY actiedatum desc  limit 50"
        return Database.get_rows(sql)
    
    
    @staticmethod 
    def create_historiek(deviceid,actieid,actiedatum,waarde,commentaar):
        sql = "INSERT INTO historiek (deviceid, actieid,actiedatum, waarde, commentaar) VALUES (%s,%s,%s,%s,%s)"
        params = [deviceid,actieid, actiedatum, waarde, commentaar]
        return Database.execute_sql(sql, params)
    
    @staticmethod
    def create_frigo_historiek(userid,naam,datum):
        sql="INSERT INTO frigohistoriek (userid,naam, datum) VALUES (%s,%s,%s)"
        params=[userid,naam,datum]
        return Database.execute_sql(sql,params)