from mc import mc
import hieu_citydata as citydata


def initial_city():
    # Make ground
    mc.postToChat('Make ground')

    mc.setBlocks(
        citydata.startPoint['x'],
        citydata.startPoint['y'],
        citydata.startPoint['z'],
        citydata.endPoint['x'],
        citydata.endPoint['y'],
        citydata.endPoint['z'],
        citydata.cityGroundBlock,
        citydata.cityGroundData

    )

    # make space
    mc.postToChat('Make space')
    mc.setBlocks(
        citydata.startPoint['x'],
        citydata.startPoint['y'] + 1,
        citydata.startPoint['z'],
        citydata.endPoint['x'],
        citydata.endPoint['y'] + citydata.cityHeight,
        citydata.endPoint['z'],
        citydata.cityGroundBlock,
        0)


# initial_city()


def teleport():
    main_id = mc.getPlayerEntityId(citydata.main_player)
    x, y, z = citydata.startPoint['x'], citydata.startPoint['y'], citydata.startPoint['z']
    mc.entity.setPos(main_id, x, y + 2, z)
    mc.postToChat('teleport {}'.format(citydata.main_player))


# teleport()

def make_street():
    x, y, z = citydata.street['x'], citydata.street['y'], citydata.street['z']
    mc.setBlocks(x, y - 1, z, x + citydata.street['long'], y, z + citydata.street['width'] - 1, 0)
    mc.setBlocks(x, y - 1, z, x + citydata.street['long'], y - 1, z + citydata.street['width'] - 1,
                 citydata.street['block'],
                 citydata.street['data'])
    # kẻ vạch
    # mc.setBlocks(x, y - 1, z + citydata.street['width'] // 2, x + citydata.street['long'], y - 1,
    #              z + citydata.street['width'] // 2,
    #              0)
    for yellowLine in range(citydata.street['long'] // 5):
        mc.setBlocks(x + yellowLine * 5 + 1, y - 1, z + citydata.street['width'] // 2,
                     x + (yellowLine + 1) * 5 - 1, y - 1,
                     z + citydata.street['width'] // 2,
                     35,
                     4)


make_street()
