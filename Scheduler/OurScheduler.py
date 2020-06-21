from astroplan.scheduling import Schedule, ObservingBlock
from astroplan import FixedTarget, Observer, Transitioner, AirmassConstraint
from astropy.time import Time
from SimpleScheduler import SimpleScheduler
import astropy.units as u
import matplotlib.pyplot as plt
from astroplan.plots import plot_schedule_airmass

con = AirmassConstraint(2)
apo = Observer.at_site('apo')
deneb = FixedTarget.from_name('Deneb')
m13 = FixedTarget.from_name('M13')
blocks = [ObservingBlock(deneb, 20 * u.minute, 0, con)]
blocks.append(ObservingBlock(m13, 20 * u.minute, 0))

# Speed of telescope
transitioner = Transitioner(slew_rate=2 * u.deg / u.second)

# Schedule the observing blocks
schedule = Schedule(Time('2016-07-06 19:00'), Time('2016-07-07 19:00'))
scheduler = SimpleScheduler(observer=apo, transitioner=transitioner,
                            constraints=[con])
scheduler(blocks, schedule)

plot_schedule_airmass(schedule)
plt.legend()
#plt.show()
plt.savefig('Our_scheduler.png')
