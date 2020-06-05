import pypyodbc


def find_data(a, b, c):
    x = '[\'' + str(a) + '$\']'
    y = '\'' + str(b) + '\''
    if c == 'all':
        z = ''
    else:
        z = ' AND [Number of rooms] =' + str(c)

    my_server = "DESKTOP-UDMCM4L\SQLEXPRESS"
    my_database = "real_estate"
    connection = pypyodbc.connect('Driver={SQL Server};'
                                  'Server=' + my_server + ';'
                                                          'Database=' + my_database + ';')
    cursor = connection.cursor()
    my_query = ("""SELECT       [Month]
                              ,[City / Village]
                              ,[District]
                              ,[Street / Residential complex]
                              ,[House number]
                              ,[Number of rooms]
                              ,[Floor / Floors]
                              ,[Total area]
                              ,[Characteristic]
                              ,[Price / all, $]
                              ,[Price / per sq.m, $]
                              ,[Comments] 
                    FROM""" + x + """
                    WHERE [Street / Residential complex] =""" + y + z
                )
    cursor.execute(my_query)
    results = cursor.fetchall()
    connection.close()
    return results
