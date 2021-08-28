class SQLHelper():
    def query_sql(self, table, column=None, value=None):
        if column and value:
            if isinstance(column, str):
                sql = "select * from " + table + " where " + column + " = " + value + ";"
            else:
                num = len(column)
                sql = "select * from " + table + " where " + column + " = " + value + " and "
                # 未完成
