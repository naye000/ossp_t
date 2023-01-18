import pygame
import pygame_menu
import random
import os
class Var:
    pygame.mixer.init()

    # 사운드 관련
    ai_bgm = pygame.mixer.Sound('assets/sounds/ai_sound.wav')
    ai_bgm.set_volume(0.1)

    base_bgm = pygame.mixer.Sound('assets/sounds/base_sound.wav')
    base_bgm.set_volume(0.1)

    block_fall = pygame.mixer.Sound('assets/sounds/block_fall.wav')
    block_fall.set_volume(0.1)

    click = pygame.mixer.Sound('assets/sounds/click.wav')
    click.set_volume(1)

    game_over = pygame.mixer.Sound('assets/sounds/game_over.wav')
    game_over.set_volume(0.05)

    line_clear = pygame.mixer.Sound('assets/sounds/Line_Clear.wav')
    line_clear.set_volume(0.2)

    level_up = pygame.mixer.Sound('assets/sounds/level_up.wav')
    level_up.set_volume(0.2)

    #ai 블럭 모양
    ai_tetris_shapes = [
        [[1, 1, 1],
         [0, 1, 0]],
        [[0, 2, 2],
         [2, 2, 0]],

        [[3, 3, 0],
         [0, 3, 3]],

        [[4, 0, 0],
         [4, 4, 4]],

        [[0, 0, 5],
         [5, 5, 5]],

        [[6, 6, 6, 6]],

        [[7, 7],
         [7, 7]]
    ]
    O = (((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 1, 1, 0), (0, 0, 1, 1, 0), (0, 0, 0, 0, 0)),) * 4

    I = (((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 2, 2, 2, 2), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 2, 0, 0), (0, 0, 2, 0, 0), (0, 0, 2, 0, 0), (0, 0, 2, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (2, 2, 2, 2, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 2, 0, 0), (0, 0, 2, 0, 0), (0, 0, 2, 0, 0), (0, 0, 2, 0, 0), (0, 0, 0, 0, 0)))

    L = (((0, 0, 0, 0, 0), (0, 0, 3, 0, 0), (0, 0, 3, 0, 0), (0, 0, 3, 3, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 3, 3, 3, 0), (0, 3, 0, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 3, 3, 0, 0), (0, 0, 3, 0, 0), (0, 0, 3, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 0, 3, 0), (0, 3, 3, 3, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)))

    J = (((0, 0, 0, 0, 0), (0, 0, 4, 0, 0), (0, 0, 4, 0, 0), (0, 4, 4, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 4, 0, 0, 0), (0, 4, 4, 4, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 4, 4, 0), (0, 0, 4, 0, 0), (0, 0, 4, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 4, 4, 4, 0), (0, 0, 0, 4, 0), (0, 0, 0, 0, 0)))

    Z = (((0, 0, 0, 0, 0), (0, 0, 0, 5, 0), (0, 0, 5, 5, 0), (0, 0, 5, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 5, 5, 0, 0), (0, 0, 5, 5, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 5, 0, 0), (0, 5, 5, 0, 0), (0, 5, 0, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 5, 5, 0, 0), (0, 0, 5, 5, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)))

    S = (((0, 0, 0, 0, 0), (0, 0, 6, 0, 0), (0, 0, 6, 6, 0), (0, 0, 0, 6, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 6, 6, 0), (0, 6, 6, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 6, 0, 0, 0), (0, 6, 6, 0, 0), (0, 0, 6, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 6, 6, 0), (0, 6, 6, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)))

    T = (((0, 0, 0, 0, 0), (0, 0, 7, 0, 0), (0, 0, 7, 7, 0), (0, 0, 7, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 7, 7, 7, 0), (0, 0, 7, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 7, 0, 0), (0, 7, 7, 0, 0), (0, 0, 7, 0, 0), (0, 0, 0, 0, 0)),
         ((0, 0, 0, 0, 0), (0, 0, 7, 0, 0), (0, 7, 7, 7, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)))


    weights = [3.39357083734159515, -1.8961941343266449, -5.107694873375318, -3.6314963941589093,
               -2.9262681134021786,
               -2.146136640641482, -7.204192964669836, -3.476853402227247, -6.813002842291903, 4.152001386170861,
               -21.131715861293525, -10.181622180279133, -5.351108175564556, -2.6888972099986956,
               -2.684925769670947,
               -4.504495386829769, -7.4527302422826, -6.3489634714511505, -4.701455626343827, -10.502314845278828,
               0.6969259450910086, -4.483319180395864, -2.471375907554622, -6.245643268054767, -1.899364785170105,
               -5.3416512085013395, -4.072687054171711, -5.936652569831475, -2.3140398163110643, -4.842883337741306,
               17.677262456993276, -4.42668539845469, -6.8954976464473585, 4.481308299774875]  # 21755 lignes

    error_type = {'no_error': 0, 'right_wall': 1, 'left_wall': 2, 'bottom': 3, 'overlap': 4} # 충돌 에러 판단용
    shapes_rotation = {4: 4, 8: 2, 12: 2, 16: 4, 20: 4, 24: 2, 28: 1} #ai 블럭 회전 판단용



    #            R    G    B
    BLACK = (0, 0, 0)
    RED = (225, 13, 27)
    GREEN = (98, 190, 68)
    BLUE = (64, 111, 249)
    ORANGE = (253, 189, 53)
    YELLOW = (246, 227, 90)
    PINK = (242, 64, 235)
    CYON = (70, 230, 210)
    GRAY = (26, 26, 26)
    DARK_GRAY = (55, 55, 55)
    WHITE = (255, 255, 255)
    MAIN_BLUE = (62, 149, 195)
    MAIN_WHITE = (228, 230, 246)
    MAIN_VIOLET  = (153, 153, 255)
    MAIN_VIOLET_W = (153, 153, 255, 50)
    MAIN_YELLOW = (255, 217, 90)
    w_pink = (231, 59, 109)
    w_sky = (165, 216, 243)
    z_yellow = (252, 215, 2)
    z_green = (185, 205, 12)
    z_blue = (159, 68, 145)
    y_red = (241, 141, 56)
    y_violet = (96, 57, 140)


    T_COLOR = [w_pink, w_sky, z_blue, z_green, MAIN_VIOLET, y_violet, y_red]
    colors = [BLACK, RED, GREEN, BLUE, ORANGE, YELLOW, PINK, CYON, GRAY]

    #keyboard_delay = 200
    #keyboard_interval = 150

    infoObject = () #디스플레이 사이즈 받는 용

    display_max_height = 792
    display_min_height = 450
    bar_size = 25

    x_move_scale = 1  # 블럭의 x축 이동 수
    y_move_scale = 1  # 블럭의 y축 이동 수
    collide_move_rate =2 #벽과 충돌하는 경우 움직이는 배수
    x_move_scale_zero = 0  # 블럭의 x축 이동 x
    y_move_scale_zero = 0 # 블럭의 y축 이동 x

    board_start_x = 0      # 보드의 시작점 x좌표
    board_start_y = 0      # 보드의 시작점 y좌표
    board_die_line=1      # 보드에서 다으면 죽는 라인 즉 맨 윗줄
    board_line_start = 1  # 보드 지울때 첫 줄
    delete_line=1         # 보드 지울때 한칸씩 지우기

    board_die_num=0    # 맨 위에서 보드가 몇개 이상이면 죽을 것인지
    line_size=1      # 그림자나 블록 라인 사이즈
    ai_matrix_line_size = 0 #ai  매트릭스를 만들때 라인 사이즈
    ai_line_size = 2 # ai에서 board를 나누는 선의 두께

    fps = 30  # 게임의 fps
    initial_score = 0   # 시작 점수
    initial_level = 1   # 시작 레벨
    count_level = 1     #레벨 증가률
    goal_zero_state = 0  # 골수가 0이 된 상태
    level_goal_per = 3   #레벨당 목표 goal수
    initial_combo = 0    # 시작 콤보 및 초기화
    count_combo = 1   #콤보 증가량
    count_goal = 1    #골수 증갈야
    initial_block_state= 0  #처음 블럭의 회전 상태
    ai_score_weight = 2     #ai점수 가중치
    board_empty_state = 0 #보드 처음 상태

    rotate_start = 0      #회전 인덱스 시작값
    rotate_cycle = 4      #회전 사이클
    next_block_shape = 1  #다음 회전한 모양 블럭 기준
    block_start_index = 0 #블럭 인덱스 시작점

    # 현재 블럭의 x축 기준 길이
    def piece_length(piece):
        return piece[0]

    initial_page = 'page0'
    initial_mode = 0  # 모드 초기값
    initial_id = 0  # id 초기값


    user_start_speed = 600  #유저의 시작 스피드(몇초에 한번 이벤트가 진행되는가)
    user_per_speed = 40   #레벨에 따른 유저의 속도 증가


    combo_max=9
    combo_reset=0

    basic_block_size = 25   #블록 사이즈
    basic_next_block_size_rate = 0.6  #화면에 표시되는 다음 블럭의 사이즈 비율


    basic_block_size = 25   # 블록 사이즈
    basic_next_block_size_rate = 0.6  #화면에 표시되는 다음 블럭의 사이즈 비율


    next_loc = 0.05
    score_loc = 0.3
    score_val_loc = 0.35
    level_loc = 0.45
    level_val_loc = 0.5
    goal_loc = 0.6
    goal_val_loc = 0.65
    combo_loc = 0.75
    combo_val_loc = 0.8
    time_loc = 0.92

    font_size_small = 14    #폰트 사이즈 작은거
    font_size_middle = 16   #중간
    font_size_big = 18      #큰거
    font_resize = 1
    font_size_double = 2 #fontsize 두 배

    block_start_basic_x = 3  #몇번 쨰 칸에서 블럭이 시작 하는가
    block_start_two_x = 12
    block_start_mini_x = 0
    block_start_y = -2

    combo_score_rate = 10  #콤보에 따른 점수 가중치
    level_score_rate = 10  # 레벨에 따른 점수 가중치
    max_level = 10         #최대 레벨

    menu_display_w = 600  # 메뉴 시작시 처음 가로 크기
    menu_display_h = 600  # 메뉴 시작시 처음 세로 크기

    myscore_display=(160,270)
    myscore_font=50

    # 기본 사이즈 조정
    basic_width = 10  #맵의 좌에서 우로 사이즈
    basic_height = 18 #맵 위에서 아래로 사이즈
    basic_block_size = basic_block_size  #바꾸면 맵 블럭크기 변경
    basic_status_size = 6   #상태 바 사이즈 (블럭의 개수 기준으로 )
    basic_display_width = (basic_width + basic_status_size) * basic_block_size

    dark_width = 10  #맵의 좌에서 우로 사이즈
    dark_height = 18 #맵 위에서 아래로 사이즈
    dark_block_size = basic_block_size  #바꾸면 맵 블럭크기 변경
    dark_status_size = 6   #상태 바 사이즈 (블럭의 개수 기준으로 )
    dark_display_width = (basic_width + basic_status_size) * basic_block_size



    current_w = 1855
    resize_cut_up = 1.001
    resize_cut_down = 1.0
    start_status_bar_y = 0 #상태표시 바 시작 y 좌표
    resize_basic = 1 # 리사이징 관련 고정 변수

