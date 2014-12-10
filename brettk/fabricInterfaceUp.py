import APICCoreFuncs
import sys
from cobra.model.fabric import Node
from cobra.model.ethpm import PhysIf as ethpmPhysIf
from cobra.model.l1 import PhysIf
from cobra.mit.request import DnQuery
from cobra.mit.request import ClassQuery


def get_children(session, referer):
    dnQuery = DnQuery(referer.dn)
    dnQuery.queryTarget = 'children'
    childMo = session.query(dnQuery)
    return childMo


def get_class_mo(session, refClass, propFilter):
    #help(ClassQuery)
    classQuery = ClassQuery(refClass)
    classQuery.queryTarget = 'subtree'
    classQuery.propFilter = propFilter
    return session.query(classQuery)


def main(argv):
    aci = APICCoreFuncs.APICHandler()

    # Create a new session
    session = aci.do_login()

    interfaces = []
    # loc = aci.target_location_lookup(session, 'topology/pod-1/')
    # children = get_children(session, loc)
    # for newMo in children:
    #     # only act on children that are Node type
    #     if type(newMo) == Node:
    #         currNode = str(newMo.dn) + '/sys'
    #         loc = aci.target_location_lookup(session, currNode)
    #         targets = get_children(session, loc)
    #         for target in targets:
    #             if type(target) == PhysIf:
    #                 interfaces.append(target)

    # for intf in interfaces:
    #     phys_int = str(intf.dn) + '/phys'
    #     loc = aci.target_location_lookup(session, phys_int)
    #     print 'Interface', str(intf.dn), 'state is', loc.operSt

    interfaces = get_class_mo(session, 'l1.PhysIf', 'and (eq(ethpmPhysIf.operSt, "up"), eq(ethpmPhysIf.operMode,"trunk"))')
    for intf in interfaces:
        print str(intf.dn), intf.operSt
        # print dir(intf)

    print "************************************************"

    interfaces = get_class_mo(session, 'top.System', 'and (eq(l1PhysIf.adminSt, "up"), eq(ethpmPhysIf.operSt,"up"))')
    for intf in interfaces:
        print str(intf.dn), intf.operSt

    # Wrap it up
    aci.logout(session)

if __name__ == '__main__':
    main(sys.argv[1:])
