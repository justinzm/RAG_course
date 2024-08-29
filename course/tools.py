#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/6/21 下午2:26
# @Author : justin.郑 3907721@qq.com
# @File : DocumentLoaders.py
# @desc : 工具类


def replace_t_with_space(list_of_documents):
    """
    将每个文档页面内容中的所有制表符('\t')替换为空格。
    """
    for doc in list_of_documents:
        doc.page_content = doc.page_content.replace('\t', ' ')
    return list_of_documents


def show_context(context):
    """
    显示所提供的上下文列表的内容。

    Args:
        context (list):要显示的上下文项列表。

    打印列表中的每个上下文项，并使用指示其位置的标题。
    """
    for i, c in enumerate(context):
        print(f"Context {i+1}:")
        print(c)
        print("\n")