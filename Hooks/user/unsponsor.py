# Unsponsor a user

import re
from .variables import access
from .Core.modules import M
loadable = M.loadable.loadable

class unsponsor(loadable.loadable):
    """Unsponsor one of your gimps."""
    def __init__(self):
        loadable.__init__(self)
        self.access = access['member']
        self.paramre = re.compile(r"\s([\w-]+)")
        self.usage += " pnick"
        
    def execute(self, message):
        user, params = loadable.execute(self, message) or (None,None)
        if not params:
            return

        # assign param variables
        recruit=params.group(1)
        
        # do stuff here
        gimp = M.DB.Maps.Gimp.load(name=recruit)
        if gimp is None:
            message.alert("No gimp with that pnick exists!")
            return
        if gimp.sponsor is not user:
            message.alert("That's not your gimp!")
            return
        user.invites += 1
        session = M.DB.Session()
        session.add(user)
        session.delete(gimp)
        session.commit()
        session.close()
        message.reply("You have unsponsored '%s'." % (recruit,)
    
callbacks = [("PRIVMSG", unsponsor())]