# SPDX-License-Identifier: GPL-2.0
# Copyright (C) 2016-present Team LibreELEC (https://libreelec.tv)

import subprocess
import xbmc
import xbmcaddon
import xbmcgui

class Monitor(xbmc.Monitor):

   def __init__(self, *args, **kwargs):
      xbmc.Monitor.__init__(self)
      self.id = xbmcaddon.Addon().getAddonInfo('id')
 
      OVPN_SERVER = xbmcaddon.Addon().getSetting('OVPN_SERVER')
      if OVPN_SERVER == "":
		dialog = xbmcgui.Dialog()
		dialog.ok('', "After defining the server name in the configuration window,\n"+\
				"go to the console and execute:\n"+\
				"  'openvpn-add-server' to create the server;\n"+\
				"  'openvpn-add-user' to create the users(s).")
		xbmcaddon.Addon().openSettings('id')
  
   def onSettingsChanged(self):
      subprocess.call(['systemctl', 'restart', self.id])

if __name__ == "__main__":
   Monitor().waitForAbort()
