from astroplan import ObservingBlock, AirmassConstraint

### There will be more types of observing block
## each observing type will have some constainst and configuration that more blocks will share
surveyConfig = None
surveyConst = AirmassConstraint(2)
folowUpConfig = None
folowUpConst = None


#
def survey(target, duration, priority, configuration, constraints):
    conf = surveyConfig + configuration
    const = constraints + surveyConst
    return ObservingBlock(target=target, duration=duration, priority=priority, configuration=conf,
                          constraints=constraints)


def folow_up(target, duration, priority, configuration, constraints):
    conf = folowUpConfig + configuration
    const = constraints + folowUpConst
    return ObservingBlock(target=target, duration=duration, priority=priority, configuration=conf,
                          constraints=constraints)
