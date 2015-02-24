import unittest
import datetime

from mustaine import protocol
from mustaine.client import HessianProxy

# Caucho's Hessian 2.0 reference service
# interface: http://caucho.com/resin-javadoc/com/caucho/hessian/test/TestHessian2.html

class ParserV1TestCase(unittest.TestCase):

    def get_client(self, cls=HessianProxy):
        return cls("http://hessian.caucho.com/test/test", version=1)

    def setUp(self):
        self.client = self.get_client()

    def test_parse_binary_0(self):
        expected = protocol.Binary("")
        reply = self.client.replyBinary_0()
        self.assertEqual(expected, reply)

    def test_parse_binary_1(self):
        expected = protocol.Binary("0")
        reply = self.client.replyBinary_1()
        self.assertEqual(expected, reply)

    def get_reply_str_1024(self):
        reply_str = ""
        for i in xrange(0, 16):
            reply_str += "%d%d%s" % (
                i // 10, i % 10, " 456789012345678901234567890123456789012345678901234567890123\n")
        return reply_str[:1024]

    def get_reply_str_65536(self):
        reply_str = ""
        for i in xrange(0, 64 * 16):
            reply_str += "%d%d%d%s" % (
                i // 100, (i // 10) % 10, i % 10, " 56789012345678901234567890123456789012345678901234567890123\n")
        return reply_str[:65536]

    def test_parse_binary_1023(self):
        expected = protocol.Binary(self.get_reply_str_1024()[:1023])
        reply = self.client.replyBinary_1023()
        self.assertEqual(expected, reply)

    def test_parse_binary_1024(self):
        expected = protocol.Binary(self.get_reply_str_1024()[:1024])
        reply = self.client.replyBinary_1024()
        self.assertEqual(expected, reply)

    def test_parse_binary_15(self):
        self.assertEqual(self.client.replyBinary_15(), protocol.Binary("012345678901234"))

    def test_parse_binary_16(self):
        self.assertEqual(self.client.replyBinary_16(), protocol.Binary("0123456789012345"))

    # def test_parse_binary_65536(self):
    #     expected = protocol.Binary(self.get_reply_str_65536())
    #     reply = self.client.replyBinary_65536()
    #     import ipdb; ipdb.set_trace()
    #     self.assertEqual(expected, reply)

    def test_parse_date_0(self):
        expected =  datetime.datetime.utcfromtimestamp(0)
        reply = self.client.replyDate_0()
        self.assertEqual(expected, reply)

    def test_parse_date_1(self):
        expected = datetime.datetime(1998, 5, 8, 9, 51, 31)
        reply = self.client.replyDate_1()
        self.assertEqual(expected, reply)

    def test_parse_date_2(self):
        expected = datetime.datetime(1998, 5, 8, 9, 51, 0)
        reply = self.client.replyDate_2()
        self.assertEqual(expected, reply)

    def test_parse_double_0_0(self):
        self.assertEqual(self.client.replyDouble_0_0(), 0.0)

    def test_parse_double_0_001(self):
        expected = 0.001
        reply = self.client.replyDouble_0_001()
        self.assertEqual(expected, reply)

    def test_parse_double_1_0(self):
        expected = 1.0
        reply = self.client.replyDouble_1_0()
        self.assertEqual(expected, reply)

    def test_parse_double_127_0(self):
        expected = 127.0
        reply = self.client.replyDouble_127_0()
        self.assertEqual(expected, reply)

    def test_parse_double_128_0(self):
        expected = 128.0
        reply = self.client.replyDouble_128_0()
        self.assertEqual(expected, reply)

    def test_parse_double_2_0(self):
        expected = 2.0
        reply = self.client.replyDouble_2_0()
        self.assertEqual(expected, reply)

    def test_parse_double_3_14159(self):
        expected = 3.14159
        reply = self.client.replyDouble_3_14159()
        self.assertEqual(expected, reply)

    def test_parse_double_32767_0(self):
        expected = 32767.0
        reply = self.client.replyDouble_32767_0()
        self.assertEqual(expected, reply)

    def test_parse_double_65_536(self):
        expected = 65.536
        reply = self.client.replyDouble_65_536()
        self.assertEqual(expected, reply)

    def test_parse_double_m0_001(self):
        expected = -0.001
        reply = self.client.replyDouble_m0_001()
        self.assertEqual(expected, reply)

    def test_parse_double_m128_0(self):
        expected = -128.0
        reply = self.client.replyDouble_m128_0()
        self.assertEqual(expected, reply)

    def test_parse_double_m129_0(self):
        expected = -129.0
        reply = self.client.replyDouble_m129_0()
        self.assertEqual(expected, reply)

    def test_parse_double_m32768_0(self):
        expected = -32768.0
        reply = self.client.replyDouble_m32768_0()
        self.assertEqual(expected, reply)

    def test_parse_false(self):
        expected = False
        reply = self.client.replyFalse()
        self.assertEqual(expected, reply)

    def test_parse_int_0(self):
        expected = 0
        reply = self.client.replyInt_0()
        self.assertEqual(expected, reply)

    def test_parse_int_0x30(self):
        expected = 0x30
        reply = self.client.replyInt_0x30()
        self.assertEqual(expected, reply)

    def test_parse_int_0x3ffff(self):
        expected = 0x3ffff
        reply = self.client.replyInt_0x3ffff()
        self.assertEqual(expected, reply)

    def test_parse_int_0x40000(self):
        expected = 0x40000
        reply = self.client.replyInt_0x40000()
        self.assertEqual(expected, reply)

    def test_parse_int_0x7ff(self):
        expected = 0x7ff
        reply = self.client.replyInt_0x7ff()
        self.assertEqual(expected, reply)

    def test_parse_int_0x7fffffff(self):
        expected = 0x7fffffff
        reply = self.client.replyInt_0x7fffffff()
        self.assertEqual(expected, reply)

    def test_parse_int_0x800(self):
        expected = 0x800
        reply = self.client.replyInt_0x800()
        self.assertEqual(expected, reply)

    def test_parse_int_1(self):
        expected = 1
        reply = self.client.replyInt_1()
        self.assertEqual(expected, reply)

    def test_parse_int_47(self):
        expected = 47
        reply = self.client.replyInt_47()
        self.assertEqual(expected, reply)

    def test_parse_int_m0x40000(self):
        expected = -0x40000
        reply = self.client.replyInt_m0x40000()
        self.assertEqual(expected, reply)

    def test_parse_int_m0x40001(self):
        expected = -0x40001
        reply = self.client.replyInt_m0x40001()
        self.assertEqual(expected, reply)

    def test_parse_int_m0x800(self):
        expected = -0x800
        reply = self.client.replyInt_m0x800()
        self.assertEqual(expected, reply)

    def test_parse_int_m0x80000000(self):
        expected = -0x80000000
        reply = self.client.replyInt_m0x80000000()
        self.assertEqual(expected, reply)

    def test_parse_int_m0x801(self):
        expected = -0x801
        reply = self.client.replyInt_m0x801()
        self.assertEqual(expected, reply)

    def test_parse_int_m16(self):
        expected = -16
        reply = self.client.replyInt_m16()
        self.assertEqual(expected, reply)

    def test_parse_int_m17(self):
        expected = -17
        reply = self.client.replyInt_m17()
        self.assertEqual(expected, reply)

    def test_parse_long_0(self):
        expected = 0L
        reply = self.client.replyLong_0()
        self.assertEqual(expected, reply)

    def test_parse_long_0x10(self):
        expected = 0x10L
        reply = self.client.replyLong_0x10()
        self.assertEqual(expected, reply)

    def test_parse_long_0x3ffff(self):
        expected = 0x3ffffL
        reply = self.client.replyLong_0x3ffff()
        self.assertEqual(expected, reply)

    def test_parse_long_0x40000(self):
        expected = 0x40000L
        reply = self.client.replyLong_0x40000()
        self.assertEqual(expected, reply)

    def test_parse_long_0x7ff(self):
        expected = 0x7ffL
        reply = self.client.replyLong_0x7ff()
        self.assertEqual(expected, reply)

    def test_parse_long_0x7fffffff(self):
        expected = 0x7fffffffL
        reply = self.client.replyLong_0x7fffffff()
        self.assertEqual(expected, reply)

    def test_parse_long_0x800(self):
        expected = 0x800L
        reply = self.client.replyLong_0x800()
        self.assertEqual(expected, reply)

    def test_parse_long_0x80000000(self):
        expected = 0x80000000L
        reply = self.client.replyLong_0x80000000()
        self.assertEqual(expected, reply)

    def test_parse_long_1(self):
        expected = 1L
        reply = self.client.replyLong_1()
        self.assertEqual(expected, reply)

    def test_parse_long_15(self):
        expected = 15L
        reply = self.client.replyLong_15()
        self.assertEqual(expected, reply)

    def test_parse_long_m0x40000(self):
        expected = -0x40000L
        reply = self.client.replyLong_m0x40000()
        self.assertEqual(expected, reply)

    def test_parse_long_m0x40001(self):
        expected = -0x40001L
        reply = self.client.replyLong_m0x40001()
        self.assertEqual(expected, reply)

    def test_parse_long_m0x800(self):
        expected = -0x800L
        reply = self.client.replyLong_m0x800()
        self.assertEqual(expected, reply)

    def test_parse_long_m0x80000000(self):
        expected = -0x80000000L
        reply = self.client.replyLong_m0x80000000()
        self.assertEqual(expected, reply)

    def test_parse_long_m0x80000001(self):
        expected = -0x80000001L
        reply = self.client.replyLong_m0x80000001()
        self.assertEqual(expected, reply)

    def test_parse_long_m0x801(self):
        expected = -0x801L
        reply = self.client.replyLong_m0x801()
        self.assertEqual(expected, reply)

    def test_parse_long_m8(self):
        expected = -8L
        reply = self.client.replyLong_m8()
        self.assertEqual(expected, reply)

    def test_parse_long_m9(self):
        expected = -9L
        reply = self.client.replyLong_m9()
        self.assertEqual(expected, reply)

    def test_parse_null(self):
        expected = None
        reply = self.client.replyNull()
        self.assertEqual(expected, reply)

    def test_parse_object_0(self):
        expected = protocol.object_factory('com.caucho.hessian.test.A0')
        reply = self.client.replyObject_0()
        self.assertEqual(expected, reply)

    def test_parse_object_1(self):
        expected = protocol.object_factory('com.caucho.hessian.test.TestObject', _value=0)
        reply = self.client.replyObject_1()
        self.assertEqual(expected, reply)

    def test_parse_object_16(self):
        expected = [
            protocol.object_factory('com.caucho.hessian.test.A0'),
            protocol.object_factory('com.caucho.hessian.test.A1'),
            protocol.object_factory('com.caucho.hessian.test.A2'),
            protocol.object_factory('com.caucho.hessian.test.A3'),
            protocol.object_factory('com.caucho.hessian.test.A4'),
            protocol.object_factory('com.caucho.hessian.test.A5'),
            protocol.object_factory('com.caucho.hessian.test.A6'),
            protocol.object_factory('com.caucho.hessian.test.A7'),
            protocol.object_factory('com.caucho.hessian.test.A8'),
            protocol.object_factory('com.caucho.hessian.test.A9'),
            protocol.object_factory('com.caucho.hessian.test.A10'),
            protocol.object_factory('com.caucho.hessian.test.A11'),
            protocol.object_factory('com.caucho.hessian.test.A12'),
            protocol.object_factory('com.caucho.hessian.test.A13'),
            protocol.object_factory('com.caucho.hessian.test.A14'),
            protocol.object_factory('com.caucho.hessian.test.A15'),
            protocol.object_factory('com.caucho.hessian.test.A16')
        ]
        reply = self.client.replyObject_16()
        self.assertEqual(expected, reply)

    def test_parse_object_2(self):
        expected = [
            protocol.object_factory('com.caucho.hessian.test.TestObject', _value=0),
            protocol.object_factory('com.caucho.hessian.test.TestObject', _value=1)
        ]
        reply = self.client.replyObject_2()
        self.assertEqual(expected, reply)

    def test_parse_object_2a(self):
        payload = protocol.object_factory('com.caucho.hessian.test.TestObject', _value=0)
        expected = [payload, payload]
        reply = self.client.replyObject_2a()
        self.assertEqual(expected, reply)

    def test_parse_object_2b(self):
        expected = [
            protocol.object_factory('com.caucho.hessian.test.TestObject', _value=0),
            protocol.object_factory('com.caucho.hessian.test.TestObject', _value=0)
        ]
        reply = self.client.replyObject_2b()
        self.assertEqual(expected, reply)

    def test_parse_object_3(self):
        expected = protocol.object_factory('com.caucho.hessian.test.TestCons', _first='a', _rest=None)
        expected._rest = expected
        reply = self.client.replyObject_3()
        self.assertEqual(expected, reply)

    def test_parse_string_0(self):
        expected = ""
        reply = self.client.replyString_0()
        self.assertEqual(expected, reply)

    def test_parse_string_1(self):
        expected = "0"
        reply = self.client.replyString_1()
        self.assertEqual(expected, reply)

    def test_parse_string_31(self):
        expected = "0123456789012345678901234567890"
        reply = self.client.replyString_31()
        self.assertEqual(expected, reply)

    def test_parse_string_32(self):
        expected = "01234567890123456789012345678901"
        reply = self.client.replyString_32()
        self.assertEqual(expected, reply)

    def test_parse_string_1023(self):
        expected = self.get_reply_str_1024()[:1023]
        reply = self.client.replyString_1023()
        self.assertEqual(expected, reply)

    def test_parse_string_1024(self):
        self.assertEqual(self.client.replyString_1024(), self.get_reply_str_1024())

    # def test_parse_string_65536(self):
    #     expected = self.get_reply_str_65536()
    #     reply = self.client.replyString_65536()
    #     self.assertEqual(expected, str(reply))

    def test_parse_true(self):
        expected = True
        reply = self.client.replyTrue()
        self.assertEqual(expected, reply)


class ParserV2TestCase(ParserV1TestCase):

    def get_client(self, cls=HessianProxy):
        return cls("http://localhost:62833/api", version=2)

    def setUp(self):
        self.client = self.get_client()

    def test_parse_object_16(self):
        expected = (
            protocol.object_factory('com.caucho.hessian.test.A0'),
            protocol.object_factory('com.caucho.hessian.test.A1'),
            protocol.object_factory('com.caucho.hessian.test.A2'),
            protocol.object_factory('com.caucho.hessian.test.A3'),
            protocol.object_factory('com.caucho.hessian.test.A4'),
            protocol.object_factory('com.caucho.hessian.test.A5'),
            protocol.object_factory('com.caucho.hessian.test.A6'),
            protocol.object_factory('com.caucho.hessian.test.A7'),
            protocol.object_factory('com.caucho.hessian.test.A8'),
            protocol.object_factory('com.caucho.hessian.test.A9'),
            protocol.object_factory('com.caucho.hessian.test.A10'),
            protocol.object_factory('com.caucho.hessian.test.A11'),
            protocol.object_factory('com.caucho.hessian.test.A12'),
            protocol.object_factory('com.caucho.hessian.test.A13'),
            protocol.object_factory('com.caucho.hessian.test.A14'),
            protocol.object_factory('com.caucho.hessian.test.A15'),
            protocol.object_factory('com.caucho.hessian.test.A16'),
        )
        reply = self.client.replyObject_16()
        self.assertEqual(expected, reply)

    def test_parse_object_2(self):
        expected = (
            protocol.object_factory('com.caucho.hessian.test.TestObject', _value=0),
            protocol.object_factory('com.caucho.hessian.test.TestObject', _value=1),
        )
        reply = self.client.replyObject_2()
        self.assertEqual(expected, reply)

    def test_parse_object_2a(self):
        payload = protocol.object_factory('com.caucho.hessian.test.TestObject', _value=0)
        expected = (payload, payload)
        reply = self.client.replyObject_2a()
        self.assertEqual(expected, reply)

    def test_parse_object_2b(self):
        expected = (
            protocol.object_factory('com.caucho.hessian.test.TestObject', _value=0),
            protocol.object_factory('com.caucho.hessian.test.TestObject', _value=0),
        )
        reply = self.client.replyObject_2b()
        self.assertEqual(expected, reply)

    def test_parse_untyped_fixed_list_0(self):
        expected = tuple([])
        reply = self.client.replyUntypedFixedList_0()
        self.assertEqual(expected, reply)

    def test_parse_untyped_fixed_list_1(self):
        expected = ("1", )
        reply = self.client.replyUntypedFixedList_1()
        self.assertEqual(expected, reply)

    def test_parse_untyped_fixed_list_7(self):
        expected = ("1", "2", "3", "4", "5", "6", "7")
        reply = self.client.replyUntypedFixedList_7()
        self.assertEqual(expected, reply)

    def test_parse_untyped_fixed_list_8(self):
        expected = ("1", "2", "3", "4", "5", "6", "7", "8")
        reply = self.client.replyUntypedFixedList_8()
        self.assertEqual(expected, reply)


    def test_parse_typed_fixed_list_0(self):
        expected = tuple([])
        reply = self.client.replyTypedFixedList_0()
        self.assertEqual(expected, reply)

    def test_parse_typed_fixed_list_1(self):
        expected = ("1", )
        reply = self.client.replyTypedFixedList_1()
        self.assertEqual(expected, reply)

    def test_parse_typed_fixed_list_7(self):
        expected = ("1", "2", "3", "4", "5", "6", "7")
        reply = self.client.replyTypedFixedList_7()
        self.assertEqual(expected, reply)

    def test_parse_typed_fixed_list_8(self):
        expected = ("1", "2", "3", "4", "5", "6", "7", "8")
        reply = self.client.replyTypedFixedList_8()
        self.assertEqual(expected, reply)

    def test_parse_untyped_map_0(self):
        expected = {}
        reply = self.client.replyUntypedMap_0()
        self.assertEqual(expected, reply)

    def test_parse_untyped_map_1(self):
        expected = {"a": 0}
        reply = self.client.replyUntypedMap_1()
        self.assertEqual(expected, reply)

    def test_parse_untyped_map_2(self):
        expected = {0: "a", 1: "b"}
        reply = self.client.replyUntypedMap_2()
        self.assertEqual(expected, reply)

    def test_parse_untyped_map_3(self):
        reply = self.client.replyUntypedMap_3()
        expected = {('a', ): 0}
        self.assertEqual(expected, reply)

    def test_parse_typed_map_0(self):
        expected = {}
        reply = self.client.replyTypedMap_0()
        self.assertEqual(expected, reply)

    def test_parse_typed_map_1(self):
        expected = {"a": 0}
        reply = self.client.replyTypedMap_1()
        self.assertEqual(expected, reply)

    def test_parse_typed_map_2(self):
        expected = {0: "a", 1: "b"}
        reply = self.client.replyTypedMap_2()
        self.assertEqual(expected, reply)

    def test_parse_typed_map_3(self):
        reply = self.client.replyTypedMap_3()
        expected = {('a', ): 0}
        self.assertEqual(expected, reply)
