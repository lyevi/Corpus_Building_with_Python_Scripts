import os
import pythoncom
from win32com import client as win32
from docx import Document


def convert_doc_to_txt(input_folder, output_folder):
    # 创建目标文件夹（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 初始化 Word 应用程序实例
    pythoncom.CoInitialize()  # 初始化 COM
    word = win32.Dispatch("Word.Application")
    word.Visible = False  # 隐藏 Word 应用

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(input_folder):
        # 检查是否为 .doc 文件
        if filename.lower().endswith('.doc') and not filename.lower().endswith('.docx'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

            try:
                # 使用 win32com.client 读取 .doc 文件并保存为 .txt
                doc = word.Documents.Open(input_path)
                doc.SaveAs(output_path, FileFormat=2)  # FileFormat=2 表示保存为纯文本格式
                doc.Close()
                print(f"Converted {filename} to {output_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

        # 处理 .docx 文件
        elif filename.lower().endswith('.docx'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.txt")

            try:
                # 使用 python-docx 读取 .docx 文件
                doc = Document(input_path)
                with open(output_path, "w", encoding="utf-8") as txt_file:
                    for para in doc.paragraphs:
                        txt_file.write(para.text + "\n")
                print(f"Converted {filename} to {output_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

    # 关闭 Word 应用程序实例
    word.Quit()
    pythoncom.CoUninitialize()


# 定义源文件夹和目标文件夹路径
input_folder = r'C:\Users\luziy\Desktop\source_docs'  # 替换为您的 source_docs 文件夹路径
output_folder = r'C:\Users\luziy\Desktop\output_txts'  # 替换为您的 output_txts 文件夹路径

# 运行转换函数
convert_doc_to_txt(input_folder, output_folder)

