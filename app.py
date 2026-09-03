import streamlit as st

st.title("🧑‍🤝‍🧑 好友检测器")

with st.form("detector"):
    my_name     = st.text_input("你的姓名")
    friend_name = st.text_input("好友姓名")
    my_birth    = st.text_input("你的生日")
    friend_birth= st.text_input("好友生日")
    place_ok    = st.radio("还记得初次相遇的地方吗？", ["是", "否"])
    sport_ok    = st.radio("记得好友喜欢什么运动吗？", ["记得", "不记得"])
    submit = st.form_submit_button("开始检测")

if submit:
    if place_ok == "是":
        st.write("✅ 你们是有一定印象的好友")
    else:
        st.write("ℹ️ 看来第一次见面没成为好友")

    if sport_ok == "记得":
        st.success("🎉 你们是知心朋友！")
    else:
        st.info("🙂 你们只是普通朋友")
