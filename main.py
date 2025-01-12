import streamlit as st

from utils import generate_xiaohongshu

st.header("爆款小紅書寫作助手")

with st.sidebar:
    openai_api_key = st.text_input("enter your OpenAI API", type="password")
    st.markdown("[get OpenAI API](https://openai.com/index/openai-api/)")

theme = st.text_input("主題")
submit = st.button("start writing")

if submit and not openai_api_key:
    st.info("enter your openai api")
    st.stop()
if submit and not theme:
    st.info("enter the theme")
    st.stop()
if submit:
    with st.spinner("ai is thinking..."):
        result, search_result = generate_xiaohongshu(theme, openai_api_key)
    st.divider()
    left_columns, right_columns = st.columns(2)
    with left_columns:
        st.markdown("##### 小紅書標題1: ")
        st.write(result.title[0])
        st.markdown("##### 小紅書標題2: ")
        st.write(result.title[1])
        st.markdown("##### 小紅書標題3: ")
        st.write(result.title[2])
        st.markdown("##### 小紅書標題4: ")
        st.write(result.title[3])
        st.markdown("##### 小紅書標題5: ")
        st.write(result.title[4])
    with right_columns:
        st.markdown("##### 小紅書正文: ")
        st.write(result.content)
    with st.expander("Wikipedia search result: "):
        st.info(search_result)