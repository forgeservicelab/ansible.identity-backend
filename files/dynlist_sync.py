#!/usr/bin/python

import ldap
import ldap.modlist

conn = ldap.initialize('ldaps://localhost')
conn.bind_s('cn=admin,ou=accounts,{{ ldap_dn }}','{{ ldap_admin_password }}', ldap.AUTH_SIMPLE)

for role in ['developers', 'partners', 'partners_cra', 'technical_contacts']:
    oldmembers = conn.search_s('cn=%s,ou=roles,{{ ldap_dn }}' % role, ldap.SCOPE_BASE, attrlist=['member'])[0][1]
    newmembers = conn.search_s('cn=dyn_%s,ou=roles,{{ ldap_dn }}' % role, ldap.SCOPE_BASE, attrlist=['member'])[0][1]
    
    conn.modify_s('cn=%s,ou=roles,{{ ldap_dn }}' % role, ldap.modlist.modifyModlist(oldmembers, newmembers))
