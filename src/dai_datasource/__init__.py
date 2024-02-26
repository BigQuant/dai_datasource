"""引用 DAI 数据集，根据输入的 DataSource ID 返回一个 dai.DataSource 对象"""
from bigmodule import I  # noqa: N812

# metadata
# 模块作者
author = "BigQuant"
# 模块分类
category = "数据输入输出"
# 模块显示名
friendly_name = "DataSource (DAI)"
# 文档地址, optional
doc_url = "https://bigquant.com/data/home"
# 是否自动缓存结果
cacheable = True


def run(id: I.str("DataSource ID")) -> [I.port("输出DAI DataSource", "data")]:
    """输出dai DataSource"""
    import dai
    data = dai.DataSource(id=id)
    return I.Outputs(data=data)


def post_run(outputs):
    """后置运行函数"""
    return outputs
