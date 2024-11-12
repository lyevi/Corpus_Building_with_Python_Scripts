import os
import re


def rename_doc_files(directory):
    # 遍历指定目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否为 .doc 或 .docx 文件
        if filename.lower().endswith(('.doc', '.docx')):
            # 将文件名转换为小写
            lowercase_name = filename.lower()

            # 使用正则表达式提取 "guiding case no. xxx" 的编号
            match = re.search(r'guiding case no\. ?(\d+)', lowercase_name)
            if match:
                # 获取案件编号
                case_no = match.group(1)

                # 生成新的文件名
                new_filename = f"guiding_case_no_{case_no}_en.docx" if lowercase_name.endswith(
                    '.docx') else f"guiding_case_no_{case_no}_en.doc"

                # 获取文件的完整路径
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)

                # 重命名文件
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
            else:
                print(f"No guiding case number found in: {filename}")


# 使用方法：将 'your_directory_path' 替换为包含 .doc 文件的实际目录路径
directory_path = r'C:\Users\luziy\Desktop\source_docs'  # 替换成实际目录路径
rename_doc_files(directory_path)
