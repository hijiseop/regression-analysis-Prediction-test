import pandas as pd
import matplotlib
from fbprophet import Prophet


class PreProcess :
    
    def csvFileRead (self,locateCSV) :
        df = pd.read_csv(locateCSV)
        df = df.rename(columns={'Date': 'ds', 'Close': 'y'})
        df.head
        

        m = Prophet(changepoint_prior_scale=0.3)
        m.fit(df)

        future = m.make_future_dataframe(periods=30)
        future.tail()

        forecast = m.predict(future)
        forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
        fig1 = m.plot(forecast)
        return fig1






    
