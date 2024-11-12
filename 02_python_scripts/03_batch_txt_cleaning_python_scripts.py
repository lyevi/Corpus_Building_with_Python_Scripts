import os
import re
import chardet


def clean_text(text):
    # 1.删除所有空行
    text = re.sub(r"\n\s*\n", "\n", text)

    # 2. 删除文本的第一行（如果它以 "Guiding Case No." 开头）
    text = re.sub(r"^Guiding Case No\..*?\n", "", text, flags=re.IGNORECASE)

    # 3. 删除特定信息，包括版权声明、Pkulaw Express、链接、页码和保存日期的整行内容
    text = re.sub(
        r"^(.*\(c\)Pkulaw.*\n)|"  # 匹配包含 (c)Pkulaw 的版权声明整行
        r"^(.*Pkulaw Express.*\n)|"  # 匹配包含 Pkulaw Express 信息的整行
        r"^(.*Scan QR Code.*\n)|"  # 匹配包含 QR 代码提示的整行
        r"^(.*Original Link:.*\n)|"  # 匹配包含 Original Link 链接的整行
        r"^(.*\[CLI Code\].*\n)|"  # 匹配包含 CLI Code 的整行
        r"^\d+/\d+\n|"  # 匹配页码行，例如 "1/2"
        r"^Saved on: \d{2}/\d{2}/\d{4}\n?",  # 匹配保存时间行
        "",
        text,
        flags=re.IGNORECASE | re.MULTILINE
    )

    # 4. 删除段落之间的回车符，使文本成为一个连续的段落
    text = re.sub(r"\n+", " ", text)

    # 5. 删除单词和标点符号周围多余的空格
    # 删除标点符号前的空格
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)

    # 删除标点符号后的多余空格，确保句子之间只有一个空格
    text = re.sub(r"([.,!?;:])\s+", r"\1 ", text)

    # 删除多余的空格，确保单词之间只保留一个空格
    text = re.sub(r"\s{2,}", " ", text)

    # 移除开头和结尾的空格
    text = text.strip()

    return text


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']


def process_files(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)  # 创建目标文件夹（如果不存在）

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):  # 仅处理 .txt 文件
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # 检测文件编码
            encoding = detect_encoding(input_path)
            print(f"Detected encoding for {filename}: {encoding}")

            with open(input_path, "r", encoding=encoding) as file:
                text = file.read()

            # 清洗文本
            cleaned_text = clean_text(text)

            # 保存清洗后的文本
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(cleaned_text)

            print(f"Processed {filename}")


# 指定源文件夹和输出文件夹路径
input_folder = r"C:\Users\luziy\Desktop\output_txts"  # 替换为实际的源文件夹路径
output_folder = r"C:\Users\luziy\Desktop\output_cleaned_1"  # 替换为实际的输出文件夹路径

# 执行文件清洗
process_files(input_folder, output_folder)
