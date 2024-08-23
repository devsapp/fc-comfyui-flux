
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# fc-comfyui-flux 帮助文档
<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-comfyui-flux&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc-comfyui-flux" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-comfyui-flux&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc-comfyui-flux" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-comfyui-flux&type=packageDownload">
  </a>
</p>

<description>

部署 ComfyUI + Flux 到阿里云函数计算

</description>

<codeUrl>



</codeUrl>
<preview>



</preview>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>

| 服务 |  备注  |
| --- |  --- |
| 函数计算 FC |  提供 CPU、GPU 等计算资源 |
| 文件存储 NAS |  存储大模型文件 |

</service>

<remark>



</remark>

<disclaimers>



</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=fc-comfyui-flux) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=fc-comfyui-flux) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init fc-comfyui-flux -d fc-comfyui-flux`
  - 进入项目，并进行项目部署：`cd fc-comfyui-flux && s deploy -y`
   
</deploy>

## 案例介绍

<appdetail id="flushContent">

本案例展示了如何将 Flux 部署到阿里云函数计算上，从而在云端体验 Flux 文生图的 AIGC 创作活动。

Flux 是由 Black Forest Labs 推出的文生图模型，其在文本控制、绘图质量、排版能力等多方面已经超越了包括 Midjourney、Stable Diffusion 等常用的文生图模型。

ComfyUI 是一个为 Stable Diffusion 模型设计的，功能强大且高度模块化的图形用户界面（GUI）。它允许用户基于节点构建 AIGC 创作流程，非常适合那些想要摆脱传统编程方法、采用更直观操作流程的用户。该工具由 Comfyanonymous 在 2023 年 1 月创建，初衷是深入了解 Stable Diffusion 模型的运作机制。由于其易用性，Stable Diffusion 的开发者 Stability AI 也采用了 ComfyUI 进行内部测试，并聘请 Comfyanonymous 协助开发内部工具。目前，ComfyUI 在 Github 上的 Fork 数超过 3000，Star 数超过 30000。

ComfyUI 提供了方便的能力使用 Flux 进行文本绘图。通过 Serverless 开发平台，您只需要几步，就可以基于 Flux 体验 Comfyui，并享受Serverless 架构带来的降本提效的技术红利。







</appdetail>

## 使用流程

<usedetail id="flushContent">

### 基本文生图

1. 打开 ComfyUI，点击“Queue Prompt”开始。
2. 稍等片刻后，您将得到第一张图片。若需要恢复默认工作流，请使用“Load Default”，并记得保存您的工作流以避免丢失。

![](https://img.alicdn.com/imgextra/i2/O1CN01nML52f1mIRwjP3sPy_!!6000000004931-0-tps-1226-889.jpg)

### 挂载 NAS 和使用自定义节点

为使用自定义模型和节点，需先绑定文件管理 NAS。通过函数控制台的网络配置，绑定专有网络/交换机。若无相关资源，需先创建。

我们已为您自动创建并挂载的通用性能型 NAS 实例，NAS 会根据存储的文件大小进行计费，不通规格的 NAS 计费单价不一致，请参考相关文档。


### 进入 ComfyUI 终端

函数计算支持登入运行中的函数实例，您可以在终端中执行需要的操作（如手动安装自定义节点、依赖等）

注意，在 Serverless 环境下，您的所有改动都不会真正保存，您需要将改动的文件放置在 NAS 中以持久化

![](https://img.alicdn.com/imgextra/i2/O1CN01p2zERS21sNFaFIFlK_!!6000000007040-0-tps-1522-846.jpg)


### 文件上传及下载

借助 NAS 文件浏览器功能，您可以方便地进行云上文件管理

![](https://img.alicdn.com/imgextra/i1/O1CN01qBoRgE1Us1czB7Doi_!!6000000002572-0-tps-1533-574.jpg)


### 安装自定义节点

以安装中文翻译插件 [AIGODLIKE-COMFYUI-TRANSLATION](https://github.com/AIGODLIKE/AIGODLIKE-COMFYUI-TRANSLATION) 为例，使用 ComfyUI-Manager 进行安装。

![](https://img.alicdn.com/imgextra/i1/O1CN01cpHWUJ1WQfCKAZoVB_!!6000000002783-0-tps-1339-893.jpg)

搜索要安装的节点名称，点击 install

![](https://img.alicdn.com/imgextra/i2/O1CN014lNLJe1lebUP6PYxn_!!6000000004844-0-tps-1368-270.jpg)

**注意**
- 安装过程中请不要关闭页面。安装完成后，除去需要点击 restart 外，还需要刷新页面
- 安装过程中可能会访问 Github、HuggingFace 等境外网站，由于网络问题可能会导致访问较慢或失败，您可以在网络上检索如何解决类似的问题。 )

### 加速依赖下载

使用国内 pypi 镜像加速依赖下载。编辑 `/mnt/auto/comfyui/root/.pip/pip.conf` 文件，设置镜像源为阿里云。

```
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = https://mirrors.aliyun.com
```

### 解决缺失节点的问题

导入第三方的工作流，可能会遇到节点不存在的报错，可以借助 ComfyUI Manager 安装缺失的节点

![](https://img.alicdn.com/imgextra/i4/O1CN015Ovmyr1VPSXWcUvit_!!6000000002645-0-tps-840-442.jpg)

![](https://img.alicdn.com/imgextra/i2/O1CN01aSPkBh22XatVsvQrX_!!6000000007130-0-tps-1363-886.jpg)


部分节点升级后，可能仍然提示未安装，可参考 [ComfyUI Guides](https://comfyui-guides.runcomfy.com/) 的相关讨论解决。

> How to fix: A red node for “IPAdapterApply”?
> You must already follow our instructions on how to install IP-Adapter V2, and it should all working properly. Now you see a red node for “IPAdapterApply”.
>
> That is because you are working on a workflow with IPAdapter V1 node, simply just replace the V1 node with the V2 ones or uninstall IPA v2 and rollback to V1 if you feel like it.


### ControlNet 的使用

展示了使用 ControlNet 对比直接输出的差异，提供了工作流 JSON 示例以及对应模型的下载说明。

![](https://img.alicdn.com/imgextra/i4/O1CN01R8bT461O1STVjkkfy_!!6000000001645-0-tps-2090-1062.jpg)

<details><summary>工作流文件</summary>

```json
{
  "last_node_id": 12,
  "last_link_id": 16,
  "nodes": [
    {
      "id": 11,
      "type": "FluxGuidance",
      "pos": [
        857,
        185
      ],
      "size": {
        "0": 317.4000244140625,
        "1": 58
      },
      "flags": {},
      "order": 5,
      "mode": 0,
      "inputs": [
        {
          "name": "conditioning",
          "type": "CONDITIONING",
          "link": 10,
          "label": "conditioning"
        }
      ],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            11
          ],
          "shape": 3,
          "slot_index": 0,
          "label": "CONDITIONING"
        }
      ],
      "properties": {
        "Node name for S&R": "FluxGuidance"
      },
      "widgets_values": [
        3.5
      ]
    },
    {
      "id": 8,
      "type": "VAEDecode",
      "pos": [
        866,
        623
      ],
      "size": {
        "0": 210,
        "1": 46
      },
      "flags": {},
      "order": 7,
      "mode": 0,
      "inputs": [
        {
          "name": "samples",
          "type": "LATENT",
          "link": 7,
          "label": "Latent"
        },
        {
          "name": "vae",
          "type": "VAE",
          "link": 8,
          "label": "VAE"
        }
      ],
      "outputs": [
        {
          "name": "IMAGE",
          "type": "IMAGE",
          "links": [
            9
          ],
          "slot_index": 0,
          "label": "图像"
        }
      ],
      "properties": {
        "Node name for S&R": "VAEDecode"
      }
    },
    {
      "id": 9,
      "type": "SaveImage",
      "pos": [
        1220,
        187
      ],
      "size": {
        "0": 661.95703125,
        "1": 923.08984375
      },
      "flags": {},
      "order": 8,
      "mode": 0,
      "inputs": [
        {
          "name": "images",
          "type": "IMAGE",
          "link": 9,
          "label": "图像"
        }
      ],
      "properties": {
        "Node name for S&R": "SaveImage"
      },
      "widgets_values": [
        "ComfyUI"
      ]
    },
    {
      "id": 3,
      "type": "KSampler",
      "pos": [
        861,
        308
      ],
      "size": {
        "0": 315,
        "1": 262
      },
      "flags": {},
      "order": 6,
      "mode": 0,
      "inputs": [
        {
          "name": "model",
          "type": "MODEL",
          "link": 14,
          "label": "模型"
        },
        {
          "name": "positive",
          "type": "CONDITIONING",
          "link": 11,
          "label": "正面条件"
        },
        {
          "name": "negative",
          "type": "CONDITIONING",
          "link": 6,
          "label": "负面条件"
        },
        {
          "name": "latent_image",
          "type": "LATENT",
          "link": 2,
          "label": "Latent"
        }
      ],
      "outputs": [
        {
          "name": "LATENT",
          "type": "LATENT",
          "links": [
            7
          ],
          "slot_index": 0,
          "label": "Latent"
        }
      ],
      "properties": {
        "Node name for S&R": "KSampler"
      },
      "widgets_values": [
        453117095366540,
        "randomize",
        20,
        1,
        "euler",
        "normal",
        1
      ]
    },
    {
      "id": 7,
      "type": "CLIPTextEncode",
      "pos": [
        397,
        391
      ],
      "size": {
        "0": 425.27801513671875,
        "1": 180.6060791015625
      },
      "flags": {},
      "order": 4,
      "mode": 0,
      "inputs": [
        {
          "name": "clip",
          "type": "CLIP",
          "link": 16,
          "label": "CLIP"
        }
      ],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            6
          ],
          "slot_index": 0,
          "label": "条件"
        }
      ],
      "properties": {
        "Node name for S&R": "CLIPTextEncode"
      },
      "widgets_values": [
        ""
      ]
    },
    {
      "id": 4,
      "type": "CheckpointLoaderSimple",
      "pos": [
        56,
        176
      ],
      "size": {
        "0": 315,
        "1": 98
      },
      "flags": {},
      "order": 0,
      "mode": 0,
      "outputs": [
        {
          "name": "MODEL",
          "type": "MODEL",
          "links": [
            13
          ],
          "slot_index": 0,
          "label": "模型"
        },
        {
          "name": "CLIP",
          "type": "CLIP",
          "links": [
            12
          ],
          "slot_index": 1,
          "label": "CLIP"
        },
        {
          "name": "VAE",
          "type": "VAE",
          "links": [
            8
          ],
          "slot_index": 2,
          "label": "VAE"
        }
      ],
      "properties": {
        "Node name for S&R": "CheckpointLoaderSimple"
      },
      "widgets_values": [
        "flux1-dev-fp8.safetensors"
      ]
    },
    {
      "id": 5,
      "type": "EmptyLatentImage",
      "pos": [
        403,
        622
      ],
      "size": {
        "0": 315,
        "1": 106
      },
      "flags": {},
      "order": 1,
      "mode": 0,
      "outputs": [
        {
          "name": "LATENT",
          "type": "LATENT",
          "links": [
            2
          ],
          "slot_index": 0,
          "label": "Latent"
        }
      ],
      "properties": {
        "Node name for S&R": "EmptyLatentImage"
      },
      "widgets_values": [
        768,
        1024,
        1
      ]
    },
    {
      "id": 12,
      "type": "LoraLoader",
      "pos": [
        420,
        -50
      ],
      "size": {
        "0": 315,
        "1": 126
      },
      "flags": {},
      "order": 2,
      "mode": 0,
      "inputs": [
        {
          "name": "model",
          "type": "MODEL",
          "link": 13,
          "label": "模型"
        },
        {
          "name": "clip",
          "type": "CLIP",
          "link": 12,
          "label": "CLIP",
          "slot_index": 1
        }
      ],
      "outputs": [
        {
          "name": "MODEL",
          "type": "MODEL",
          "links": [
            14
          ],
          "shape": 3,
          "tooltip": "The modified diffusion model.",
          "label": "模型",
          "slot_index": 0
        },
        {
          "name": "CLIP",
          "type": "CLIP",
          "links": [
            15,
            16
          ],
          "shape": 3,
          "tooltip": "The modified CLIP model.",
          "label": "CLIP",
          "slot_index": 1
        }
      ],
      "properties": {
        "Node name for S&R": "LoraLoader"
      },
      "widgets_values": [
        "flux-lora-000003.safetensors",
        3,
        1
      ]
    },
    {
      "id": 6,
      "type": "CLIPTextEncode",
      "pos": [
        402,
        175
      ],
      "size": {
        "0": 422.84503173828125,
        "1": 164.31304931640625
      },
      "flags": {},
      "order": 3,
      "mode": 0,
      "inputs": [
        {
          "name": "clip",
          "type": "CLIP",
          "link": 15,
          "label": "CLIP"
        }
      ],
      "outputs": [
        {
          "name": "CONDITIONING",
          "type": "CONDITIONING",
          "links": [
            10
          ],
          "slot_index": 0,
          "label": "条件"
        }
      ],
      "properties": {
        "Node name for S&R": "CLIPTextEncode"
      },
      "widgets_values": [
        "wukong, monkey king, monkey face, gray hair，play computer"
      ]
    }
  ],
  "links": [
    [
      2,
      5,
      0,
      3,
      3,
      "LATENT"
    ],
    [
      6,
      7,
      0,
      3,
      2,
      "CONDITIONING"
    ],
    [
      7,
      3,
      0,
      8,
      0,
      "LATENT"
    ],
    [
      8,
      4,
      2,
      8,
      1,
      "VAE"
    ],
    [
      9,
      8,
      0,
      9,
      0,
      "IMAGE"
    ],
    [
      10,
      6,
      0,
      11,
      0,
      "CONDITIONING"
    ],
    [
      11,
      11,
      0,
      3,
      1,
      "CONDITIONING"
    ],
    [
      12,
      4,
      1,
      12,
      1,
      "CLIP"
    ],
    [
      13,
      4,
      0,
      12,
      0,
      "MODEL"
    ],
    [
      14,
      12,
      0,
      3,
      0,
      "MODEL"
    ],
    [
      15,
      12,
      1,
      6,
      0,
      "CLIP"
    ],
    [
      16,
      12,
      1,
      7,
      0,
      "CLIP"
    ]
  ],
  "groups": [],
  "config": {},
  "extra": {
    "ds": {
      "scale": 1.2100000000000002,
      "offset": [
        -36.69525444125759,
        72.04083143388111
      ]
    }
  },
  "version": 0.4
}
```

</details>

</usedetail>

## 注意事项

<matters id="flushContent">

fc-comfyui 是一个第三方工具，旨在帮助用户将 ComfyUI 项目部署到阿里云函数计算服务。请注意，该工具与 ComfyUI 项目及阿里云官方无直接联系。

- **第三方链接**：本工具提供的第三方网站或服务链接仅为用户方便，开发者对这些内容、隐私政策或操作不承担责任，亦不代表认可。
- **社区同步**：ComfyUI 为活跃的开源社区项目，功能丰富且更新频繁，如果您希望使用更新版本的 ComfyUI，可自行基于 Dockerfile 文件进行构建。
- **费用提示**：在阿里云部署 ComfyUI 可能产生费用，请参考阿里云的计费文档。若需持久化存储（如模型、节点），还需开通文件管理 NAS，可能产生额外费用。
- **许可协议**：使用 ComfyUI 项目需遵守其开源许可协议。使用前，请确保已阅读并理解 ComfyUI 项目及相关第三方工具的许可协议。
- **遵守服务条款**：部署至阿里云函数计算服务，需同意阿里云服务条款和使用政策。
- **无担保声明**：本工具“按现状”提供，不包含任何形式的担保。使用风险由用户自担，开发者不负责任何直接或间接损害。
- **资源消耗**：ComfyUI 页面建立长连接请求，<span style="color:red">**持续消耗计算资源**</span>。为避免不必要费用，请不使用时关闭所有页面。

使用本工具即表示您已理解并同意以上声明。若不同意，请勿使用。

</matters>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
