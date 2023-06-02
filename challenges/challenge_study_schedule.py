def study_schedule(permanence_period, target_time):
    counter = 0

    if target_time is None:
        return None

    for entry, exit in permanence_period:
        if type(entry) is not int or type(exit) is not int:
            return None

        if target_time >= entry and target_time <= exit:
            counter += 1
    return counter
