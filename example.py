#Here is an example usage (it will read all unique settings into a list, reset the instrument and then program the unique settings back into the instrument):

import time
import pyvisa
from tektronix_afg3102 import tektronics_afg3102

rm = pyvisa.ResourceManager()
tekafg3102 = rm.open_resource('USB::0x000::0x000::C000000::INSTR')
tektronics_afg3102 = tektronics_afg3102(pyvisa_instr=tekafg3102)

current_setting_list = tektronics_afg3102.get_unique_scpi_list()

tekafg3102.write('*RST')
time.sleep(2)
for scpi_cmd in current_setting_list:
  tekafg3102.write(scpi_cmd)
time.sleep(4)
