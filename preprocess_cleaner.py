# テキスト前処理：全ての改行とスペース（半角・全角）を削除する

def preprocess_text(text):
    """
    テキストの前処理：
    ・全ての改行（\n）を削除
    ・全角/半角スペースをすべて削除
    """
    text = text.replace('\n', '')           # 改行を除去
    text = text.replace(' ', '').replace('　', '')  # スペース全削除
    return text
