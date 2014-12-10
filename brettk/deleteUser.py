import sys
import APICCoreFuncs


def delete_user(name, controller, session):
    user_loc = 'uni/userext/user-' + name
    user = controller.target_location_lookup(session, user_loc)
    user.delete()
    controller.update_config(session, user)


def main(argv):
    aci = APICCoreFuncs.APICHandler()
    if argv and len(argv[0]) > 0:
        user_name = argv[0]

        # Create a new session
        session = aci.do_login()

        #print type(tenant)
        delete_user(user_name, aci, session)

        # Wrap it up
        aci.logout(session)

if __name__ == '__main__':
    main(sys.argv[1:])
