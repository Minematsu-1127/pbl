pip install bert-extractive-summarizer

import streamlit as st
from summarizer import Summarizer

def main():
    st.title("Text Summarizer App")

    # テキスト入力
    input_text = st.text_area("入力テキストを入力してください", "")

    # 要約ボタンがクリックされたときの処理
    if st.button("要約する"):
        # BERT Extractive Summarizerを使用した要約
        model = Summarizer()
        summary = model(input_text, min_length=30, max_length=100)

        # 要約結果の表示
        st.subheader("要約結果")
        st.write(summary)

if __name__ == "__main__":
    main()

