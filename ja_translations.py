#!/usr/bin/env python3
"""Japanese translations for breed pages - fixes for remaining English phrases."""

# Best For translations (English → Japanese)
BEST_FOR = {
    # English phrases that slipped through
    "Those who appreciate independence": "独立心を尊重できる方",
    "Experienced dog owners": "経験豊富な犬の飼い主",
    "families with children": "子供のいる家庭",
    "active people": "アクティブな人",
    "first-time owners": "初めての飼い主",
    "apartment living": "マンション住まい",
    "Active families": "活発な家族",
    "Experienced owners": "経験豊富な飼い主",
    "Families": "家族",
    "Seniors": "高齢者",
    "Singles": "独身者",
    "Hunters": "狩猟愛好家",
    "Allergy sufferers": "アレルギー体質の人",
}

# Not Ideal For translations (English → Japanese)
NOT_IDEAL = {
    # English phrases that slipped through
    "Multi-dog households": "多頭飼いの家庭",
    "Off-leash enthusiasts": "ノーリードを好む方",
    "Active families": "活発な家族",
    "Homes with rough children": "荒っぽい子供のいる家庭",
    "First-time owners": "初めての飼い主",
    "Apartment dwellers": "マンション住まい",
    "Hot climates": "暑い気候",
    "Cold climates": "寒い気候",
    "Allergy sufferers": "アレルギー体質の方",
}

# Temperament tags translations (English → Japanese)
TEMPERAMENT_TAGS = {
    # English words that need translation
    "attentive": "注意深い",
    "cat-like": "猫のような",
    "loyal": "忠実",
    "intelligent": "賢い",
    "friendly": "フレンドリー",
    "playful": "遊び好き",
    "alert": "警戒心",
    "confident": "自信のある",
    "independent": "独立心",
    "affectionate": "愛情深い",
    "gentle": "優しい",
    "brave": "勇敢な",
    "calm": "穏やか",
    "energetic": "元気",
    "protective": "保護的",
    "reserved": "控えめ",
    "stubborn": "頑固",
    "trainable": "訓練しやすい",
    "devoted": "献身的",
    "dignified": "威厳のある",
}

if __name__ == "__main__":
    print(f"Best For: {len(BEST_FOR)} translations")
    print(f"Not Ideal: {len(NOT_IDEAL)} translations")
    print(f"Temperament Tags: {len(TEMPERAMENT_TAGS)} translations")
