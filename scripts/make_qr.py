# -*- coding: utf-8 -*-
"""生成巴达通官网联系区二维码占位图（用户可自行替换 public/qrcode.png）"""
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont

OUT = r"C:\Users\hp\WorkBuddy\2026-08-16-15-30-44\badatong-website\public\qrcode.png"

# 占位内容：正式使用时请将 public/qrcode.png 替换为你自己的二维码
payload = "巴达通 BADATONG 巴西本土店注册 / 税务申报 / 店铺注册 · 扫码联系专属顾问"

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=12,
    border=4,
)
qr.add_data(payload)
qr.make(fit=True)
img = qr.make_image(fill_color="#0b2a6b", back_color="#ffffff").convert("RGB")

# 中间加"巴"字 logo（白底圆角 + 绿色方块 + 白色文字）
size = int(img.size[0] * 0.22)
logo_bg = Image.new("RGBA", (size, size), (255, 255, 255, 255))
draw = ImageDraw.Draw(logo_bg)
draw.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * 0.22), fill=(0, 162, 91, 255))

# 尝试加载中文字体
font = None
candidates = [
    r"C:\Windows\Fonts\msyhbd.ttc",  # 微软雅黑 Bold
    r"C:\Windows\Fonts\simhei.ttf",  # 黑体
    r"C:\Windows\Fonts\msyh.ttc",
]
for c in candidates:
    try:
        font = ImageFont.truetype(c, int(size * 0.58))
        break
    except Exception:
        continue
if font is None:
    font = ImageFont.load_default()

text = "巴"
bbox = draw.textbbox((0, 0), text, font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.text(((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1]), text, font=font, fill=(255, 255, 255, 255))

img.paste(logo_bg, ((img.size[0] - size) // 2, (img.size[1] - size) // 2), logo_bg)
img = img.resize((600, 600), Image.LANCZOS)
img.save(OUT, "PNG")
print("QR placeholder saved:", OUT)
