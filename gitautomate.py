from datetime import datetime
with open('streak.txt','w+') as f:
    f.write(str(datetime.now()))