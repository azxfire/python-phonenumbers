"""Auto-generated file, do not edit by hand. ZW metadata"""
from ..util import u
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ZW = PhoneMetadata(id='ZW', country_code=263, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='2(?:[012457-9]\\d{3,8}|6\\d{3,6})|[13-79]\\d{4,8}|86\\d{8}', possible_number_pattern='\\d{3,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='(?:1[3-9]|2(?:0[45]|[16]|2[28]|[49]8?|58[23]|7[246]|8[1346-9])|3(?:08?|17?|3[78]|[2456]|7[1569]|8[379])|5(?:[07-9]|1[78]|483|5(?:7?|8))|6(?:0|28|37?|[45][68][78]|98?)|848)\\d{3,6}|(?:2(?:27|5|7[135789]|8[25])|3[39]|5[1-46]|6[126-8])\\d{4,6}|2(?:0|70)\\d{5,6}|(?:4\\d|9[2-8])\\d{4,7}', possible_number_pattern='\\d{3,10}', example_number='1312345'),
    mobile=PhoneNumberDesc(national_number_pattern='7[137]\\d{7}', possible_number_pattern='\\d{9}', example_number='711234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    premium_rate=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    shared_cost=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='86(?:1[12]|22|30|44|8[367]|99)\\d{6}', possible_number_pattern='\\d{10}', example_number='8686123456'),
    pager=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    emergency=PhoneNumberDesc(national_number_pattern='(?:112|99[3459])', possible_number_pattern='\\d{3}', example_number='999'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='([49])(\\d{3})(\\d{2,5})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['4|9[2-9]'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='([179]\\d)(\\d{3})(\\d{3,4})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['[19]1|7'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='([1-356]\\d)(\\d{3,5})', format=u('\\1 \\2'), leading_digits_pattern=['1[3-9]|2(?:[1-469]|0[0-35-9]|[45][0-79])|3(?:0[0-79]|1[0-689]|[24-69]|3[0-69])|5(?:[02-46-9]|[15][0-69])|6(?:[0145]|[29][0-79]|3[0-689]|[68][0-69])'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='([1-356]\\d)(\\d{3})(\\d{3})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['1[3-9]|2(?:[1-469]|0[0-35-9]|[45][0-79])|3(?:0[0-79]|1[0-689]|[24-69]|3[0-69])|5(?:[02-46-9]|[15][0-69])|6(?:[0145]|[29][0-79]|3[0-689]|[68][0-69])'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='([2356]\\d{2})(\\d{3,5})', format=u('\\1 \\2'), leading_digits_pattern=['2(?:[278]|0[45]|48)|3(?:08|17|3[78]|[78])|5[15][78]|6(?:[29]8|37|[68][78])'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='([2356]\\d{2})(\\d{3})(\\d{3})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['2(?:[278]|0[45]|48)|3(?:08|17|3[78]|[78])|5[15][78]|6(?:[29]8|37|[68][78])'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='([25]\\d{3})(\\d{3,5})', format=u('\\1 \\2'), leading_digits_pattern=['(?:25|54)8', '258[23]|5483'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='([25]\\d{3})(\\d{3})(\\d{3})', format=u('\\1 \\2 \\3'), leading_digits_pattern=['(?:25|54)8', '258[23]|5483'], national_prefix_formatting_rule=u('0\\1')),
        NumberFormat(pattern='(8\\d{3})(\\d{6})', format=u('\\1 \\2'), leading_digits_pattern=['8'], national_prefix_formatting_rule=u('0\\1'))])
