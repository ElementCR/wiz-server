from actionupdater import *

class ChaosExplodeUpdater(ActionUpdater):
  def topic(self):
    return 'explodedchaos'

  def processEvent(self, name, details, avatar):
    avatar.intent['type'] = 'chaos'
    avatar.logMessage('The witch cackles as you fumble')













