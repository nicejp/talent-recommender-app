# data.py
# 本来はWebスクレイピング等で動的に収集するデータのサンプル
# ResearchMapやJ-GLOBALの情報を想定 

def get_researchers():
    """
    サンプルの研究者データを返す関数
    """
    researchers = [
        {
            "id": 1,
            "name": "山田 太郎 (Taro Yamada)",
            "affiliation": "東都大学 大学院情報理工学系研究科",
            "url": "https://example.com/yamada-taro",
            "profile_text": """
            専門は自然言語処理、特に対話システムと機械翻訳。
            最近は大規模言語モデル(LLM)の継続学習手法に関心を持ち、
            特に医療ドメインへの応用を研究している。
            Pythonでの開発経験が豊富で、Hugging Face Transformersライブラリを多用。
            過去に国際学会での発表経験あり。
            """
        },
        {
            "id": 2,
            "name": "佐藤 花子 (Hanako Sato)",
            "affiliation": "先進技術研究所",
            "url": "https://example.com/sato-hanako",
            "profile_text": """
            強化学習と自律エージェントの研究開発に従事。
            特にマルチエージェントシステムにおける協調行動の学習がテーマ。
            論文多数。最近はLLMをエージェントの思考プロセスに組み込む研究を開始した。
            使用言語はPython, C++。DeepMindの論文の再現実装などを行う。
            """
        },
        {
            "id": 3,
            "name": "鈴木 一郎 (Ichiro Suzuki)",
            "affiliation": "帝都工業大学 理学部",
            "url": "https://example.com/suzuki-ichiro",
            "profile_text": """
            専門はコンピュータビジョン。画像認識、物体検出に関する研究を行う。
            特に、少ないデータセットから効率的に学習するFew-shot learningに関心。
            機械学習の基礎には詳しいが、言語モデルに関する業務経験は少ない。
            """
        },
        {
            "id": 4,
            "name": "田中 真紀 (Maki Tanaka)",
            "affiliation": "西京大学 先端情報学研究室",
            "url": "https://example.com/tanaka-maki",
            "profile_text": """
            松尾研究室の出身。博士課程では、LLMの社会的リスク、特にバイアスと公平性の研究に取り組んでいた。
            日本語の大規模コーパスを整備し、Hugging Face Hubにて公開した経験を持つ。
            分散学習ライブラリであるDeepSpeedを用いたマルチノード・マルチGPUでのモデル学習経験を有する。
            現在はLLMのフルスクラッチ開発プロジェクトをリードしている。
            """
        },
    ]
    return researchers