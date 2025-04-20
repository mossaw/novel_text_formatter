# 改行処理を行うモジュール
# 「」や（）の前後で改行を入れ、会話と地の文の区切りに応じて空行を追加する

import re

def is_dialogue_line(line):
    # 行が会話文（「または（で始まる）かどうかを判定
    return bool(re.match(r'^\s*[「（]', line))

def process_text(text):
    """改行処理"""
    lines = text.split('\n')
    result = []
    prev_type = None  # 前の行の種類を記録（dialogue/narration）

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue

        # 「や（の前後に改行を挿入
        line = re.sub(r'(?=[「（])', '\n', line)
        line = re.sub(r'(?<=[」）])', '\n', line)

        # 改行で分割した行をさらに処理
        sublines = line.split('\n')
        for subline in sublines:
            subline = subline.strip()
            if not subline:
                continue

            # 会話文か地の文か判定
            current_type = "dialogue" if is_dialogue_line(subline) else "narration"

            # 切り替わるときに空行を入れる（会話→地の文 or 地の文→会話）
            if current_type == "dialogue":
                if prev_type != "dialogue":
                    result.append("")
                result.append(subline)
            else:
                if prev_type == "dialogue":
                    result.append("")
                result.append(subline)

            prev_type = current_type

    return '\n'.join(result)
