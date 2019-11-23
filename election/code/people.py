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
people_0 = list(data[data['population2014'] <= 50000].county_fips)
people_1 = list(data[(data['population2014'] <= 100000) & (data['population2014'] > 50000)].county_fips)
people_2 = list(data[(data['population2014'] <= 200000) & (data['population2014'] > 100000)].county_fips)
people_3 = list(data[(data['population2014'] <= 500000) & (data['population2014'] > 200000)].county_fips)
people_4 = list(data[data['population2014'] > 500000].county_fips)

for i in cc.records():
    facecolor = [0.9, 0.9, 0.9]
    edgecolor = 'black'
    if int(i.attributes['GEOID']) in people_0:
        facecolor = [0.6, 0.96, 1]
    elif int(i.attributes['GEOID']) in people_1:
        facecolor = [0, 1, 1]
    elif int(i.attributes['GEOID']) in people_2:
        facecolor = [0, 0.75, 1]
    elif int(i.attributes['GEOID']) in people_3:
        facecolor = [0.1176, 0.56, 1]
    elif int(i.attributes['GEOID']) in people_4:
        facecolor = [0, 0, 1]
    ax.add_geometries([i.geometry], cartopy.crs.PlateCarree(), edgecolor='grey',facecolor=facecolor)

patch = mpatches.Patch(color=[0.6, 0.96, 1], label='Population less than 50 Thousand')
patch_1 = mpatches.Patch(color=[0, 1, 1], label='Population less  than 100 Thousand')
patch_2 = mpatches.Patch(color=[0, 0.75, 1], label='Population less  than 200 Thousand')
patch_3 = mpatches.Patch(color=[0.1176, 0.56, 1], label='Population less  than 500 Thousand')
patch_4 = mpatches.Patch(color=[0, 0, 1], label='Population greater  than 500 Thousand')
plt.legend(handles=[patch,patch_1,patch_2,patch_3,patch_4],fontsize=20)
plt.show()

