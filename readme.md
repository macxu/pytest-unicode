
## 环境配置:

pip install -r requirements.txt

# 如何重现问题:
在根目录下运行:
```python
pytest
```

这个命令会执行test_case_id.py里面的测试用例，这个文件里的测试用例是参数化的:
```python
@pytest.mark.parametrize("input_str, expected_str", [
        pytest.param("abC", "abc", id="this is test 1"),
        pytest.param("aBC", "abc", id="这是测试用例2")
    ]
)
```

以上的代码是设计两个测试用例，分别用pytest.param来创建，pytest.param有一个参数，叫做id, 这个参数用于标识这个测试用例。

问题是：如果id是用英文字符串，一切正常，如果是中文(unicode)字符串，id会被设置成相应的byte string，无法阅读。
我想看看如何解决用中文设置id。

