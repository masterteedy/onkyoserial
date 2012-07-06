import serial

class onkyoserial:
  def __init__(self, serport):
    self.ser = serial.Serial(port=serport,baudrate=9600,timeout=0,rtscts=0,xonxoff=0)

  def ser_cmd(self, cmd):
    if self.ser.isOpen():
      self.ser.write(''.join(['!1', cmd, '\r']))

  def pwr_on(self):
    """System power on."""
    self.ser_cmd('PWR01')

  def pwr_off(self):
    """System power off."""
    self.ser_cmd('PWR00')

  def vol_up(self):
    """Main volume up."""
    self.ser_cmd('MVLUP')

  def vol_down(self):
    """Main volume down."""
    self.ser_cmd('MVLDOWN')
