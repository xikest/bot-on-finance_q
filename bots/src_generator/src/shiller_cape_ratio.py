from datetime import datetime
import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from tools.qndl.qndl import Qndl

# def DatetimeToDate(idx: datetime.timestamp) -> datetime.date:
#   return idx.date()
def prepare_dataset(qndlKeys: list = ['SHILLER_PE_RATIO_MONTH'], periods=10) -> pd.DataFrame:
    qndl = Qndl()
    df = qndl.getData('MULTPL', qndlKeys, periods) \
        .ffill().resample('MS').last()
    return df
def get_annot(ds:pd.Series, pos:str="recent") -> tuple:
    if pos == 'min':
        x = ds.index[ds.argmin()]
    elif pos == 'max':
        x = ds.index[ds.argmax()]
    elif pos == 'recent':
        x = ds.sort_index().index[-1]
    elif pos == 'first':
        x = ds.sort_index().index[0]
    y = ds[x]
    if isinstance(x, datetime):
        x_pos = x.strftime('%Y-%m')
    else:
        x_pos = x
    txtPos = f'({x_pos}, {y})'
    return {"x":x,"y":y, "text":txtPos}

class ShillerRatio:
    """
    srp = ShillerRatio()
    srp.plot("SHILLER_PE_RATIO_MONTH", modeBinary:bool = False)
    srp.plot("SP500_DIV_YIELD_MONTH", modeBinary:bool = False)
    srp.plot("SP500_EARNINGS_YIELD_MONTH", modeBinary:bool = False)
    srp.plot("SP500_REAL_PRICE_MONTH", modeBinary:bool = False)
    srp.plot("SP500_PE_RATIO_MONTH", modeBinary:bool = False)
    """
    def __init__(self, modeBinary=True):

        pio.templates.default = 'plotly_white'
        self.dictQndlKeysMultpl = {'SHILLER_PE_RATIO_MONTH': 'Shiller PE Ratio by Month',
                              'SP500_DIV_YIELD_MONTH': 'S&P 500 Dividend Yield by Month',
                              'SP500_EARNINGS_YIELD_MONTH': 'S&P 500 Earnings Yield by Month',
                              'SP500_REAL_PRICE_MONTH': 'S&P 500 Real Price by Month',
                              'SP500_PE_RATIO_MONTH': 'S&P 500 PE Ratio by Month'}
        self.modeBinary = modeBinary
        self.df = prepare_dataset(list(self.dictQndlKeysMultpl))
        pass



    def shillerPlots(self):
        yield from [plot( self.df.loc[:, dataKey], self.dictQndlKeysMultpl.get(dataKey), self.modeBinary) for dataKey in self.dictQndlKeysMultpl.keys()]



def plot(ds1:pd.Series, title:str=None, modeBinary:bool = False):
    fig = make_subplots()  # 그래프 준비
    fig.add_trace(
        go.Scatter(x = ds1.index, y = ds1, mode = 'lines', marker = dict(size = 10), name=title))
    fig.add_annotation(get_annot(ds = ds1, pos ='recent'), showarrow=False, arrowhead=1)\
        .add_annotation(get_annot(ds = ds1, pos ='max'),showarrow=False, arrowhead=1)\
        .add_annotation(get_annot(ds = ds1, pos ='min'),showarrow=False, arrowhead=1) # 화살표 헤드 표시: arrowhead=1
    if title == 'Shiller PE Ratio by Month': #CAPE 범위 표시
        fig.add_hline(y=26, annotation_text='CAPE:26',  annotation_position= 'bottom left', annotation_font_color='gray')
        fig.add_hline(y=32, annotation_text='CAPE:32', annotation_position='bottom left', annotation_font_color='gray')
    fig.update_layout(title=f'{title}', width=500, height=700)
    if modeBinary:
        return fig.to_image(format="png", scale=2)
    return fig.show()

