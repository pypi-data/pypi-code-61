import ldap.ldapobject
import pytest
import slapdtest


@pytest.fixture(scope="session")
def slapd_server():
    """
    Launch a slapd server instance during the test.
    You can retrieve its connection information with `slapd_server.root_dn` and `slapd_server.root_pw`.
    :return: a :class:`~slapdtest.SlapdObject` instance.
    """
    slapd = slapdtest.SlapdObject()
    try:
        slapd.start()
        suffix_dc = slapd.suffix.split(",")[0][3:]

        slapd.ldapadd(
            "\n".join(
                [
                    "dn: " + slapd.suffix,
                    "objectClass: dcObject",
                    "objectClass: organization",
                    "dc: " + suffix_dc,
                    "o: " + suffix_dc,
                    "",
                    "dn: " + slapd.root_dn,
                    "objectClass: applicationProcess",
                    "cn: " + slapd.root_cn,
                ]
            )
            + "\n"
        )

        yield slapd
    finally:
        slapd.stop()


@pytest.fixture
def slapd_connection(slapd_server):
    """
    Launch a temporary slapd server, and returns a connection to this server.
    :return: a :class:`~ldap.ldapobject.LDAPObject` instance.
    """
    conn = ldap.ldapobject.SimpleLDAPObject(slapd_server.ldap_uri)
    conn.protocol_version = 3
    conn.simple_bind_s(slapd_server.root_dn, slapd_server.root_pw)
    yield conn
    conn.unbind_s()
