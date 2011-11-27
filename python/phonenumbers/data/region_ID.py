"""Auto-generated file, do not edit by hand. ID metadata"""
from ..util import u
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ID = PhoneMetadata(id='ID', country_code=62, international_prefix='0(?:0[1789]|10(?:00|1[67]))',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{6,10}', possible_number_pattern='\\d{5,11}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='2[124]\\d{7,8}|(?:2(?:[35][1-4]|6[0-8]|7[1-6]|8\\d|9[1-8])|3(?:1|2[1-578]|3[1-68]|4[1-3]|5[1-8]|6[1-3568]|7[0-46]|8\\d)|4(?:0[1-589]|1[01347-9]|2[0-36-8]|3[0-24-68]|5[1-378]|6[1-5]|7[134]|8[1245])|5(?:1[1-35-9]|2[25-8]|3[1246-9]|4[1-3589]|5[1-46]|6[1-8])|6(?:19?|[25]\\d|3[1-469]|4[1-6])|7(?:1[1-46-9]|2[14-9]|[36]\\d|4[1-8]|5[1-9]|7[0-36-9])|9(?:0[12]|1[0134-8]|2[0-479]|5[125-8]|6[23679]|7[159]|8[01346]))\\d{5,8}', possible_number_pattern='\\d{5,10}', example_number='612345678'),
    mobile=PhoneNumberDesc(national_number_pattern='8[1-35-9]\\d{7,9}', possible_number_pattern='\\d{9,11}', example_number='812345678'),
    toll_free=PhoneNumberDesc(national_number_pattern='177\\d{6,8}|800\\d{5,7}', possible_number_pattern='\\d{8,11}', example_number='8001234567'),
    premium_rate=PhoneNumberDesc(national_number_pattern='809\\d{7}', possible_number_pattern='\\d{10}', example_number='8091234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='11[02389]', possible_number_pattern='\\d{3}', example_number='112'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d{2})(\\d{7,8})', format=u('\\1 \\2'), leading_digits_pattern=['2[124]|[36]1'], national_prefix_formatting_rule=u('(0\\1)')),
        NumberFormat(pattern='(\\d{3})(\\d{5,7})', format=u('\\1 \\2'), leading_digits_pattern=['[4579]|2[035-9]|[36][02-9]'], national_prefix_formatting_rule=u('(0\\1)')),
        NumberFormat(pattern='(8\\d{2})(\\d{3,4})(\\d{3,4})', format=u('\\1-\\2-\\3'), leading_digits_pattern=['8[1-35-9]'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='(177)(\\d{6,8})', format=u('\\1 \\2'), leading_digits_pattern=['1'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='(800)(\\d{5,7})', format=u('\\1 \\2'), leading_digits_pattern=['800'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='(809)(\\d)(\\d{3})(\\d{3})', format=u('\\1 \\2 \\3 \\4'), leading_digits_pattern=['809'], national_prefix_formatting_rule=u('0\\1'))])
