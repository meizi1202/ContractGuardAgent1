# 代码注释规范

## 注释原则

- **必要注释**：解释"为什么"而不是"是什么"
- **保持更新**：代码修改后，注释必须同步更新
- **清晰简洁**：避免冗余，用简洁语言表达

## 行内注释

用于解释复杂的逻辑分支，放在代码上方或行尾，与代码之间留一个空格。

```python
# 判断是否为工作日（排除周末）
if dayType == 1:  # 1=工作日
    processWorkday()
```

## 块注释

用于标记代码区块功能，使用 `#` 包围，保持一致性。

```python
####################
# 数据处理模块
# 负责解析、转换、验证数据
####################
def processData():
    pass
```

## TODO 注释

使用统一格式标记待办事项。

```python
# TODO(用户名): 待完成功能说明
# FIXME(用户名): 需要修复的问题
```

## 文档字符串 (docstring)

每个公开的类、函数都要有 docstring。

### Google 风格

```python
def calculateTotal(items: List[Dict]) -> float:
    """计算订单总金额。

    Args:
        items: 商品列表，每个商品包含 price 和 quantity

    Returns:
        订单总金额

    Raises:
        ValueError: 当商品列表为空或数据格式错误时

    Example:
        >>> items = [{"price": 100, "quantity": 2}]
        >>> calculateTotal(items)
        200.0
    """
```

### NumPy 风格

```python
def calculateTotal(items: List[Dict]) -> float:
    """
    计算订单总金额。

    Parameters
    ----------
    items : List[Dict]
        商品列表，每个商品包含 price 和 quantity

    Returns
    -------
    float
        订单总金额

    Raises
    ------
    ValueError
        当商品列表为空或数据格式错误时

    Examples
    --------
    >>> items = [{"price": 100, "quantity": 2}]
    >>> calculateTotal(items)
    200.0
    """
```

## 类注释

```python
class documentParser:
    """文档解析器，支持解析 doc、docx、pdf 格式的文档。

    Attributes:
        supportedFormats: 支持的文件格式列表
        verbose: 是否输出详细日志
    """

    def __init__(self, verbose: bool = False):
        """初始化解析器。

        Args:
            verbose: 是否输出详细日志，默认 False
        """
        pass
```

## 重要提示

1. **注释不是越多越好**：避免显而易见的注释
2. **代码先行，注释后改**：先写功能，再补充注释
3. **英文优先**：代码和注释尽量使用英文
4. **统一风格**：整个项目保持一致的注释风格
