import tkinter as tk
from tkinter import filedialog, messagebox
import os
from datetime import datetime
from text_format_linebreak import process_text
from text_format_spacing import apply_space_rules
from preprocess_cleaner import preprocess_text

class TextFormatterApp:
    def __init__(self, root):
        self.root = root
        self.file_path = ""
        self.temp_text = ""
        self.temp_path = ""

        # ウィンドウサイズを指定
        self.root.geometry("360x300")
        self.root.title("小説用テキスト加工ツール")

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="テキストファイルを選択してください")
        self.label.pack(pady=10)

        self.select_button = tk.Button(self.root, text="ファイルを選択", command=self.select_file)
        self.select_button.pack(pady=5)

        self.preprocess_button = tk.Button(self.root, text="① 改行・スペース全削除", command=self.apply_preprocess, state=tk.DISABLED)
        self.preprocess_button.pack(pady=5)

        self.linebreak_button = tk.Button(self.root, text="② 改行処理", command=self.apply_linebreak, state=tk.DISABLED)
        self.linebreak_button.pack(pady=5)

        self.spacing_button = tk.Button(self.root, text="③ スペース処理", command=self.apply_spacing, state=tk.DISABLED)
        self.spacing_button.pack(pady=5)

        self.reset_button = tk.Button(self.root, text="④ 元ファイルに戻す", command=self.reset_temp, state=tk.DISABLED)
        self.reset_button.pack(pady=5)

        self.finish_button = tk.Button(self.root, text="完了して出力", command=self.finish_output, state=tk.DISABLED)
        self.finish_button.pack(pady=10)

    def select_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if path:
            self.file_path = path
            self.temp_path = os.path.join(os.path.dirname(path), "temp.txt")
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.temp_text = f.read()
            self.write_temp_file()
            self.label.config(text=f"選択中: {os.path.basename(path)}")
            self.enable_buttons()

    def enable_buttons(self):
        self.linebreak_button.config(state=tk.NORMAL)
        self.spacing_button.config(state=tk.NORMAL)
        self.preprocess_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)
        self.finish_button.config(state=tk.NORMAL)

    def write_temp_file(self):
        if self.temp_path:
            with open(self.temp_path, 'w', encoding='utf-8') as f:
                f.write(self.temp_text)

    def apply_linebreak(self):
        self.temp_text = process_text(self.temp_text)
        self.write_temp_file()
        messagebox.showinfo("成功", "改行処理を適用しました！")

    def apply_spacing(self):
        self.temp_text = apply_space_rules(self.temp_text)
        self.write_temp_file()
        messagebox.showinfo("成功", "スペース処理を適用しました！")

    def apply_preprocess(self):
        self.temp_text = preprocess_text(self.temp_text)
        self.write_temp_file()
        messagebox.showinfo("成功", "改行とスペースを全削除しました！")

    def reset_temp(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.temp_text = f.read()
        self.write_temp_file()
        messagebox.showinfo("リセット", "元のファイル内容に戻しました")

    def finish_output(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = self.file_path.replace(".txt", f"_{timestamp}.txt")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(self.temp_text)
        messagebox.showinfo("完了", f"ファイルを出力しました:\n{output_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextFormatterApp(root)
    root.mainloop()
