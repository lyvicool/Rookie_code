from pandas import *

# 根据path读取Excel文件，并赋值给变量Excel(此时的Excel是个元素为字典的列表)
Excel = read_excel('e:\\Users\\lxy41\\Desktop\\Test\\test.xlsx')
# print(Excel)

# Excel['header'] Excel的key是header；对应的value是该表头下的列表
# 不知道原理，但是从结果来看
# Excel['header'] == "a",相当于将header下的列表根据条件输出True和Fasle
TrueLst1 = Excel['Column1'] == "a"
TrueLst2 = Excel['Column1'] == "g"

NewExcel = Excel[TrueLst1 | TrueLst2]

# print(NewExcel)
# 根据path创建一个可以被写入的空白Excel，并赋值给变量writer
EW = ExcelWriter('e:\\Users\\lxy41\\Desktop\\Test\\test.xlsx',engine = 'openpyxl', mode = 'a')
# 当你选择mdoe = 'a'，则只能是在已有的列表中进行写入

NewExcel.to_excel(EW, sheet_name='应用平台领域常驻内存',index=False)

EW._save()

resident_memory = read_excel(EW)
sum_memory = resident_memory['Column2'].sum()

print(sum_memory)
# #使用了pd的两个函数（read_excel/ExcelWriter/to_excel）

