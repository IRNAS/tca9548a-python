# TCA9554a driver

Python driver for TCA9548A I2C mux for python to be used with RPi

## Basic usage

Initialize by providing devices I2C address

```python3
i2c_address = 0x70
pca_driver = pca9554.Pca9554(i2c_address)
```

Enable/Disable all channels via the control register

```python3
tca_driver.set_control_register(0b01010101)  # each value is one channels
```

Enable or disble a single channel

```python3
tca_driver.set_channel(4, 0)  # channel 4 disabled
tca_driver.set_channel(5, 1)  # channel 5 enabled
```

Read channel configuration

```python3
ch7 = tca_driver.get_channel(7)  # config of channel 7
```

For other functionality see [tca9548a.py](tca9548a.py)
