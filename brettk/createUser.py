import APICCoreFuncs
from cobra.model.aaa import User
import sys


def new_user(active_location, name):
    user = User(active_location, name)
    return user


def main(argv):
    aci = APICCoreFuncs.APICHandler()
    if argv and len(argv[0]) > 0:
        user_name = argv[0]

        # Create a new session
        session = aci.do_login()

        loc = aci.target_location_lookup(session, 'uni/userext')
        user = new_user(loc, user_name)
        user.firstName = 'Brett'
        user.lastName = 'Kugler'
        aci.update_config(session, loc)

        # Wrap it up
        aci.logout(session)

if __name__ == '__main__':
    main(sys.argv[1:])
