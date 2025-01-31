import datetime as dt
import psycopg2
from typing import List
from src.config.appConfig import getAppConfig
import pandas as pd

class EmailsSummaryRepo():
    """Repository class for transmission data
    """
    localConStr: str = ""

    def __init__(self, dbConStr: str) -> None:
        """constructor method
        Args:
            dbConf (DbConfig): database connection string
        """
        self.localConStr = dbConStr
        # print(dbConStr)

    def fetchEmailsList(self, generatingStationList: List) -> bool:
        """_summary_

        Returns:
            List[Emails]: _description_
        """
        try:
            dbConfig = getAppConfig()
            dbConn = None
            dbCur = None
            # Connect to your PostgreSQL database
            conn = psycopg2.connect(host=dbConfig.db_host, dbname=dbConfig.db_name,
                                    user=dbConfig.db_username, password=dbConfig.db_password)
            # Create a cursor object using the connection
            dbCur = conn.cursor()

            # Convert the list into a properly formatted string for SQL
            formatted_stations = "'" + "','".join(generatingStationList) + "'"

            sql_fetch = 'SELECT emails FROM "emailsTable" where "generating_station" in ({0})'.format(formatted_stations)

            data = pd.read_sql(sql_fetch, con=conn)

        except Exception as err:
            print('Error while fetching PQ Violation')
            print(err)

        finally:
            if dbCur is not None:
                dbCur.close()
            if dbConn is not None:
                dbConn.close()

        generatingStationsEmails = data['emails']

        return generatingStationsEmails