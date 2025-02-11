import streamlit as st
from utils.data_handler import save_data, load_data

st.title("1️⃣ First App")

# Load existing data
data = load_data()
who_placeholder = data.get("who", "")
why_placeholder = data.get("why", "")
what_placeholder = data.get("what", "")

who = st.text_input(label="私は、", placeholder="あなたの呼び名", value=who_placeholder)

why = st.text_input(label="なぜ、夢を叶える？", placeholder="夢を叶えて、どうしますか？", value=why_placeholder)

st.markdown("""
        夢を叶えるための道筋は遠く、険しいものです。  
        その夢を叶えれば、あなたは幸せになれますか？  
        その夢は、本当に**あなたが**叶える必要がありますか？  
        他人の夢よりも、優先されるべきものですか？  
        あなたに夢が無いのなら、それでもいいのです。  
        それでも、どうしても、叶えたい夢があるのなら、  
          
        **Yumelit**は、その夢を叶えます。  
""")

what = st.text_input(label="あなたの夢は？", placeholder="一文で、簡潔に", value=what_placeholder)

if st.button("保存"):
    if why and what:
        data = {"who": who, "why": why, "what": what}
        save_data(data)
        st.success("データが保存されました！")
    else:
        st.warning("すべてのフィールドを入力してください。")

st.text("次のAppに進んでください。")

st.divider()

st.code("""
        僕は夢を叶えることがあまりにも大事すぎて
        叶えられないことが怖くて何もできなかった

        叶わなければ夢じゃないと思ってて壊れたら終わりだと思ってた
        諦めなければ夢は終わらないのに
""")
st.caption("SEKAI NO OWARI – yume")

st.code("""
        夢なき者に理想なし、
        理想なき者に計画なし、
        計画なき者に実行なし、
        実行なき者に成功なし。
        故に、夢なき者に成功なし。
""")
st.caption("吉田松陰 – 出典不明")

st.code("""
        千里の道も一歩から
        石の上にも三年
        雨垂れ石を穿つ
        塵も積もれば山となる
""")
st.caption("日本のことわざ")
