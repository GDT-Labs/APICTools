import sys
import APICCoreFuncs


def delete_tenant(name, controller, session):
    tenant_loc = 'uni/tn-' + name
    tenant = controller.target_location_lookup(session, tenant_loc)
    tenant.delete()
    controller.update_config(session, tenant)


def main(argv):
    aci = APICCoreFuncs.APICHandler()
    if argv and len(argv[0]) > 0:
        tenant_name = argv[0]

        # Create a new session
        session = aci.do_login()

        #print type(tenant)
        delete_tenant(tenant_name, aci, session)

        # Wrap it up
        aci.logout(session)

if __name__ == '__main__':
    main(sys.argv[1:])
