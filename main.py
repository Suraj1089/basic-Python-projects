import pandas as pd 


class DigitalMozarts:
    """
        class for DigitalMozarts Assignment
        filePath: path to the csv file
    """
    def __init__(self,filePath):
        self.filePath = filePath 
    
    def readFile(self):
        return pd.read_csv(self.filePath)
    

    def getImpression(self):
        df = self.readFile()
        return df[df['age'] == '30-34']['impressions'].sum()

    
    def getAdIds(self):
        df = self.readFile()
        return df.groupby('campaign_id')['ad_id'].apply(list)
    

    def getClicksBetweenDates(self):
        df = self.readFile()
        df['report_start'] = pd.to_datetime(df['reporting_start'])
        return df[(df['reporting_start'] >= '2017-08-19') & (df['reporting_start'] <= '2017-08-22')]['clicks'].sum()
    

d = DigitalMozarts(r"C:\Users\Suraj\Downloads\data.csv")
print(d.getImpression())
print(d.getAdIds())
print(d.getClicksBetweenDates())
