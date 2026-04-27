"""マッチングアプリコンパス - ブログ固有設定"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_NAME = "マッチングアプリコンパス"
BLOG_DESCRIPTION = "マッチングアプリの徹底比較とプロフィール・メッセージ術の実践ガイド。Pairs・with・タップル・Omiai・ペアフルなど主要アプリを年代別・目的別に解説。"
BLOG_URL = "https://musclelove-777.github.io/matching-compass/"
BLOG_LANGUAGE = "ja"
GITHUB_REPO = "MuscleLove-777/matching-compass"

TARGET_CATEGORIES = [
    "マッチングアプリ比較",
    "プロフィール作成術",
    "メッセージ・会話術",
    "初デート攻略",
    "婚活・恋活戦略",
    "年代別マッチング",
    "アプリ別攻略法",
    "トラブル・安全対策",
]

THEME = {
    "primary": "#ec7c8a",
    "accent": "#9b59b6",
    "gradient_start": "#ec7c8a",
    "gradient_end": "#9b59b6",
}

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_FALLBACK_MODEL = "gemini-2.5-flash-lite"

OUTPUT_DIR = BASE_DIR / "output"
ARTICLES_DIR = OUTPUT_DIR / "articles"
SITE_DIR = OUTPUT_DIR / "site"
TOPICS_DIR = OUTPUT_DIR / "topics"

MAX_ARTICLE_LENGTH = 4000
SEO_KEYWORD_DENSITY = 0.02
