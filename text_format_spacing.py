# スペース処理を行うモジュール
# 会話文かどうかに応じて行頭の一字下げや感嘆符後のスペース追加などを行う

import re
from text_format_linebreak import is_dialogue_line

def apply_space_rules(text):
    """スペース処理"""
    lines = text.split('\n')
    result = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            result.append("")
            continue

        is_dialogue = is_dialogue_line(stripped)

        # 地の文かつ「―」以外で始まる場合、一字下げ
        if not is_dialogue and not stripped.startswith("―"):
            line = '　' + stripped
        else:
            line = stripped

        if is_dialogue:
            # 「！」「？」「♡」が連続していない最後の記号の後に全角スペースを追加
            def insert_space(match):
                return match.group() + '　'
            line = re.sub(r'([！？♡]{1,})(?![！？♡])', insert_space, line)

        # 「」や（）の終わり直前のスペースを削除
        line = re.sub(r'\s+(?=[」）])', '', line)
        result.append(line)

    return '\n'.join(result)
