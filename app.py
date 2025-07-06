# app.py
import streamlit as st
from data import get_researchers
from matcher import find_candidates

# --- Streamlit UI設定 ---
st.set_page_config(page_title="有望人材レコメンドシステム (MVP)", layout="wide")

st.title("有望人材レコメンドシステム (MVP版)")
st.write("""
このシステムは、AIシステム開発の講義課題の要求に基づき作成された最小実行可能製品（MVP）です。 
左側のテキストエリアに人材要件（求人情報など）を貼り付け、「マッチング開始」ボタンを押してください。
""")

# --- サンプルデータ読み込み ---
# 本来はデータベースやAPIから取得 
researchers_data = get_researchers()

# --- サイドバーに入力UIを配置 ---
st.sidebar.header("人材要件入力")
# PDFからLLM開発エンジニアの募集要項をデフォルト値として設定
job_description_input = st.sidebar.text_area(
    "こちらに求人情報などを貼り付けてください。",
    """
【職務内容】
大規模言語モデル (LLM) の実用化が加速すると同時に、その本質的な理解や社会実装する上でのリスクを制御する手法など、行うべき重要な研究開発テーマは増加しています。松尾研は、これまでLLMに関する主要な研究を精力的に行い、100億パラメータサイズのLLMの開発、経産省及びNEDOが進める日本国内の生成AI基盤モデル開発を推進する 「GENIAC」プロジェクトにおいて、「Tanuki-8×8B」の開発などを行ってきました。
[1] LLMのフルスクラッチ構築、継続学習 (1B~1000B)
[2] LLMの社会的リスクに関する研究開発 (Bias, Halucination)
[3] 外部知識や外部ツールとの融合(LLM Agent)

【必須スキル】
・修士以上の学位を有する方
・生成系の言語モデルに関する、データ加工、モデル学習、評価の一連のサイクルを実施した経験
・日本語でのコミュニケーション及び文章作成能力、英語での文章読解能力

【歓迎スキル】
・医療/製薬領域への知見
・開発チームをリードした経験
・マルチノードマルチGPUでのニューラルネットの学習経験 (Deep SpeedやMegatron LM)
    """,
    height=400
)

if st.sidebar.button("マッチング開始"):
    if job_description_input:
        with st.spinner("候補者を検索中..."):
            # --- マッチング実行 ---
            candidates, extracted_keywords = find_candidates(job_description_input, researchers_data)

            st.header("マッチング結果")

            if candidates:
                st.success(f"{len(candidates)}名の候補者が見つかりました。")

                # --- 結果表示 ---
                for candidate in candidates:
                    with st.expander(f"**{candidate['name']}** -  スコア: {candidate['score']}"):
                        st.markdown(f"**所属:** {candidate['affiliation']}")
                        st.markdown(f"**URL:** [{candidate['url']}]({candidate['url']})")
                        st.markdown(f"**マッチしたキーワード:** `{', '.join(candidate['matched_keywords'])}`")
                        st.markdown("**プロフィール概要:**")
                        st.text_area("profile", candidate['profile_text'], height=150, disabled=True, key=candidate['name'])
            else:
                st.warning("条件にマッチする候補者が見つかりませんでした。")

            st.subheader("抽出されたキーワード（参考）")
            st.info(f"{', '.join(extracted_keywords)}")

    else:
        st.sidebar.error("人材要件を入力してください。")