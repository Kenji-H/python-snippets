# -*- coding: utf-8 -*

from progressbar import ProgressBar, Percentage, Bar
import time

#----------------------------------------------------------------------------------------
# シンプルなステータスバー
#----------------------------------------------------------------------------------------
def MyTask():
    time.sleep(0.01)

pbar = ProgressBar(widgets=["MyTask:", Percentage(), Bar()], maxval=3000).start()
for i in range(3000):
    MyTask()
    pbar.update(i)
pbar.finish()


