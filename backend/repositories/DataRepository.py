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
        sql = "SELECT * from historiek where commentaar like 'deur%'"
        return Database.get_rows(sql)
    @staticmethod
    def read_user():
        sql="SELECT * from user"
        return Database.get_rows(sql)
    # @staticmethod
    # def read_status_lamp_by_id(id):
    #     sql = "SELECT * from lampen WHERE id = %s"
    #     params = [id]
    #     return Database.get_one_row(sql, params)

    @staticmethod
    def update_status_lamp(id, status):
        sql = "UPDATE lampen SET status = %s WHERE id = %s"
        params = [status, id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_status_alle_lampen(status):
        sql = "UPDATE lampen SET status = %s"
        params = [status]
        return Database.execute_sql(sql, params)
    
    @staticmethod 
    def create_historiek(deviceid,actieid,actiedatum,waarde,commentaar):
        sql = "INSERT INTO historiek (deviceid, actieid,actiedatum, waarde, commentaar) VALUES (%s,%s,%s,%s,%s)"
        params = [deviceid,actieid, actiedatum, waarde, commentaar]
        return Database.execute_sql(sql, params)
    
    @staticmethod
    def create_frigo_historiek(userid,datum):
        sql="INSERT INTO frigohistoriek (userid, datum) VALUES (%s,%s)"
        params=[userid,datum]
        return Database.execute_sql(sql,params)