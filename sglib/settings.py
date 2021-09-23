import pygame

def scale_factor():
    pygame.init()
    screen_ratio = pygame.display.Info()
    sizes_d = (screen_ratio.current_w, screen_ratio.current_h)
    #sizes_d = (1366, 1366)
    if round(sizes_d[0]/sizes_d[1], 1) == round(16/9, 1) :
        print("hellooo") # eğer oranımız 16/9 ise yapılacaklar
        # scale factor direkt olarak hhesaplanır
        # tasarımın yapıldığı boyutlandırma = 1280
        scl_fac = sizes_d[0]/1280
        x_or_y = "xy"
        
    else :
        screen_s_f = sizes_d[0]/sizes_d[1]
        x_scl_f = sizes_d[0]/1280
        y_scl_f = sizes_d[1]/720
        print(screen_s_f)
        print(x_scl_f/y_scl_f)
        
        if x_scl_f >= y_scl_f: # x büyü kolan
            scl_fac = y_scl_f
            x_or_y = "x"

        else :
            scl_fac = x_scl_f # y büyük olan
            x_or_y = "y"

    return scl_fac ,x_or_y