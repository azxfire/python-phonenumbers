"""Auto-generated file, do not edit by hand. IE metadata"""
from ..util import u
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_IE = PhoneMetadata(id='IE', country_code=353, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[124-9]\\d{6,9}', possible_number_pattern='\\d{5,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='1\\d{7,8}|2(?:1\\d{6,7}|[24-9]\\d{5}|3\\d{5,7})|4(?:0[24]\\d{5}|[1269]\\d{7}|[34]\\d{5,7}|5\\d{6}|7\\d{5}|8[0-46-9]\\d{7})|5(?:0[45]\\d{5}|1\\d{6}|2\\d{5,7}|[3679]\\d{7}|8\\d{5})|6(?:1\\d{6}|4\\d{5,7}|[237-9]\\d{5}|[56]\\d{7})|7[14]\\d{7}|9(?:1\\d{6}|[04]\\d{7}|[3-9]\\d{5})', possible_number_pattern='\\d{5,10}', example_number='2212345'),
    mobile=PhoneNumberDesc(national_number_pattern='8(?:22\\d{6}|[35-9]\\d{7,8})', possible_number_pattern='\\d{9,10}', example_number='850123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='1800\\d{6}', possible_number_pattern='\\d{10}', example_number='1800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='15(?:1[2-9]|[2-8]0|59|9[089])\\d{6}', possible_number_pattern='\\d{10}', example_number='1520123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='18[59]0\\d{6}', possible_number_pattern='\\d{10}', example_number='1850123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='700\\d{6}', possible_number_pattern='\\d{9}', example_number='700123456'),
    voip=PhoneNumberDesc(national_number_pattern='76\\d{7}', possible_number_pattern='\\d{9}', example_number='761234567'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='818\\d{6}', possible_number_pattern='\\d{9}', example_number='818123456'),
    emergency=PhoneNumberDesc(national_number_pattern='112|999', possible_number_pattern='\\d{3}', example_number='112'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='18[59]0\\d{6}', possible_number_pattern='\\d{10}', example_number='1850123456'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(1)(\\d{3,4})(\\d{4})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['1'], national_prefix_formatting_rule=u('(0\\1)')),
        NumberFormat(pattern='(\\d{2})(\\d{5})', format=u('\\1 \\2'), leading_digits_pattern=['2[2-9]|4[347]|5[2-58]|6[2-47-9]|9[3-9]'], national_prefix_formatting_rule=u('(0\\1)')),
        NumberFormat(pattern='(\\d{3})(\\d{5})', format=u('\\1 \\2'), leading_digits_pattern=['40[24]|50[45]'], national_prefix_formatting_rule=u('(0\\1)')),
        NumberFormat(pattern='(48)(\\d{4})(\\d{4})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['48'], national_prefix_formatting_rule=u('(0\\1)')),
        NumberFormat(pattern='(818)(\\d{3})(\\d{3})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['81'], national_prefix_formatting_rule=u('(0\\1)')),
        NumberFormat(pattern='(\\d{2})(\\d{3})(\\d{3,4})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['[24-69]|7[14]'], national_prefix_formatting_rule=u('(0\\1)')),
        NumberFormat(pattern='([78]\\d)(\\d{3,4})(\\d{4})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['76|8[35-9]'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='(700)(\\d{3})(\\d{3})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['70'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='(\\d{4})(\\d{3})(\\d{3})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['1(?:8[059]|5)', '1(?:8[059]0|5)'], national_prefix_formatting_rule=u('\\1'))])
