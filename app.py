import streamlit as st
import xml.etree.ElementTree as ET
import re

st.title("person要素の抽出ツール（シンプル版）")

uploaded_file = st.file_uploader("XMLファイルをアップロードしてください", type="xml")

keywords_input = st.text_input("検索キーワード（複数ある場合はカンマで区切る）", "")

if uploaded_file and keywords_input:
    content_bytes = uploaded_file.read()
    xml_content = content_bytes.decode("utf-8")

    keywords = [kw.strip() for kw in keywords_input.split(",")]
    results = []

    # <person>タグ単位で分割
    person_blocks = re.findall(r"<person[\s\S]*?</person>", xml_content)

    for block in person_blocks:
        for keyword in keywords:
            if keyword in block:
                results.append(f"\n{block}\n")

    if results:
        st.success(f"{len(results)} 件見つかりました。")
        st.code("\n\n".join(results), language="xml")
    else:
        st.warning("一致するキーワードが見つかりませんでした。")
