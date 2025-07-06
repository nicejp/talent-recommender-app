# matcher.py
import re
import pandas as pd

def extract_keywords(job_description):
    """
    求人情報からキーワードを抽出する（簡単版）
    ここでは、大文字小文字を区別せずにアルファベットの単語と日本語の単語を抽出
    """
    # LLM, GPUなどの英単語と日本語の単語を抽出する簡単な正規表現
    words = re.findall(r'[a-zA-Z]+|\w+', job_description.lower())
    # 重複を除き、一般的な単語（ストップワード）を除外する（今回は簡単化のため未実装）
    return list(set(words))

def calculate_match_score(profile_text, keywords):
    """
    プロフィールのテキストとキーワードリストに基づき、マッチスコアを計算する 
    単純なキーワード含有数でスコアを算出
    """
    score = 0
    matched_keywords = []
    for keyword in keywords:
        if keyword.lower() in profile_text.lower():
            score += 1
            matched_keywords.append(keyword)
    return score, matched_keywords


def find_candidates(job_description, researchers):
    """
    求人情報にマッチする候補者を探し、スコア順にソートして返す
    """
    # 1. 求人情報からキーワードを抽出
    keywords = extract_keywords(job_description)

    # 2. 各研究者のプロフィールとキーワードを照合してスコアリング
    results = []
    for researcher in researchers:
        score, matched = calculate_match_score(researcher["profile_text"], keywords)
        if score > 0:
            results.append({
                "name": researcher["name"],
                "affiliation": researcher["affiliation"],
                "url": researcher["url"],
                "score": score,
                "matched_keywords": matched,
                "profile_text": researcher["profile_text"]
            })

    # 3. スコアの高い順に並べ替え
    sorted_results = sorted(results, key=lambda x: x['score'], reverse=True)

    return sorted_results, keywords