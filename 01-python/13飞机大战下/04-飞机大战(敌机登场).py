import pygame
import random

# 屏幕的宽度
SCREEN_WIDTH = 512
# 屏幕的高度
SCREEN_HEIGHT = 768

# 敌机类
class EnemyPlane(object):
    def __init__(self):
        # 生成一个1-7的随机数字
        random_num = random.randint(1, 7)
        # 加载敌机图片
        self.enemy_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img-plane_%d.png" % random_num)
        # 获取图片的矩形对象
        self.enemy_img_rect = self.enemy_img.get_rect()
        # 随机产生一个x坐标
        random_x = random.randint(0, SCREEN_WIDTH - self.enemy_img_rect[2])
        # 设置矩形对象的位置
        self.enemy_img_rect[0] = random_x
        self.enemy_img_rect[1] = -self.enemy_img_rect[3]

        # 移动速度
        self.speed = random.randint(4, 6)

    # 重置敌机位置
    def reset(self):
        # 随机产生一个x坐标
        random_x = random.randint(0, SCREEN_WIDTH - self.enemy_img_rect[2])
        # 设置矩形对象的位置
        self.enemy_img_rect[0] = random_x
        self.enemy_img_rect[1] = -self.enemy_img_rect[3]

        # 移动速度
        self.speed = random.randint(4, 6)


    # 敌机往下移动的方法
    def move_down(self):
        self.enemy_img_rect.move_ip(0, self.speed)

        # 判断敌机的矩形对象的y坐标是否大于屏幕的高度，如果大于说明飞机已经超出屏幕需要重新设置位置到顶部外
        if self.enemy_img_rect[1] > SCREEN_HEIGHT:
            # 重置敌机的位置
            self.reset()



# 子弹类
class Bullet(object):
    def __init__(self):
        # 产生一个9-14的随机数
        random_num = random.randint(9, 14)
        # 加载子弹的图片对象
        self.bullet_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/bullet_%d.png" % random_num)

        # 获取子弹图片的矩形对象，因为图片的移动都是通过矩形对象来控制的
        self.bullet_img_rect = self.bullet_img.get_rect()
        # 子弹的速度
        self.speed = 5
        # 子弹的状态
        self.is_shot = False

    # 子弹向上移动的方法
    def move_up(self):
        self.bullet_img_rect.move_ip(0, -self.speed)
        # 判断子弹是否超出屏幕外
        if self.bullet_img_rect[1] < -self.bullet_img_rect[3]:
            # 把子弹的状态改成未发射的状态
            self.is_shot = False


# 英雄飞机类
class HeroPlane(object):
    def __init__(self):
        # 加载英雄飞机的图片对象
        self.hero_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/hero2.png")
        # 获取图片的矩形对象
        self.hero_img_rect = self.hero_img.get_rect()
        # 修改矩形对象的位置
        self.hero_img_rect[0] = SCREEN_WIDTH / 2 - self.hero_img_rect[2] / 2
        self.hero_img_rect[1] = SCREEN_HEIGHT - self.hero_img_rect[3] - 20

        # 移动速度
        self.speed = 5

        # 飞机携带子弹列表, '_': 忽略不使用的参数
        self.bullet_list = [Bullet() for _ in range(5)]


    # 飞机发射子弹
    def shot(self):
        for bullet in self.bullet_list:
            # 遍历每一颗子弹，判断子弹的状态
            # if bullet.is_shot == False:
            if not bullet.is_shot:
                # 1. 把子弹改成发射状态
                bullet.is_shot = True
                # 2. 飞机发射子弹的时候，因为飞机的位置已经确定下来的，那么这个时候需要设置子弹的位置
                bullet.bullet_img_rect[0] = self.hero_img_rect[0] + self.hero_img_rect[2] / 2 - bullet.bullet_img_rect[2] / 2
                bullet.bullet_img_rect[1] = self.hero_img_rect[1] - bullet.bullet_img_rect[3]
                # 按下空格发射一颗子弹， 只改变一颗子弹的状态
                break

    # 上
    def move_up(self):
        if self.hero_img_rect[1] > 0:
            self.hero_img_rect.move_ip(0, -self.speed)

    # 下
    def move_down(self):
        if self.hero_img_rect[1] < SCREEN_HEIGHT - self.hero_img_rect[3]:
            self.hero_img_rect.move_ip(0, self.speed)

    # 左
    def move_left(self):
        if self.hero_img_rect[0] > 0:
            self.hero_img_rect.move_ip(-self.speed, 0)

    # 右边
    def move_right(self):
        if self.hero_img_rect[0] < SCREEN_WIDTH - self.hero_img_rect[2]:
            self.hero_img_rect.move_ip(self.speed, 0)



