"""
Tca9548a basic usage example
"""
import time

import tca9548a


def example():
    # init
    i2c_address = 0x70
    tca_driver = tca9548a.TCA9548A(i2c_address)

    # disable all i2c channels
    tca_driver.set_control_register(0b00000000)  # each bit controls a channel

    # enable channel 4
    tca_driver.set_channel(4, 1)

    # read state of channel 4
    ch4 = tca_driver.get_channel(4)
    print("Channel 4 is set to {}".format(ch4))

    # disable channel 4
    tca_driver.set_channel(4, 0)

    # read state of all channels
    state = tca_driver.get_control_register()
    print("Channel 4 is set to {0:b}".format(state))

    # enable all channels
    tca_driver.set_control_register(0xFF)


if __name__ == '__main__':
    example()
