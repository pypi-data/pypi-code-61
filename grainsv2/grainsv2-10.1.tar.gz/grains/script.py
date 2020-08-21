import pop.hub


def start():
    hub = pop.hub.Hub()
    hub.pop.sub.add(dyne_name="grains")
    hub.grains.init.cli()
