
def get_case_special_field_list():
    """
    【 获 取 excel 用 例 的 指 定 字 段 名 称 】
    01.接口名称：interface_name（ 必填 ）
    02.接口地址：interface_url（ 必填 ）
    03.请求方式：request_method（ 必填 ）
    04.请求头文件：request_header
    05.请求参数：request_params
    06.验证模式：verify_mode（ 必填 ）   < (Excel)float  -> (Mongo)int >
    07.待比较关键字段名列表：compare_core_field_name_list（ 必填 ）< (Excel)string -> (Mongo)list >（以","分割）
    08.期望的关键字段值列表：expect_core_field_value_list（ 必填 ）< (Excel)string -> (Mongo)list >（以","分割）
    09.期望的响应字段列表：expect_field_name_list                 < (Excel)string -> (Mongo)list >（以","分割）
    10.依赖接口名列表：depend_interface_list                    < (Excel)string -> (Mongo)list >（以","分割）
    11.依赖字段名列表：depend_field_name_list                     < (Excel)string -> (Mongo)list >（以","分割）
    12.用例状态：case_status          < (Excel)int|string -> (Mongo)bool >

    < 以下字段不显示在导入Excel中>
    13.响应信息：response_info
    14.依赖字段值列表：depend_field_value_list                 < (Mongo)list -> (Excel)string >
    15.实际的关键字段值列表：actual_core_field_value_list       < (Mongo)list -> (Excel)string >
    16.关键字段值比较结果：result_core_field_value
    17.响应字段列表比较结果：result_field_name_list
    18.测试结果：test_result
    19.创建时间：create_time   < (Mongo)ISODate -> (Excel)string >
    20.更新时间：update_time   < (Mongo)ISODate -> (Excel)string >

    【 备 注 】
     验证模式：verify_mode
    （1）验证：关键字段值   ->  1
    （2）验证：关键字段值、响应字段列表 ->  2
    """
    special_list = ["interface_name", "interface_url", "request_method", "request_header", "request_params",
                    "verify_mode", "compare_core_field_name_list", "expect_core_field_value_list",
                    "expect_field_name_list", "depend_interface_list", "depend_field_name_list", "case_status"]
    return special_list


def get_not_null_field_list():
    """
    【 获 取 必 填 字 段 列 表 】
    01.接口名称：interface_name（ 必填 ）
    02.接口地址：interface_url（ 必填 ）
    03.请求方式：request_method（ 必填 ）
    04.验证模式：verify_mode（ 必填 ）
    05.待比较关键字段名列表：compare_core_field_name_list（ 必填 ）
    06.期望的关键字段值列表：expect_core_field_value_list（ 必填 ）
    :return:
    """
    not_null_field_list = ["interface_name", "interface_url", "request_method", "verify_mode",
                           "compare_core_field_name_list", "expect_core_field_value_list"]
    return not_null_field_list


def get_list_field():
    """
    【 获 取 列 表 字 段 】< 表示可以通过","分割多个字段值 (Excel)string -> (Mongo)list  >
    01.待比较关键字段名列表：compare_core_field_name_list
    02.期望的关键字段值列表：expect_core_field_value_list
    03.期望的响应字段列表：expect_field_name_list
    04.依赖接口名称：depend_interface_list
    05.依赖字段名：depend_field_name_list
    06.依赖字段值：depend_field_value_list
    07.实际的关键字段值列表：actual_core_field_value_list
    :return:
    """
    list_field = ["compare_core_field_name_list", "expect_core_field_value_list", "expect_field_name_list",
                  "depend_interface_list", "depend_field_name_list", "depend_field_value_list",
                  "actual_core_field_value_list"]
    return list_field