# 游戏地图类
class GameMap(object):
    def __init__(self):
        # 获取背景图片的随机数字
        random_num = random.randint(1, 5)
        # 加载背景图片1
        self.bg_img1 =  pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img_bg_level_%d.jpg" % random_num)
        # 加载背景图片2
        self.bg_img2 = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/img_bg_level_%d.jpg" % random_num)


        # 获取背景2图片的矩形对象
        self.bg_img2_rect = self.bg_img2.get_rect()
        # 修改背景图片的矩形对象的位置
        self.bg_img2_rect[1] = -SCREEN_HEIGHT
        self.bg_img2_rect[0] = 0

        # 获取背景1图片的矩形对象
        self.bg_img1_rect = self.bg_img1.get_rect()
        self.bg_img1_rect[1] = 0
        self.bg_img1_rect[0] = 0

        # 地图滚动的速度
        self.speed = 3

    # 地图滚动
    def scoll_map(self):
        # 矩形对象每次移动指定的大小
        self.bg_img1_rect.move_ip(0, self.speed)
        self.bg_img2_rect.move_ip(0, self.speed)

        # 判断矩形对象的y轴是否超出屏幕
        if self.bg_img1_rect[1] >= SCREEN_HEIGHT:
            print("第一张背景图片超出了屏幕")
            print("第一张:", self.bg_img1_rect[1])
            self.bg_img1_rect[1] = 0-SCREEN_HEIGHT

        if self.bg_img2_rect[1] >= SCREEN_HEIGHT:
            print("第二张背景图片超出了屏幕")
            print("第二张:", self.bg_img2_rect[1])
            self.bg_img2_rect[1] = -SCREEN_HEIGHT






# 游戏窗口类
class GameWindow(object):
    def __init__(self):
        # 初始化pygame
        pygame.init()
        # 创建游戏窗口
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # 设置窗口的标题
        pygame.display.set_caption("飞机大战")
        # 加载图标对象
        app_img = pygame.image.load("/mnt/hgfs/WorkSpace/data/planeBattle/res/app.ico")
        # 设置窗口的图标
        pygame.display.set_icon(app_img)

        # 创建一个地图对象
        self.game_map = GameMap()
        # 创建英雄飞机对象
        self.hero = HeroPlane()
        # 敌机列表
        self.enemy_list = [EnemyPlane() for _ in range(5)]


    # 程序运行的方法
    def run(self):
        # 游戏运行起来就是一个大循环，需要循环获取窗口的事件
        while True:
            # 获取窗口事件
            event_list = pygame.event.get()
            for event in event_list:
                # 判断事件的类型
                if event.type == pygame.QUIT:
                    # 代码执行到此说明用户点击的关闭按钮
                    exit()
                elif event.type == pygame.KEYDOWN:
                    # 判断按键操作
                    if event.key == pygame.K_ESCAPE:
                        # 按下的是esc键
                        exit()
                    elif event.key == pygame.K_SPACE:
                        # 发射子弹
                        self.hero.shot()

            # 获取长按键的列表，判断关心的长按的键对应的value值是否为1
            key_list = pygame.key.get_pressed()
            if key_list[pygame.K_UP] or key_list[pygame.K_w]:
                self.hero.move_up()
            elif key_list[pygame.K_DOWN]:
                self.hero.move_down()
            elif key_list[pygame.K_LEFT]:
                self.hero.move_left()
            elif key_list[pygame.K_RIGHT]:
                self.hero.move_right()

            # 让地图先滚动
            self.game_map.scoll_map()
            # 绘制地图图片对象
            self.window.blit(self.game_map.bg_img1, (self.game_map.bg_img1_rect[0], self.game_map.bg_img1_rect[1]))
            # 绘制地图图片对象
            self.window.blit(self.game_map.bg_img2, (self.game_map.bg_img2_rect[0], self.game_map.bg_img2_rect[1]))

            # 绘制英雄飞机图片到窗口
            self.window.blit(self.hero.hero_img, (self.hero.hero_img_rect[0], self.hero.hero_img_rect[1]))

            # 遍历每一个敌机，然后让敌机往下移动，然后绘制敌机移动后的位置在窗口上显示
            for enemy in self.enemy_list:
                # 让敌机移动
                enemy.move_down()
                self.window.blit(enemy.enemy_img, (enemy.enemy_img_rect[0], enemy.enemy_img_rect[1]))


            # 遍历子弹列表，找到发射的子弹，让子弹向上移动，然后在绘制移动后的子弹
            for bullet in self.hero.bullet_list:
                # 判断子弹的发射状态
                if bullet.is_shot:
                    # 让子弹向上移动
                    bullet.move_up()
                    # 绘制子弹移动的位置
                    self.window.blit(bullet.bullet_img, (bullet.bullet_img_rect[0], bullet.bullet_img_rect[1]))

            # 刷新窗口，显示图片对象
            pygame.display.update()

if __name__ == '__main__':
    # 测试代码
    game_window = GameWindow()
    # 运行游戏
    game_window.run()