# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words

CARDINAL_TEST_CASES = (
    ('0', 'нула'),
    ('1', 'едно'),
    ('10', 'десет'),
    ('100', 'сто'),
    ('101', 'сто и едно'),
    ('110', 'сто и десет'),
    ('120', 'сто и двадесет'),
    ('121', 'сто двадесет и едно'),
    ('1000', 'хиляда'),
    ('1001', 'хиляда и едно'),
    ('1021', 'хиляда двадесет и едно'),
    ('1020', 'хиляда и двадесет'),
    ('1200', 'хиляда и двеста'),
    ('1201', 'хиляда двеста и едно'),
    ('2201', 'две хиляди двеста и едно'),
    ('3200', 'три хиляди и двеста'),
    ('10000', 'десет хиляди'),
    ('10001', 'десет хиляди и едно'),
    ('50001', 'петдесет хиляди и едно'),
    ('51000', 'петдесет и една хиляди'),
    ('100000', 'сто хиляди'),
    ('155000', 'сто петдесет и пет хиляди'),
    ('155201', 'сто петдесет и пет хиляди двеста и едно'),
    ('251000', 'двеста петдесет и една хиляди'),
    ('1000000', 'един милион'),
    ('1200000', 'един милион и двеста хиляди'),
    ('1250000', 'един милион двеста и петдесет хиляди'),
    ('1250001', 'един милион двеста и петдесет хиляди и едно'),
    ('1251000', 'един милион двеста петдесет и една хиляди'),
    ('1251001', 'един милион двеста петдесет и една хиляди и едно'),
    ('1500000', 'един милион и петстотин хиляди'),
    ('1000000000', 'един милиард'),
    ('1500000000', 'един милиард и петстотин милиона'),
    ('1548000001', 'един милиард петстотин четиридесет и осем милиона и едно'),
    ('20045309847', 'двадесет милиарда четиридесет и пет милиона триста и девет хиляди осемстотин четиридесет и седем'),
)

CURRENCY_TEST_CASES = (
    ('1', 'един лев и нула стотинки'),
    ('1.01', 'един лев и една стотинка'),
    ('1.21', 'един лев и двадесет и една стотинки'),
    ('10', 'десет лева и нула стотинки'),
    ('10.45', 'десет лева и четиридесет и пет стотинки'),
    ('1555.55', 'хиляда петстотин петдесет и пет лева и петдесет и пет стотинки')
)

YEAR_TEST_CASES = (
    ('681', 'шестстотин осемдесет и първа'),
    ('1924', 'хиляда деветстотин двадесет и четвърта'),
    ('1991', 'хиляда деветстотин деветдесет и първа'),
    ('2004', 'две хиляди и четвърта'),
    ('6666', 'шест хиляди шестстотин шейсет и шеста'),
)

ORDINAL_TEST_CASES = (
    ('1', 'първи'),
    ('7', 'седми'),
    ('10', 'десети'),
    ('101', 'сто и първи'),
)

ORDINAL_NUMERIC_TEST_CASES = (
    ('1', '1-ви'),
    ('7', '7-ми'),
    ('10', '10-ти'),
    ('101', '101-ви'),
)


class Num2WordsBGTest(TestCase):
    def test_cardinal(self):
        for test in CARDINAL_TEST_CASES:
            self.assertEqual(
                test[1], num2words(test[0], lang='bg', to='cardinal')
            )

    def test_currency(self):
        for test in CURRENCY_TEST_CASES:
            self.assertEqual(
                test[1], num2words(test[0], lang='bg', to='currency')
            )

    def test_years(self):
        for test in YEAR_TEST_CASES:
            self.assertEqual(
                test[1], num2words(test[0], lang='bg', to='year')
            )

    def test_ordinal(self):
        for test in ORDINAL_TEST_CASES:
            self.assertEqual(
                test[1], num2words(test[0], lang='bg', to='ordinal')
            )

    def test_ordinal_numeric(self):
        for test in ORDINAL_NUMERIC_TEST_CASES:
            self.assertEqual(
                test[1], num2words(test[0], lang='bg', to='ordinal_num')
            )
