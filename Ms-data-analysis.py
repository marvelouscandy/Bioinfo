
from bioinfokit import visuz
visuz.volcano(table = "LFQ-volcano.csv" ,  lfc = "logFC", pv = "P-value", geneid = "Gene names", genenames = ("Nfu1", "Hk2", "Hars", "Bckdhb", "Mrpl20", "Lyrm7", "Ephx2", "Dhrs7b","Cox5a","Snd1","Cpt1a","Atp5d","Hibadh","Hspa9","Ndufb10","Mrpl41","Lamc1","Acot2","Uqcrq" ), color = ("#00239CFF" , "#E10600FF"))

###visuz.ma(table = "MAplot.csv", lfc = "logFC", ct_count = "average-WT", st_count = "average-KO", lfc_thr = 1)

###visuz.hmap(table = "Heatmap.csv", cmap = "seismic", scale = True, dim = (6,8), clus = True, zscore = None, xlabel = True, ylabel = True, tickfont = (10,10))