######################메뉴 관련 #########################
##########################################################################################
    ## 메뉴 부분
    ## 메뉴 이미지 추가 부분
    menu_image = pygame_menu.baseimage.BaseImage(
        image_path='assets/images/메인메뉴.png',
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL	)
    widget_image = pygame_menu.baseimage.BaseImage(
        image_path='assets/images/메인위젯.png',
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
    PATH=os.path.join('assets/images/메인메뉴.png')


    #메뉴 기본 테마 만들기

    mytheme=pygame_menu.themes.THEME_ORANGE.copy()                  # 메뉴 기본 테마 설정
    mytheme.widget_font_color=WHITE                         # 메뉴 위젯 폰트 컬러
    mytheme.background_color = menu_image                           # 메뉴 배경 설정
    #mytheme.widget_background_color = widget_image                 # 메뉴 위젯 배경 설정
    mytheme.title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE  # 메뉴 타이틀 바 모양 설정
    mytheme.widget_alignment=pygame_menu.locals.ALIGN_CENTER        # 메뉴 가운데 정렬 설정
    mytheme.widget_font =pygame_menu.font.FONT_NEVIS                # 메뉴 폰트 설정
    mytheme.widget_margin=(0,40)




    min_display_w =400      # 메뉴 최소 사이즈 가로
    min_display_h =400      # 메뉴 최소 사이즈 세로
    widget_center = 0
    sleep_time = 0.3
    initial_page = 'page0'  # 메뉴 시작 페이지

    # 리사이징 시 변하는 비율 화면과 비례하는 비율
    font_rate_main = 15          #메인 폰트 리사이징 비율
    font_rate_sub = 20           #서브 폰트들 리사이징 비율
    widget_rate_main = 15        #메인 화면 리젯들 사이 간격 비율
    widget_rate_showpage = 30   #showpage 위젯 간격 비율
    widget_rate_rank = 60       #rank페이지 위젯 간격 비율
    rate_main=6                 #메인 위젯 시작 하는 위치 비율
    rate_show=40                #show 위젯 시작 하는 위치 비율
    rate_rank=30                #rank 위젝 시작 위치 비율
    rate_help=1.25              #help 창 위젯 시작 위치 비율


    #폰트 사이즈
    font_main = int((menu_display_h) / font_rate_main)   # 메뉴 기본 폰트 사이즈
    font_sub = int((menu_display_h) / font_rate_sub)     # 메뉴 서브 폰트 사이즈

      