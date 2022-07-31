# natural language APIを試す
# https://cloud.google.com/natural-language/docs/setup#windows

import os
from pathlib import Path

# Imports the Google Cloud client library
from google.cloud import language_v1

# 環境変数に秘密鍵のパスを持たせる（とりあえずHOME直下にある）
# いちおうlinuxとwindowsどっちもいけるような書き方になってる（はず）
key_path = Path(os.path.expanduser('~')) / "gcp-service-account-file.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(key_path)

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = "Hello, world!"
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
result = client.analyze_sentiment(
    request={"document": document}
)

print(result.document_sentiment)
