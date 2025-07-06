# 有望人材レコメンドシステム (Talent Recommendation System)

AIシステム開発の講義課題として作成した、有望な人材を推薦するシステムのプロトタイプです。

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://talent-recommender-app-b4pp7zcehzgh44rdmbzmdl.streamlit.app/)

## 概要

このプロジェクトは、松尾・岩澤研究室の採用課題を想定し、特定の要件にマッチする優秀な人材を効率的に発見することを目的としています。ウェブサイトやSNS、学術データベース(ResearchMapなど)から得られる情報を基に、まだアプローチできていない有望な人材を特定する技術の開発を目指します。

このリポジトリには、まず最小限の機能を持つMVP（Minimum Viable Product）として開発したバージョンが含まれています。

## ✨ 主な機能 (MVP)

- **要件入力**: 人材要件（求人票など）をテキストで入力できます。
- **キーワードマッチング**: 入力された要件からキーワードを抽出し、候補者のプロフィールと照合してマッチ度をスコアリングします 。
- **候補者リスト表示**: マッチ度が高い順に候補者のリスト、プロフィール概要、マッチしたキーワードなどを表示します。

## 🛠️ 使用技術

- **言語**: Python
- **フレームワーク**: Streamlit
- **ライブラリ**: Pandas

## 🚀 使い方（ローカル環境での実行）

1.  このリポジトリをクローンまたはダウンロードします。
    ```bash
    git clone [https://github.com/nicejp/talent-recommender-app.git](https://github.com/nicejp/talent-recommender-app.git)
    cd talent-recommender-app
    ```
2.  必要なライブラリをインストールします。
    ```bash
    pip install -r requirements.txt
    ```
3.  Streamlitアプリケーションを実行します。
    ```bash
    streamlit run app.py
    ```
4.  ブラウザで `http://localhost:8501` が開かれ、アプリケーションが表示されます。

## 今後の展望 (Next Steps)

このMVPを基に、さらに高機能なシステムを目指します。

- **マッチング精度の向上** 
  - 単純なキーワードマッチングから、BERTなどの事前学習済み言語モデルを用いたセマンティック検索（意味に基づいた検索）へ移行する 。
- **「有望度」スコアの高度化** 
  - 論文数、被引用数、学会発表歴、GitHubでの活動などを指標に加え、より多角的なスコアリングモデルを設計する 。
- **人材ネットワークの可視化** 
  - 論文の共著者関係などを抽出し、グラフデータベース(Neo4jなど)に格納 。
  - D3.jsなどを用いて、人材同士や松尾研究室との繋がりをインタラクティブに可視化する 。
- **アプローチ戦略の立案支援** 
  - 大規模言語モデル（LLM）を活用し、候補者の興味関心に合わせたスカウトメールのドラフトを自動生成する機能を追加する 。

---
