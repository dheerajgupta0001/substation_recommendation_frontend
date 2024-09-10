import datetime as dt
import psycopg2
from typing import List
from src.config.appConfig import getJsonConfig
from src.typeDefs.latestRecommendationSummary import ILatestRecommendationSummary
import pandas as pd

class RecommendationSummaryRepo():
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

    # def fetchLatestRecommendation(self) -> List[ILatestRecommendationSummary]:
    def fetchLatestRecommendation(self, isRecommendation: bool) -> bool:
        """_summary_

        Returns:
            List[ILatestRecommendationSummary]: _description_
        """
        try:
            dbConfig = getJsonConfig()
            dbConn = None
            dbCur = None
            # Connect to your PostgreSQL database
            conn = psycopg2.connect(host=dbConfig.db_host, dbname=dbConfig.db_name,
                                    user=dbConfig.db_username, password=dbConfig.db_password)
            # Create a cursor object using the connection
            dbCur = conn.cursor()

            sql_fetch = 'SELECT * FROM "Latest_Recommendation" where "isRecommendation" = {0} order by time_stamp desc'.format(isRecommendation)

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

        
        latestRecommendationList: List[ILatestRecommendationSummary] = []
        for i in data.index:
            latestRecommendation: ILatestRecommendationSummary = {
                'time_stamp': dt.datetime.strftime(data['time_stamp'][i], "%Y-%m-%d %X"),
                'substation_name': data['substation_name'][i],
                'recommendation': data['recommendation'][i],
                'voltage_str': data['voltage_str'][i]
            }
            latestRecommendationList.append(latestRecommendation)
        return latestRecommendationList