import datetime as dt
from time import strftime
now = dt.datetime.now()
delta = dt.timedelta(minutes= 5)
t = now.time()
print(t)
# 12:39:11.039864

print((dt.datetime.combine(dt.date(1,1,1),t) + delta).time())
# 00:39:11.039864
# ranges=[(now.ti)]
import pandas as pd
range_=pd.date_range(  "13:00" , "14:30", freq="10min").strftime('%H:%M')
data={i:{} for i in range_}
from dataclasses import dataclass
from dataclasses import asdict

@dataclass
class candels:
    open:float
    close:float
    high:float
    low:float

c=candels(100.0,34,3435,232323)
print(asdict(c))