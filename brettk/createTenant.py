import APICCoreFuncs
from cobra.model.fv import Tenant
import sys


def new_tenant(active_location, tenant_name):
    tenant = Tenant(active_location, tenant_name)
    return tenant


def main(argv):
    aci = APICCoreFuncs.APICHandler()
    if argv and len(argv[0]) > 0:
        tenant_name = argv[0]

        # Create a new session
        session = aci.do_login()

        loc = aci.target_location_lookup(session, 'uni')
        tenant = new_tenant(loc, tenant_name)
        aci.update_config(session, loc)

        # Wrap it up
        aci.logout(session)

if __name__ == '__main__':
    main(sys.argv[1:])
