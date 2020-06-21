from astropy.coordinates import EarthLocation
import astropy.units as u
from astroplan import Observer


def createObserver(long, lat, ele, name, timeZone):
    location = EarthLocation.from_geodetic(long * u.deg, lat * u.deg, ele * u.m)
    observer = Observer(location=location, timezone=timeZone, name=name)

    return observer


def obsChangeWeater(temp, humid, presure, obs):
    obs.pressure = presure
    obs.relative_humidity = humid
    obs.temperature = temp
