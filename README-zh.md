# StableDiffusion的roop

这是StableDiffusion的[AUTOMATIC1111 web-ui](https://github.com/AUTOMATIC1111/stable-diffusion-webui/)的扩展，可以在图像中替换人脸。它基于[roop](https://github.com/s0md3v/roop)，但将分别开发。

![example](example/example.png)

### 免责声明

这个软件旨在为快速增长的人工智能生成媒体行业做出有效的贡献。它将协助艺术家完成一些任务，例如动画制作自定义角色或将该角色用作服装模特等。

该软件的开发者知道它可能存在的不道德应用，并致力于采取预防措施。它具有内置的检查机制，防止该程序用于不适当的媒体中。我们将继续朝着积极的方向开发这个项目，恪守法律和道德标准。如果根据法律要求，这个项目可能会被关闭或在输出上加上水印。

使用这个软件的用户应该在遵守当地法律的同时负责任地使用。如果使用了真实人物的面部，用户建议从有关人士获得同意，并在发布在线内容时清楚说明它是深度伪造的。该软件的开发者不对最终用户的行为负责。

## Installation
首先，如果由于某些原因无法安装，不要在此处开立问题事项。通过谷歌搜索你遇到的错误。

针对Windows，下载并安装Visual Studio。在安装过程中，确保安装了Python和C++程序包。

+ 运行此命令：`pip install insightface==0.7.3`
+ 在web-ui中，转到“扩展”选项卡，并在“从URL安装”选项卡中使用此URL `https://github.com/s0md3v/sd-webui-roop`
+ 关闭web-ui并重新运行它
+ 如果遇到" 'NoneType' object has no attribute 'get' "错误，请下载inwapper_128.onnx模型，并将其放置在`<webui_dir>/models/roop/`目录中。

对于其余的错误，请使用谷歌搜索。祝你好运。

## 使用方法

1. 在“roop”下拉菜单中导入一张包含人脸的图像。
2. 打开“启用”复选框
3. 就这样，现在生成的结果将包含您选择的人脸。

## 提示
#### 获得高质量的结果
首先，确保“恢复面容”选项已启用。您还可以尝试“ Upscaler”选项或更细致的控制，使用“ Extras”选项卡中的较高比例尺。

为了获得更好的质量，请使用denoise设置为`0.1`的img2img，并逐渐增加它，直到您获得质量和相似度的平衡为止。

#### 替换特定的面孔
如果图像中有多个面孔，请使用“逗号分隔的面部编号（s）”选项选择您想要交换的面部编号。

#### 这张脸没有被交换吗？
你有单击“启用”吗？

如果您确实这样做，并且您的控制台没有显示任何错误，则表示roop检测到您的图像要么不适合家庭，要么无法检测到面部。