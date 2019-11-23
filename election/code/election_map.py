from pretreatment import *
import matplotlib
import matplotlib.patches as mpatches
import cartopy
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

cc = shpreader.Reader('cb_2015_us_county_500k.shx')
pp = cc.records()
cl = cc.geometries()

fig = plt.figure(figsize = (20, 20))
ax = plt.axes(projection = ccrs.Mercator())
gl = ax.gridlines(linewidth = 0.2, color = 'gray', alpha = 0.5, linestyle = '-', draw_labels = False)
ax.set_extent([-128, -67, 24, 53], cartopy.crs.PlateCarree())
counties = cartopy.feature.ShapelyFeature(cl, cartopy.crs.PlateCarree(), facecolor = 'none')
states = cfeature.NaturalEarthFeature(category='cultural', scale='50m', facecolor='none', name='admin_1_states_provinces_shp')

ax.add_feature(cartopy.feature.LAND)
ax.add_feature(cartopy.feature.OCEAN)
ax.coastlines(resolution='110m')  
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', lw=.1)
ax.add_feature(cartopy.feature.RIVERS)
states = cfeature.NaturalEarthFeature(category='cultural', scale='50m', facecolor='none',
                             name='admin_1_states_provinces_lines_shp')
grid1=ax.gridlines(linewidth=0.2, color='black', alpha=0.2, linestyle='-', draw_labels=True)
ax.add_feature(counties, edgecolor='grey') 
ax.add_feature(states, edgecolor='black')
grid1.xlocator = matplotlib.ticker.FixedLocator([-120, -105, -90, -75])    
grid1.xformatter = LONGITUDE_FORMATTER
grid1.yformatter = LATITUDE_FORMATTER 
grid1.xlabels_top = False  
grid1.ylabels_right = False
grid1.xlabel_style = {'size': 15, 'color': 'gray','weight': 'bold'}  
grid1.ylabel_style = {'size': 15,'color': 'gray', 'weight': 'bold'}
ax.set_title('US: States and Counties',y=1.01,fontsize=18)  

data = pretreatment()
gop = list(data[data['result_2016'] == 0].county_fips)
dem = list(data[data['result_2016'] == 1].county_fips)

for i in cc.records():
    facecolor = [0.9, 0.9, 0.9]
    edgecolor = 'black'
    if int(i.attributes['GEOID']) in gop:
        facecolor = 'red'
    elif int(i.attributes['GEOID']) in dem:
        facecolor = 'blue'
    ax.add_geometries([i.geometry], cartopy.crs.PlateCarree(), edgecolor='grey',facecolor=facecolor)

red_patch = mpatches.Patch(color='red', label='Counties won by Trump')
blue_patch = mpatches.Patch(color='blue', label='Counties won by Clinton')
grey_patch = mpatches.Patch(color='grey', label='Results not know')
plt.legend(handles=[red_patch,blue_patch,grey_patch],fontsize=20)
plt.show()

