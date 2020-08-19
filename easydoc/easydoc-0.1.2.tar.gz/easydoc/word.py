#!/usr/bin/env python
# coding: utf-8
# author: Frank YCJ
# email: 1320259466@qq.com
# date: $ $
# desc:
import base64
import os
import shutil
import uuid

from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage, RichText


class EasyWord:
    def __init__(self, template_file_path):
        doc_t = DocxTemplate(template_file_path)
        self.doc_t = doc_t

    def export_data_to_word(self, save_file_path, context_data_list=[], word_template_data_alias='data_list'):
        self.doc_t.render({word_template_data_alias: context_data_list})
        self.doc_t.save(save_file_path)
        self.doc_t.render(context_data_list)
        self.doc_t.save(save_file_path)
        return word_template_data_alias

    def picture_format(self, picture_file_path, width=100, height=60):
        return InlineImage(self.doc_t, picture_file_path, width=Mm(width), height=Mm(height))

    def base64_t0_picture(self, save_file_dir, data):
        img_data = base64.b64decode(data)

        if not os.path.exists(save_file_dir):
            os.makedirs(save_file_dir)
        # uuid随机生成的不重复字符串
        img_path = save_file_dir + str(uuid.uuid4()) + '.png'
        with open(img_path, 'wb') as f:
            f.write(img_data)
        return img_path

    def empty_dir(self, dir_path):
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
        os.makedirs(dir_path)
        return dir_path

    def delete_dir(self, dir_path):
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

    def format_links(self, links_list, add_index=False, indexs_list=None):
        related_links = []
        links_size = len(links_list)
        for index in range(links_size):
            if not links_list[index]:
                continue
            link=None
            if add_index:
                if indexs_list:
                    link = RichText('[%s] ' % indexs_list[index])
                else:
                    link = RichText('[%s] ' % index)
            else:
                link=RichText()

            link.add(links_list[index], color='#255FA6', underline=True,
                     url_id=self.doc_t.build_url_id(links_list[index]))

            related_links.append(link)
        return related_links
