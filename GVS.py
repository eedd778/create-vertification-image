import random,string
from PIL import Image,ImageDraw,ImageFont

def gernerate_image(length=4,
                    mode='RGB',
                    size=(120,30),
                    font_size=18,
                    bg_color=(255,255,255),
                    font_color=(0,0,0),
                    font_type='./id-ftmaru400a.ttf',
                    image_type='PNG',
                    ):
    """生成驗證圖片
    :param length:字串長度
    :param size:圖片大小
    :param font_size:字體大小
    :param bg_color:圖片背景顏色
    :param font_color:字體顏色
    :param font_type:字型
    :param image_type:輸出圖片格式
    """
    width,height=size
    gen_str=''.join(random.choice(string.ascii_letters+string.digits) for x in range(length))
    image_str='  '.join(i for i in gen_str)#字串空格分開(用於圖片)
    
    im=Image.new(mode,size,bg_color)
    draw=ImageDraw.Draw(im)
    font=ImageFont.truetype(font_type,font_size)
    draw.text((width/(length+2),height/3),image_str,font_color,font)
    im.save('test.{}'.format(image_type.lower()),image_type)
    return gen_str

if __name__=="__main__":
    print(gernerate_image())