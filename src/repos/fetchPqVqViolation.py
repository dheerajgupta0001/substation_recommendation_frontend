import datetime as dt
import psycopg2
from typing import List
from src.config.appConfig import getAppConfig
from src.typeDefs.pqVqViolationSummary import IPqVqViolationSummary
import pandas as pd

class PqVqViolationSummaryRepo():
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

    def fetchPqVqViolation(self) -> bool:
        """_summary_

        Returns:
            List[IPqVqViolationSummary]: _description_
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

            sql_fetch = 'SELECT * FROM "pq_violation" order by time_stamp desc'

            data = pd.read_sql(sql_fetch, con=conn)
            # print(data)

        except Exception as err:
            print('Error while fetching PQ Violation')
            print(err)

        finally:
            if dbCur is not None:
                dbCur.close()
            if dbConn is not None:
                dbConn.close()

        
        pqVqViolationList: List[IPqVqViolationSummary] = []
        for i in data.index:
            pqVqViolation: IPqVqViolationSummary = {
                'id':str(data['id'][i]),
                'time_stamp': dt.datetime.strftime(data['time_stamp'][i], "%Y-%m-%d %X"),
                'generating_station': data['generating_station'][i],
                'voltage': float(data['voltage'][i]),
                'substation_mvar': float(data['substation_mvar'][i]),
                'farm_p': float(data['farm_p'][i]),
                'farm_q': float(data['farm_q'][i]),
                'isVqViolated': bool(data['isVqViolated'][i]),
                'isPqViolated': bool(data['isPqViolated'][i]),
                'isPqVqViolated': bool(data['isPqVqViolated'][i])
            }
            pqVqViolationList.append(pqVqViolation)
        return pqVqViolationList
    
    def fetchPqViolation(self, isRecommendation: bool) -> bool:
        """_summary_

        Returns:
            List[IPqVqViolationSummary]: _description_
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

            sql_fetch = 'SELECT * FROM "pq_violation" where "isRecommendation" = {0} order by time_stamp desc'.format(isRecommendation)

            data = pd.read_sql(sql_fetch, con=conn)
            # print(data)

        except Exception as err:
            print('Error while inserting unit name for {} from master table'.format())
            print(err)

        finally:
            if dbCur is not None:
                dbCur.close()
            if dbConn is not None:
                dbConn.close()

        
        pqVqViolationList: List[IPqVqViolationSummary] = []
        for i in data.index:
            pqVqViolation: IPqVqViolationSummary = {
                'id':str(data['Id'][i]),
                'time_stamp': dt.datetime.strftime(data['time_stamp'][i], "%Y-%m-%d %X"),
                'generating_station': data['generating_station'][i],
                'voltage': data['voltage'][i],
                'substation_mvar': data['substation_mvar'][i],
                'farm_p': data['farm_p'][i],
                'farm_q': data['farm_q'][i]
            }
            pqVqViolationList.append(pqVqViolation)
        return pqVqViolationList
    
    def fetchVqViolation(self, isRecommendation: bool) -> bool:
        """_summary_

        Returns:
            List[IPqVqViolationSummary]: _description_
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

            sql_fetch = 'SELECT * FROM "pq_violation" where "isRecommendation" = {0} order by time_stamp desc'.format(isRecommendation)

            data = pd.read_sql(sql_fetch, con=conn)
            # print(data)

        except Exception as err:
            print('Error while inserting unit name for {} from master table'.format())
            print(err)

        finally:
            if dbCur is not None:
                dbCur.close()
            if dbConn is not None:
                dbConn.close()

        
        pqVqViolationList: List[IPqVqViolationSummary] = []
        for i in data.index:
            pqVqViolation: IPqVqViolationSummary = {
                'id':str(data['Id'][i]),
                'time_stamp': dt.datetime.strftime(data['time_stamp'][i], "%Y-%m-%d %X"),
                'generating_station': data['generating_station'][i],
                'voltage': data['voltage'][i],
                'substation_mvar': data['substation_mvar'][i],
                'farm_p': data['farm_p'][i],
                'farm_q': data['farm_q'][i]
            }
            pqVqViolationList.append(pqVqViolation)
        return pqVqViolationList