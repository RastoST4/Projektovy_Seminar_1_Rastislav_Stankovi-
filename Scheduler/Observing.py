from astropy.coordinates import SkyCoord
from astroplan import FixedTarget
from astropy.time import Time
from astroplan import Observer
import matplotlib.pyplot as plt
from astroplan.plots import plot_airmass,plot_sky
import numpy as np
import astropy.units as u
#Get Targets(obj)
altair = FixedTarget.from_name('Altair')
vega = FixedTarget.from_name('Vega')
#Time of observation we will make it as variable for the next day

time = Time('2015-06-16 12:00:00')
# observer
subaru = Observer.at_site('subaru')

# subaru.is_night(time)
def is_observable(time,obj,observer):
    print(observer.target_is_up(time, obj))

def airmass():
    plot_airmass(altair, subaru, time)
    plot_airmass(vega, subaru, time)
    plt.legend(loc=1, bbox_to_anchor=(1, 1))
    plt.show()

def plot_night_movement():

    #when obj rise and set
    altair_rise = subaru.target_rise_time(time, altair) + 5 * u.minute
    altair_set = subaru.target_set_time(time, altair) - 5 * u.minute
    vega_rise = subaru.target_rise_time(time, vega) + 5 * u.minute
    vega_set = subaru.target_set_time(time, vega) - 5 * u.minute
    # we will make  starting time for bouth obj and ending time too
    all_up_start = np.max([altair_rise, vega_rise])
    all_up_end = np.min([altair_set, vega_set])
    # sun rise and set for specific observer
    sunrise_tonight = subaru.sun_rise_time(time, which='nearest')
    sunset_tonight = subaru.sun_set_time(time, which='nearest')
    # when obseration starts and ends
    start = np.max([sunset_tonight, all_up_start])
    end = np.min([sunrise_tonight, all_up_end])
    time_window = start + (end - start) * np.linspace(0, 1, 10)
    altair_style = {'color': 'r'}

    plot_sky(altair, subaru, time_window, style_kwargs=altair_style)
    plot_sky(vega, subaru, time_window)

    plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
    plt.show()


def main():
    is_observable(time,altair,subaru)
   # airmass()
    plot_night_movement()

if __name__ == "__main__":
    main()