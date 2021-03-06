import streamlit as st
import time 


st.title('Streamlit 超入門')


st.write('プログレスバーの表示')

'start!!!'

latest_iteration = st.empty()

bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!!!!!!!!!!!!!'


left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ1')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ2')
expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ3')

# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味：',text
# 'コンディション:',condition

#if st.checkbox('show Image'):
##    st.image(img,caption='car',use_column_width=True)

#option = st.selectbox(
#    'あなたが好きな数字を教えてください。',
#    list(range(1,11))
#)


#'あなたの好きな数字は、',option,'です。'

#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50] + [35.69,139.70],
#    columns = ['lat','lon']
#)
# st.map(df)
#st.table(df.style.highlight_max(axis=0))


"""
# 章
## 節
### 項


```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""