from astroplan import Observer
from astroplan import FixedTarget
from astropy.time import Time
from astroplan.constraints import AtNightConstraint, AirmassConstraint
from astroplan import ObservingBlock
from astroplan.constraints import TimeConstraint
from astropy import units as u
from astroplan.scheduling import Transitioner
from astroplan.scheduling import SequentialScheduler, PriorityScheduler
from astroplan.scheduling import Schedule
from astroplan.plots import plot_schedule_airmass
import matplotlib.pyplot as plt

deneb = FixedTarget.from_name('Deneb')
m13 = FixedTarget.from_name('M13')
apo = Observer.at_site('apo')
# Start and end of observational time
noon_before = Time('2016-07-06 19:00')
noon_after = Time('2016-07-07 19:00')

# Global constraints all objects must satisfy it
global_constraints = [AirmassConstraint(max = 3, boolean_constraint = False),AtNightConstraint.twilight_civil()]
# read_out time
read_out = 20 * u.second
# expotion time
deneb_exp = 60*u.second
m13_exp = 100*u.second
# number of expotion per observation

n = 16
# observation blocks will go to the schedule
blocks = []
half_night_start = Time('2016-07-07 02:00')
half_night_end = Time('2016-07-07 08:00')
first_half_night = TimeConstraint(half_night_start, half_night_end)
def prio_schedule():
    for priority, bandpass in enumerate(['B', 'G', 'R']):
        b = ObservingBlock.from_exposures(deneb, priority, deneb_exp, n, read_out,configuration = {'filter': bandpass},constraints = [first_half_night])
        blocks.append(b)
        b = ObservingBlock.from_exposures(m13, priority, m13_exp, n, read_out,configuration = {'filter': bandpass},constraints = [first_half_night])
        blocks.append(b)
    slew_rate = .8 * u.deg / u.second
    # define how telescope transition between block
    transitioner = Transitioner(slew_rate,
                                {'filter': {('B', 'G'): 10 * u.second,
                                ('G', 'R'): 10 * u.second,
                                'default': 30 * u.second}})
    # init new seq scheduler
    prior_scheduler = PriorityScheduler(constraints = global_constraints,observer = apo,transitioner = transitioner)
    #Initialize a Schedule object, to contain the new schedule
    priority_schedule = Schedule(noon_before, noon_after)
    prior_scheduler(blocks, priority_schedule)
    plt.figure(figsize = (14,6))
    plot_schedule_airmass(priority_schedule)
    plt.legend(loc = "upper right")
    #plt.show()
    plt.savefig('prior_scheduler.png')



def main():
   prio_schedule()

if __name__ == "__main__":
    main()