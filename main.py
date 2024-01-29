import zenn_api
import notion_api
import config

ZENN_SESSION = config.ZENN_SESSION
REMEMBER_TOKEN = config.REMEMBER_TOKEN
NOTION_DATABASE_ID = config.NOTION_DATABASE_ID
NOTION_API_KEY = config.NOTION_API_KEY

cookie = f"_zenn_session={ZENN_SESSION}; remember_user_token={REMEMBER_TOKEN}"

old_likes_urls = notion_api.fetch_article_urls(NOTION_DATABASE_ID, NOTION_API_KEY)
print(f"Found {len(old_likes_urls)} articles in Notion database.")

new_likes = zenn_api.fetch_likes(cookie, old_likes_urls)
print(f"Found {len(new_likes)} new articles in Zenn likes.")

print("Inserting articles to Notion database...")
for i, article in enumerate(new_likes):
    print(f"Inserting article {i+1}...")
    notion_api.insert_article(NOTION_DATABASE_ID, article, NOTION_API_KEY, article.get("emoji"))
