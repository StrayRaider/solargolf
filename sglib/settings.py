import pygame

def scale_factor():
    pygame.init()
    screen_ratio = pygame.display.Info()
    sizes_d = (screen_ratio.current_w, screen_ratio.current_h)
    #sizes_d = (1280, 720)
    if round(sizes_d[0]/sizes_d[1], 1) == round(16/9, 1) :
        print("hellooo") # eğer oranımız 16/9 ise yapılacaklar
        # scale factor direkt olarak hhesaplanır
        # tasarımın yapıldığı boyutlandırma = 1280
        scl_fac = sizes_d[0]/1280
        
    else :
        print("problemmmm")
        pass
        #eğer oranımız 16/9 değilse yapılacaklar
        #hangi trafın daha büyük olduğunu bulmakla başlamalıyız
        #büyük taraf sabit kalırken küçük tarafın boşluklarının siyah kalması sağlanmalı
    return scl_fac
        
    #anlık ekran boyutklarımız = 1366,768
    #print(sizes_d[0]/sizes_d[1])
    #print(1280/720)
    #print(*sizes_d)