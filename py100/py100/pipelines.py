# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class Py100Pipeline(object):
    def process_item(self, item, spider):
        """
                :param item: 填充了相应元素类实体
                :param spider:
                :return:
                """

        # 获取当前工作目录
        base_dir = os.getcwd()
        # 文件存在data目录下的weather.txt文件内
        filename = base_dir + '/problems.txt'

        # 以追加的方式打开文件，并写入对应的数据
        with open(filename, 'a') as f:
            f.write(str(item['problem']) + '\n')
        return item
