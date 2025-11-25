import os
from jinja2 import Environment, FileSystemLoader

def apply_prompt_template(template_name: str, **kwargs) -> str:
  """
  使用 Jinja2 模板引擎渲染 prompt 模板。

  jinja2可以自动获取到当前目录下templates文件夹里面的prompt为变量,方便调试prompt,
  也可以有if else之类的语法实现真正的dynamic prompt
    
  该函数会在当前文件所在目录的 templates 子目录中查找指定的模板文件，
  并使用传入的参数进行渲染。
  
  Args:
      template (str): 模板文件名（不含 .jinja-md 扩展名）
      **kwargs: 传递给模板的变量，用于模板渲染
  
  Returns:
      str: 渲染后的字符串内容
      
  Raises:
      TemplateNotFound: 当指定的模板文件不存在时
      
  Example:
      >>> result = apply_prompt_template('greeting', name='张三', age=25)
      >>> print(result)
  """
  # 获取当前文件所在目录下的 templates 子目录的完整路径
  template_dir = os.path.join(os.path.dirname(__file__), "templates")
  # 创建 Jinja2 文件系统加载器，指定模板文件的搜索目录
  loader = FileSystemLoader(template_dir)
  # 使用加载器创建 Jinja2 环境对象，用于渲染模板
  env = Environment(loader=loader)
  # 根据模板名称加载对应的 .jinja-md 文件
  template = env.get_template(f"{template_name}.jinja-md")
  # 使用传入的关键字参数渲染模板并返回渲染后的字符串
  return template.render(**kwargs)
