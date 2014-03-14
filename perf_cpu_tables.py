# This function is trying to find the closest CPU performance for a given model
def get_generic_cpu_perf(cpu_struct, cpu_type):
    # Let's find in the cpu already exist in the list of known CPUs
    for cpu_list in sorted(cpu_struct, reverse=True):
        if cpu_list in cpu_type:
            return cpu_struct[cpu_list]
    else:
        # Unless, retry by shortening the string by one word
        if (len(cpu_type.split()) > 1):
            shorten_cpu_type = cpu_type.rsplit(' ', 1)[0]
            return get_generic_cpu_perf(cpu_struct, shorten_cpu_type)
        else:
            return 0


def get_cpu_min_perf(cpu_type):
    cpu_struct = {
        "Intel(R) Xeon(R) CPU": 300,
        "Intel(R) Xeon(R) CPU E5-2650 0 @ 2.00GHz": 456,
        "Intel(R) Xeon(R) CPU E5-2650": 420,
        "Intel(R) Xeon(R) CPU E5": 400}

    return get_generic_cpu_perf(cpu_struct, cpu_type)