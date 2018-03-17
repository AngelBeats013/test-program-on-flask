# 图像处理的库
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import os
#使验证码名字唯一
import uuid

class VariCode:
    # 随机一个字母或数字
    def random_chr(self):
        num = random.randint(1, 3)
        if num == 1:
            # 随机一个0-9
            char = random.randint(48, 57)
            pass
        elif num == 2:
            # 随机一个a-z
            char = random.randint(97, 122)
            pass
        else:
            # 随机一个A-Z
            char = random.randint(65, 90)
            pass
        return chr(char)

    # 随机加入干扰字符，防止暴力破解
    def random_dis(self):
        arr = ["^", "_", "-", "."]
        return arr[random.randint(0, 3)]

    # 定义干扰字符颜色 三原色 rgb 0-255
    def random_color1(self):
        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # 定义字符颜色
    def random_color2(self):
        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

    # 生成验证码
    def create_code(self):
        width = 240
        height = 60
        # 创建图片
        image = Image.new("RGB", (width, height), (192, 192, 192))
        # 创建font定义字体和大小
        font_name = random.randint(1, 3)
        font_file = os.path.join(os.path.dirname(__file__), "static/fonts") + "/%d.ttf" % font_name
        # font_file = os.path.join(os.path.dirname(__file__), "static/fonts/3.ttf")
        font = ImageFont.truetype(font_file, 30)
        # 船舰draw，填充像素点,然后imae就可以编辑了
        draw = ImageDraw.Draw(image)
        for x in range(0, width, 5):
            for y in range(0, height, 5):
                draw.point((x, y), fill=self.random_color1())
        #填充干扰字符
        for v in range(0,width,30):
            dis=self.random_dis()
            w=5+v
            #距离图上边距最多15，最低5px
            h=random.randint(5,15)
            draw.text((w,h),dis,font=font,fill=self.random_color1())
        #填充字符
        chars=""
        for v in range(4):
            c=self.random_chr()
            chars+=str(c)
            #图片上边距5-15px
            h=random.randint(5,15)
            #站图片宽度1/4，间隙10px
            w=width/4*v+10
            draw.text((w,h),c,font=font,fill=self.random_color2())
        #模糊效果
        image.filter(ImageFilter.BLUR)
        image_name="%s.jpg" % uuid.uuid4().hex
        save_dir=os.path.join(os.path.dirname(__file__),"static/code")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        image.save(save_dir+"/"+image_name,"jpeg")
        return dict(
            img_name=image_name,
            code=chars
        )
        # image.show()



# if __name__ == "__main__":
#     c = Code()
#     c.create_code()
