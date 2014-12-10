from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.mit.request import ConfigRequest


class APICHandler():
    def __init__(self):
        self.host = 'https://192.168.1.100'
        self.user = 'admin'
        self.pwd = 'GDTlabs123'
        self.session = None

    def do_login(self):
        loginSession = LoginSession(self.host, self.user, self.pwd)
        self.session = MoDirectory(loginSession)
        self.session.login()
        # print loginSession.cookie
        return self.session

    def target_location_lookup(self, active_session, location):
        change_location = self.session.lookupByDn(location)
        return change_location

    def update_config(self, active_session, change_location):
        configReq = ConfigRequest()
        configReq.addMo(change_location)
        self.session.commit(configReq)

    def logout(self, active_session):
        self.session.logout()
