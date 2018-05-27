# -*- coding: utf-8 -*-
# 다음은 주식알고리즘 전문회사 사이트이다
# 상장 주식들의 코드를 제공한다.
# http://bigdata-trader.com/itemcodehelp.jsp

# Install해야 할 package들
#   : pip install lxml
#   : pip install html5lib
#   : pip install beautifulsoup4

import os
import numpy as np
import html5lib
import pandas as pd

if float(pd.__version__[0:3]) >= 0.2:
    # Need to install  "pip3 install pandas_datareader"
    import pandas_datareader.data as pdr
else:
    import pandas.io.data as pdr

code_df = pd.read_html('http://bigdata-trader.com/itemcodehelp.jsp', header=0)[0]

code_df = code_df.rename(columns={'종목코드': 'Code', '종목명': 'Name', '종류': 'Market'})
code_df = code_df[['Code', 'Name', 'Market']]

# 종목코드가 6자리이기 때문에 6자리를 맞춰주기 위해 설정해줌
#code_df.Code = code_df.Code.map('{:06d}'.format)

savepath = os.getcwd() + '/korea_all_stock_code.csv'
code_df.to_csv(savepath, sep=',', index=False)


