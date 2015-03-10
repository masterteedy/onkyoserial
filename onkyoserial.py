import serial


class onkyoserial:
    def __init__(self, serport):
        self.ser = serial.Serial(
            port=serport,
            baudrate=9600,
            timeout=0,
            rtscts=0,
            xonxoff=0)

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

    def disp_info_format(self):
        """Display program format.
        (Check disp_mode_* if this does not work)"""
        self.ser_cmd('DIF00')

    def disp_info_digital_input(self):
        """Display digital input position.
        (Check disp_mode_* if this does not work)"""
        self.ser_cmd('DIF01')

    def disp_info_digital_format(self):
        """Display digital format position.
        (Check disp_mode_* if this does not work)"""
        self.ser_cmd('DIF02')

    def disp_info_bass(self):
        """Display bass level.
        (Check disp_mode_* if this does not work)"""
        self.ser_cmd('DIF03')

    def disp_info_treble(self):
        """Display treble level.
        (Check disp_mode_* if this does not work)"""
        self.ser_cmd('DIF04')

    def disp_mode_volume(self):
        """Display volume mode / sets Selector.
        (Check disp_info_* if this does not work)"""
        self.ser_cmd('DIF0')

    def disp_mode_listening(self):
        """Display listening mode / sets Selector.
        (Check disp_info_* if this does not work)"""
        self.ser_cmd('DIF0')

    def disp_mode_digital_format(self):
        """Display digital format.
        (Check disp_info_* if this does not work)"""
        self.ser_cmd('DIF02')

    def disp_mode_video_format(self):
        """Display video format.
        (Check disp_info_* if this does not work)"""
        self.ser_cmd('DIF03')

    def setup_key_menu(self):
        """Setup operation; menu key."""
        self.ser_cmd('OSDMENU')

    def setup_key_up(self):
        """Setup operation; up key."""
        self.ser_cmd('OSDUP')

    def setup_key_down(self):
        """Setup operation; down key."""
        self.ser_cmd('OSDDOWN')

    def setup_key_left(self):
        """Setup operation; left key."""
        self.ser_cmd('OSDLEFT')

    def setup_key_right(self):
        """Setup operation; right key."""
        self.ser_cmd('OSDRIGHT')

    def setup_key_enter(self):
        """Setup operation; enter key."""
        self.ser_cmd('OSDENTER')

    def setup_key_exit(self):
        """Setup operation; exit key."""
        self.ser_cmd('OSDEXIT')

    def setup_key_audio(self):
        """Setup operation; audio key."""
        self.ser_cmd('OSDAUDIO')

    def setup_key_video(self):
        """Setup operation; video key."""
        self.ser_cmd('OSDVIDEO')

    def setup_key_home(self):
        """Setup operation; home key."""
        self.ser_cmd('OSDHOME')

    def mem_setup_store(self):
        """Store memory."""
        self.ser_cmd('MEMSTR')

    def mem_setup_recall(self):
        """Recall memory."""
        self.ser_cmd('MEMRCL')

    def mem_setup_lock(self):
        """Lock memory."""
        self.ser_cmd('MEMLOCK')

    def mem_setup_unlock(self):
        """Unlock memory."""
        self.ser_cmd('MEMUNLK')

    def mem_setup_info(self):
        """Audio memory information."""
        self.ser_cmd('MEMIFA')
