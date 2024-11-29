library(tidyverse)
library(tidygraph)
library(ggraph)

g <- play_geometry(100, .2, torus = FALSE)

g %>% 
	ggraph() + 
	geom_edge_link(alpha = 0.01) + 
	geom_node_point(color = "#f2f8ff") + 
	theme_void()


ggsave("img/background-network.png", dpi = 300, width = 6, height = 6)