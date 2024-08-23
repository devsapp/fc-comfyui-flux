import os
import requests

def download_file(url, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # 发送 GET 请求
    response = requests.get(url, stream=True)
    response.raise_for_status()  # 检查请求是否成功

    # 将内容写入文件
    with open(save_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

def handler(event, context):
    try:
        region = os.getenv("FC_REGION")
        root = os.getenv("NAS_ROOT")
        download_file("https://dipper-cache-%s.oss-%s-internal.aliyuncs.com/models/loras/flux_wukong.safetensors" % (region, region), "%s/models/loras/flux_wukong.safetensors" % root)
    except Exception as e:
        print(e)
        raise e
        
    return 'initial done'