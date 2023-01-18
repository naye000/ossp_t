import pygame
from variable import Var
import pygame_menu
from Tetris import *
import time
class Menu:

    def __init__(self):
        pygame.init()
        Var.infoObject = pygame.display.Info()
        self.tetris=Tetris()
        self.w=Var.menu_display_w
        self.h=Var.menu_display_h
        self.Mode = Var.initial_mode
        self.page=Var.initial_page
        self.surface=pygame.display.set_mode((self.w,self.h),RESIZABLE)
        self.mytheme=Var.mytheme
        self.mytheme2=Var.mytheme_help
        self.menu = pygame_menu.Menu(self.h,self.w, '', theme=self.mytheme)
        self.font_main=Var.font_main   # 메인 폰트 사이즈
        self.font_sub=Var.font_sub     # 서브 폰트 사이즈
        self.widget_margin_main=Var.widget_margin_main         #메인 위젯 사이 간격
        self.widget_margin_showpage=Var.widget_margin_showpage #show 페이지 위젯 사이 간격
        self.margin_main=Var.margin_main                       #메인 페이지 x,y 위젯 시작 위치
        self.margin_show=Var.margin_show                       #show 페이지 x,y 위젯 시작 위치


#add_button 이거는 선택하는 버튼 만들기
#clear()는 초기화하기
#add_vertical_margin 위에서 부터 간격 설정하기
#add_label 은 텍스트만 있는 것 만들기
#add_text_input 은 텍스트 입력 받아 함수 실행 가능한 것
#자세한 것은 깃허브 pygame_menu에 자세하게 나와있습니다. 참고하세요

    def run(self):   # 실행하는 함
        print('test2')
        self.page=Var.initial_page   #시작하면 기본 모드로 모드가 설정
        self.menu.clear()
        self.mytheme.widget_margin=self.widget_margin_main
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_button('   Select mode   ', self.show_game,font_size=self.font_main)
        self.menu.add_button('        Quit         ', pygame_menu.events.EXIT,font_size=self.font_main)


    def reset(self):  ## 뒤로 갈때 보여줄 목록들
        self.surface = pygame.display.set_mode((self.w, self.h), RESIZABLE)
        self.menu = pygame_menu.Menu(self.h, self.w, '', theme=self.mytheme)
        self.page='page0'
        self.mytheme.widget_margin=self.widget_margin_main
        Var.click.play()
        self.page=Var.initial_page
        self.menu.clear()
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_button('   Select mode   ', self.show_game,font_size=self.font_main)
        self.menu.add_button('        Quit         ', pygame_menu.events.EXIT,font_size=self.font_main)




    def show_game(self):  ## 게임 목록 들어가면 나오는 목록들
        self.page='page1'
        Var.click.play()
        self.menu.clear()
        self.mytheme.widget_margin=self.widget_margin_showpage
        self.menu.add_vertical_margin(self.margin_main)
        self.menu.add_label("    --Start game--    ",selectable=False,font_size=self.font_main)
        self.menu.add_vertical_margin(self.margin_show)
        self.menu.add_button('      Single mode      ', self.start_the_game,font_size=self.font_main)
        self.menu.add_button('       MiNi mode       ', self.start_the_Mini,font_size=self.font_main)
        self.menu.add_button('           back            ', self.reset,font_size=self.font_main)
    

    def stop(self):
        Var.click.play()
        self.menu.disable()

    def pass_(self):
        pass