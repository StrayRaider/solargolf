from sglib import planets, blackhole

#blackhole.Blackhole((500,500),50)

lvls = {1:{"planets":[planets.Planet((300,300),30),
					  planets.Planet((700,200),50)],
				      "blackhole":[]},
        2:{"planets":[planets.Planet((300,300),30),
        			  planets.Planet((700,200),50),
        			  planets.Planet((600,500),50)],
        			  "blackhole":[]},
        3:{"planets":[planets.Planet((300,300),30),
        			  planets.Planet((700,200),50),
        			  planets.Planet((600,500),50),
        			  planets.Planet((1000,300),50)],
        			  "blackhole":[]},
        4:{"planets":[planets.Planet((300,300),30),
        			  planets.Planet((700,200),50),
        			  planets.Planet((600,500),50),
        			  planets.Planet((1000,300),50),
        			  planets.Planet((200,550),30)],
        			  "blackhole":[]},
        5:{"planets":[planets.Planet((300,300),30),
        			  planets.Planet((700,200),50),
        			  planets.Planet((600,500),50),
        			  planets.Planet((1000,300),50),
        			  planets.Planet((1000,550),30)],
        			  "blackhole":[]},
        6:{"planets":[planets.Planet((1000,550),40),
        			  planets.Planet((300,200),50),
        			  planets.Planet((900,200),30),
        			  planets.Planet((600,500),30)],
        			  "blackhole":[]},
        7:{"planets":[planets.Planet((600,350),30),
        			  planets.Planet((300,250),50),
        			  planets.Planet((900,350),30),
        			  planets.Planet((500,600),30),
        			  planets.Planet((700,150),40)],
        			  "blackhole":[]},
        8:{"planets":[planets.Planet((200,100),30),
        			  planets.Planet((300,500),50),
        			  planets.Planet((900,500),40),
        			  planets.Planet((900,300),30),
        			  planets.Planet((700,150),40)],
        			  "blackhole":[]},
        9:{"planets":[planets.Planet((200,150),30),
        			  planets.Planet((200,500),30),
        			  planets.Planet((700,150),30),
        			  planets.Planet((800,500),50),
        			  planets.Planet((500,350),50)],
        			  "blackhole":[]},
        10:{"planets":[planets.Planet((200,100),30),
        			  planets.Planet((200,500),30),
        			  planets.Planet((700,100),30),
        			  planets.Planet((800,500),50)],
        			  "blackhole":[]},#burdan ekleme yap
		11: {"planets": [planets.Planet((300, 300), 30),
						planets.Planet((700, 200), 50)],
			            "blackhole": [blackhole.Blackhole((500,250),50)]}}






