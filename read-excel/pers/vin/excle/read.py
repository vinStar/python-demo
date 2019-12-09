#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd

workbook = xlrd.open_workbook(u'../../../aa.xlsx')


def read_excel():
    sheet_names = workbook.sheet_names()

    for sheet_name in sheet_names:

        sheet2 = workbook.sheet_by_name(sheet_name)
        # for index in range(len(sheet2)):
        #     print
        #     '当前水果 :', sheet2.row_values(index)

        cols = sheet2.col_values(0)
        len_list = len(cols)
        print(cols[1:len_list])
        for index in range(len(cols)):
            if (index == 0):
                continue
            else:
                print(cols[index])

        # 　　 print sheet_name rows = sheet2.row_values(i) # 获取第四行内容


#
# 　　 cols = sheet2.col_values(1) # 获取第二列内容
#
# 　　 print rows
#
# 　　 print cols


# print("Good bye!");

if __name__ == "__main__":
    print("main")
    read_excel()
